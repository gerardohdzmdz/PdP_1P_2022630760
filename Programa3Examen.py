# Código hecho por: Cuevas Romero Desire y Hernández Méndez Gerardo Antonio. Grupo 3BV2. Paradigmas de Programación.
# Libreria de funciones
import math

class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Funcion que calcula la distancia entre dos puntos
def distancia_euclidiana(punto1, punto2):
    dx = punto2.x - punto1.x
    dy = punto2.y - punto1.y
    dz = punto2.z - punto1.z

    distancia = math.sqrt(dx**2 + dy**2 + dz**2)
    return distancia

# funcion que encuentra los dos puntos mas cercanos entre si del arreglo 'puntos'
def encontrar_par_mas_cercano(puntos):
    num_puntos = len(puntos)
    if num_puntos < 2:
        return None

    par_cercano = (puntos[0], puntos[1])
    distancia_minima = distancia_euclidiana(puntos[0], puntos[1])

    for i in range(num_puntos):
        for j in range(i + 1, num_puntos):
            distancia = distancia_euclidiana(puntos[i], puntos[j])
            if distancia < distancia_minima:
                distancia_minima = distancia
                par_cercano = (puntos[i], puntos[j])

    return par_cercano


# Ingreso de puntos desde el código
puntos = []
num_puntos = 20

for i in range(num_puntos):
    print("Ingrese las coordenadas para el punto", i + 1)
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))
    z = float(input("Ingrese la coordenada z: "))

    punto = Punto3D(x, y, z)
    puntos.append(punto)

par_cercano = encontrar_par_mas_cercano(puntos)

if par_cercano is not None:
    punto_a, punto_b = par_cercano
    print("El par más cercano de puntos es:")
    print("Punto A:", punto_a.x, punto_a.y, punto_a.z)
    print("Punto B:", punto_b.x, punto_b.y, punto_b.z)
    print("Distancia:", distancia_euclidiana(punto_a, punto_b))
else:
    print("No hay suficientes puntos para encontrar un par cercano.")