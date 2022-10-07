import requests

print("Benvenuto nel tool iptv. Inserisci le informazioni per proseguire: ")
nameP = input("Inserisci il nome utente della lista:")
serverP = input("Inserisci il server (nomeserver:porta):")
passwordP = input("Inserisci la password della lista:")
listaP = ('http://'+serverP+'/get.php?username='+nameP+'&password='+passwordP+'&type=m3u&output=hls')
responseC = requests.get(listaP)
open("lista.m3u", "wb").write(responseC.content)

print("Per far funzionare al meglio il programma eliminare i live aprendo il file m3u con il blocco note. Lasiciare all'inizo #EXTM3U")


e = input("Premi un tasto per continuare!")
