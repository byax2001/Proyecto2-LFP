import Menus
import Gramaticalibre1
import Gramaticalibre2
import Gramaticalibre3
import Gramaticalibre4
import AutomataPila1
import AutomataPila2


import time
from io import open


#transicion de pilas: estadoinicio, simbolo que se lee de la pila la pila, simbolo que se extrae de la pila estado receptor,simbolo insertado a la pila
Glibre=[]
Automatapila=[]

Menu= Menus.Menu('Brandon Oswaldo Yax Campos',201800534)
#Menu.Bienvenida()
Menu.MenuPrincipal()
opcion=Menu.OpcionCorrecta(3)
while opcion!=4:
#-------------------------------------------------MODULO 1----------------------------------------------------
    if opcion==1:
        # Nombre,noterminales,terminales,Noterminalinicial,producciones
        Menu.MenuGramaticalibre()
        n=Menu.OpcionCorrecta(5)
        while n!=5:
            if n==1:
                print("\n ---------------------Ingreso de Gramaticas libres del contexto------------------")
                nombre = input("Ingrese el nombre de un archivo .glc : ")
                ingreso=Gramaticalibre1.Glibre(nombre)
                Glibre=ingreso.IngresoGlibre()
            elif n==2:
                index=0
                print("\n--------------------Informacion General de las Gramaticas libres del contexto-------------")
                if len(Glibre)==0:
                    print("-----------------No existen gramaticas ingresadas-------------")
                else:
                    for i in Glibre:
                        index+=1
                        print(f"{index}.{i}")
                    numero=int(input("Ingrese el numero de la Gramatica a escoger: "))
                    print("")
                    info=Gramaticalibre2.Infogl(Glibre[numero-1])
                    info.Impresioninformacion()
                    print("")
            elif n==3:
                index = 0
                print("\n ----------------------Arboles de Derivación-------------------")
                if len(Glibre)==0:
                    print("-----------------No existen gramaticas ingresadas-------------")
                else:
                    for i in Glibre:
                        index+=1
                        print(f"{index}.{i}")
                    numero=int(input("Ingrese el numero de la Gramatica libre para realizar el arbol: "))
                    print("")
                    info=Gramaticalibre3.Arboldev(Glibre[numero-1])
                    info.generarArbol()

            elif n==4:
                index=0
                print("\n ----------------------Generar Automata de Pila Equivalente-------------------")
                if len(Glibre) == 0:
                    print("-----------------No existen gramaticas ingresadas-------------")
                else:
                    for i in Glibre:
                        index+=1
                        print(f'{index}.{i}')
                    name=input("Ingrese el nombre de la Gramatica libre de contexto para generar automata equivalente: ")
                    ingreso2=Gramaticalibre4.AutomataPequivalente(name,Glibre)
                    ingreso2.PdfPila()


            Menu.MenuGramaticalibre()
            n=Menu.OpcionCorrecta(5)


#--------------------------------------------------MODULO 2---------------------------------------------------
    if opcion==2:
        Menu.AutomatasdePila()
        n=Menu.OpcionCorrecta(7)
        while n!=7:
            if n==1:
                print("-------------Ingreso de Automatas de Pila---------------")
                nombre=input("Ingrese el nombre de un archivo .ap : ")
                ingreso=AutomataPila1.Pila(nombre)
                Automatapila=ingreso.IngresoAutomataPila()
            elif n==2:
                print("\n--------------Informacion de Automata-------------------")
                for i in Automatapila:
                    print(i)
                nombre=input("Ingrese el nombre de un Automata de pila: ")
                pdfpila=AutomataPila2.PdfPilaAutomata(nombre,Automatapila)
                pdfpila.reporte()


            Menu.AutomatasdePila()
            n = Menu.OpcionCorrecta(7)

    if opcion==3:
        Menu.Salir()
        break
    Menu.MenuPrincipal()
    opcion = Menu.OpcionCorrecta(3)