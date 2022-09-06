import requests
import sqlite3

def getRequestJson():
    BASE_URL = requests.get(f'https://rickandmortyapi.com/api/character')
    BASE_URL_JSON = BASE_URL.json()

    return BASE_URL_JSON

def database(character):
    con = sqlite3.connect('rick-and-morty.db')
    cur = con.cursor()

    try:
        cur.execute('CREATE TABLE characters (id, name, status, species, type,gender, origin, location, image, episode, url, created)')
    except:
        pass

    con.execute(
        "INSERT INTO characters (id, name, status, species, type,gender, origin, location, image, episode, url, created) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?)",
        ((character["id"]), (character["name"]), (character["status"]), (character["species"]), (character["type"]),
        (character["gender"]), str(character["origin"]), str(character["location"]),
        str(character["image"]), str(character["episode"]), (character["url"]), (character["created"]))
    )
    con.commit()
    con.close()

def getUser():
    countCharacter = int(getRequestJson()['info']['count'])
    # count = idCharacter - paramter URL
    count = 1
    countAliveHuman = 0

    for i in range(countCharacter):
        r = requests.get(f'https://rickandmortyapi.com/api/character/{count}')
        rJson = r.json()

        # verificar se sao humanos vivos,se sim guardar os dados em um dicionario
        if ('Human' in rJson['species']) and ('Alive' in rJson['status']):
            character = {
                "id": rJson["id"],
                "name": rJson["name"],
                "status": rJson["status"],
                "species": rJson["species"],
                "type": rJson["type"],
                "gender": rJson["gender"],
                "origin": rJson["origin"],
                "location": rJson["location"],
                "image": rJson["image"],
                "episode": rJson["episode"],
                "url": rJson["url"],
                "created": rJson["created"]
            }
            countAliveHuman = countAliveHuman + 1
            print(f"{countAliveHuman} - Salvando...")
            database(character)
        count = count + 1

getUser()











