from io import open
import os

class Arboldev:
    def __init__(self,lgramaticas,nombre):
        self.listaGl=lgramaticas
        self.nombre=nombre


    def generarArbol(self):
        existe=Arboldev.existe(self)
        if existe==-1:
            print("El nombre de la gramatica indicada no existe")
        else:
            existe2=Arboldev.existe2(self)
            listaescogida=self.listaGl[existe2]
            # Nombre,noterminales,terminales,Noterminalinicial,producciones
            nombre = listaescogida[0]
            listaNt = listaescogida[1]
            listat = listaescogida[2]
            linicial = listaescogida[3][0]
            listaP=listaescogida[4]
            archivo=open(f"{nombre}.dot","w")
            archivo.write("graph "+nombre+"{\n")
            archivo.write('node[shape=none];\n')
            archivo.write('rankdir=TB;\n')
            num=0
            #Se crean nodos de los no terminales:
            listaptotal=[]
            index=0


            # i para cada produccion
            for i in listaP:
                for k in range(len(i)):
                    n=Arboldev.Int(listaNt,i[k])
                    if n==0:
                        listaptotal.append(i[k])
                    else:
                        listaptotal.append(f'{i[k]}{index}')

                    if k==(len(i)-1):
                        listaptotal.append("%")
                index+=1


            actual=0
            n2=0
            for i in listaNt:
                index = 0
                n2=0
                for k in range(index,len(listaptotal)):
                    if listaptotal[k][0]==i and n2==0:
                        actual=int(listaptotal[k][1])
                        n2+=1
                    elif listaptotal[k][0]==i and n2!=0:
                        if listaptotal[k][1]!=(actual+1):
                            listaptotal.insert(index,f"{i}{(actual+1)}")
                            listaptotal.pop(index+1)
                            actual=actual+1
                    index+=1
    #lt1 posee todas es como producciones solo que aqui los no terminales tienen numeros
            lt=[]
            lt1=[]
            for i in listaptotal:
                if i!="%":
                    lt.append(i)
                else:
                    lt0=lt.copy()
                    lt1.append(lt0)
                    lt.clear()
            lfinal=[]
            lfinal1=[]
            for k in lt1:
                for i in range(len(k)):
                    if len(k[i])==2 and int(k[i][1])>0 and i==0:
                        k[i]=f'{k[i][0]}{(int(k[i][1])-1)}'
                    lfinal1.append(k[i])

                lfinal2=lfinal1.copy()
                lfinal.append(lfinal2)
                lfinal1.clear()


            for k in lfinal[len(lfinal)-1]:
                existe=Arboldev.Int(listaNt,k[0])
                if existe>0:
                    for z in lfinal[len(lfinal)-2]:
                        n2=Arboldev.Int(lfinal[len(lfinal)-2],k)
                        if n2==0:
                            if k[0]==z[0] and k[1]!=z[1]:
                                print(lfinal[len(lfinal)-1])
                                n1= lfinal[len(lfinal)-1].index(k)
                                lfinal[len(lfinal)-1].insert(n1,z)
                                lfinal[len(lfinal)-1].pop(n1+1)


            for i in lfinal:
                for k in i:
                    for k in i:
                        existe = Arboldev.Int(listat, k)
                        if existe==0:
                            archivo.write(f'{k}[label="{k[0]}"]\n')

            num2=0
            for i in lfinal:
                for k in i:
                    if k!=i[0]:
                        existe=Arboldev.Int(listat,k)
                        if existe>0:
                            archivo.write(f'{num2}[label="{k[0]}"]\n')
                            archivo.write(f'{i[0]}--{num2}\n')
                            num2+=1
                        else:
                            archivo.write(f'{i[0]}--{k}\n')

            archivo.write("}\n")
            archivo.close()
            os.system(f"dot -Tpng {nombre}.dot -o {nombre}.png ")
            os.system(f"{nombre}.png")

    def Int(listaNt,termino):
        n=0
        for i in listaNt:
            if i==termino:
                n+=1
        return n

    def existe2(self):
        n = -1
        for i in self.listaGl:
            if i[0] == self.nombre:
                n += 1
                break
        return n

    def existe(self):
        n=-1
        for i in self.listaGl:
            if i[0]==self.nombre:
                n+=1
                break
            n+=1
        return n
