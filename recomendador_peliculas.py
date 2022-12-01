import pandas as pd
import re
import signal 
import sys 

def choose_search_type():
    # Selecciona una opción de entre las posibles
    # Si la entrada es ENTER, devuelve un False para salir del bucle principal
    # Si la entrada no es válida, devuelve un -1 que da un error controlado en el bucle principal

    print(" 1. Search by genre\n 2. Search by language\n 3. Search by similar films")
    opciones = ["1","2","3","genre","language","film"]
    opcion = input("Choose your search settings or press ENTER to exit: ",)
    if opcion in opciones:
        return opcion

    elif opcion == "":
        return False
    
    else:
        return -1

def aux(df,param):
    # Función auxiliar que recorre el DataFrame por filas buscando coincidencias con el parámetro indicado
    data = pd.DataFrame(columns = ["Title","Genre","Premiere","Runtime","IMDB Score","Language"])
    
    for i in range(len(df.axes[0])):
        fila = df.iloc[i]
        if re.search(param,str(fila),re.IGNORECASE) != None:
            data.loc[len(data)] = fila
    return data

def search_by_genre(df):
    # Utiliza la función auxiliar para buscar las filas con el género pedido
    genre = input("What genre would you like? ",)
    data = aux(df,genre)

    # Comprobar si el parametro introducido es un género
    data_comprobacion = aux_2(data['Genre'],genre)
    if len(data_comprobacion) != len(data.axes[0]):
        print("WARNING: Your input is not a valid genre")

    return data

def aux_2(columna,param):
    # Función para comprobar si el input corresponde con la categoría pediada por el usuario en primer lugar
    data_check = []
    for i in range(len(columna)):
        idioma = columna[i]
        if re.search(param,str(idioma),re.IGNORECASE) != None:
            data_check.append(idioma)
    return data_check 

def search_by_language(df):
    language = input("What language would you like? ", )
    data = aux(df,language)
    
    # Comprobar que la entrada inrtoducida es un idioma
    data_comprobacion = aux_2(data['Language'],language)
    if len(data_comprobacion) != len(data.axes[0]):
        print("WARNING: Your input is not a language")

    return data

def similar_films(df):
    film = input("What film do you want to look for? ", )
    data = pd.DataFrame(columns = ["Title","Genre","Premiere","Runtime","IMDB Score","Language"])
    encontrado = False

    # Añade todas las películas siguientes a las película introducida
    for i in range(len(df.axes[0])):
        fila = df.iloc[i]
        if re.search(film,str(fila),re.IGNORECASE) != None or encontrado == True:
            # Añade a data si encuentra la película por primera o si ya la ha encontrad
            data.loc[len(data)] = fila
            encontrado = True

    if len(data) == 0:
        print("We don't have the film you're looking for. Try another type of search")
        return data

    else:
        # Mejora de la búsqueda para que devuelva películas similares por género

        genero = data['Genre'][0]
        data_final = pd.DataFrame(columns = ["Title","Genre","Premiere","Runtime","IMDB Score","Language"])
        data_final = aux(data,genero)
        
        if len(data_final) == 1:
            # Si solo existe una película con ese género, te devuelve todas las que había encontrado al principio
            # Esto ocurre si la película tiene más de un género
            return data

    return data_final


def handler_signal(signal, frame):
    '''
    Función que maneja la señal SIGINT (CTRL + C)
    '''
    # Imprime un mensaje y sale del programa
    print("\n\n[!] Out ............. \n")
    sys.exit(1)

if __name__ == "__main__":

    signal.signal(signal.SIGINT, handler_signal)

    # Cargo el DataFrame que voy a utilizar
    df_peliculas = pd.read_csv('NetflixOriginals.csv',sep=",",encoding="LATIN_1")

    # Ordeno las películas según su puntuación, para que recomiende primero las mejores
    df_peliculas["IMDB Score"] = df_peliculas["IMDB Score"].astype(str).astype(float) 
    df_peliculas.sort_values(by=['IMDB Score'], inplace=True, ascending=False)

    # Selecciona la opción de búsqueda
    opcion = choose_search_type()

    # Puedes hacer tantas búsquedas como quieras
    while opcion != False:
        
        # Búsqueda por género
        if opcion == "1" or opcion == "genre":

            data = search_by_genre(df_peliculas)
            print(data.head(10) if len(data) != 0 else "We couldn't find any films from that genre")

        # Búsqueda por idioma
        elif opcion == "2" or opcion == "language":

            data = search_by_language(df_peliculas)
            print(data.head(10) if len(data)!= 0 else "We couldn't find any films in that language")

        # Búsqueda películas similares
        elif opcion == "3" or opcion == "film":

            data = similar_films(df_peliculas)
            
            # Solo lo imprime si hay películas
            # El caso contrario está gestionado en la función similar_films
            if len(data) != 0:
                print("Try watching: ")
                print(data.head(10))

        else:

            print("Select a valid type search")

        # Imprimir un espacio en blanco entre búsquedas para diferenciarlas
        print("")
        opcion = choose_search_type()




