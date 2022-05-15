import tkinter as tk
from tkinter import PhotoImage, messagebox
import tkinter.font as tkFont

class CF(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        
        self.frame = None
       
        self.geometry("1000x650")
        
        self.title("ChiroFinder")
        
        self.iconbitmap("C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/ico.ico")
        
        self.switch_frame(inicio)

    def switch_frame(self, frame_class):
        
        new_frame = frame_class(self)
        
        if self.frame is not None:
            
            self.frame.destroy()
        
        self.frame = new_frame
        
        self.frame.pack()


class inicio(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        
        princ_font = tkFont.Font(family="Cascadia Code", size=18)
        
        logo = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        tk.Label(self, image=logo).grid(column=1, row=0)
        
        tk.Button(self, text="Inicio", font=princ_font, wraplength=600, command=lambda: comand.switch_frame(preg_murc_1)).grid(column=0, row=1)
        
        tk.Button(self, text="Créditos", font=princ_font, wraplength=600, command=lambda: comand.switch_frame(créditos)).grid(column=2, row=1)


class créditos(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)

        princ_font = tkFont.Font(family="Cascadia Code", size=15)

        sec_font = tkFont.Font(family="Cascadia Code", size=12)

        logo_img = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        logo=tk.Label(self, image=logo_img)
        logo.grid(column=1, row=0)

        tk.Label(self, text="Créditos", font=princ_font, wraplength=600).grid(column=1, row=1, pady=20)

        tk.Label(self, text="José Huertas-Desarrollador", font=sec_font).grid(column=0, row=2, columnspan=3, sticky=tk.W)
        tk.Label(self, text="José Fung-Mentor", font=sec_font).grid(column=0, row=3, columnspan=3, sticky=tk.W)
        tk.Label(self, text="Katia Chérigo-Adulto Coordinador", font=sec_font).grid(column=0, row=4, columnspan=3, sticky=tk.W)
        tk.Label(self, text="Iris Gómez-Coordinadora del Programa de Conservación de Murciélagos del CRU Coclé", font=sec_font).grid(column=0, row=5, columnspan=3, sticky=tk.W)
        tk.Label(self, text="Fernando Guardia & Pablo Gutiérrez-Especialistas del Programa de Conservación de Murciélagos del CRU Coclé", font=sec_font).grid(column=0, row=6, columnspan=3, sticky=tk.W)
        tk.Label(self, text="CIDETE del CRU Coclé", font=sec_font).grid(column=0, row=7, columnspan=3, sticky=tk.W)
        tk.Label(self, text="Programa basado en: Clave a los Murciélagos de Tierras Bajas de Panamá - Charles G. Handley, Jr.", font=sec_font).grid(column=0, row=8, columnspan=3, sticky=tk.W)

        tk.Button(self, text="Volver", font = princ_font, command=lambda: comand.switch_frame(inicio)).grid(column=0, row=0)

class preg_murc_1(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        
        princ_font = tkFont.Font(family="Cascadia Code", size=18)

        sec_font = tkFont.Font(family="Cascadia Code", size=15)

        logo_img = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        logo=tk.Label(self, image=logo_img)
        logo.grid(column=1, row=0, columnspan=2)

        pregunta=tk.Label(self, text="Estructura en forma de hoja encima de la nariz (apéndice nasal foliar libre):", font=princ_font, wraplength=600)
        pregunta.grid(column=1, row=1, columnspan=2)
        
        op_1=tk.Button(self, text="Presente", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_2))
        op_1.grid(column=0, row=2, columnspan=2, padx=10)
        
        op_2=tk.Button(self, text="Ausente", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_52))
        op_2.grid(column=2, row=2, columnspan=2, padx=10)
        
        tk.Button(self, text="Volver", font=sec_font, command=lambda:comand.switch_frame(inicio)).grid(column=0, row=0)

class preg_murc_2(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        
        princ_font = tkFont.Font(family="Cascadia Code", size=18)

        sec_font = tkFont.Font(family="Cascadia Code", size=15)

        logo_img = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        logo=tk.Label(self, image=logo_img)
        logo.grid(column=1, row=0, columnspan=2)
        
        pregunta=tk.Label(self, text="Cola:", font=princ_font, wraplength=600)
        pregunta.grid(column=1, row=1, columnspan=2)
        
        op_1=tk.Button(self, text="Presente", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_3))
        op_1.grid(column=0, row=2, columnspan=2, padx=10)
        
        op_2=tk.Button(self, text="Ausente", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_33))
        op_2.grid(column=2, row=2, columnspan=2, padx=10)
        
        tk.Button(self, text="Volver", font=sec_font, command=lambda:comand.switch_frame(preg_murc_1)).grid(column=0, row=0)

