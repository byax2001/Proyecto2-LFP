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
        Automatadepila=Glibre.Descartar(Automatadepila)
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
    #descartar los que no cumplan con ser gramaticas libres del contexto
    #que posea algun elemento de tamaño 4 o que posea un elemento en el que su segundo valor sea un no terminal (noterminal>noterminal)
    def Descartar(la):


        listadescarte=[]
        for i in la:
            n = 0
            t = 0
            n1 = 0
            for k in i[4]:
                if len(k)==4:
                    t+=1
                n=Glibre.ExisteEnNt(i[1],k[1])
                if n>0:
                    n1+=1
            if t>0 or n1>0:
                listadescarte.append(i)
        return listadescarte

    def ExisteEnNt(lnoterminales,signo):
        n=0
        for i in lnoterminales:
            if i==signo:
                n+=1
        return n


