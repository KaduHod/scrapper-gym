from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import json
import unidecode
import search

def main():
    exerciciosWiki = open('./jsons/exercises.json', 'r').read()
    jsonData = json.loads(exerciciosWiki)
    print(jsonData)
    return 1


if __name__ == "__main__" : 
    main()