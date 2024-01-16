from collections import defaultdict
from datetime import *
from typing import NamedTuple, List, Tuple, Optional, Union, Dict
import csv

Jugador = NamedTuple('Jugador', [('ape_nom', str), ('licencia', str), ('fecha_nacto', date), ('federacion', str), ('handicap', float), 
                                 ('fec_hor_act', datetime), ('senior', bool), ('resultados', list)])

# --------- EJERCICIO 1 --------------------------------------------------------------------------------------------------------------------------------

def lee_jugadores(fichero:str) -> List[Jugador]:

    registros = []
    with open(fichero, encoding = 'UTF-8') as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados in lector:

            fecha_ncto = datetime.strptime(fecha_ncto, "%d/%m/%Y").date()
            handicap = float(handicap)
            fec_hor_act = datetime.strptime(fec_hor_act, "%d/%m/%Y %H:%M:%S")
            senior = parse_bool(senior)
            resultados = parse_lista(resultados)

            tupla = Jugador(ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados)
            registros.append(tupla)

    return registros

def parse_bool(cadena):
    valor = None
    if cadena == "S":
        valor = True
    elif valor == "N":
        valor = False
    return valor   

def parse_lista(cadena):

    return cadena.split(",")

# --------- EJERCICIO 2 --------------------------------------------------------------------------------------------------------------------------------

def mejores_jugadores(jugadores:List[Jugador], anyo:int, n:int) -> List[Tuple[str, str, float]]:

    lista = []
    for j in jugadores:
        if j.fecha_nacto.year == anyo:
            lista.append((j.licencia, j.ape_nom, j.handicap))

    return sorted(lista, key=lambda x:x[2])[:n]

# --------- EJERCICIO 3 --------------------------------------------------------------------------------------------------------------------------------

def jugadores_por_golpes(jugadores:List[Jugador]) -> List[Tuple[int, List[str]]]:

    d = licencias_por_numero_de_golpes(jugadores)
    lista = []

    for clave, valor in d.items():
        lista.append((clave, valor))

    return sorted(lista, key=lambda x:x[0], reverse= True)


def licencias_por_numero_de_golpes(jugadores):

    dicc = defaultdict(set)
    for j in jugadores:
        for elem in j.resultados:
            dicc[elem].add(j.licencia)

    return dicc

# --------- EJERCICIO 4 --------------------------------------------------------------------------------------------------------------------------------

def promedio_ultimos_resultados(jugadores:List[Jugador], f1:Optional[Union[date, None]]=None, f2:Optional[Union[date, None]]=None):

    d = golpes_por_licencia(jugadores)
    lista = []

    for j in jugadores:
        for clave, valor in d.items():
            if ((j.senior is True) and ((f1 is None or j.fec_hor_act.date() >= f1) and (f2 is None or j.fec_hor_act.date() <= f2))):
                media = sum(valor)/len(valor)
                lista.append((clave, media))

    return lista

def golpes_por_licencia(jugadores):

    dicc = defaultdict(list)
    for j in jugadores:
        for elem in j.resultados:
            dicc[j.licencia].append(int(elem))

    return dicc

# --------- EJERCICIO 5 --------------------------------------------------------------------------------------------------------------------------------

def jugador_menor_handicap_por_federacion(jugadores:List[Jugador]) -> Dict[str, Tuple[str, float]]:

    d = jugadores_por_federacion(jugadores)
    dicc = defaultdict(list)

    for clave, valor in d.items():
        ordenado = sorted(valor, key=lambda x:x[1])[:1]
        dicc[clave].append(ordenado)

    return dicc

def jugadores_por_federacion(jugadores):
    
    dicc = defaultdict(list)
    for j in jugadores:
        dicc[j.federacion].append((j.ape_nom, j.handicap))

    return dicc