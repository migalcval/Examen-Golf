from jugadores import *

def mostrar_iterable(iterable):
    for elem in iterable:
        print(elem)

def mostrar_dicc(dicc):
    for clave, valor in dicc.items():
        print(f"{clave} ---> {valor}")

# --------- EJERCICIO 1 --------------------------------------------------------------------------------------------------------------------------------

def test_lee_jugadores(datos):
    print(f"Se han leído {len(datos)} jugadores")
    print("Los 3 primeros jugadores son:")
    mostrar_iterable(datos[:3])
    print("Los 3 ultimos jugadores son:")
    mostrar_iterable(datos[-3:])

# --------- EJERCICIO 2 --------------------------------------------------------------------------------------------------------------------------------
    
def test_mejores_jugadores(datos, anyo, n):
    res = mejores_jugadores(datos, anyo, n)
    print(f"Los {n} mejores jugadores nacidos en el {anyo} son: {res}")

# --------- EJERCICIO 3 --------------------------------------------------------------------------------------------------------------------------------

def test_jugadores_por_golpes(datos):
    res = jugadores_por_golpes(datos)
    mostrar_iterable(res)

# --------- EJERCICIO 4 --------------------------------------------------------------------------------------------------------------------------------

def test_promedio_ultimos_resultados(datos, f1=None, f2=None):
    res = promedio_ultimos_resultados(datos, f2, f2)
    print(f"El promedio de cada jugador senior con fecha de actualización entre {f1} y {f2} son: {res}")

# --------- EJERCICIO 5 --------------------------------------------------------------------------------------------------------------------------------

def test_jugador_menor_handicap_por_federacion(datos):
    res = jugador_menor_handicap_por_federacion(datos)
    mostrar_dicc(res)

if __name__=="__main__":

    datos = lee_jugadores("data/jugadores.csv")

    print("EJERCICIO 1")
    test_lee_jugadores(datos)
    print("EJERCICIO 2")
    test_mejores_jugadores(datos, 1969, 4)
    print("EJERCICIO 3")
    test_jugadores_por_golpes(datos)
    print("EJERCICIO 4")
    f1 = date(2020,3,1)
    f2 = date(2020,5,31)
    test_promedio_ultimos_resultados(datos, f1, f2)
    print("EJERCICIO 5")
    test_jugador_menor_handicap_por_federacion(datos)