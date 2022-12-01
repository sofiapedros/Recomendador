# Recomendador
En el repositorio se encuentran dos ficheros:
- recomendador.py
- requirements.txt

RECOMENDADOR.py
Recomendador de películas usando expresiones regulares.

Permite buscar películas por género e idioma, además de buscar películas similares a una dada.
Para este último tipo de búsqueda, recomienda películas del mismo género que la pedida en caso de que existan, o peliculas
cercanas en calificación a la película pedida.
En todos los casos, devuelve las películas de mayor calificación primero.
En cada búsqueda, devuelve un máximo de 10 películas en forma de dataframe con los datos relevantes de la(s) película(s) buscada(s).

Para su correcto funcionamiento, se ejecuta el programa .py y se solicita al usuario que seleccione un tipo de búsqueda de las opciones dadas por teclado (solicita una opción hasta que la opción dada sea válida). Después, se debe introducir el título de la película que se desea buscar. Se pueden hacer tantas búsquedas cómo se deseen y para salir se debe pulsar ENTER. 

requirements.txt
Fichero de texto con las librerías utilizadas para que el usuario se las pueda descargar con pip install -r requirements.txt
