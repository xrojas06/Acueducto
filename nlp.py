import re

def busqueda(texto):
    elementos_a_buscar= ['Avenida Primera de Mayo', 'Avenida Boyacá', 'Avenida Villavicencio']

    patron_calle = r'Calle\s+(\d+[A-Z]?(?:\s+Sur)?(?:\s+Bis(?:\s+Sur)?)?)'
    patron_carrera = r'Carrera\s+(\d+[A-Z]?(?:\s+Sur)?(?:\s+Bis(?:\s+Sur)?)?)'
    patron_transversal = r'Transversal\s+(\d+[A-Z]?(?:\s+Sur)?(?:\s+Bis(?:\s+Sur)?)?)'
    patron_diagonal = r'Diagonal\s+(\d+[A-Z]?(?:\s+Sur)?(?:\s+Bis(?:\s+Sur)?)?)'
    patron_avenida = '|'.join(map(re.escape, elementos_a_buscar))
    coincidencias_1 = re.findall(patron_calle, texto)
    coincidencias_2 = re.findall(patron_carrera, texto)
    coincidencias_3 = re.findall(patron_diagonal, texto)
    coincidencias_4 = re.findall(patron_transversal, texto)
    coincidencias_5 = re.findall(patron_avenida, texto)
    coincidencias = [coincidencias_1, coincidencias_2, coincidencias_3, coincidencias_4, coincidencias_5]
    lista = ['Calle', 'Carrera','Transversal','Diagonal','Avenidas']
    dicc = {}
    for i,match in enumerate(coincidencias):
        dicc[lista[i]] = match

    return dicc
