def mostrar_menu(opciones):
    '''
Es la funcion que me permite realizar un menu de opciones.
    '''  
    print(opciones)
    opcion=int(input("Ingrese una opción: "))
   
    return opcion

def validar_nota(nota):
    '''
    Valida que la nota esté entre 1 y 10 (como string).
    '''
    es_valida = False

    if len(nota) == 1 and nota >= "1" and nota <= "9":
        es_valida = True
    elif len(nota) == 2 and nota == "10":
        es_valida = True

    return es_valida

def validar_legajo(legajo)-> None:
    '''
Valida que el legajo tenga 5 cifras numéricas.
    '''
    es_valido = False

    if len(legajo) == 5:
        es_valido = True
        for c in legajo:
            if c < "0" or c > "9":
                es_valido = False
                break
            
    return es_valido


def mostrar_uno(nota, nombre, genero, legajo, promedio)-> None:
    '''
Devuelve una cadena con los datos de un solo estudiante.
    '''
    mostrar = f"Legajo: {legajo} - Nombre: {nombre} - Género: {genero} - Notas: {nota} - Promedio: {promedio}"
    
    return mostrar


def mostrar_todos(notas, nombres, generos, legajos, promedios):
    '''
Muestra todos los estudiantes
    '''
    mostrar = ""  # Acumula todo el texto
    for i in range(len(notas)):
        if len(promedios) == len(notas):
            mostrar += mostrar_uno(notas[i], nombres[i], generos[i], legajos[i], promedios[i]) + "\n"
        else:
            mostrar += mostrar_uno(notas[i], nombres[i], generos[i], legajos[i], "-") + "\n"
    
    return print(mostrar)

'''
Calcula el promedio de cada estudiante
'''
def calcular_promedios(notas):
    '''
Calcula el promedio de cada estudiante
    '''
    promedios = [0] * len(notas)  # Creo una lista con la cantidad correcta de elementos
    for i in range(len(notas)):
        suma = 0
        for nota in notas[i]:
            suma = suma + nota
        promedio = suma / 5
        promedios[i] = promedio  # Asigno el promedio en la posición i
   
    return promedios


def ordenar_por_promedio(notas, nombres, generos, legajos, promedios, orden):
    '''
Ordena los estudiantes según promedio
    '''
    largo = len(promedios)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if (orden == "DESC" and promedios[i] < promedios[j]) or (orden == "ASC" and promedios[i] > promedios[j]):
                # Intercambiar todos los elementos
                promedios[i], promedios[j] = promedios[j], promedios[i]
                nombres[i], nombres[j] = nombres[j], nombres[i]
                generos[i], generos[j] = generos[j], generos[i]
                legajos[i], legajos[j] = legajos[j], legajos[i]
                notas[i], notas[j] = notas[j], notas[i]
    return notas, nombres, generos, legajos, promedios



def materia_mayor_promedio(notas):
    '''
Muestra la materia con mayor promedio general
    '''
    cant_alumnos = len(notas)
    cant_materias = 5
    mayores = [-1] * cant_materias  # Lista con tamaño fijo
    k = 0  # Posición donde guardar la próxima materia
    mayor_prom = 0

    for j in range(cant_materias):
        suma = 0
        for i in range(cant_alumnos):
            suma = suma + notas[i][j]
        promedio = suma / cant_alumnos

        if j == 0 or promedio > mayor_prom:
            mayor_prom = promedio
            mayores[0] = j
            k = 1
        elif promedio == mayor_prom:
            mayores[k] = j
            k = k + 1

    # Armamos un texto con las materias
    resultado = "Materia/s con mayor promedio:\n"
    for i in range(k):
        resultado += f"MATERIA_{mayores[i] + 1}" + "\n"
    
    return resultado


def buscar_estudiante(notas, nombres, generos, legajos, promedios, legajo_buscado):
    '''
Buscar estudiante por legajo
    '''
    i = 0
    resultado = "Estudiante no encontrado"
    while i < len(legajos):
        if legajos[i] == legajo_buscado:
            resultado = mostrar_uno(notas[i], nombres[i], generos[i], legajos[i], promedios[i])
            break
        i = i + 1
    return print(resultado)

def contar_notas_por_materia(matriz, indice_materia):

    repeticiones = [0] * 10  # índices 0 a 9 representan notas 1 a 10
    for fila in matriz:
        nota = fila[indice_materia]
        if nota >= 1 and nota <= 10:
            repeticiones[nota - 1] += 1
    return repeticiones
