import tkinter as tk
from tkinter import PhotoImage, messagebox
import tkinter.font as tkFont

class CF(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        
        self.frame = None
       
        self.geometry("1300x750")
        
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
        tk.Frame.__init__(self, comand)
        
        fuente = tkFont.Font(family="Cascadia Code", size=20)
        
        logo = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        tk.Label(self, image=logo).grid(column=1, row=0)
        
        tk.Button(self, text="Inicio", font= fuente, command=lambda: comand.switch_frame(preg_murc_1)).grid(column=0, row=1)
        
        tk.Button(self, text="Créditos", font= fuente, command=lambda: comand.switch_frame(créditos)).grid(column=2, row=1)

class créditos(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self, comand)

        logo = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        tk.Label(self, image=logo).grid(column=1, row=0, columnspan=2)

        fuente = tkFont.Font(family="Cascadia Code", size=12)

        fuente2 = tkFont.Font(family="Cascadia Code", size=15)

        tk.Label(self, text="José Huertas-Desarrollador", font=fuente).grid(column=0, row=1, columnspan=2, sticky=tk.W)
        tk.Label(self, text="José Fung-Mentor", font=fuente).grid(column=0, row=2, columnspan=2, sticky=tk.W)
        tk.Label(self, text="Katia Chérigo-Adulto Coordinador", font=fuente).grid(column=0, row=3, columnspan=2, sticky=tk.W)
        tk.Label(self, text="Iris Gómez-Coordinadora del Programa de Conservación de Murciélagos del CRU Coclé", font=fuente).grid(column=0, row=4, columnspan=2, sticky=tk.W)
        tk.Label(self, text="Fernando Guardia & Pablo Gutiérrez-Especialistas del Programa de Conservación de Murciélagos del CRU Coclé", font=fuente).grid(column=0, row=5, columnspan=2, sticky=tk.W)
        tk.Label(self, text="CIDETE del CRU Coclé", font=fuente).grid(column=0, row=6, columnspan=2, sticky=tk.W)
        tk.Label(self, text="Programa basado en: Clave a los Murciélagos de Tierras Bajas de Panamá - Charles G. Handley, Jr.", font=fuente).grid(column=0, row=7, columnspan=2, sticky=tk.W)

        tk.Button(self, text="Volver", font = fuente2, command=lambda: comand.switch_frame(inicio)).grid(column=0, row=0)

class preg_murc_1(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self, comand)
        
        logo = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        tk.Label(self, image=logo).grid(column=2, row=0)
        
        fuente = tkFont.Font(family="Cascadia Code", size=15)

        tk.Label(self, text="Estructura en forma de hoja encima de la nariz (apéndice nasal foliar libre):", font=fuente).grid(column=2, row=1)
        
        tk.Button(self, text="Presente", font=fuente, command=lambda:comand.switch_frame(preg_murc_2)).grid(column=1, row=2)
        
        tk.Button(self, text="Ausente", font=fuente, command=lambda:comand.switch_frame(preg_murc_52)).grid(column=3, row=2)
        
        tk.Button(self, text="Volver", font=fuente, command=lambda:comand.switch_frame(inicio)).grid(column=0, row=0)

class preg_murc_2(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self, comand)
        
        logo = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        tk.Label(self, image=logo).grid(column=2, row=0)
        
        fuente = tkFont.Font(family="Cascadia Code", size=15)

        tk.Label(self, text="Cola:", font=fuente).grid(column=2, row=1)
        
        tk.Button(self, text="Presente", font=fuente, command=lambda:comand.switch_frame(preg_murc_3)).grid(column=1, row=2)
        
        tk.Button(self, text="Ausente", font=fuente, command=lambda:comand.switch_frame(preg_murc_33)).grid(column=3, row=2)
        
        tk.Button(self, text="Volver", font=fuente, command=lambda:comand.switch_frame(preg_murc_1)).grid(column=0, row=0)

class preg_murc_3(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self, comand)
        
        logo = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        tk.Label(self, image=logo).grid(column=2, row=0)
        
        fuente = tkFont.Font(family="Cascadia Code", size=15)

        tk.Label(self, text="¿La cola se extiende hasta el margen de la membrana interfemoral(MI)?", font=fuente).grid(column=2, row=1)
        
        tk.Button(self, text="Sí", font=fuente, command=lambda:comand.switch_frame(preg_murc_4)).grid(column=1, row=2)
        
        tk.Button(self, text="No", font=fuente, command=lambda:comand.switch_frame(preg_murc_5)).grid(column=3, row=2)
        
        tk.Button(self, text="Volver", font=fuente, command=lambda:comand.switch_frame(preg_murc_2)).grid(column=0, row=0)

class preg_murc_4(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self, comand)
        
        logo = tk.PhotoImage(file = "C:/Users/jeman/Desktop/Escritorio/Programacion/VS code/PYTHON/SENACYT/códigos/Imagenes usadas/logo.png")
        
        tk.Label(self, image=logo).grid(column=2, row=0)
        
        fuente = tkFont.Font(family="Cascadia Code", size=15)

        tk.Label(self, text="Seleccione la opción más acertada:", font=fuente).grid(column=2, row=1)
        
        tk.Button(self, text="Posee líneas de dentículos dermales en el margen ventral posterior de la MI, orejas alrededor del tamaño de la cabeza, peso el cuerpo +/- 8g, antebrazo 34-37mm", wraplength=300, font=fuente, command=lambda:[messagebox.showinfo("ChiroFinder", "Su murciélago es Macrophyllum macrophyllum."), comand.switch_frame(inicio)]).grid(column=1, row=2)
        
        tk.Button(self, text="Posee el margen posterior de la membrana interfemoral desnudo, orejas y hoja de la nariz mucho más alargado que la cabeza, peso corporal +/- 18g, antebrazo 49-54mm", wraplength=300, font=fuente, command=lambda:[messagebox.showinfo("ChiroFinder", "Su murciélago es Lonchorhina aurita."), comand.switch_frame(inicio)]).grid(column=3, row=2)
        
        tk.Button(self, text="Volver", font=fuente, command=lambda:comand.switch_frame(preg_murc_3)).grid(column=0, row=0)

if __name__ == "__main__":
    app = CF()
    app.mainloop()