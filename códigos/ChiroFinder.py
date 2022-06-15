import tkinter as tk
from tkinter import *
import tkinter.font as Tkfont

#configuración de los botones de cambio
class btn_cambio (tk.Button):
    def __init__(self, texto, comando, pestaña):
        tk.Button.__init__(self)
        font=Tkfont.Font(family="Cascadia Code", size=15)
        self.configure(text=texto, width=39, height=15, font=font, bg="White", wraplength=480, command=lambda:comando.switch(pestaña))

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
        self.configure(text=texto, width=39, height=15, font=font, bg="White", wraplength=480, command=lambda:[respuesta(especie, imagen), comando.switch(inicio)])

#configuración de la raíz del programa
class CF(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        self.title("ChiroFinder")
        self.geometry("1000x650")
        self.resizable(0, 0)
        self.iconbitmap("C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/ico.ico")
        self.canva = None
        self.switch(preg_murc_39)

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
        creditos=btn_cambio("Créditos", comand, créditos)
        self.create_image(0, 0, image=fondo, anchor="nw")
        self.create_image(500, 20, image=logo, anchor="n")
        self.create_window(250, 215, anchor="n", window=inicio)
        self.create_window(750, 215, anchor="n", window=creditos)
        self.fondo_ref=fondo
        self.logo_ref=logo

class créditos (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        volver=btn_cambio("Volver", comand, inicio)
        volver.configure(width=10, height=1)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        font_2=Tkfont.Font(family="Cascadia Code", size=13)
        self.create_image(0, 0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_window(10, 10, anchor="nw", window=volver)
        self.create_text(500, 200, text="CRÉDITOS", font=font_1, width=480)
        self.create_text(20, 240, anchor="w", text="José Huertas - Desarrollador", font=font_2)
        self.create_text(20, 280, anchor="w", text="José Fung - Mentor", font=font_2)
        self.create_text(20, 320, anchor="w", text="Katia Chérigo-Adulto Coordinador", font=font_2)
        self.create_text(20, 360, anchor="w", text="Iris Gómez-Coordinadora del Programa de Conservación de Murciélagos del CRU Coclé", font=font_2)
        self.create_text(20, 400, anchor="w", text="Fernando Guardia - Especialista del Programa de Conservación de Murciélagos del CRU Coclé", font=font_2)
        self.create_text(20, 440, anchor="w", text="Pablo Gutiérrez - Especialista del Programa de Conservación de Murciélagos del CRU Coclé", font=font_2)
        self.create_text(20, 480, anchor="w", text="CIDETE del CRU Coclé", font=font_2)
        self.create_text(20, 520, anchor="w", text="José Isaza - Colaborador", font=font_2)
        self.create_text(20, 560, anchor="w", text="Programa basado en: Clave a los Murciélagos de Tierras Bajas de Panamá - Charles G. Handley, Jr.", font=font_2)
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
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Estructura en forma de hoja encima de la nariz (apéndice nasal foliar libre):", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
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
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Cola:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
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
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="¿La cola se extiende hasta el margen de la membrana interfemoral(MI)?", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_4 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Posee líneas de dentículos dermales en el margen ventral posterior de la MI, orejas alrededor del tamaño de la cabeza, peso corporal +/- 8g, antebrazo 34-37mm", comand, "Macrophyllum macrophyllum", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Posee el margen posterior de la membrana interfemoral desnudo, orejas y hoja de la nariz mucho más alargado que la cabeza, peso corporal +/- 18g, antebrazo 49-54mm", comand, "Lonchorhina aurita", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_3)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_5 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Obviamente más alargado que el pie", comand, preg_murc_6)
        op_2=btn_cambio("Igual o más corto que el pie", comand, preg_murc_15)
        volver=btn_cambio("Volver", comand, preg_murc_3)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Calcar(o calcáneo):", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_6 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Con una línea medio-dorsal blanca, hoja en la nariz con pelos y mellada, peso corporal +/-15g, antebrazo de 46-55mm", comand, "Mimon crenulatum", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Sin línea, hoja en la nariz desnuda", comand, preg_murc_7)
        volver=btn_cambio("Volver", comand, preg_murc_5)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_7 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Menos de 48mm", comand, preg_murc_8)
        op_2=btn_cambio("Más de 48mm", comand, preg_murc_11)
        volver=btn_cambio("Volver", comand, preg_murc_6)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Antebrazo de:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_8 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo +40mm, dedos del pie y antebrazo notablemente peludo, una cresta de pelos largos en la corona de los machos adultos, con 4 incisivos inferiores, Micronycteris tiene un ornamento simple en la barbilla (cojincillos suaves alargados), faja entre las orejas (una membrana delgada que conecta en parte o enteramente las bases de las orejas a través de la frente), peso corporal de 16g y antebrazo de 42-46mm", comand, "Micronycteris hirsuta", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Antebrazo -40mm, dedos del pie y antebrazo sin pelos notables", comand, preg_murc_9)
        volver=btn_cambio("Volver", comand, preg_murc_7)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_9 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Parte inferior del cuerpo blanquizco, 4 incisivos inferiores, peso corporal +/-7g y antebrazo de 34-38mm", comand, "Micronycteris schmidtorum", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Partes inferiores del cuerpo chocolate", comand, preg_murc_10)
        volver=btn_cambio("Volver", comand, preg_murc_8)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

