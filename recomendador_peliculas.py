import pandas as pd
import re

def choose_search_type():

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
    data_comprobacion = aux_2(data['Language'],language)
    if len(data_comprobacion) != len(data.axes[0]):
        print("WARNING: Your input is not a language")

    return data

def similar_films(df):
    film = input("What film do you want to look for? ", )
    data = pd.DataFrame(columns = ["Title","Genre","Premiere","Runtime","IMDB Score","Language"])
    encontrado = False
    for i in range(len(df.axes[0])):
        fila = df.iloc[i]
        if re.search(film,str(fila),re.IGNORECASE) != None or encontrado == True:
            data.loc[len(data)] = fila
            encontrado = True

    if len(data) == 0:
        print("We don't have the film you're looking for. Try another type of search")
        return data

    else:
        genero = data['Genre'][0]

        data_final = pd.DataFrame(columns = ["Title","Genre","Premiere","Runtime","IMDB Score","Language"])
        data_final = aux(data,genero)
        if len(data_final) == 1:
            # Si solo existe una película con ese género, te devuelve todas las que había encontrado al principio
            # Esto ocurre si la película tiene más de un género
            return data

    return data_final

if __name__ == "__main__":
    # Cargo el DataFrame que voy a utilizar
    df_peliculas = pd.read_csv('NetflixOriginals.csv',sep=",",encoding="LATIN_1")

    # Ordeno las películas según su puntuación, para que recomiende primero las mejores
    df_peliculas["IMDB Score"] = df_peliculas["IMDB Score"].astype(str).astype(float) 
    df_peliculas.sort_values(by=['IMDB Score'], inplace=True, ascending=False)

    # Puedes hacer tantas búsquedas como quieras
    opcion = choose_search_type()
    while opcion != False:

        if opcion == "1" or opcion == "genre":

            data = search_by_genre(df_peliculas)
            print(data.head(10) if len(data) != 0 else "We couldn't find any films from that genre")

        elif opcion == "2" or opcion == "language":

            data = search_by_language(df_peliculas)
            print(data.head(10) if len(data)!= 0 else "We couldn't find any films in that language")

        elif opcion == "3" or opcion == "film":

            data = similar_films(df_peliculas)
            if len(data) != 0:
                print("Try watching: ")
                print(data.head(10))
        else:
            print("Select a valid type search")
        print("")
        opcion = choose_search_type()




