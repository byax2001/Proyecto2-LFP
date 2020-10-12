import Menus
import AutomataPila1
import time
from io import open


#transicion de pilas: estadoinicio, simbolo que se lee de la pila la pila, simbolo que se extrae de la pila estado receptor,simbolo insertado a la pila
Gramaticalibre=[]
Automatapila=[]

Menu= Menus.Menu('Brandon Oswaldo Yax Campos',201800534)
Menu.Bienvenida()
Menu.MenuPrincipal()
opcion=Menu.OpcionCorrecta(3)
while opcion!=4:
#-------------------------------------------------MODULO 1----------------------------------------------------
    if opcion==1:
        Menu.MenuGramaticalibre()


#--------------------------------------------------MODULO 2---------------------------------------------------
    if opcion==2:
        Menu.AutomatasdePila()
        n=Menu.OpcionCorrecta(7)
        while n!=7:
            if n==1:
                print("-------------Ingreso de Automatas de Pila---------------")
                nombre=input("Ingrese el nombre de un archivo .adp : ")
                ingreso=AutomataPila1.Pila(nombre)
                Automatapila=ingreso.IngresoAutomataPila()

    if opcion==3:
        Menu.Salir()
        break
    Menu.MenuPrincipal()
    opcion = Menu.OpcionCorrecta(3)