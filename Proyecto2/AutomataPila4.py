
class Validacion:
    def __init__(self,lista,nombre,cadena):
        self.AP=lista
        self.nombre=nombre
        self.cadena=cadena

    def Rvalidar(self):
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
                print("\n-----------La cadena es valida-----------\n")
                for z in tusadas:
                    T=f'{z[0]},{z[1]},{z[2]};{z[4]},{z[3]}'
                    print(T)
            else:
                print("\n-----------------La cadena es invalida----------------\n")


    def existencia(ltransiciones,actual,letra):
        n=0
        for z in ltransiciones:
            if z[0]==actual and letra==z[1]:
                n+=1
        return n
    def index(transicion,actual,letra):
        n=-1
        for z in transicion:
            if z[0] == actual and letra == z[1]:
                n+=1
                break
            n+=1
        return  n

    def Nexiste2(self):
        n = -1
        for i in self.AP:
            if i[0] == self.nombre:
                n += 1
                break
        return n
    def Nexiste(self):
        n=-1
        for i in self.AP:
            if i[0]==self.nombre:
                n+=1
                break
            n+=1
        return n
