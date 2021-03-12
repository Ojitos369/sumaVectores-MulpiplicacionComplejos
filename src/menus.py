#-----------  IMPORTACIONES ----------------
from src.extras import pausar,limpiar, convertir
#-----------  FUNCIONES ----------------
def main():
    incorrecto = True
    while incorrecto:
        limpiar()
        print('https://github.com/Ojitos369/sumaVectores-MulpiplicacionComplejos.git')
        opc = input('''1.- Multiplicacion de complejos
2.- Suma de Vectores
3.- Salir
Elige una opción: ''')
        opc = convertir(opc)
        if opc < 4 and opc > 0:
            incorrecto = False
        else:
            print('Opcion no valida. Intenta nuevamente. ')
            pausar()
    return opc

def complejo(text):
    complex = []
    limpiar()
    opc = input(f'Ingresa el valor Real del {text} complejo: ')
    complex.append(convertir(opc))
    opc = input(f'Ingresa el valor Imaginario del {text} complejo: ')
    complex.append(convertir(opc))
    return complex

def vectores(text):
    vector = []
    limpiar()
    opc = input(f'Ingresa el valor de X del {text} vector: ')
    vector.append(convertir(opc))
    opc = input(f'Ingresa el valor de Y del {text} vector: ')
    vector.append(convertir(opc))
    return vector
