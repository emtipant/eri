#Calcular la temperatura de las ciudades en una matriz 3D:

#Estructura de la matriz 3D

#Dimensiones: Ciudad x Semana x Día
#Ciudad: 0 (Pujilí), 1 (Quito), 2 (latacunga), etc.
#Semana: 0 (Semana 1), 1 (Semana 2), 2 (Semana 3), etc.
#Día: 0 (Lunes), 1 (Martes), 2 (Miércoles), 3 (Jueves), 4 (Viernes), 5 (Sábado), 6 (Domingo)

# Definir la matriz 3D
temperaturas = [
    # Pujilí
    [
        [18, 20, 19, 18, 17, 16, 15],  # Semana 1
        [19, 21, 20, 19, 18, 17, 16],  # Semana 2
        [20, 22, 21, 20, 19, 18, 17]   # Semana 3
    ],
    # Quito
    [
        [12, 14, 13, 12, 11, 10, 9],   # Semana 1
        [13, 15, 14, 13, 12, 11, 10],  # Semana 2
        [14, 16, 15, 14, 13, 12, 11]   # Semana 3
    ],
    #Latacunga
    [
        [22, 24, 23, 22, 21, 20, 19],  # Semana 1
        [23, 25, 24, 23, 22, 21, 20],  # Semana 2
        [24, 26, 25, 24, 23, 22, 21]   # Semana 3
    ]
]

# Calcular el promedio de temperatura para cada ciudad y semana
ciudades = ["Pujilí", "Quito", "Latacunga"]
for i, ciudad in enumerate(ciudades):
    for j in range(len(temperaturas[i])):
        suma = sum(temperaturas[i][j])
        promedio = suma / len(temperaturas[i][j])
        print(f"Promedio de temperatura en {ciudad} durante la semana {j+1}: {promedio:.2f}°C")

