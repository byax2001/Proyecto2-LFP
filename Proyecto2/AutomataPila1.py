from io import open
class Pila:
    def __init__(self,nombre):
        self.nombre=nombre

    def IngresoAutomataPila(self):

        archivo=open(f"{self.nombre}.ap",'r')
        lista=archivo.readlines()
        archivo.close()
        listaautomatas=[]
        for i in lista:
            listaautomatas.append(i.rstrip("\n"))
        Automatadepila=Pila.Organizar(listaautomatas)
        return Automatadepila

    def Organizar(la):
        n=0
        listaorganizada=[]
        nombre=""
        Alfabeto=[]
        Simbolosdepila=[]
        Estados=[]
        Estadoinicial=""
        Estadodeaceptacion=""
        transiciones=[]
        while n!=len(la):
            nombre=la[n]
            n+=1
            Alfabeto=la[n].split(",")
            n+=1
            Simbolosdepila=la[n].split(",")
            n+=1
            Estados=la[n].split(",")
            n+=1
            Estadoinicial=la[n]
            n+=1
            Estadodeaceptacion=la[n]
            n+=1
            parte1=[]
            parte2=[]
            parte3=[]
            while la[n]!="%":
                parte1=la[n].split(";")
                parte2=parte1[0].split(",")
                parte3=parte1[1].split(",")
                parte2.extend(parte3)
                transiciones.append(parte2)
                n+=1
            transiciones1=transiciones.copy()
            transiciones.clear()
            lista=[nombre,Alfabeto,Simbolosdepila,Estados,Estadoinicial,Estadodeaceptacion,transiciones1]
            listaorganizada.append(lista)
            if la[n]=="%":
                n+=1
        return listaorganizada











