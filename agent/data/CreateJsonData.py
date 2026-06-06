import json

from data.getData import getDataForJson

def createJson(data):
    print("criando json")
    file = open("dataPc.json", "w")
    json.dump(data,file)
    file.close()
    print("json criado")

def checkIfJsonExists():
    try:
        file = open("dataPc.json", "r")
        dataF = json.load(file)
        file.close()
        print("json já existe")
        return dataF

    except:
        print("json não existe")
        data = getDataForJson()
        createJson(data)
