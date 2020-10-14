class Infogl:
    def __init__(self,listaGl):
        self.listagl=listaGl

    def Impresioninformacion(self):
        #Nombre,noterminales,terminales,Noterminalinicial,producciones
        la=self.listagl
        producciones=la[4]
        noterminales=la[1]
        print("Información General: ")
        print(f"Nombre de la gramatica: {la[0]}")
        Infogl.impl(la[1],"No Terminales")
        Infogl.impl(la[2],"Terminales")
        print(f"No terminal inicial: {la[3][0]}")
        print("Producciones: ")
        Infogl.imprimirproducciones(producciones,noterminales)


    def impl(la,nombre):
        n=0
        secuencia=""
        for i in la:
            if n==0:
                secuencia=f"{nombre}: {i}"
                n+=1
            else:
                secuencia=f"{secuencia},{i}"
        print(secuencia)

    def imprimirproducciones(P,nt):
        for i in nt:
            n = 0
            for z in P:
                k=0
                if z[0]==i and n==0:
                    print(i,end=" > ")
                    for w in range(len(z)):
                        if k>0:
                            print(z[w],end=" ")
                        k+=1
                    print("")
                    n+=1
                elif z[0]==i and n!=0:
                    print(" ", end=" | ")
                    for w in range(len(z)):
                        if k > 0:
                            print(z[w], end=" ")
                        k += 1
                    print("")




