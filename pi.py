#Alexandre Silveira Jozala
#RA00279987

import math
import random

Npontos_quadrado = int(input('Digite o Número de pontos do Quadrado: '))
Npontos_circulo = 0

acumulador = 1 
while acumulador <= Npontos_quadrado:
    Px = random.random()
    Py = random.random()
    deltaX = math.pow((Px-0.5),2)
    deltaY = math.pow((Py-0.5),2)
    DistE = math.sqrt(deltaX+deltaY)
    if DistE < 0.5:
        Npontos_circulo = Npontos_circulo + 1
    acumulador = acumulador + 1

ValorPi = 4*(float(Npontos_circulo))/(float(Npontos_quadrado)) 

print("O Valor Aproximado de π é %.3f" %ValorPi)