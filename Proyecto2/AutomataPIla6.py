from io import open
import os

class Validacion:
    def __init__(self,lista,nombre,cadena):
        self.AP=lista
        self.nombre=nombre
        self.cadena=cadena

    def ValidarPasada(self):

        #si llego al estado final y es valido este numero estara en 1 si no en 0:
        nfinal=0
        #-------------------------------------
        Lpilas=[]
        Lcadenas=[]
        #numero de la imagen,pcadena
        pcadena=[]
        #---------------------------------------------

        index = Validacion.Nexiste(self)
        index2 = Validacion.Nexiste2(self)
        if index2==-1:
            print("No existe dicho automata de pila")
        else:
            AP=self.AP[index]
            pila=[]
            tusadas=[]
            perror=0
            cadena=self.cadena
            nombre=AP[0]
            alfabeto=AP[1]
            Spila=AP[2]
            Estados=AP[3]
            Ei=AP[4]
            Ea=AP[5]
            transiciones=AP[6]
            actual=Ei
            cadena=f"${cadena}$"
        # la validacion se va a tratar en base a existencia y index si existe la transicion con los datos que se
        #piden que son el estado actual del entonces se buscara el estado actual del recorrido y una letra de la
        #cadena una vez encontrados se trabajara dicha posicion y se actualizara el estado actual que sera
        #el estado que precede el estado actual en dicha posicion y se repetira el mismo procedimiento hasta
        #la ultima letra de la cadena.

            n=0
            for i in cadena:
                existencia=Validacion.existencia(transiciones,actual,i)
                if existencia==0:
                    break
                else:
                    try:
                        n+=1

                        index=Validacion.index(transiciones,actual,i)

                        tescogido=transiciones[index]
                        Esiguiente=tescogido[3]
                        Sextrae=tescogido[2]
                        Sinserta=tescogido[4]
                        # se guardara la pcadena con los $
                        pcadena.append(i)
                        #----------------------------------------------------------------
                        #listas para crear la tabla
                        tusadas.append(transiciones[index])
                        t=""
                        for i in pcadena:
                            if i!="$":
                                t=f"{t}{i}"
                        Lcadenas.append(t)

                        t = ""
                        for i in pila:
                            t = f"{t}{i}"
                        Lpilas.append(t)
                        #----------------------------------------------------------------
                        if Sinserta!="$":
                            pila.append(Sinserta)
                        if Sextrae!="$":
                            pila.remove(Sextrae)
                        actual = Esiguiente
                    except:
                        if n==len(cadena):
                            n-=1
                            perror=1

            if perror==1:
                tusadas.pop((len(tusadas)-1))

            if n==len(cadena) and len(pila)==0:
                print("\n-----------La cadena es valida-----------")
                nfinal=1
                Validacion.GenerarTabla(nombre,tusadas,Lpilas,Lcadenas,nfinal)
            else:
                print("\n-----------------La cadena es invalida----------------")
                Validacion.GenerarTabla(nombre, tusadas, Lpilas, Lcadenas, nfinal)

    def GenerarTabla(nombre,tusadas,Lpilas,Lcadenas,nfinal):
        num=0
        archivo = open(f"{nombre}.dot", "w")
        archivo.write("digraph " + nombre + "{\n")
        archivo.write('node[style="filled", shape=circle, fillcolor="white"];\n')
        archivo.write('rankdir=LR;\n')
        archivo.write("tf [shape=none, margin=0, \n")
        archivo.write('label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="3" CELLPADDING="4">\n')
        archivo.write('<TR>\n')
        archivo.write('<TD>Iteracion </TD>\n')
        archivo.write('<TD>Pila </TD>\n')
        archivo.write('<TD>Entrada </TD>\n')
        archivo.write('<TD>Transicion </TD>\n')
        archivo.write('</TR>\n')
        for i in range(len(tusadas)):
            archivo.write('<TR>\n')
            archivo.write(f'<TD> {num} </TD>\n')
            t=""
            for k in range(len(tusadas[i])):
                if k==0:
                    t=tusadas[i][k]
                elif k==3:
                    t=f"{t};{tusadas[i][k]}"
                else:
                    t = f"{t},{tusadas[i][k]}"
            archivo.write(f'<TD> {Lpilas[i]} </TD>\n')
            archivo.write(f'<TD> {Lcadenas[i]} </TD>\n')
            archivo.write(f'<TD> {t} </TD>\n')
            archivo.write('</TR>\n')
            num+=1
        if nfinal>0:
            archivo.write('<TR>\n')
            archivo.write(f'<TD>{num}</TD>\n')
            archivo.write('<TD> </TD>\n')
            archivo.write(f'<TD>{Lcadenas[(len(Lcadenas)-1)]}</TD>\n')
            archivo.write('<TD> </TD>\n')
            archivo.write('</TR>\n')

        archivo.write('</TABLE>>]\n')
        archivo.write("}")
        archivo.close()
        os.system(f"dot -Tpng {nombre}.dot -o {nombre}.png ")
        os.system(f"{nombre}.png")


    def existencia(ltransiciones, actual, letra):
        n = 0
        for z in ltransiciones:
            if z[0] == actual and letra == z[1]:
                n += 1
        return n

        # indice de la transicion con la letra y el estado actual
    def index(transicion, actual, letra):
        n = -1
        for z in transicion:
            if z[0] == actual and letra == z[1]:
                n += 1
                break
            n += 1
        return n

        # existencia del automata de pila con el nombre que se ingreso
    def Nexiste2(self):
        n = -1
        for i in self.AP:
            if i[0] == self.nombre:
                n += 1
                break
        return n

        # Indice del automata de pila con el nombe que se ingreso
    def Nexiste(self):
        n = -1
        for i in self.AP:
            if i[0] == self.nombre:
                n += 1
                break
            n += 1
        return n