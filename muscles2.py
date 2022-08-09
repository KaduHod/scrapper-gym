import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import json
import unidecode




def main():
    url = 'https://en.wikipedia.org/wiki/Shoulder_shrug'
    page = webSiteContent(url)
    table = getTableWithExercises(page)
    rows = getLines(table)
    Exercises = getExercisesWithMuscles(rows)    
    writeJsonFile(Exercises)
    return 'oi'

def getTableWithExercises(page):
    return  page.find('tbody')

def getLines(table):
    trs = []
    for index, tr in enumerate(table.find_all('tr')):
        if index != 0:
            trs.append(tr)
        
    return trs

def getExercisesWithMuscles(rows):
    arrContent = []
    for index,row in enumerate(rows):
        if index == 0:
            arrContent.append({
                'Chest' : getExercises(row)
            })
        if index == 1:
            arrContent.append({
                'Lats' : getExercises(row)
            })
            arrContent.append({
                'Trapezius' : getExercises(row)
            })
        if index == 2:
            arrContent.append({
                'Deltoids' : getExercises(row)
            })
        if index == 3:
            arrContent.append({
                'B\u00edceps' : getExercises(row)
            })
        if index == 4:
            arrContent.append({
                'Tr\u00edceps' : getExercises(row)
            })
        if index == 5:
            arrContent.append({
                'Forearms' : getExercises(row)
            })
        if index == 6:
            arrContent.append({
                'Abdominals' : getExercises(row)
            })
            arrContent.append({
                'Obliques' : getExercises(row)
            })
        if index == 7:
            arrContent.append({
                'Lower back' : getExercises(row)
            })
        if index == 8:
            arrContent.append({
                'Hips' : getExercises(row)
            })
            arrContent.append({
                'Gluteus' : getExercises(row)
            })
        if index == 9:
            arrContent.append({
                'Quadr\u00edceps' : getExercises(row)
            })
        if index == 10:
            arrContent.append({
                'Hamstrings' : getExercises(row)
            })
        if index == 11:
            arrContent.append({
                'Adductors' : getExercises(row)
            })
        if index == 12:
            arrContent.append({
                'Calves' : getExercises(row)
            })
    return arrContent

def getExercises(row):
    td = row.find('td')
    links = td.find_all('a')
    exercises = []
    try:
        for exer in links : 
            obj = {}
            obj['name'] = exer.get_text()
            if(obj['name'] != 'Shoulder shrug'):
                obj['link'] = 'https://en.wikipedia.org'+ exer['href']
                exercises.append(obj) 
               
    except KeyError:
        print(KeyError)
    return exercises

def webSiteContent(url):
    try :
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except HTTPError as e:
        print(e)
        return None
        
def writeJsonFile(info):
    with open('./jsons/muscles2.json', 'w') as exercicios:
        exercicios.write(json.dumps(info))
        
if __name__ == "__main__":
    main()