class preg_murc_3(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        
        princ_font = tkFont.Font(family="Cascadia Code", size=18)

        sec_font = tkFont.Font(family="Cascadia Code", size=15)

        logo_img = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        logo=tk.Label(self, image=logo_img)
        logo.grid(column=1, row=0, columnspan=2)
        
        pregunta=tk.Label(self, text="¿La cola se extiende hasta el margen de la membrana interfemoral(MI)?", font=princ_font,  wraplength=600)
        pregunta.grid(column=1, row=1, columnspan=2)
        
        op_1=tk.Button(self, text="Sí", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_4))
        op_1.grid(column=0, row=2, columnspan=2, padx=10)
        
        op_2=tk.Button(self, text="No", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_5))
        op_2.grid(column=2, row=2, columnspan=2, padx=10)
        
        tk.Button(self, text="Volver", font=sec_font, command=lambda:comand.switch_frame(preg_murc_2)).grid(column=0, row=0)

class preg_murc_4(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        
        princ_font = tkFont.Font(family="Cascadia Code", size=18)

        sec_font = tkFont.Font(family="Cascadia Code", size=15)

        logo_img = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        logo = tk.Label(self, image=logo_img)
        logo.grid(column=1, row=0, columnspan=2)
        
        pregunta=tk.Label(self, text="Seleccione la opción más acertada:", font=princ_font, wraplength=300)
        pregunta.grid(column=1, row=1, columnspan=2)
        
        op_1=tk.Button(self, text="Posee líneas de dentículos dermales en el margen ventral posterior de la MI, orejas alrededor del tamaño de la cabeza, peso el cuerpo +/- 8g, antebrazo 34-37mm", font=sec_font, wraplength=480, command=lambda:[messagebox.showinfo("ChiroFinder", "Su murciélago es Macrophyllum macrophyllum."), comand.switch_frame(inicio)])
        op_1.grid(column=0, row=2, columnspan=2, padx=10)
        
        op_2=tk.Button(self, text="Posee el margen posterior de la membrana interfemoral desnudo, orejas y hoja de la nariz mucho más alargado que la cabeza, peso corporal +/- 18g, antebrazo 49-54mm", font=sec_font, wraplength=480, command=lambda:[messagebox.showinfo("ChiroFinder", "Su murciélago es Lonchorhina aurita."), comand.switch_frame(inicio)])
        op_2.grid(column=2, row=2, columnspan=2, padx=10)
        
        tk.Button(self, text="Volver", font=sec_font, command=lambda:comand.switch_frame(preg_murc_3)).grid(column=0, row=0)

class preg_murc_5(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        
        princ_font = tkFont.Font(family="Cascadia Code", size=18)

        sec_font = tkFont.Font(family="Cascadia Code", size=15)

        logo_img = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        logo=tk.Label(self, image=logo_img)
        logo.grid(column=1, row=0, columnspan=2)
        
        pregunta=tk.Label(self, text="Calcar(o calcáneo):", font=princ_font,  wraplength=600)
        pregunta.grid(column=1, row=1, columnspan=2)
        
        op_1=tk.Button(self, text="Obviamente más alargado que el pie", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_6))
        op_1.grid(column=0, row=2, columnspan=2, padx=10)
        
        op_2=tk.Button(self, text="Igual o más corto que el pie", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_15))
        op_2.grid(column=2, row=2, columnspan=2, padx=10)
        
        tk.Button(self, text="Volver", font=sec_font, command=lambda:comand.switch_frame(preg_murc_3)).grid(column=0, row=0)

