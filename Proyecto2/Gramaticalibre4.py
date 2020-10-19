from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import open
import os

class AutomataPequivalente:
    def __init__(self,nombre,listaGl):
        self.nombre=nombre
        self.listaGl=listaGl

    def PdfPila(self):

        lGl=self.listaGl
        index=AutomataPequivalente.existe(self)
        if index==-1:
            print("\nNo existe dicha Gramaticca libre del contexto\n")
        else:
            Glescogida=lGl[index]
            nombre=Glescogida[0]
            noterminales=""
            terminales=""
            producciones=Glescogida[4]
        # Glibre: Nombre,noterminales,terminales,Noterminalinicial,producciones
        #Pila: Alfabeto (terminales),Alfabetodepila(noterminales+terminales),estados(ipqf),estadoi(i),estadof(f)
            w, h = A4
            Titulodocumento = f"Nombre:{nombre}"
            pdf = canvas.Canvas(f"{nombre}.pdf", pagesize=A4)
            pdf.drawString(w - (w / 2) - len(Titulodocumento) - 10, h - 50, Titulodocumento)
            cuerpotexto = pdf.beginText(50, h - 70)
            cuerpotexto.setFont("Times-Roman", 12)
            cuerpotexto.textLine("")
            for i in Glescogida[1]:
                if i==Glescogida[1][0]:
                    noterminales=f'{i}'
                else:
                    noterminales=f'{noterminales},{i}'

            for i in Glescogida[2]:
                if i==Glescogida[2][0]:
                    terminales=f'{i}'
                else:
                    terminales=f'{terminales},{i}'

            Alfabeto="Alfabeto={"+noterminales+"}"
            AlfabetodeP=f'{noterminales},{terminales},#'
            AlfabetodeP="Alfabeto de Pila={"+AlfabetodeP+"}"
            Estados="Estados={i,p,q,f}"
            Ei="Estado inicial={i}"
            Ef="Estado de aceptación={f}"
            Cpdf=[Alfabeto,AlfabetodeP,Estados,Ei,Ef]
            for i in Cpdf:
                cuerpotexto.textLine(i)
            pdf.drawText(cuerpotexto)
            AutomataPequivalente.GenerarImagen(Glescogida)
            pdf.drawImage(f"{nombre}.png", w - (w / 2) - 220, h - 90 - 410, width=480, height=300)
            pdf.save()
            os.system(f"{nombre}.pdf")

    def GenerarImagen(la):
        nombre=la[0]
        terminales=la[2]
        producciones=la[4]
        inicial=la[3]
        archivo = open(f"{nombre}.dot", "w")
        archivo.write("digraph " + nombre + "{\n")
        archivo.write('node[style="filled", shape=circle, fillcolor="white"];\n')
        archivo.write('rankdir=LR;')
        e="i,p,q,f"
        estados=e.split(",")
        for i in estados:
            if i=="f":
                archivo.write(f'{i}[label="{i}",shape="doublecircle"];\n')
            elif i=="q":
                archivo.write(f'{i}[label="{i}",height="1"];\n')
            else:
                archivo.write(f'{i}[label="{i}"];\n')
        archivo.write(f'guia[label=" ",shape="point"];\n')
        archivo.write("guia->i[arrowsize=3]\n")
        archivo.write('i->p[label="$,$;#"]\n')
        archivo.write(f'p->q[label="$,$;{inicial[0]}",tailport="e",headport="nw"]\n')


        n=(int(len(producciones)/3))
        n1=2*n

        for i in range(len(producciones)):
            produccion = ""
            for z in range(len(producciones[i])):
                if z!=0:
                    produccion = produccion+producciones[i][z]
            if i<=n:
                archivo.write(f'q->q[label="$,{producciones[i][0]};{produccion}",tailport="n",headport="n"]\n')
            elif i>n and i<=n1:
                archivo.write(f'q->q[label="$,{producciones[i][0]};{produccion}",tailport="e",headport="e"]\n')
            elif i>n1:
                archivo.write(f'q->q[label="$,{producciones[i][0]};{produccion}",tailport="w",headport="w"]\n')



        for i in terminales:
            archivo.write(f'q->q[label="{i},{i};$",tailport="s",headport="s"];\n')
        archivo.write('q->f[label="$,#;$",minlen="1.0",tailport="se",arrowsize="0.5"]\n')
        archivo.write("}")
        archivo.close()
        os.system(f"dot -Tpng {nombre}.dot -o {nombre}.png ")






    def existe(self):
        n=-1
        for i in self.listaGl:
            if i[0]==self.nombre:
                n+=1
                break
            n+=1
        return n