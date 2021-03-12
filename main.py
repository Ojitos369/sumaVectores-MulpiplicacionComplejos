#-----------  IMPORTACIONES  ----------
from src.extras import pausar,limpiar
from time import sleep
import src.menus as menus
from src.multiplicacion import main as multiplicacion
from src.vectores import main as sumaVec
#-----------  FUNCIONES ----------

def main():
    mostrar_menu = True
    while mostrar_menu:
        opc = menus.main()
        if opc != 3:
            if opc == 1:
                multiplicacion()
                pausar()
            if opc == 2:
                sumaVec()
                pausar()
        else:
            print('Adios')
            sleep(.5)
            mostrar_menu = False

#-----------  EJECUCION ----------
if __name__ == "__main__":
    main()