class preg_murc_6(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        
        princ_font = tkFont.Font(family="Cascadia Code", size=18)

        sec_font = tkFont.Font(family="Cascadia Code", size=15)

        logo_img = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        logo=tk.Label(self, image=logo_img)
        logo.grid(column=1, row=0, columnspan=2)
        
        pregunta=tk.Label(self, text="Seleccione la opción más acertada:", font=princ_font,  wraplength=300)
        pregunta.grid(column=1, row=1, columnspan=2)
        
        op_1=tk.Button(self, text="Con una línea medio-dorsal blanca, hoja en la nariz con pelos y mellada, peso corporal +/-15g, antebrazo de 46-55mm", font=sec_font, wraplength=480, command=lambda:[messagebox.showinfo("ChiroFinder", "Su murciélago es Mimon crenulatum."), comand.switch_frame(inicio)])
        op_1.grid(column=0, row=2, columnspan=2, padx=10)
        
        op_2=tk.Button(self, text="Sin línea, hoja en la nariz desnuda", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_7))
        op_2.grid(column=2, row=2, columnspan=2, padx=10)
        
        tk.Button(self, text="Volver", font=sec_font, command=lambda:comand.switch_frame(preg_murc_5)).grid(column=0, row=0)

class preg_murc_7(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        
        princ_font = tkFont.Font(family="Cascadia Code", size=18)

        sec_font = tkFont.Font(family="Cascadia Code", size=15)

        logo_img = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        logo=tk.Label(self, image=logo_img)
        logo.grid(column=1, row=0, columnspan=2)
        
        pregunta=tk.Label(self, text="Antebrazo de:", font=princ_font,  wraplength=600)
        pregunta.grid(column=1, row=1, columnspan=2)
        
        op_1=tk.Button(self, text="Menos de 48mm", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_8))
        op_1.grid(column=0, row=2, columnspan=2, padx=10)
        
        op_2=tk.Button(self, text="Más de 48mm", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_11))
        op_2.grid(column=2, row=2, columnspan=2, padx=10)
        
        tk.Button(self, text="Volver", font=sec_font, command=lambda:comand.switch_frame(preg_murc_6)).grid(column=0, row=0)

class preg_murc_8(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        
        princ_font = tkFont.Font(family="Cascadia Code", size=18)

        sec_font = tkFont.Font(family="Cascadia Code", size=15)

        logo_img = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        logo=tk.Label(self, image=logo_img)
        logo.grid(column=1, row=0, columnspan=2)
        
        pregunta=tk.Label(self, text="Seleccione la opción más acertada:", font=princ_font,  wraplength=300)
        pregunta.grid(column=1, row=1, columnspan=2)
        
        op_1=tk.Button(self, text="Antebrazo +40mm, dedos del pie y antebrazo notablemente peludo, una cresta de pelos largos en la corona de los machos adultos, con 4 incisivos inferiores, Micronycteris tiene un ornamento simple en la barbilla (cojincillos suaves alargados), faja entre las orejas (una membrana delgada que conecta en parte o enteramente las bases de las orejas a través de la frente), peso corporal de 16g y antebrazo de 42-46mm", font=sec_font, wraplength=480, command=lambda:[messagebox.showinfo("ChiroFinder", "Su murciélago es Micronycteris hirsuta."), comand.switch_frame(inicio)])
        op_1.grid(column=0, row=2, columnspan=2, padx=10)
        
        op_2=tk.Button(self, text="Antebrazo -40mm, dedos del pie y antebrazo sin pelos notables", font=sec_font, wraplength=480, command=lambda:comand.switch_frame(preg_murc_9))
        op_2.grid(column=2, row=2, columnspan=2, padx=10)
        
        tk.Button(self, text="Volver", font=sec_font, command=lambda:comand.switch_frame(preg_murc_7)).grid(column=0, row=0)

if __name__ == "__main__":
    app = CF()
    app.mainloop()