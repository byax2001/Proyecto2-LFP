from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import open
import os
class PdfPilaAutomata:
    def __init__(self,nombre,listapilaautomata):
        self.nombre=nombre
        self.lista=listapilaautomata

    def reporte(self):
        index=PdfPilaAutomata.existe(self)
        index2 = PdfPilaAutomata.existe2(self)
        if index2==-1:
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
        pdf.drawText(cuerpotexto)
        PdfPilaAutomata.generarImagen(l)
        pdf.drawImage(f"{l[0]}.png", w - (w / 2) - 220, h - 90 - 210, width=480, height=100)
        pdf.save()
        os.system(f"{l[0]}.pdf")


    def generarImagen(listaescogida):
        listatransiciones=listaescogida[6]
        listaestados=listaescogida[3]
        nombre=listaescogida[0]
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
        for i in listatransiciones:
            archivo.write(f'{i[0]}->{i[3]}[label="{i[1]},{i[2]};{i[4]}"];\n')
        archivo.write("}")
        archivo.close()
        os.system(f"dot -Tpng {nombre}.dot -o {nombre}.png ")


    def existe2(self):
        n = -1
        for i in self.lista:
            if i[0] == self.nombre:
                n += 1
                break
        return n
    def existe(self):
        n=-1
        for i in self.lista:
            if i[0]==self.nombre:
                n+=1
                break
            n+=1
        return n




