import os
import requests


#############################################################
#      VARIABILI CHE DOVETE SISTEMARE A VOSTRO PIACIMENTO
#############################################################
FILEDASCARICARE = 100
DIRECTORYDOWN = "C:/download/"   #SCRIVERE IN QUESTO MODO


##############################################################
#           NON MODIFICARE PIu' NIENTE !
#############################################################

os.system('cls' )

filename = open("Data/name.txt","r+",errors="ignore")
fileflux = open("Data/flux.txt","r+",errors="ignore")

reset = input("Desideri resettare la memoria (si / no): ")

if reset == "si":
    filename.truncate()
    fileflux.truncate()
    filename.write("1")
    filename.close()
    fileflux.write("2")
    fileflux.close()
else:
    print("Avvio del programma seguendo i vecchi dati")

filename = open("Data/name.txt","r+")
fileflux = open("Data/flux.txt","r+")
i = 0
lineaname = filename.read()
lineaflux = fileflux.read()
filescaricati = 0

listass = input("Inserisci il nome della lista(.m3u): ")

while i < FILEDASCARICARE: #MODIFICARE IL 10 PER IL NUMERO DEI DOWNLOAD CHE SI VOGLIONO FARE
    i+=1
    print("")
    print("-----------------------------")
    print("File scaricati: ")
    print(filescaricati)
    print("")
    print("-----------------------------")
    with open(listass) as f:
        lineaname = (int(lineaname)+ 2)
        name = f.readlines()[lineaname]
        name = name.replace("#EXTINF:-1,", "")
        name = name.replace(":", "-")
        print("download in corso di : "+name)

    with open(listass) as f:
        lineaflux = (int(lineaflux)+2)
        flusso = f.readlines()[lineaflux]
        print(flusso)
        responseD = requests.get(flusso)
        if responseD.status_code == 200:

            namedow = (DIRECTORYDOWN+name+ ".mkv")   #ATTENZIONE !! QUI BISOGNA INSERIRE LA DIRECTORY DOVE SCARICARE!
            namedow = namedow.replace("\n","")
            open(namedow, "wb").write(responseD.content )
            filescaricati = filescaricati+1
            print("Download finito!")
        else:
            pass
        f = open("Data/name.txt","w")
        f.write(str(lineaname))
        f2 = open("Data/flux.txt","w")
        f2.write(str(lineaflux))

    os.system('cls' )
