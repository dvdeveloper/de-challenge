#Fecha: 30/12/2021
#Autor: Diego Valladares

from threading import Thread
import pandas as pd
import time
import argparse

def best_games_for_all_consoles(df,column):
    result = df.sort_values(column, ascending=False).head(REGISTROS)
    result.to_csv('output/best-games-for-all-consoles-'+str(REGISTROS)+'.csv')
    
def worst_games_for_all_consoles(df,column):
    result = df.sort_values(column, ascending=True).head(REGISTROS)
    result.to_csv('output/worst-games-for-all-consoles-'+str(REGISTROS)+'.csv')

def worst_games_console(df,column,filtro):
    result = df[df.console == filtro].sort_values(column, ascending=True).head(REGISTROS)
    result.to_csv('output/worst-'+str(REGISTROS)+'-'+str(filtro)+'.csv')

def top_games_console(df,column,filtro):
    result = df[df.console == filtro].sort_values(column, ascending=False).head(REGISTROS)
    result.to_csv('output/best-'+str(REGISTROS)+'-'+str(filtro)+'.csv')

if __name__ == '__main__':

    #argumentos
    COLUMN_FILTER = ['metascore','userscore']
    parser = argparse.ArgumentParser()
    parser.add_argument('-r',type=int,default=10,help='Cantidad de registro a mostrar, por defecto: 10')
    parser.add_argument('-f',type=str,default='metascore',help='Columna a utilizar para ordenamiento (sort) = metascore o userscore, por defecto: metascore')
    args = parser.parse_args()
    
    #parámetros generales
    CONSOLAS    = 'data/consoles.csv'
    ARCHIVO     = 'data/result.csv'
    REGISTROS   = args.r
    COLUMNA     = args.f if args.f in COLUMN_FILTER else COLUMN_FILTER[0] 

    inicio      = time.time()
    consoles    = pd.read_csv(CONSOLAS)['console'].tolist()
    df = pd.read_csv(ARCHIVO)
    
    for console in consoles:
        #mejor juego por consola
        Thread(target=top_games_console, args=(df,COLUMNA,console)).start()
    
        #peor juego por consola
        Thread(target=worst_games_console, args=(df,COLUMNA,console)).start()
        
    #mejor juego de todos
    best_games_for_all_consoles(df,COLUMNA)
    
    #peor juego de todos
    worst_games_for_all_consoles(df,COLUMNA)
    
    fin = time.time()
    tiempo = "Tiempo de ejecucion: " + str(round(fin-inicio,2)) + "s"
    
    print("-r: " + str(REGISTROS))
    print("-f: " + str(COLUMNA))
    print("Obtener más información: main.py --h");
    print(tiempo)
