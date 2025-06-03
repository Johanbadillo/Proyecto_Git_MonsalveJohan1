import json

def abrirJSON():
    dicFinal=[]
    with open("./data/datos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./data/datos.json",'w') as outFile:
        json.dump(dic,outFile)
