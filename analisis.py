# Importamos las librerias necesarias
import pandas as pd #ºpara trabajar con dataframes
import os #para trabajar con los directorios
import re #para trabajar con expresiones regulares
import matplotlib.pyplot as plt
import seaborn as sns


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
        df.to_csv('datos_archivo_ETFs.csv', sep=';')
    return df
union_archivos_ETFs(ruta_carpeta_ETFs())

def renombrar_columnas_ETFs(df):
    df.rename(columns={'Open':'Apertura','High':'Crecimiento','Low':'Bajadas','Close':'Finalizado','Volume':'Volumen'}, inplace=True)
    return df
renombrar_columnas_ETFs(union_archivos_ETFs(ruta_carpeta_ETFs()))


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

#saca una grafica con como evoluciona volumen de cada uno de los archivos
def grafica_volumen_ETFs(df):
    df_volumen=df.groupby('Date').sum()
    df_volumen.plot(x='Date',y='Volume')
    plt.show()
grafica_volumen_ETFs(union_archivos_ETFs(ruta_carpeta_ETFs()))



