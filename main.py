from mis_funciones import *

nombres = [
            "Leslie Lopez", "Bruno Diaz", "Carla Gómez", "Diego Torres", "Elena Vega",
            "Francisco Ruiz", "Gabriela Mendez", "Hugo Silva", "Irene Ríos", "Joaquin Perez",
            "Karina Sosa", "Luis Ortega", "Marta Funes", "Nicolas Castro", "Olga Herrera",
            "Pablo Varela", "Quintina Gil", "Raul Vazquez", "Sofia Moreno", "Tomas Gimenez",
            "Ursula Peña", "Valeria Cruz", "Walter Álvarez", "Ximena Luna", "Alex Salas",
            "Zoe Molina", "Ariel Bracco", "Beatriz Soto", "Cesar Pineda", "Daniela Juárez"
        ]

generos = [
            "X", "M", "F", "M", "F", "M", "F", "M", "F", "M",
            "F", "M", "F", "M", "F", "M", "F", "M", "F", "M",
            "F", "F", "M", "F", "X", "F", "M", "F", "M", "F"
        ]

legajos = [
            10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010,
            10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019, 10020,
            10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029, 10030
        ]


notas = [
            [8, 7, 6, 9, 7], [6, 5, 7, 6, 5], [9, 9, 10, 10, 9], [4, 6, 5, 7, 5], [7, 8, 6, 9, 8],
            [6, 6, 7, 6, 6], [10, 10, 9, 9, 10], [5, 5, 6, 5, 6], [8, 8, 7, 8, 7], [7, 6, 8, 6, 7],
            [9, 9, 9, 9, 9], [5, 6, 5, 6, 5], [8, 9, 8, 8, 9], [6, 7, 6, 7, 6], [10, 9, 10, 10, 9],
            [4, 5, 4, 5, 4], [7, 8, 7, 8, 7], [5, 5, 5, 5, 5], [9, 8, 9, 8, 9], [6, 6, 7, 6, 6],
            [8, 8, 8, 8, 8], [9, 9, 10, 9, 10], [4, 4, 5, 5, 4], [7, 6, 7, 6, 7], [10, 10, 10, 10, 10],
            [5, 6, 5, 6, 5], [9, 8, 9, 8, 9], [6, 6, 6, 6, 6], [8, 8, 7, 7, 8], [7, 7, 8, 8, 7]
        ]

promedios = []


while True:
    print("\nMENÚ DE OPCIONES")
    print("1 – Mostrar todos los datos")
    print("2 – Calcular promedio por estudiante")
    print("3 – Ordenar por promedio")
    print("4 – Materia con mayor promedio")
    print("5 – Buscar estudiante por legajo")
    print("6 – Salir")

    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            mostrar_todos(notas, nombres, generos, legajos, promedios)
        case "2":
            promedios = calcular_promedios(notas)
            print("Promedios calculados.")
        case "3":
            if len(promedios) > 0:
                ordenar_por_promedio(notas, nombres, generos, legajos, promedios, "DESC")
                mostrar_todos(notas, nombres, generos, legajos, promedios)
            else:
                print("Primero debe calcular los promedios.")
        case "4":
            print(materia_mayor_promedio(notas))
        case "5":
            if len(promedios) > 0:
                legajo_buscar = input("Ingrese el legajo a buscar: ")
                if validar_legajo(legajo_buscar):
                    legajo_buscar = int(legajo_buscar)
                    buscar_estudiante(notas, nombres, generos, legajos, promedios, legajo_buscar)
                else:
                    print("Legajo inválido.")
            else:
                print("Primero debe calcular los promedios.")
        case "6":
            print("Fin del programa.")
            break
        case _:
            print("Opción no válida.")
