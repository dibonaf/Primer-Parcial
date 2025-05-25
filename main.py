from mis_funciones import *

nombres = [
            "Leslie Lopez", "Luciano Cabral", "Carla Gómez", "Diego Torres", "Elena Vega",
            "Francisco Ruiz", "Gabriela Mendez", "Hugo Silva", "Irene Ríos", "Joaquin Perez",
            "Karina Sosa", "Luis Ortega", "Marta Funes", "Alvaro Angulo", "Olga Herrera",
            "Pablo Varela", "Quintina Gil", "Raul Vazquez", "Sofia Moreno", "Tomas Gimenez",
            "Ursula Peña", "Valeria Cruz", "Walter Álvarez", "Ximena Luna", "Ricardo Enrique Bochini",
            "Zoe Molina", "Kevin Lomonaco", "Beatriz Soto", "Julio Vaccari", "Daniela Juárez"
        ]

generos = [
            "X", "M", "F", "M", "F", "M", "F", "M", "F", "M",
            "F", "M", "F", "M", "F", "M", "F", "M", "F", "M",
            "F", "F", "M", "F", "M", "F", "M", "F", "M", "F"
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

datos_cargados = False

while True:
    
    opcion= mostrar_menu("\nMENÚ DE OPCIONES" "\n1 – Cagar los datos" "\n2 – Mostrar todos los datos" "\n3 – Calcular promedio por estudiante" "\n4 – Ordenar por promedio" "\n5 – Materia con mayor promedio" "\n6 – Buscar estudiante por legajo" "\n7 - Contar repeticiones de calificaciones por materia"  "\n8 – Salir")
   
    match opcion:
        case 1:
            datos_cargados = True
            print("Datos cargados exitosamente.")
            
        case 2:
            if datos_cargados:
                mostrar_todos(notas, nombres, generos, legajos, promedios)
            else:
                print("Debe cargar los datos primero (opción 1).")

        case 3:
            if datos_cargados:
                promedios = calcular_promedios(notas)
                print("Promedios calculados.")
            else:
                print("Debe cargar los datos primero (opción 1).")

        case 4:
            if datos_cargados:
                if len(promedios) > 0:
                    ordenar_por_promedio(notas, nombres, generos, legajos, promedios, "DESC")
                    mostrar_todos(notas, nombres, generos, legajos, promedios)
                else:
                    print("Primero debe calcular los promedios.")
            else:
                print("Debe cargar los datos primero (opción 1).")

        case 5:
            if datos_cargados:
                print(materia_mayor_promedio(notas))
            else:
                print("Debe cargar los datos primero (opción 1).")

        case 6:
            if datos_cargados:
                if len(promedios) > 0:
                    legajo_buscar = input("Ingrese el legajo a buscar: ")
                    if validar_legajo(legajo_buscar):
                        legajo_buscar = int(legajo_buscar)
                        buscar_estudiante(notas, nombres, generos, legajos, promedios, legajo_buscar)
                    else:
                        print("Legajo inválido.")
                else:
                    print("Primero debe calcular los promedios.")
            else:
                print("Debe cargar los datos primero (opción 1).")

        case 7:
            if datos_cargados:
                materia = input("Ingrese el número de materia (1 a 5): ")
                while materia not in ["1", "2", "3", "4", "5"]:
                    materia = input("Número inválido. Ingrese un número entre 1 y 5: ")
                materia = int(materia) - 1
                repeticiones = contar_notas_por_materia(notas, materia)
                print(f"Repeticiones de cada nota en la materia {materia + 1}:")
                for i in range(10):
                    print(f"Nota {i + 1}: {repeticiones[i]} vez/veces")
            else:
                print("Debe cargar los datos primero (opción 1).")

        case 8:
            print("Fin del programa.")
            break

        case _:
            print("Opción no válida.")
