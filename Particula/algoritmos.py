import math

def distancia_euclidiana(x_1=0.0, x_2=0.0, y_1=0.0, y_2=0.0):
    distancia = math.sqrt(((x_2-x_1)**2)+((y_2-y_1)**2))
    return distancia