import requests
from googletrans import Translator

trans=Translator()

def mahsulot(name):
    responce=requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')
    asd=responce.json()
    lang=asd['meals'][0]['strInstructions']
    t=trans.translate(lang,dest='uz')
    return (f"Name: {asd['meals'][0]['strMeal']}\n\nRecept: {t.text}\n\n\nPhoto:\n{asd['meals'][0]['strMealThumb']}\n\n"
            f"Video Instruction:\n{asd['meals'][0]['strYoutube']}")

def random():
    responce=requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    asd=responce.json()
    lang=asd['meals'][0]['strInstructions']
    t=trans.translate(lang,dest='uz')
    return (f"Name: {asd['meals'][0]['strMeal']}\n\nRecept: {t.text}\n\n\n"
            f"Video Instruction:\n{asd['meals'][0]['strYoutube']}")

def random1():
    responce=requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    asd=responce.json()
    return asd['meals'][0]['strMealThumb']