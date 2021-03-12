#-----------  IMPORTACIONES  ----------
from src.extras import limpiar
import src.menus as menus
import matplotlib.pyplot as plt
#-----------  FUNCIONES ----------

def suma(v1,v2):
    vr = [0,0]
    vr[0] = v1[0]+v2[0]
    vr[1] = v1[1]+v2[1]
    return vr

def main():
    vector1 = menus.vectores('primer')
    vector2 = menus.vectores('segundo')
    resultado = suma(vector1,vector2)
    print('la suma de los vectores: ')
    print(f'{vector1}+{vector2} = {resultado}')
    x1 = [0,vector1[0]]
    y1 = [0,vector1[1]]
    x2 = [0,vector2[0]]
    y2 = [0,vector2[1]]
    rx = [0,resultado[0]]
    ry = [0,resultado[1]]
    xs1 = [vector2[0], resultado[0]]
    ys1 = [vector2[1], resultado[1]]
    xs2 = [vector1[0], resultado[0]]
    ys2 = [vector1[1], resultado[1]]
    plt.plot(rx,ry, 'x-k', label='resultado', linewidth = 4)
    plt.plot(x1,y1, '^-r', label='vector1', linewidth = 3)
    plt.plot(x2,y2, '^-m', label='vector2', linewidth = 3)
    plt.plot(xs1,ys1, '--r', label='suma1', linewidth = 2)
    plt.plot(xs2,ys2, '--m', label='suma2', linewidth = 2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Suma')
    plt.show()
