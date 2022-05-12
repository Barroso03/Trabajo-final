# Importamos las librerias necesarias
import pandas as pd #ºpara trabajar con dataframes
import os #para trabajar con los directorios
import re #para trabajar con expresiones regulares

#PASO 1: Unimos los archivos de cada una de las carpetas ETFs y Stock

def ruta_carpeta_ETFs():
    path='/Users/hectorbernaltrujillo/Downloads/archive (3)/ETFs'
    os.chdir(path)
ruta_carpeta_ETFs()

def union_datos_ETFs():
    archivos= [x for x in os.listdir() if re.search('.txt',x)]
    print(archivos)
    dataset_ETFs=pd.DataFrame()
    for i in archivos:
        archivo=pd.read_csv(i)
        dataset_ETFs= pd.concat[(dataset_ETFs,archivo)]
    dataset_ETFs.to_csv('union_datos_ETFs.csv')
    return dataset_ETFs
union_datos_ETFs()





