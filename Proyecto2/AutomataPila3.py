
class Validacion:
    def __init__(self,Apescogido,cadena):
        self.AP=Apescogido
        self.cadena=cadena

    def validar(self):
        valida=False
        pila=[]
        cadena=self.cadena
        nombre=self.AP[0]
        alfabeto=self.AP[1]
        Spila=self.AP[2]
        Estados=self.AP[3]
        Ei=self.AP[4]
        Ea=self.AP[5]
        transiciones=self.AP[6]
        pila.append("#")
        actual=Ei
        index = Validacion.index(transiciones, actual,"$")
        actual=transiciones[index][3]
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
                    if Sinserta!="$":
                        pila.append(Sinserta)
                    if Sextrae!="$":
                        pila.remove(Sextrae)
                    actual = Esiguiente
                except:
                    if n==len(cadena):
                        n-=1

        if len(pila)==1:
            pila.remove("#")

        if n==len(cadena) and len(pila)==0:
            valida=True
            return valida
        else:
            valida==False
            return valida

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



