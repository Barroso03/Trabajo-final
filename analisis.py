# Importamos las librerias necesarias
import pandas as pd #ºpara trabajar con dataframes
import os #para trabajar con los directorios
import re #para trabajar con expresiones regulares

#PASO 1: Unimos los archivos de cada una de las carpetas ETFs y Stock

def ruta_carpeta_ETFs():
    path='/Users/juanlu_navarro/Documents/Carrera Juan/programacion/Trabajo-final/ETFs'
    os.chdir(path)
ruta_carpeta_ETFs()

def union_archivos_ETFs(path):
    archivos= [ x for x in os.listdir() if re.search('.txt',x)]
    print(archivos)
    df= pd.DataFrame()
    for i in archivos:
        archivo=pd.read_csv(i)
        df= pd.concat([df,archivo])
        df.to_csv('datos_archivo_ETFs.csv')
    return df
union_archivos_ETFs(ruta_carpeta_ETFs())

