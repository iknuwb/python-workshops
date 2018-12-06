import os
import shutil
from datetime import datetime

def zrobFolder(sciezka):
  try:
    os.makedirs(sciezka)
  except OSError:
    pass
  #-----------------------
def folder_zdjecia(folderGlowny,plik):
    data = datetime.utcfromtimestamp(os.path.getmtime(plik)).strftime('%Y-%m-%d %H:%M:%S')
    print("Kopiowanie pliku:",plik," Zmodyfikowane:", data)
    miesiac = datetime.utcfromtimestamp(os.path.getmtime(plik)).strftime('%m')
    mies = "/Brak"
    if miesiac == "01":
        mies = "/Styczen"
    elif miesiac == "02":
        mies = "/Luty"
    elif miesiac == "03":
        mies = "/Marzec"
    elif miesiac == "04":
        mies = "/Kwiecien"
    elif miesiac == "05":
        mies = "/Maj"
    elif miesiac == "06":
        mies = "/Czerwiec"
    elif miesiac == "07":
        mies = "/Lipiec"
    elif miesiac == "08":
        mies = "/Sierpien"
    elif miesiac == "09":
        mies = "/Wrzesien"
    elif miesiac == "10":
        mies = "/Pazdziernik"
    elif miesiac == "11":
        mies = "/Listopad"
    elif miesiac == "12":
        mies = "/Grudzien"
    nowyfolder = folderGlowny+mies
    zrobFolder(nowyfolder)
    shutil.copy2(plik, nowyfolder)


#-------------Gdzie są zdjęcia------------------
zdjecia_path = "D:/zdjecia/"
os.chdir(zdjecia_path)
#-------------Tworzenie folderu docelowego---------
path1 = "D:/Python/"
path2 = input("Podaj nazwę folderu \n")
path = path1+path2
print(path)
zrobFolder(path)
#------------Kopiowanie zdjęć i tworzenie podfolderów------------------
listaZdjec = os.listdir(zdjecia_path)
print("Znaleziono pliki: ",listaZdjec)
for i in range(len(listaZdjec)):
    folder_zdjecia(path, listaZdjec[i])

