from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import json
import unidecode

def webSiteContent(url):
    try :
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except HTTPError as e:
        print(e)
        return None
    
def main():
    url = 'https://en.wikipedia.org/wiki/List_of_weight_training_exercises'
    page = webSiteContent(url)
    exercicios = exercicesSearch(page)
    writeJsonFile(exercicios)    

def exercicesSearch(page):
    table = page.find('table', class_='wikitable')
    trs = table.find_all('tr')
    exercicios = []
    for index, tr in enumerate(trs) :
        if(index == 0):
            continue
        name = tr.find('th').find('a').get_text()
        link = tr.find('th').find('a')['href']
        exercicios.append({
            'id' : index -1,
            'name' : name,
            'link' : f'https://en.wikipedia.org{link}',
            'muscles' : getMusclesActivated(tr)
        })
    
    return exercicios

def getMusclesActivated(tr):
    ths = tr.find_all('td')
    muscles = []
    for index, field in enumerate(ths) :
        value = field.get_text().strip()
        if(value != ''):
            muscles.append(getMuscleByIdInTh(index))
    return muscles
        
   
def getMuscleByIdInTh(index):
    muscles = [
        'Calves', 'Quadríceps', 'Hamstrings', 'Gluteus', 'Hips', 'Lower back', 'Lats', 'Trapezius', 'Abdominals', 'Chest', 'Deltoids', 'Tríceps', 'Bíceps', 'Forearms'
    ] 
    return muscles[index]
    

def writeJsonFile(info):
    with open('./jsons/exercises.json', 'w') as exercicios:
        exercicios.write(json.dumps(info))
    
if __name__ == "__main__" : 
    main()