from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import open
import os
class PdfPilaAutomata:
    def __init__(self,nombre,listapilaautomata):
        self.nombre=nombre
        self.lista=listapilaautomata

    def reporte(self):
        index=PdfPilaAutomata.existe()
        if index==-1:
            print("No existe dicho automata de pila")
        else:
            l=self.lista[index]
            w, h = A4
            nombre=""
            alfabeto=""
            simbolospila=""
            estados=""
            estadoincial=""
            estadofinal=""
            transicion=""
            Titulodocumento = f"Nombre:{l[0]}"
            pdf = canvas.Canvas(f"{l[0]}.pdf", pagesize=A4)
            pdf.drawString(w - (w / 2) - len(Titulodocumento) - 10, h - 50, Titulodocumento)
            cuerpotexto = pdf.beginText(50, h - 70)
            cuerpotexto.setFont("Times-Roman", 12)
            cuerpotexto.textLine("")
#ALFABETO
            for i in l[1]:
                if i==l[1][0]:
                    alfabeto=i
                else:
                    alfabeto = alfabeto + "," +i
            cuerpotexto.textLine("Alfabeto={"+alfabeto+"}")
#ALFABETO DE PILA
            for i in l[2]:
                if i==l[2][0]:
                    simbolospila=i
                else:
                    simbolospila = simbolospila+","+i
            cuerpotexto.textLine("Alfabeto de Pila={" + simbolospila + "}")
#ESTADOS
            for i in l[3]:
                if i==l[3][0]:
                    estados=i
                else:
                    estados = estados+","+i
            cuerpotexto.textLine("Estados={" + estados + "}")
#ESTADO INICIAL
            estadoincial=l[4]
            cuerpotexto.textLine("Estado inicial={"+estadoincial+"}")
#ESTADO FINAL
            estadofinal=l[5]
            cuerpotexto.textLine("Estado de Aceptación={" + estadofinal + "}")


    def generarImagen(transiciones):
        listaafd=afdescogido
        listatransiciones=listaafd[5]
        listaestados=listaafd[1]
        nombre=listaafd[0]
        archivo=open(f"{nombre}.dot","w")
        archivo.write("digraph "+nombre+"{\n")
        archivo.write('node[style="filled", shape=circle, fillcolor="white"];\n')
        archivo.write('rankdir=LR;')
        for i in listaestados:
            n=0
            for z in listaafd[4]:
                if z==i:
                    n+=1
            if n>0:
                archivo.write(f'{i}[label="{i}",shape="doublecircle"];\n')
            else:
                archivo.write(f'{i}[label="{i}"];\n')
        archivo.write(f'apuntador[label="",shape="point"];\n')
        archivo.write(f'apuntador->{listaafd[3]};\n')
        for i in listatransiciones:
            archivo.write(f'{i[0]}->{i[2]}[label="{i[1]}"];\n')
        archivo.write("}")
        archivo.close()
        os.system(f"dot -Tpng {listaafd[0]}.dot -o {listaafd[0]}.png ")





    def existe(self):
        n=-1
        for i in self.lista:
            if i[0]==self.nombre:
                n+=1
                break
            n+=1
        return n




