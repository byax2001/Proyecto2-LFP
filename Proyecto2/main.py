import Menus
import time


Menu= Menus.Menu('Brandon Oswaldo Yax Campos',201800534)
Menu.Bienvenida()
Menu.MenuPrincipal()
opcion=Menu.OpcionCorrecta()
while opcion!=4:
    if opcion==1:
        print("")
    if opcion==2:
        print("")
    if opcion==3:
        Menu.Salir()
        break
    Menu.MenuPrincipal()
    opcion = Menu.OpcionCorrecta()