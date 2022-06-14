import tkinter as tk
from tkinter import *
import tkinter.font as Tkfont

#configuración de los botones de cambio
class btn_cambio (tk.Button):
    def __init__(self, texto, comando, pestaña):
        tk.Button.__init__(self)
        font=Tkfont.Font(family="Cascadia Code", size=15)
        self.configure(text=texto, font=font, bg="White", wraplength=480, command=lambda:comando.switch(pestaña))

#configuración de los botones de resultado
class btn_resultado (tk.Button):
    def __init__(self, texto, comando, especie, imagen):
        tk.Button.__init__(self)

        def respuesta(esp, img):
                resp=Toplevel()
                resp.geometry("480x480")
                resp.configure(background="#FFE598")
                font=Tkfont.Font(family="Cascadia Code", size=18, slant="italic")
                font_2=Tkfont.Font(family="Cascadia Code", size=18)
                murc_img=tk.PhotoImage(file=img)
                tk.Label(resp, text=f"Su murciélago es {esp}", font=font, wraplength=450, background="#FFE598").pack(side=tk.TOP, pady=20)
                tk.Label(resp, image=murc_img).pack(side=tk.TOP, pady=20)
                tk.Button(resp, height=15, text="Cerrar", font=font_2, command=lambda:resp.destroy()).pack(side=tk.TOP, pady=20)
                self.ref=murc_img

        font=Tkfont.Font(family="Cascadia Code", size=15)
        self.configure(text=texto, font=font, bg="White", wraplength=480, command=lambda:[respuesta(especie, imagen), comando.switch(inicio)])

#configuración de la raíz del programa
class CF(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        self.title("ChiroFinder")
        self.geometry("1000x650")
        self.resizable(0, 0)
        self.iconbitmap("C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/ico.ico")
        self.canva = None
        self.switch(inicio)

    def switch(self, canva):
        new_canva = canva(self)
        if self.canva is not None:
            self.canva.destroy()

        self.canva = new_canva
        self.canva.pack(expand=True, fill=tk.BOTH)

class inicio (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        inicio=btn_cambio("Inicio", comand, preg_murc_1)
        inicio.configure(font=Tkfont.Font(family="Cascadia Code", size=18))
        creditos=btn_cambio("Créditos", comand, créditos)
        creditos.configure(font=Tkfont.Font(family="Cascadia Code", size=18))
        self.create_image(0, 0, image=fondo, anchor="nw")
        self.create_image(500, 20, image=logo, anchor="n")
        self.create_window(250, 325, window=inicio, anchor="w")
        self.create_window(750, 325, anchor="e", window=creditos)
        self.fondo_ref=fondo
        self.logo_ref=logo

class créditos (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        volver=btn_cambio("Volver", comand, inicio)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        font_2=Tkfont.Font(family="Cascadia Code", size=13)
        self.create_image(0, 0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_window(10, 10, anchor="nw", window=volver)
        self.create_text(500, 200, text="CRÉDITOS", font=font_1, width=480)
        self.create_text(20, 250, anchor="w", text="José Huertas - Desarrollador", font=font_2)
        self.create_text(20, 300, anchor="w", text="José Fung - Mentor", font=font_2)
        self.create_text(20, 350, anchor="w", text="Katia Chérigo-Adulto Coordinador", font=font_2)
        self.create_text(20, 400, anchor="w", text="Iris Gómez-Coordinadora del Programa de Conservación de Murciélagos del CRU Coclé", font=font_2)
        self.create_text(20, 450, anchor="w", text="Fernando Guardia - Especialista del Programa de Conservación de Murciélagos del CRU Coclé", font=font_2)
        self.create_text(20, 500, anchor="w", text="Pablo Gutiérrez - Especialista del Programa de Conservación de Murciélagos del CRU Coclé", font=font_2)
        self.create_text(20, 550, anchor="w", text="CIDETE del CRU Coclé", font=font_2)
        self.create_text(20, 600, anchor="w", text="Programa basado en: Clave a los Murciélagos de Tierras Bajas de Panamá - Charles G. Handley, Jr.", font=font_2)
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_1 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Presente", comand, preg_murc_2)
        op_2=btn_cambio("Ausente", comand, preg_murc_52)
        volver=btn_cambio("Volver", comand, inicio)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 230, text="Estructura en forma de hoja encima de la nariz (apéndice nasal foliar libre):", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 325, window=op_1)
        self.create_window(750, 325, window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_2 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Presente", comand, preg_murc_3)
        op_2=btn_cambio("Ausente", comand, preg_murc_33)
        volver=btn_cambio("Volver", comand, preg_murc_1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 230, text="Cola:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 325, window=op_1)
        self.create_window(750, 325, window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_3 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Sí", comand, preg_murc_4)
        op_2=btn_cambio("No", comand, preg_murc_5)
        volver=btn_cambio("Volver", comand, preg_murc_2)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 230, text="¿La cola se extiende hasta el margen de la membrana interfemoral(MI)?", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 325, window=op_1)
        self.create_window(750, 325, window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_4 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Posee líneas de dentículos dermales en el margen ventral posterior de la MI, orejas alrededor del tamaño de la cabeza, peso el cuerpo +/- 8g, antebrazo 34-37mm", comand, "Macrophyllum macrophyllum", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Posee el margen posterior de la membrana interfemoral desnudo, orejas y hoja de la nariz mucho más alargado que la cabeza, peso corporal +/- 18g, antebrazo 49-54mm", comand, "Lonchorhina aurita", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_3)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 230, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 325, window=op_1)
        self.create_window(750, 325, window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

#inicio del programa
if __name__ == "__main__":
    app = CF()
    app.mainloop()