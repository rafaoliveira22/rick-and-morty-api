import requests
import sqlite3

def getRequestJson():
    BASE_URL = requests.get(f'https://rickandmortyapi.com/api/character')
    BASE_URL_JSON = BASE_URL.json()

    return BASE_URL_JSON

def database(character):
    con = sqlite3.connect('teste.db')
    cur = con.cursor()

    try:
        cur.execute('CREATE TABLE characters (id,name,status,species)')
    except:
        pass

    con.execute(f"""INSERT INTO characters VALUES ("{character['id']}", "{character['name']}", "{character['status']}", "{character['species']}")""")
    con.commit()

    con.close()

def getUser():
    countCharacter = int(getRequestJson()['info']['count'])
    # count = idCharacter - paramter URL
    count = 1

    for i in range(countCharacter):
        r = requests.get(f'https://rickandmortyapi.com/api/character/{count}')
        rJson = r.json()

        # verificar se sao humanos vivos,se sim guardar os dados em um dicionario
        if ('Human' in rJson['species']) and ('Alive' in rJson['status']):
            character = {
                'id': rJson['id'],
                'name': rJson['name'],
                'status': rJson['status'],
                'species': rJson['species']
            }

            database(character)
        count = count + 1

getUser()











