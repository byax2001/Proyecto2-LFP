import time
import os
import subprocess as sp

class Menu:
    def __init__(self,nombre,carnet):
        self.nombre=nombre
        self.carnet=carnet
    def Bienvenida(self):
        print("Bienvenido")
        print(f"Programador: {self.nombre}")
        print(f'carnet: {self.carnet}')
        n=5
        for i in range(5):
            print(n)
            n-=1
            time.sleep(1)
        Menu.clear("")
    def MenuPrincipal(self):
        print("---------Menu Principal----------")
        print('1. Modulo Gramatica Libre del Contexto')
        print('2. Modulo Automatas de Pila')
        print('3. Salir')
    def MenuGramaticalibre(self):
        print('----------Modulo Gramatica Libre del Contexto------------')
        print("1.Cargar Archivo")
        print("2.Mostrar Informacion General")
        print('3.Arbol de Derivacion')
        print("4.Generar Automata de Pila Equivalente")
        print("5.Salir")
    def AutomatasdePila(self):
        print('----------Modulo Automatas de Pila------------')
        print("1.Cargar Archivo")
        print("2.Mostrar Informacion del Automata")
        print('3.Validar una Cadena')
        print("4.Ruta de validacion")
        print("5.Recorrido Paso a Paso")
        print("6.Validar una Cadena Pasada")
        print("7.Salir")


    def OpcionCorrecta(self):
        try:
            opcion = int(input('Ingrese una opcion: '))
            if opcion > 3 or opcion < 1:
                opcion = int(input(("Opcion incorrecta ingrese otra: ")))
        except:
            opcion = int(input(("Opcion incorrecta ingrese otra: ")))
            if opcion > 3 or opcion < 1:
                opcion = int(input(("Opcion incorrecta ingrese otra: ")))
        return opcion

    def Salir(self):
        print("\n ------------Saliendo del programa-----------")
        n = 5
        for i in range(5):
            print(n)
            n -= 1
            time.sleep(1)

    def clear(self):
       print('\n'*50)


