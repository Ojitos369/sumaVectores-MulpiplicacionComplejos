#-----------  IMPORTACIONES  ----------
from src.extras import limpiar
import src.menus as menus
#-----------  FUNCIONES ----------
def multiplicacion(complejo1,complejo2):
    resultado = [0,1]
    a = complejo1[0]*complejo2[0]
    b = complejo1[1]*complejo2[1]
    resultado[0] = a - b

    a = complejo1[0]*complejo2[1]
    b = complejo1[1]*complejo2[0]
    resultado[1] = a + b
    return resultado

def main():
    complejo1 = menus.complejo('primer')
    complejo2 = menus.complejo('segundo')
    resultado = multiplicacion(complejo1,complejo2)
    limpiar()
    print(f'El resultado del producto de: ')
    if complejo1[1]<0:
        print(f'({complejo1[0]}+({complejo1[1]})i)', end='')
    elif complejo1[1] == 0:
        print(f'({complejo1[0]})', end='')
    else:
        print(f'({complejo1[0]}+{complejo1[1]}i)', end='')
    if complejo2[1]<0:
        print(f'({complejo2[0]}+({complejo2[1]})i)', end=' = ')
    elif complejo2[1] == 0:
        print(f'({complejo2[0]})', end=' = ')
    else:
        print(f'({complejo2[0]}+{complejo2[1]}i)', end=' = ')
    if resultado[1]<0:
        print(f'({resultado[0]}+({resultado[1]})i)')
    elif resultado[1] == 0:
        print(f'({resultado[0]})')
    else:
        print(f'({resultado[0]}+{resultado[1]}i)')