#configuraciones especiales por tener 3 botones
class preg_murc_10 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        font_2=Tkfont.Font(family="Cascadia Code", size=14)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Lóbulo anterior de la oreja densamente peludo hasta casi la punta, pelo dorsal largo (8mm) e hirsuto (velludo), 4 incisivos inferiores, longitud de las orejas de 21-22mm, pelo corto en el lóbulo basal anterior (+/-3mm), pelo más largo en la espalda superior (10-11mm), dorso rojizo-chocolate, peso corporal +/-7g y antebrazo de 32-37mm", comand, "Micronycteris megalotis", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_1.configure(width=28, height=16, wraplength=300, font=font_2)
        op_2=btn_resultado("Longitud de las orejas de 18-19mm, pelo más largo en el lóbulo basal anterior(7mm), pelo más corto en la espalda superior (8mm), dorso gris-chocolate oscuro, peso +/-7g y antebrazo de 32-37mm", comand, "Micronycteris microtis", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2.configure(width=28, height=16, wraplength=300, font=font_2)
        op_3=btn_resultado("Lóbulo anterior de las orejas escasamente peludo en la base, pelo dorsal corto (4mm), 2 incisivos inferiores, vientre chocolate, apenas diferente al torso, faja entre las orejas ausente, cara escasamente peluda, el ornamento de la barbilla es una 'V' en forma de dos frijoles, peso corporal +/-9g y antebrazo de 33-40mm", comand, "Tonatia brasilienis", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_3.configure(width=28, height=16, wraplength=300, font=font_2)
        volver=btn_cambio("Volver", comand, preg_murc_9)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(175, 215, anchor="n", window=op_1)
        self.create_window(500, 215, anchor="n", window=op_2)
        self.create_window(825, 215, anchor="n", window=op_3)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_11 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Orejas cortas, no se extienden más allá de la nariz cuando se las coloca hacia adelante, peso corporal +/-126g y antebrazo de 80-93mm", comand, "Phyllostomus hastatus", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Orejas más largas que la cabeza", comand, preg_murc_12)
        volver=btn_cambio("Volver", comand, preg_murc_7)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_12 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Orejas puntiagudas, peso corporal +/-20g y antebrazos de 53-61mm", comand, "Mimon bennetti", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Orejas redondeadas", comand, preg_murc_13)
        volver=btn_cambio("Volver", comand, preg_murc_11)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_13 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo +70mm, pelo largo y lanoso, herradura de la hoja de la nariz fuertemente bordeada ventralmente, peso corporal +/-84g y antebrazo de 77-83mm", comand, "Chrotopterus auritus", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Antebrazo -70mm, pelo más corto y no lanoso, herradura atada para bajo ventralmente", comand, preg_murc_14)
        volver=btn_cambio("Volver", comand, preg_murc_12)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_14 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo peludo, línea blanca en corona, gargante gris, peso corporal +/-36g y antebrazo de 56-61mm", comand, "Tonatia saurophila", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Antebrazo casi desnudo, sin línea en la corona, garganta blanca o blanquizca, cara desnuda, coloca las orejas para atrás cuando se toca la cabeza, peso corporal +/-34g y antebrazo 50-56mm", comand, "Tonatia silvicola", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_13)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_15 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("+50mm", comand, preg_murc_16)
        op_2=btn_cambio("-50mm", comand, preg_murc_19)
        volver=btn_cambio("Volver", comand, preg_murc_5)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Antebrazo de:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_16 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Orejas puntiagudas, peso corporal +/-24g y antebrazo de 54-58mm", comand, "Glyphonycteris daviesi", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Orejas redondeadas", comand, preg_murc_17)
        volver=btn_cambio("Volver", comand, preg_murc_15)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_17 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo peludo, labios granujientos, peso corporal +/-35g y antebrazo de 57-65mm", comand, "Trachops cirrhosus", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Antebrazo casi desnudo, labios lisos", comand, preg_murc_18)
        volver=btn_cambio("Volver", comand, preg_murc_16)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_18 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Puntas de las alas blancas, tragus atenuado, pelo corto, sedoso, hoja de la nariz tiene una forma de un triángulo de 90° en la base, peso corporal +/-61g, antebrazo de 60-68mm", comand, "Phylloderma stenops", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Alas sin puntas blancas, tragus contundente, peso corporal +/-42g, antebrazo de 60-68mm", comand, "Phyllostomus discolor", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_17)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_19 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Tricoloridos", comand, preg_murc_20)
        op_2=btn_cambio("Bicoloridos o monocoloridos", comand, preg_murc_26)
        volver=btn_cambio("Volver", comand, preg_murc_15)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Pelos dorsales:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_20 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Simple", comand, preg_murc_21)
        op_2=btn_cambio("Mosaico de verrugas", comand, preg_murc_24)
        volver=btn_cambio("Volver", comand, preg_murc_19)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Ornamento de barbilla:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_21 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Hoja de la nariz muy pequeña y triangular, lengua extensible, vibrisas conspicuas, orejas cortas y redondeadas, incisivos inferiores ausentes, peso corporal +/-8g y antebrazo de 31-35mm", comand, preg_murc_22)
        op_2=btn_cambio("Hoja de la nariz más larga que ancha, lengua no extensible, vibrisas no conspicuas, orejas de tamaño intermedio", comand, preg_murc_23)
        volver=btn_cambio("Volver", comand, preg_murc_20)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_22 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Hocico menos elongado, alas conectadas a los pies cerca de la base de los dedos", comand, "Lichonycteris obscura", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Hocico muy elongado, alas conectadas a los tobillos", comand, "Hylonycteris underwoodi", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_21)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_23 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Oreja angosta (mucho más larga que ancha), línea blanca indistinta en la espalda (normalmente), negro alrededor de los ojos, peso corporal +/-11g, antebrazo de 37-40mm, dos verrugas paralelas en la barbilla", comand, "Trinycteris nicefori", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Oreja ancha (más o menos misma largura y longitud) sin línea en la espalda, peso corporal +/-10g y antebrazo de 37-43mm", comand, "Glyphonycteris sylvestris", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_21)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_24 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Tercer diente post-canino (M1) más bajo que los dientes adyacentes, antebrazo -38mm, pelos dorsales normalmente chocolates, indistintamente tricoloridos, la menos especies de los 3 del género Carollia, peso corporal +/-13g (11-15) y antebrazo de 34-38mm", comand, "Carollia castanea", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Tercer diente post-canino (M1) tiene misma altura como los dientes adyacentes, antebrazo +38mm, pelos dorsales normalmente gris, notablemente tricoloridos", comand, preg_murc_25)
        volver=btn_cambio("Volver", comand, preg_murc_20)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_25 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Tibia y antebrazo peludo, extremidad posterior(rodilla a tobillo) +/-17mm, rodilla a puntas de garras 26-29mm, pelo más suave, largo y notablemente tricolorido en el dorso, línea de dientes superiores inclinada hacia afuera hasta PM4, peso corporal +/-15g y antebrazo de 27-42mm", comand, "Carollia brevicauda", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Antebrazo casi desnudo, rodilla a tobillo +/-21mm, rodilla a la punta de las garras 29-32mm, pelo más áspero, la especie más grande del género, peso corporal +/-19g y antebrazo de 41-45mm", comand, "Carollia perspicillata", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_24)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_26 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Hocico largo, lengua extensible, orejas cortas y redondeadas", comand, preg_murc_27)
        op_2=btn_cambio("Hocico corto, lengua no extensible, orejas largas y no redondeadas", comand, preg_murc_32)
        volver=btn_cambio("Volver", comand, preg_murc_19)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_27 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo +40mm, peso corporal +/-15g y antebrazo de 40-45mm", comand, "Lonchophylla robusta", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Antebrazo -40mm", comand, preg_murc_28)
        volver=btn_cambio("Volver", comand, preg_murc_26)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_28 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Pelos dorsales monocoloridos, dorso rojizo-chocolate, pelos cortos, rostro corto, peso corporal +/-8g y antebrazo de 32-38m", comand, "Lionycteris spurrelli", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Pelos dorsales bicoloridos", comand, preg_murc_29)
        volver=btn_cambio("Volver", comand, preg_murc_27)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_29 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Mucho más largos que los exteriores y sobresalientes", comand, preg_murc_30)
        op_2=btn_cambio("Solamente un poco más largos que los exteriores y no notablemente sobresalientes", comand, preg_murc_31)
        volver=btn_cambio("Volver", comand, preg_murc_28)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Incisivos interiores superiores:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_30 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Calcar (o calcáneo) llega hasta el final de la segunda falange cuando se le coloca a lado del pie, pulgar peludo, dorso anaranjado-chocolate, parte inferior del cuerpo amarilla o blanquizca, peso corporal +/-8g y antebrazo de 32-35mm", comand, "Lonchophylla mordax", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Calcar (o calcáneo) llega solamente un poco más allá del final de la primera falange cuando se lo coloca a lado del pie; pulgar no peludo; dorso chocolate; negruzco-chocolate en nuca; corona, cara y partes inferiores del cuerpo chocolate; peso corporal +/-6g y antebrazo de 29-34mm", comand, "Lonchophylla thomasi", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_29)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_31 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Incisivos superiores (vista oclusa) forman una creciente regular, incisivos interiores solamente poco más largos que los exteriores, incisivos inferiores separados por un espacio, peso corporal +/-7g y antebrazo 32-35mm", comand, "Glossophaga comissarisi", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Incisivos superiores (vista oclusa) forman una serie angular, incisivos interiores mucho más largos que los exteriores, incisivos inferiores interiores se tocan, peso corporal +/-11g y antebrazo de 33-38mm", comand, "Glossophaga soricina", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_29)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_32 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Partes inferiores del cuerpo amarillas o naranjas, orejas puntiagudas, peso corporal +/-14g y antebrazo de 40-42mm", comand, "Lampronycteris brachyotis", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Partes inferiores del cuerpo blanquizacas, orejas grandes y redondeadas, calcar (o calcáneo) igual o más corto que el pie, brecha en la faja entre las orejas profunda, peso corporal +/-6g y antebrazo de 33-38mm", comand, "Micronycteris minuta", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_26)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_33 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo casi de 100mm, especie más grande, peso corporal +/-151g y antebrazo de 98-110mm", comand, "Vampyrum spectrum", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Antebrazo -75mm", comand, preg_murc_34)
        volver=btn_cambio("Volver", comand, preg_murc_2)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_34 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Con por lo menos un rastro de una línea mediana blanca", comand, preg_murc_35)
        op_2=btn_cambio("Sin línea blanca", comand, preg_murc_41)
        volver=btn_cambio("Volver", comand, preg_murc_33)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Dorso:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_35 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Hasta la corona", comand, preg_murc_36)
        op_2=btn_cambio("No más allá de la nuca", comand, preg_murc_37)
        volver=btn_cambio("Volver", comand, preg_murc_34)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Extensión de la línea dorsal:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_36 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Puntas de las alas blancas (no siempre), antebrazo amarillo, el murciélago más grande con líneas blancas, peso corporal +/-36g y antebrazo de 47-56mm", comand, "Vampyrodes caraccioli", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Puntas de las alas no blancas, línea dorsal blanca brillante, membrana interfemoral (MI) angosta, en forma de 'V' y fuertemente orlada, pelos dorsales tricoloridos (la banda basal a veces indistinto) márgenes de las orejas y tragus amarillos o naranjas, de pequeño tamaño, peso corporal +/-17g y antebrazo de 37-41mm", comand, "Platyrrhinus helleri", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_35)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_37 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Hoja de la nariz lateralmente aplanada, cortada, y truncada en la punta, antebrazo y membrana interfemoral (MI) densamente peludos, ojos grandes, líneas faciales raras veces presentes, línea dorsal indistinta, llega hasta los hombros, membrana interfemoral (MI) ancha y en forma de 'U', no orlada, pelos dorsales tricoloridos, márgenes de las orejas y tragus amarillos o naranjas, peso corporal +/-22g y antebrazo de 42-47mm", comand, "Chiroderma villosum", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Hoja de la nariz aguda en la punta, antebrazo y membrana interfemoral (MI) poco peludos", comand, preg_murc_38)
        volver=btn_cambio("Volver", comand, preg_murc_35)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_38 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("Pelos dorsales notablemente tri- o tetracoloridos, línea mediana solamente en parte inferior de la espalda, incisivos interiores superiores agudos o desafilados, no truncados", comand, preg_murc_39)
        op_2=btn_cambio("Pelos dorsales bicoloridos u obscuramente tricoloridos, línea dorsal mediana se extiende hasta la nuca, incisivos interiores superiores truncados y notablemente bilobados", comand, preg_murc_40)
        volver=btn_cambio("Volver", comand, preg_murc_37)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_39 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        font_2=Tkfont.Font(family="Cascadia Code", size=14)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Puntas de los pelos dorsales escarchadas blancas, base gris, pero no muy distinta del amarillo oscuro en el medio, tercer y cuarto diente post-canino inferior (M1 y M2) tienen forma de una vasija, posteriormente sin cúspide, caninos largos y delgados, línea dorsal llega hasta los hombros, normalmente indistinta, márgenes de las orejas y tragus amarillos o naranjas, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, pelos dorsales tricoloridos (banda basal a veces indistinta), peso corporal +/-14g y antebrazo de 35-39mm", comand, "Vampyressa nymphaea", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Pelos dorsales sin puntas blancas, base de los pelos dorsales gris oscuros y bien distinguida de la banda mediana amarilla oscura, caninos cortos y gruesos, ojos grandes, líneas faciales anchas, siempre presentes, de un blanco brillante, línea dorsal presente y normalmente brillante, llega hasta los hombros, membrana interfemoral (MI) ancha y en forma de 'U' sin orlas, pelos dorsales tricoloridos, márgenes de las orejas y tragus amarillos o naranjas, peso corporal +/-17g y antebrazo de 38-41mm", comand, "Chiroderma trinitatum", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_38)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_40 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Membrana interfemoral (MI), tibia y dedos del pie peludos, líneas faciales y línea mediana dorsal a veces obscuras, brillantes, línea dorsal llega hasta los hombros o a la nuca, ojos pequeños, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, incisivos interiores superiores truncados, bilobados, márgenes de las orejas y tragus blancos o de color crema, peso corporal +/-17g y antebrazo de 41-45mm", comand, "Uroderma magnirostrum", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Extremidades posteriores (membrana del rabo y piernas) prácticamente desnudas, líneas faciales y línea dorsal siempre prominentes, línea dorsal llega hasta los hombros o la nuca, normalmente brillante, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, incisivos interiores superiores truncados, bilobados, márgenes de las orejas y tragus blancos o de color crema, peso corporal +/-17g y antebrazo de 40-44mm", comand, "Uroderma bilobatum", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_38)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_41 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_cambio("+50mm", comand, preg_murc_42)
        op_2=btn_cambio("-50mm", comand, preg_murc_44)
        volver=btn_cambio("Volver", comand, preg_murc_34)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Antebrazo:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_42 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Extremidades posteriores prácticamente desnudas, líneas faciales indistintas, peso corporal +/-48g y antebrazo de 55-67mm", comand, "Artibeus jamaicensis", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_cambio("Extremidades posteriores peludas, líneas faciales prominentes, membranas de las alas peludas cerca del cuerpo", comand, preg_murc_43)
        volver=btn_cambio("Volver", comand, preg_murc_41)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_43 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        op_1=btn_resultado("Dos pares de líneas faciales brillantes, peso corporal +/-67g y antebrazo de 69-78mm", comand, "Artibeus lituratus", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        op_2=btn_resultado("Normalmente solo un par de líneas faciales (sobre los ojos), líneas abajo de los ojos pueden ser presentes, pero indistintas, peso corporal +/-61g y antebrazo de 61-68mm", comand, "Artibeus intermedius", "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/m.png")
        volver=btn_cambio("Volver", comand, preg_murc_42)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=600)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

#inicio del programa
if __name__ == "__main__":
    app = CF()
    app.mainloop()