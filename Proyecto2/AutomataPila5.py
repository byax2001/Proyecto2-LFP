from io import open
import os

class Validacion:
    def __init__(self,lista,nombre,cadena):
        self.AP=lista
        self.nombre=nombre
        self.cadena=cadena

    def Rivalidar(self):
        #numero de la imagen,pcadena
        num=0
        pcadena=[]
        #---------------------------------------------

        #numero para pintar el el estado final
        nfinal=0
        #---------------------------------------
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
                        tusadas.append(transiciones[index])
                        tescogido=transiciones[index]
                        Esiguiente=tescogido[3]
                        Sextrae=tescogido[2]
                        Sinserta=tescogido[4]

                        # generar imagen-------------------------------------------------
                        # se guardara la pcadena con los $
                        pcadena.append(i)
                        Validacion.generarImagen(AP, pila, tusadas[len(tusadas)-1], pcadena,num,nfinal,Ea)
                        num += 1
                        # ---------------------------------------------------------------

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
                nfinal+=1
                Validacion.generarImagen(AP, pila, tusadas[len(tusadas) - 1], pcadena, num,nfinal,Ea)
                print("\n-----------La cadena es valida-----------\n")
            else:
                print("\n-----------------La cadena es invalida----------------\n")

#Para generar la imagen
    def generarImagen(listaescogida,pila,tusada,pcadena,numero,nfinal,Ea):
        listatransiciones=listaescogida[6]
        listaestados=listaescogida[3]
        nombre=f"{listaescogida[0]}{numero}"
        Eaceptacion=listaescogida[5]
        archivo=open(f"{nombre}.dot","w")
        archivo.write("digraph "+nombre+"{\n")
        archivo.write('node[style="filled", shape=circle, fillcolor="white"];\n')
        archivo.write('rankdir=LR;\n')
        for i in listaestados:
            n=0
            if i==Eaceptacion:
                n+=1
            if n>0:
                archivo.write(f'{i}[label="{i}",shape="doublecircle"];\n')
            else:
                archivo.write(f'{i}[label="{i}"];\n')
        if nfinal == 0:
            archivo.write(f'{tusada[0]}[fillcolor="yellow"];')

            for i in listatransiciones:
                if i[0]==tusada[0] and i[3]==tusada[3] and i[2]==tusada[2] and i[1]==tusada[1]:
                    archivo.write(f'{i[0]}->{i[3]}[label="{i[1]},{i[2]};{i[4]}",fontcolor="red"];\n')
                else:
                    archivo.write(f'{i[0]}->{i[3]}[label="{i[1]},{i[2]};{i[4]}"];\n')
        else:
            archivo.write(f'{Ea}[fillcolor="yellow"];')
            for i in listatransiciones:
                archivo.write(f'{i[0]}->{i[3]}[label="{i[1]},{i[2]};{i[4]}"];\n')
#TABLA:
        pl=""
        pc=""
        for i in pila:
            pl=f'{pl}{i}'
        for i in pcadena:
            if i!="$":
                pc=f'{pc}{i}'
        #si se llego al estado final colocar una tabla que indique que la cadena es valida.
        if nfinal>0:
            archivo.write("\ntz [shape=none, margin=0, \n")
            archivo.write('label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="3" CELLPADDING="4">\n')
            archivo.write('<TR>\n')
            archivo.write('<TD> Cadena Valida! </TD>\n')
            archivo.write('</TR>\n')
            archivo.write('</TABLE>>]\n\n')
        archivo.write("tf [shape=none, margin=0, \n")
        archivo.write('label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="3" CELLPADDING="4">\n')
        archivo.write('<TR>\n')
        archivo.write('<TD>Pila: </TD>\n')
        archivo.write(f'<TD>{pl}</TD>\n')
        archivo.write('</TR>\n')
        archivo.write('<TR>\n')
        archivo.write('<TD>Entrada: </TD>\n')
        archivo.write(f'<TD>{pc}</TD>\n')
        archivo.write('</TR>\n')
        archivo.write('</TABLE>>]\n')
        archivo.write("}")
        archivo.close()
        os.system(f"dot -Tpng {nombre}.dot -o {nombre}.png ")
        os.system(f"{nombre}.png")


#existencia del automata de pila con la letra y el estado actual
    def existencia(ltransiciones,actual,letra):
        n=0
        for z in ltransiciones:
            if z[0]==actual and letra==z[1]:
                n+=1
        return n

#indice de la transicion con la letra y el estado actual
    def index(transicion,actual,letra):
        n=-1
        for z in transicion:
            if z[0] == actual and letra == z[1]:
                n+=1
                break
            n+=1
        return  n

#existencia del automata de pila con el nombre que se ingreso
    def Nexiste2(self):
        n = -1
        for i in self.AP:
            if i[0] == self.nombre:
                n += 1
                break
        return n

#Indice del automata de pila con el nombe que se ingreso
    def Nexiste(self):
        n=-1
        for i in self.AP:
            if i[0]==self.nombre:
                n+=1
                break
            n+=1
        return n