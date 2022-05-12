import pandas as pd  
import os
import re


def ruta_carpeta_data():
    path='/Users/juanlu_navarro/Documents/Carrera Juan/programacion/Trabajo-final/Data'
    os.chdir(path)
ruta_carpeta_data()


def union(path):
    archivos= [ x for x in os.listdir() if re.search('.txt',x)]
    print(archivos) 
union(ruta_carpeta_data())
    

