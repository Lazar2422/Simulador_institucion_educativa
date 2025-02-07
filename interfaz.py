import json

def abrirJSON():
    dicFinal={}
    with open("./estudiantes.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./estudiantes.json",'w') as outFile:
        json.dump(dic,outFile)
f=True
estudiante={}
while f==True:
    estudiante=abrirJSON()
    print("Que desea hacer?")
    print("Para ver la informacion de los estudiantes presione 1")
    x=int(input(": "))
    if x==1:
        for i in range(len(estudiante["estudiante"])):
            y=str(0)
            met1=estudiante[y][i]
            hab1=estudiante[y][i]
            gar1=estudiante[y][i]
            año1=estudiante[y][i]
            zon1=estudiante[y][i]
            print(met1,hab1,gar1,año1,zon1)