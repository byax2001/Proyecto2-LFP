from io import open
#Nombre,noterminales,terminales,Noterminalinicial,producciones
class Glibre:
    def __init__(self,nombre):
        self.nombre=nombre

    def IngresoGlibre(self):

        archivo=open(f"{self.nombre}.glc",'r')
        lista=archivo.readlines()
        archivo.close()
        listaGl=[]
        for i in lista:
            listaGl.append(i.rstrip("\n"))
        Automatadepila=Glibre.Organizar(listaGl)
        return Automatadepila

    def Organizar(la):
        n=0
        listaorganizada=[]
        nombre=""
        noterminales=[]
        terminales=[]
        noterminalinicial=[]
        producciones=[]
        while n!=len(la):
            nombre=la[n]
            n+=1
            noterminales=la[n].split(",")
            n+=1
            terminales=la[n].split(",")
            n+=1
            noterminalinicial=la[n].split(",")
            n+=1
            parte1=[]
            parte2=[]
            parte3=[]
            while la[n]!="%":
                parte1=la[n].split(">")
                parte2=parte1[0].split(" ")
                parte3=parte1[1].split(" ")
                parte2.extend(parte3)
                producciones.append(parte2)
                n+=1
            producciones1=producciones.copy()
            producciones.clear()
            lista=[nombre,noterminales,terminales,noterminalinicial,producciones1]
            listaorganizada.append(lista)
            if la[n]=="%":
                n+=1
        return listaorganizada