# Importamos las librerias necesarias
import pandas as pd #ºpara trabajar con dataframes
import os #para trabajar con los directorios
import re #para trabajar con expresiones regulares

#PASO 1: Unimos los archivos de cada una de las carpetas ETFs y Stock



def ruta_carpeta_Stocks():
    path='/Users/juanlu_navarro/Documents/Carrera Juan/programacion/Trabajo-final/Stocks'
    os.chdir(path)
ruta_carpeta_Stocks()

def union_archivos_stocks(path):
    archivos= [ x for x in os.listdir() if re.search('.txt',x)]
    print(archivos)
    df= pd.DataFrame()
    for i in archivos:
        archivo=pd.read_csv(i)
        df= pd.concat([df,archivo])
        df.to_csv('datos_archivo_Stocks.csv', sep=';')
    return df
union_archivos_stocks(ruta_carpeta_Stocks())


