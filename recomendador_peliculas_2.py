import sys
import re
import pandas as pd

def procesar_argumentos_entrada(argumentos):

    parametro = argumentos[1]
    if len(argumentos)>1:
        parametro_2 = argumentos[2]
    return parametro

def aux(df,param):
    # Función auxiliar que recorre el DataFrame por filas buscando coincidencias con el parámetro indicado
    data = pd.DataFrame(columns = ["Title","Genre","Premiere","Runtime","IMDB Score","Language"])
    
    for i in range(len(df.axes[0])):
        fila = df.iloc[i]
        if re.search(param,str(fila),re.IGNORECASE) != None:
            data.loc[len(data)] = fila
    return data

 

if __name__ == "__main__":
    parametro = procesar_argumentos_entrada(sys.argv)

    # Cargo el DataFrame que voy a utilizar
    df_peliculas = pd.read_csv('NetflixOriginals.csv',sep=",",encoding="LATIN_1")

    # Ordeno las películas según su puntuación, para que recomiende primero las mejores
    df_peliculas["IMDB Score"] = df_peliculas["IMDB Score"].astype(str).astype(float) 
    df_peliculas.sort_values(by=['IMDB Score'], inplace=True, ascending=False)


    recomendadas = aux(df_peliculas,parametro)
    print(recomendadas.head(10))