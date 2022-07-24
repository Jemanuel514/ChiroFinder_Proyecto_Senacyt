import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as Tkfont
import webbrowser

caracteristicas=[]
clases=[]
especie_final=[]
imagen_final=[]
urls={"Macrophyllum macrophyllum":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Macrophyllum%20macrophyllum", "Lonchorhina aurita":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Lonchorhina%20aurita", "Mimon crenulatum":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Gardnerycteris%20crenulatum", "Micronycteris hirsuta":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Micronycteris%20hirsuta", "Micronycteris schmidtorum":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Micronycteris%20schmidtorum", "Micronycteris megalotis":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Micronycteris%20megalotis", "Micronycteris microtis":"https://cma.sarem.org.ar/es/especie-nativa/micronycteris-microtis", "Lophostoma brasiliensis":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Lophostoma%20brasiliense", "Phyllostomus hastatus":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Phyllostomus%20hastatus", "Mimon bennetti":"https://es.wikipedia.org/wiki/Mimon_bennettii", "Chrotopterus auritus":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Chrotopterus%20auritus", "Tonatia saurophila":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Tonatia%20saurophila", "Lophostoma silvicola":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Lophostoma%20silvicola","Glyphonycteris daviesi":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Glyphonycteris%20daviesi", "Trachops cirrhosus":"https://es.wikipedia.org/wiki/Trachops_cirrhosus", "Phylloderma stenops":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Phylloderma%20stenops", "Phyllostomus discolor":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Phyllostomus%20discolor", "Lichonycteris obscura":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Lichonycteris%20obscura", "Hylonycteris underwoodi":"https://animaldiversity.org/accounts/Hylonycteris_underwoodi/", "Trinycteris nicefori":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Trinycteris%20nicefori", "Glyphonycteris sylvestris":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Glyphonycteris%20sylvestris", "Carollia castanea":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Carollia%20castanea","Carollia brevicauda":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Carollia%20brevicaudum", "Carollia perspicillata":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Carollia%20perspicillata", "Lonchophylla robusta":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Lonchophylla%20robusta", "Lionycteris spurrelli":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Lionycteris%20spurrelli", "Lonchophylla mordax":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Lonchophylla%20concava", "Hsunycteris thomasi":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Hsunycteris%20thomasi", "Glossophaga comissarisi":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Glossophaga%20commissarisi", "Glossophaga soricina":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Glossophaga%20soricina", "Lampronycteris brachyotis":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Lampronycteris%20brachyotis", "Micronycteris minuta":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Micronycteris%20minuta", "Vampyrum spectrum":"https://es.wikipedia.org/wiki/Vampyrum_spectrum", "Vampyrodes caraccioli":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Vampyrodes%20caraccioli", "Platyrrhinus helleri":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Platyrrhinus%20helleri", "Chiroderma villosum":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Chiroderma%20villosum", "Vampyriscus nymphaea":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Vampyriscus%20nymphaea", "Chiroderma trinitatum":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Chiroderma%20trinitatum", "Uroderma magnirostrum":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Uroderma%20magnirostrum", "Uroderma bilobatum":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Uroderma%20bilobatum", "Artibeus jamaicensis":"https://es.wikipedia.org/wiki/Artibeus_jamaicensis", "Artibeus lituratus":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Artibeus%20lituratus", "Artibeus intermedius":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Artibeus%20lituratus", "Sturnira lilium":None, "Sturnira luisi":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Sturnira%20luisi", "Enchistenes hartii":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Enchisthenes%20hartii", "Artibeus phaeotis":"https://www.gbif.org/es/species/2433264", "Artibeus watsoni":"https://www.gbif.org/es/species/4265337", "Artibeus incomitatus":None, "Vampyressa pusilla":"https://cma.sarem.org.ar/es/especie-nativa/vampyressa-pusilla", "Ectophylla alba":"https://es.wikipedia.org/wiki/Ectophylla_alba", "Mesophylla macconnelli":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Mesophylla%20macconnelli", "Centurio senex":None, "Diaemus youngi":"https://es.wikipedia.org/wiki/Diaemus_youngi", "Desmodus rotundus":"https://es.wikipedia.org/wiki/Desmodus_rotundus", "Diphylla ecaudata":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Diphylla%20ecaudata", "Dasypterus ega":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Dasypterus%20ega", "Lasiurus egregius":"https://www.gbif.org/es/species/5218547", "Lasiurus blossevillii":"https://es.wikipedia.org/wiki/Lasiurus_blossevillii", "Lasiurus castaneus":None, "Natalus stramineus":"https://www.gbif.org/es/species/2432756", "Rhogeessa tumida":"https://www.gbif.org/es/species/2432270", "Eptesicus furinalis":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Eptesicus%20furinalis", "Eptesicus brasiliensis":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Eptesicus%20brasiliensis", "Eptesicus fuscus":"https://es.wikipedia.org/wiki/Eptesicus_fuscus", "Myotis albescens":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Myotis%20albescens", "Myotis riparius":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Myotis%20riparius", "Myotis nigricans":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Myotis%20nigricans", "Thyroptera tricolor":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Thyroptera%20tricolor", "Thyroptera discifera":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Thyroptera%20discifera", "Promops centralis":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Promops%20centralis", "Molossus sinaloae":"https://es.wikipedia.org/wiki/Molossus_sinaloae", "Molossus rufus":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Molossus%20rufus", "Molossus molossus":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Molossus%20molossus", "Molossus bondae":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Molossus%20currentium", "Tadarida brasiliensis":"https://es.wikipedia.org/wiki/Tadarida_brasiliensis", "Eumops auripendulus":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Eumops%20auripendulus", "Eumops glaucinus":"https://es.wikipedia.org/wiki/Eumops_glaucinus", "Eumops hansae":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Eumops%20hansae", "Eumops bonariensis":"https://cma.sarem.org.ar/es/especie-nativa/eumops-bonariensis", "Cynomops planirostris":"https://cma.sarem.org.ar/es/especie-nativa/cynomops-planirostris", "Cynomops greenhalli":"https://es.wikipedia.org/wiki/Cynomops_greenhalli", "Diclidurus albus":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Diclidurus%20albus", "Saccopteryx bilineata":"https://es.wikipedia.org/wiki/Saccopteryx_bilineata", "Saccopteryx leptura":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Saccopteryx%20leptura", "Rhynchonycteris naso":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Rhynchonycteris%20naso", "Noctilio albiventris":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Noctilio%20albiventris", "Noctilio leporinus":"https://es.wikipedia.org/wiki/Noctilio_leporinus", "Cormura brevirostris":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Cormura%20brevirostris", "Peropteryx kappleri":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Peropteryx%20kappleri", "Peropteryx macrotis":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Peropteryx%20macrotis", "Furipterus horrens":"https://bioweb.bio/faunaweb/mammaliaweb/FichaEspecie/Furipterus%20horrens", "Centronycteris maximiliani":"https://www.gbif.org/es/species/2433136", "Pteronotus gymnonotus":"https://www.gbif.org/es/species/5218624", "Pteronotus davyi":"https://es.wikipedia.org/wiki/Pteronotus_davyi", "Pteronotus parnellii":"https://www.gbif.org/es/species/5218620", "Pteronotus personatus":None}

class btn_cambio (tk.Button):
    def __init__(self, texto, caracteristicasteristica, clase, pestaña):
        tk.Button.__init__(self)
        font=Tkfont.Font(family="Cascadia Code", size=15)
        self.configure(text=texto, width=39, height=15, font=font, bg="#FCF9C6", activebackground="#FAF4B7", foreground="#654062", wraplength=480, command=lambda:[caracteristicas.append(caracteristicasteristica), clases.append(clase), self.master.cambio(pestaña)])

class btn_resultado (tk.Button):
    def __init__(self, texto, clase, especie, imagen):
        tk.Button.__init__(self)
        font=Tkfont.Font(family="Cascadia Code", size=15)
        self.configure(text=texto, width=39, height=15, font=font, bg="#FCF9C6", activebackground="#FAF4B7", foreground="#654062", wraplength=480, command=lambda:[caracteristicas.append(texto), clases.append(clase), especie_final.append(especie), imagen_final.append(imagen), self.master.cambio(confirmacion)])

class btn_normal (tk.Button):
    def __init__(self, texto, pestaña):
        tk.Button.__init__(self)
        font=Tkfont.Font(family="Cascadia Code", size=15)
        self.configure(text=texto, width=39, height=15, font=font, bg="#FCF9C6", activebackground="#FAF4B7", foreground="#654062", wraplength=480, command=lambda:self.master.cambio(pestaña))

class CF(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        self.title("ChiroFinder")
        self.geometry("1000x650")
        self.resizable(0, 0)
        self.iconbitmap("Imagenes usadas/ico.ico")
        self.window = None
        self.cambio(inicio)

    def cambio(self, window):
        new_window = window(self)
        if self.window is not None:
            self.window.destroy()

        self.window = new_window
        self.window.pack(expand=True, fill=tk.BOTH)

class inicio (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[:]
        del clases[:]
        especie_final.clear()
        imagen_final.clear()

        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        inicio=btn_normal("Inicio", preg_murc_1)
        creditos=btn_normal("Créditos", créditos)
        self.create_image(0, 0, image=fondo, anchor="nw")
        self.create_image(500, 20, image=logo, anchor="n")
        self.create_window(250, 215, anchor="n", window=inicio)
        self.create_window(750, 215, anchor="n", window=creditos)
        self.fondo_ref=fondo
        self.logo_ref=logo

class créditos (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[:]
        del clases[:]
        especie_final.clear()
        imagen_final.clear()
        
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        volver=btn_normal("Volver", inicio)
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
        del caracteristicas[:]
        del clases[:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Presente", "Tiene apéndice foliar libre", preg_murc_1, preg_murc_2)
        op_2=btn_cambio("Ausente", "No tiene apéndice foliar libre", preg_murc_1, preg_murc_52)
        volver=btn_normal("Volver", inicio)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Estructura en forma de hoja encima de la nariz (apéndice nasal foliar libre):", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_2 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[1:]
        del clases[1:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Presente", "Tiene cola", preg_murc_2, preg_murc_3)
        op_2=btn_cambio("Ausente", "No tiene cola", preg_murc_2, preg_murc_33)
        volver=btn_normal("Volver", preg_murc_1)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Cola:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_3 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[2:]
        del clases[2:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Sí", "La cola se extiende hasta el margen de la membrana interfemoral", preg_murc_3, preg_murc_4)
        op_2=btn_cambio("No", "La cola no se extiende hasta el margen de la membrana interfemoral", preg_murc_3, preg_murc_5)
        volver=btn_normal("Volver", preg_murc_2)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="¿La cola se extiende hasta el margen de la membrana interfemoral(MI)?", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_4 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[3:]
        del clases[3:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Posee líneas de dentículos dermales en el margen ventral posterior de la MI, orejas alrededor del tamaño de la cabeza, peso corporal +/- 8g, antebrazo 34-37mm", preg_murc_4, "Macrophyllum macrophyllum", "Imagenes usadas/m.png")
        op_2=btn_resultado("Posee el margen posterior de la membrana interfemoral desnudo, orejas y hoja de la nariz mucho más alargado que la cabeza, peso corporal +/- 18g, antebrazo 49-54mm", preg_murc_4, "Lonchorhina aurita", "Imagenes usadas/Murciélagos/Lonchorhina aurita.png")
        volver=btn_normal("Volver", preg_murc_3)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_5 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[3:]
        del clases[3:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Obviamente más alargado que el pie", "Calcar más alargado que el pie", preg_murc_5, preg_murc_6)
        op_2=btn_cambio("Igual o más corto que el pie", "Calcar igual o más corto que el pie", preg_murc_5, preg_murc_15)
        volver=btn_normal("Volver", preg_murc_3)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Calcar(o calcáneo):", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_6 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[4:]
        del clases[4:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Con una línea medio-dorsal blanca, hoja en la nariz con pelos y mellada, peso corporal +/-15g, antebrazo de 46-55mm", preg_murc_6, "Mimon crenulatum", "Imagenes usadas/m.png")
        op_2=btn_cambio("Sin línea, hoja en la nariz desnuda", "Sin línea, hoja en la nariz desnuda", preg_murc_6, preg_murc_7)
        volver=btn_normal("Volver", preg_murc_5)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_7 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()

        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Menos de 48mm", "Antebrazo de menos de 48mm", preg_murc_7, preg_murc_8)
        op_2=btn_cambio("Más de 48mm", "Antebrazo de más de 48mm", preg_murc_7, preg_murc_11)
        volver=btn_normal("Volver", preg_murc_6)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Antebrazo de:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_8 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo +40mm, dedos del pie y antebrazo notablemente peludo, una cresta de pelos largos en la corona de los machos adultos, con 4 incisivos inferiores, Micronycteris tiene un ornamento simple en la barbilla (cojincillos suaves alargados), faja entre las orejas (una membrana delgada que conecta en parte o enteramente las bases de las orejas a través de la frente), peso corporal de 16g y antebrazo de 42-46mm", preg_murc_8, "Micronycteris hirsuta", "Imagenes usadas/m.png")
        op_2=btn_cambio("Antebrazo -40mm, dedos del pie y antebrazo sin pelos notables", "Antebrazo -40mm, dedos del pie y antebrazo sin pelos notables", preg_murc_8, preg_murc_9)
        volver=btn_normal("Volver", preg_murc_7)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_9 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Parte inferior del cuerpo blanquizco, 4 incisivos inferiores, peso corporal +/-7g y antebrazo de 34-38mm", preg_murc_9, "Micronycteris schmidtorum", "Imagenes usadas/m.png")
        op_2=btn_cambio("Partes inferiores del cuerpo chocolate", "Partes inferiores del cuerpo chocolate", preg_murc_9, preg_murc_10)
        volver=btn_normal("Volver", preg_murc_8)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_10 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        font_2=Tkfont.Font(family="Cascadia Code", size=14)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Lóbulo anterior de la oreja densamente peludo hasta casi la punta, pelo dorsal largo (8mm) e hirsuto (velludo), 4 incisivos inferiores, longitud de las orejas de 21-22mm, pelo corto en el lóbulo basal anterior (+/-3mm), pelo más largo en la espalda superior (10-11mm), dorso rojizo-chocolate, peso corporal +/-7g y antebrazo de 32-37mm", preg_murc_10, "Micronycteris megalotis", "Imagenes usadas/m.png")
        op_1.configure(width=28, height=16, wraplength=300, font=font_2)
        op_2=btn_resultado("Longitud de las orejas de 18-19mm, pelo más largo en el lóbulo basal anterior(7mm), pelo más corto en la espalda superior (8mm), dorso gris-chocolate oscuro, peso +/-7g y antebrazo de 32-37mm", preg_murc_10, "Micronycteris microtis", "Imagenes usadas/m.png")
        op_2.configure(width=28, height=16, wraplength=300, font=font_2)
        op_3=btn_resultado("Lóbulo anterior de las orejas escasamente peludo en la base, pelo dorsal corto (4mm), 2 incisivos inferiores, vientre chocolate, apenas diferente al torso, faja entre las orejas ausente, cara escasamente peluda, el ornamento de la barbilla es una 'V' en forma de dos frijoles, peso corporal +/-9g y antebrazo de 33-40mm", preg_murc_10, "Lophostoma brasilienis", "Imagenes usadas/m.png")
        op_3.configure(width=28, height=16, wraplength=300, font=font_2)
        volver=btn_normal("Volver", preg_murc_9)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(175, 215, anchor="n", window=op_1)
        self.create_window(500, 215, anchor="n", window=op_2)
        self.create_window(825, 215, anchor="n", window=op_3)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_11 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Orejas cortas, no se extienden más allá de la nariz cuando se las coloca hacia adelante, peso corporal +/-126g y antebrazo de 80-93mm", preg_murc_11, "Phyllostomus hastatus", "Imagenes usadas/Murciélagos/Phyllostomus hastatus.png")
        op_2=btn_cambio("Orejas más largas que la cabeza", "Orejas más largas que la cabeza", preg_murc_11, preg_murc_12)
        volver=btn_normal("Volver", preg_murc_7)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_12 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Orejas puntiagudas, peso corporal +/-20g y antebrazos de 53-61mm", preg_murc_12, "Mimon bennetti", "Imagenes usadas/m.png")
        op_2=btn_cambio("Orejas redondeadas", "Orejas redondeadas", preg_murc_12, preg_murc_13)
        volver=btn_normal("Volver", preg_murc_11)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_13 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo +70mm, pelo largo y lanoso, herradura de la hoja de la nariz fuertemente bordeada ventralmente, peso corporal +/-84g y antebrazo de 77-83mm", preg_murc_13, "Chrotopterus auritus", "Imagenes usadas/Murciélagos/Chrotopterus auritus.png")
        op_2=btn_cambio("Antebrazo -70mm, pelo más corto y no lanoso, herradura atada para bajo ventralmente", "Antebrazo -70mm, pelo más corto y no lanoso, herradura atada para bajo ventralmente", preg_murc_13, preg_murc_14)
        volver=btn_normal("Volver", preg_murc_12)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_14 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[9:]
        del clases[9:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo peludo, línea blanca en corona, gargante gris, peso corporal +/-36g y antebrazo de 56-61mm", preg_murc_14, "Tonatia saurophila", "Imagenes usadas/Murciélagos/Tonatia saurophila.png")
        op_2=btn_resultado("Antebrazo casi desnudo, sin línea en la corona, garganta blanca o blanquizca, cara desnuda, coloca las orejas para atrás cuando se toca la cabeza, peso corporal +/-34g y antebrazo 50-56mm", preg_murc_14, "Lophostoma silvicola", "Imagenes usadas/Murciélagos/Lophostoma silvicola.png")
        volver=btn_normal("Volver", preg_murc_13)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_15 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[4:]
        del clases[4:]
        especie_final.clear()
        imagen_final.clear()

        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("+50mm", "Antebrazo de más de 50mm", preg_murc_15, preg_murc_16)
        op_2=btn_cambio("-50mm", "Antebrazo de menos de 50mm",preg_murc_15, preg_murc_19)
        volver=btn_normal("Volver", preg_murc_5)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Antebrazo de:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_16 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()

        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Orejas puntiagudas, peso corporal +/-24g y antebrazo de 54-58mm", preg_murc_16, "Glyphonycteris daviesi", "Imagenes usadas/m.png")
        op_2=btn_cambio("Orejas redondeadas", "Orejas redondeadas", preg_murc_16, preg_murc_17)
        volver=btn_normal("Volver", preg_murc_15)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_17 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo peludo, labios granujientos, peso corporal +/-35g y antebrazo de 57-65mm", preg_murc_17, "Trachops cirrhosus", "Imagenes usadas/m.png")
        op_2=btn_cambio("Antebrazo casi desnudo, labios lisos", "Antebrazo casi desnudo, labios lisos", preg_murc_17, preg_murc_18)
        volver=btn_normal("Volver", preg_murc_16)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_18 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Puntas de las alas blancas, tragus atenuado, pelo corto, sedoso, hoja de la nariz tiene una forma de un triángulo de 90° en la base, peso corporal +/-61g, antebrazo de 60-68mm", preg_murc_18, "Phylloderma stenops", "Imagenes usadas/m.png")
        op_2=btn_resultado("Alas sin puntas blancas, tragus contundente, peso corporal +/-42g, antebrazo de 60-68mm", preg_murc_18, "Phyllostomus discolor", "Imagenes usadas/Murciélagos/Phyllostomus discolor.png")
        volver=btn_normal("Volver", preg_murc_17)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_19 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Tricoloridos", "Pelos dorsales tricolorido", preg_murc_19, preg_murc_20)
        op_2=btn_cambio("Bicoloridos o monocoloridos", "Pelos dorsales bi o monocoloridos", preg_murc_19, preg_murc_26)
        volver=btn_normal("Volver", preg_murc_15)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Pelos dorsales:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_20 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Simple", "Ornamento de barbilla simple", preg_murc_20, preg_murc_21)
        op_2=btn_cambio("Mosaico de verrugas", "Ornamento de barbilla es un mosaico de verrgas", preg_murc_20, preg_murc_24)
        volver=btn_normal("Volver", preg_murc_19)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Ornamento de barbilla:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_21 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Hoja de la nariz muy pequeña y triangular, lengua extensible, vibrisas conspicuas, orejas cortas y redondeadas, incisivos inferiores ausentes, peso corporal +/-8g y antebrazo de 31-35mm", "Hoja de la nariz muy pequeña y triangular, lengua extensible, vibrisas conspicuas, orejas cortas y redondeadas, incisivos inferiores ausentes, peso corporal +/-8g y antebrazo de 31-35mm", preg_murc_21, preg_murc_22)
        op_2=btn_cambio("Hoja de la nariz más larga que ancha, lengua no extensible, vibrisas no conspicuas, orejas de tamaño intermedio", "Hoja de la nariz más larga que ancha, lengua no extensible, vibrisas no conspicuas, orejas de tamaño intermedio", preg_murc_21, preg_murc_23)
        volver=btn_normal("Volver", preg_murc_20)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_22 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Hocico menos elongado, alas conectadas a los pies cerca de la base de los dedos", preg_murc_22, "Lichonycteris obscura", "Imagenes usadas/m.png")
        op_2=btn_resultado("Hocico muy elongado, alas conectadas a los tobillos", preg_murc_22, "Hylonycteris underwoodi", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_21)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_23 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Oreja angosta (mucho más larga que ancha), línea blanca indistinta en la espalda (normalmente), negro alrededor de los ojos, peso corporal +/-11g, antebrazo de 37-40mm, dos verrugas paralelas en la barbilla", preg_murc_23, "Trinycteris nicefori", "Imagenes usadas/m.png")
        op_2=btn_resultado("Oreja ancha (más o menos misma largura y longitud) sin línea en la espalda, peso corporal +/-10g y antebrazo de 37-43mm", preg_murc_23, "Glyphonycteris sylvestris", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_21)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_24 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Tercer diente post-canino (M1) más bajo que los dientes adyacentes, antebrazo -38mm, pelos dorsales normalmente chocolates, indistintamente tricoloridos, la menos especies de los 3 del género Carollia, peso corporal +/-13g (11-15) y antebrazo de 34-38mm", preg_murc_24, "Carollia castanea", "Imagenes usadas/Murciélagos/Carollia castanea.png")
        op_2=btn_cambio("Tercer diente post-canino (M1) tiene misma altura como los dientes adyacentes, antebrazo +38mm, pelos dorsales normalmente gris, notablemente tricoloridos", "Tercer diente post-canino (M1) tiene misma altura como los dientes adyacentes, antebrazo +38mm, pelos dorsales normalmente gris, notablemente tricoloridos", preg_murc_24, preg_murc_25)
        volver=btn_normal("Volver", preg_murc_20)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_25 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Tibia y antebrazo peludo, extremidad posterior(rodilla a tobillo) +/-17mm, rodilla a puntas de garras 26-29mm, pelo más suave, largo y notablemente tricolorido en el dorso, línea de dientes superiores inclinada hacia afuera hasta PM4, peso corporal +/-15g y antebrazo de 27-42mm", preg_murc_25, "Carollia brevicauda", "Imagenes usadas/m.png")
        op_2=btn_resultado("Antebrazo casi desnudo, rodilla a tobillo +/-21mm, rodilla a la punta de las garras 29-32mm, pelo más áspero, la especie más grande del género, peso corporal +/-19g y antebrazo de 41-45mm", preg_murc_25, "Carollia perspicillata", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_24)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_26 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Hocico largo, lengua extensible, orejas cortas y redondeadas", "Hocico largo, lengua extensible, orejas cortas y redondeadas", preg_murc_26, preg_murc_27)
        op_2=btn_cambio("Hocico corto, lengua no extensible, orejas largas y no redondeadas", "Hocico corto, lengua no extensible, orejas largas y no redondeadas", preg_murc_26, preg_murc_32)
        volver=btn_normal("Volver", preg_murc_19)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_27 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo +40mm, peso corporal +/-15g y antebrazo de 40-45mm", preg_murc_27, "Lonchophylla robusta", "Imagenes usadas/Murciélagos/Lonchophylla robusta.png")
        op_2=btn_cambio("Antebrazo -40mm", "Antebrazo -40mm", preg_murc_27, preg_murc_28)
        volver=btn_normal("Volver", preg_murc_26)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_28 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Pelos dorsales monocoloridos, dorso rojizo-chocolate, pelos cortos, rostro corto, peso corporal +/-8g y antebrazo de 32-38m", preg_murc_28, "Lionycteris spurrelli", "Imagenes usadas/m.png")
        op_2=btn_cambio("Pelos dorsales bicoloridos", "Pelos dorsales bicoloridos", preg_murc_28, preg_murc_29)
        volver=btn_normal("Volver", preg_murc_27)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_29 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[9:]
        del clases[9:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Mucho más largos que los exteriores y sobresalientes", "Incisivos interiores superiores mucho más largos que los exteriores y sobresalientes", preg_murc_29, preg_murc_30)
        op_2=btn_cambio("Solamente un poco más largos que los exteriores y no notablemente sobresalientes", "Incisivos interiores superiores solo un poco más largos que los exteriores y no notablemente sobresalientes", preg_murc_29, preg_murc_31)
        volver=btn_normal("Volver", preg_murc_28)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Incisivos interiores superiores:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_30 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[10:]
        del clases[10:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Calcar (o calcáneo) llega hasta el final de la segunda falange cuando se le coloca a lado del pie, pulgar peludo, dorso anaranjado-chocolate, parte inferior del cuerpo amarilla o blanquizca, peso corporal +/-8g y antebrazo de 32-35mm", preg_murc_30, "Lonchophylla mordax", "Imagenes usadas/m.png")
        op_2=btn_resultado("Calcar (o calcáneo) llega solamente un poco más allá del final de la primera falange cuando se lo coloca a lado del pie; pulgar no peludo; dorso chocolate; negruzco-chocolate en nuca; corona, cara y partes inferiores del cuerpo chocolate; peso corporal +/-6g y antebrazo de 29-34mm", preg_murc_30, "Hsunycteris thomasi", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_29)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_31 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[10:]
        del clases[10:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Incisivos superiores (vista oclusa) forman una creciente regular, incisivos interiores solamente poco más largos que los exteriores, incisivos inferiores separados por un espacio, peso corporal +/-7g y antebrazo 32-35mm", preg_murc_31, "Glossophaga comissarisi", "Imagenes usadas/m.png")
        op_2=btn_resultado("Incisivos superiores (vista oclusa) forman una serie angular, incisivos interiores mucho más largos que los exteriores, incisivos inferiores interiores se tocan, peso corporal +/-11g y antebrazo de 33-38mm", preg_murc_31, "Glossophaga soricina", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_29)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_32 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Partes inferiores del cuerpo amarillas o naranjas, orejas puntiagudas, peso corporal +/-14g y antebrazo de 40-42mm", preg_murc_32, "Lampronycteris brachyotis", "Imagenes usadas/m.png")
        op_2=btn_resultado("Partes inferiores del cuerpo blanquizacas, orejas grandes y redondeadas, calcar (o calcáneo) igual o más corto que el pie, brecha en la faja entre las orejas profunda, peso corporal +/-6g y antebrazo de 33-38mm", preg_murc_32, "Micronycteris minuta", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_26)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_33 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[2:]
        del clases[2:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo casi de 100mm, especie más grande, peso corporal +/-151g y antebrazo de 98-110mm", preg_murc_33, "Vampyrum spectrum", "Imagenes usadas/m.png")
        op_2=btn_cambio("Antebrazo -75mm", "Antebrazo -75mm", preg_murc_33, preg_murc_34)
        volver=btn_normal("Volver", preg_murc_2)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_34 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[3:]
        del clases[3:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Con por lo menos un rastro de una línea mediana blanca", "Dorso con por lo menos un rastro de una línea mediana blanca", preg_murc_34, preg_murc_35)
        op_2=btn_cambio("Sin línea blanca", "Dorso sin línea blanca", preg_murc_34, preg_murc_41)
        volver=btn_normal("Volver", preg_murc_33)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Dorso:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_35 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[4:]
        del clases[4:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Hasta la corona", "La línea dorsal se extiende hasta la corona", preg_murc_35, preg_murc_36)
        op_2=btn_cambio("No más allá de la nuca", "La línea dorsal no se extiende más allá de la nuca", preg_murc_35, preg_murc_37)
        volver=btn_normal("Volver", preg_murc_34)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Extensión de la línea dorsal:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_36 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Puntas de las alas blancas (no siempre), antebrazo amarillo, el murciélago más grande con líneas blancas, peso corporal +/-36g y antebrazo de 47-56mm", preg_murc_36, "Vampyrodes caracteristicascioli", "Imagenes usadas/m.png")
        op_2=btn_resultado("Puntas de las alas no blancas, línea dorsal blanca brillante, membrana interfemoral (MI) angosta, en forma de 'V' y fuertemente orlada, pelos dorsales tricoloridos (la banda basal a veces indistinto) márgenes de las orejas y tragus amarillos o naranjas, de pequeño tamaño, peso corporal +/-17g y antebrazo de 37-41mm", preg_murc_36, "Platyrrhinus helleri", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_35)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_37 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Hoja de la nariz lateralmente aplanada, cortada, y truncada en la punta, antebrazo y membrana interfemoral (MI) densamente peludos, ojos grandes, líneas faciales raras veces presentes, línea dorsal indistinta, llega hasta los hombros, membrana interfemoral (MI) ancha y en forma de 'U', no orlada, pelos dorsales tricoloridos, márgenes de las orejas y tragus amarillos o naranjas, peso corporal +/-22g y antebrazo de 42-47mm", preg_murc_37, "Chiroderma villosum", "Imagenes usadas/Murciélagos/Chiroderma villosum.png")
        op_2=btn_cambio("Hoja de la nariz aguda en la punta, antebrazo y membrana interfemoral (MI) poco peludos", "Hoja de la nariz aguda en la punta, antebrazo y membrana interfemoral (MI) poco peludos", preg_murc_37, preg_murc_38)
        volver=btn_normal("Volver", preg_murc_35)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_38 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Pelos dorsales notablemente tri- o tetracoloridos, línea mediana solamente en parte inferior de la espalda, incisivos interiores superiores agudos o desafilados, no truncados", "Pelos dorsales notablemente tri- o tetracoloridos, línea mediana solamente en parte inferior de la espalda, incisivos interiores superiores agudos o desafilados, no truncados", preg_murc_39, preg_murc_39)
        op_2=btn_cambio("Pelos dorsales bicoloridos u obscuramente tricoloridos, línea dorsal mediana se extiende hasta la nuca, incisivos interiores superiores truncados y notablemente bilobados", "Pelos dorsales bicoloridos u obscuramente tricoloridos, línea dorsal mediana se extiende hasta la nuca, incisivos interiores superiores truncados y notablemente bilobados", preg_murc_39, preg_murc_40)
        volver=btn_normal("Volver", preg_murc_37)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_39 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Puntas de los pelos dorsales escarchadas blancas, base gris, pero no muy distinta del amarillo oscuro en el medio, tercer y cuarto diente post-canino inferior (M1 y M2) tienen forma de una vasija, posteriormente sin cúspide, caninos largos y delgados, línea dorsal llega hasta los hombros, normalmente indistinta, márgenes de las orejas y tragus amarillos o naranjas, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, pelos dorsales tricoloridos (banda basal a veces indistinta), peso corporal +/-14g y antebrazo de 35-39mm", preg_murc_39, "Vampyriscus nymphaea", "Imagenes usadas/m.png")
        op_2=btn_resultado("Pelos dorsales sin puntas blancas, base de los pelos dorsales gris oscuros y bien distinguida de la banda mediana amarilla oscura, caninos cortos y gruesos, ojos grandes, líneas faciales anchas, siempre presentes, de un blanco brillante, línea dorsal presente y normalmente brillante, llega hasta los hombros, membrana interfemoral (MI) ancha y en forma de 'U' sin orlas, pelos dorsales tricoloridos, márgenes de las orejas y tragus amarillos o naranjas, peso corporal +/-17g y antebrazo de 38-41mm", preg_murc_39, "Chiroderma trinitatum", "Imagenes usadas/Murciélagos/Chiroderma trinitatum.png")
        volver=btn_normal("Volver", preg_murc_38)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_40 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Membrana interfemoral (MI), tibia y dedos del pie peludos, líneas faciales y línea mediana dorsal a veces obscuras, brillantes, línea dorsal llega hasta los hombros o a la nuca, ojos pequeños, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, incisivos interiores superiores truncados, bilobados, márgenes de las orejas y tragus blancos o de color crema, peso corporal +/-17g y antebrazo de 41-45mm", preg_murc_40, "Uroderma magnirostrum", "Imagenes usadas/m.png")
        op_2=btn_resultado("Extremidades posteriores (membrana del rabo y piernas) prácticamente desnudas, líneas faciales y línea dorsal siempre prominentes, línea dorsal llega hasta los hombros o la nuca, normalmente brillante, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, incisivos interiores superiores truncados, bilobados, márgenes de las orejas y tragus blancos o de color crema, peso corporal +/-17g y antebrazo de 40-44mm", preg_murc_40, "Uroderma bilobatum", "Imagenes usadas/Murciélagos/Uroderma bilobatum.png")
        volver=btn_normal("Volver", preg_murc_38)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_41 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[4:]
        del clases[4:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("+50mm", "Antebrazo de más de 50mm", preg_murc_41, preg_murc_42)
        op_2=btn_cambio("-50mm", "Antebrazo de menos de 50mm", preg_murc_41, preg_murc_44)
        volver=btn_normal("Volver", preg_murc_34)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Antebrazo:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_42 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Extremidades posteriores prácticamente desnudas, líneas faciales indistintas, peso corporal +/-48g y antebrazo de 55-67mm", preg_murc_42, "Artibeus jamaicensis", "Imagenes usadas/Murciélagos/Artibeus jamaicensis.png")
        op_2=btn_cambio("Extremidades posteriores peludas, líneas faciales prominentes, membranas de las alas peludas cerca del cuerpo", "Extremidades posteriores peludas, líneas faciales prominentes, membranas de las alas peludas cerca del cuerpo", preg_murc_42, preg_murc_43)
        volver=btn_normal("Volver", preg_murc_41)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_43 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Dos pares de líneas faciales brillantes, peso corporal +/-67g y antebrazo de 69-78mm", preg_murc_43, "Artibeus lituratus", "Imagenes usadas/Murciélagos/Artibeus lituratus.png")
        op_2=btn_resultado("Normalmente solo un par de líneas faciales (sobre los ojos), líneas abajo de los ojos pueden ser presentes, pero indistintas, peso corporal +/-61g y antebrazo de 61-68mm", preg_murc_43, "Artibeus intermedius", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_42)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_44 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Membrana interfemoral (MI) ausente, hombros de color naranja o amarillo, piernas peludas, incisivos inferiores trilobados", "Membrana interfemoral (MI) ausente, hombros de color naranja o amarillo, piernas peludas, incisivos inferiores trilobados", preg_murc_44, preg_murc_45)
        op_2=btn_cambio("Membrana interfemoral (MI) presente, hombros del mismo color que el resto del dorso", "Membrana interfemoral (MI) presente, hombros del mismo color que el resto del dorso", preg_murc_44, preg_murc_46)
        volver=btn_normal("Volver", preg_murc_41)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_45 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Pelo dorsal de color pálido, líneas de los dientes maxilares arqueadas para afuera (no paralelas), peso corporal +/-15g y antebrazo de 37-42mm", preg_murc_45, "Sturnira lilium", "Imagenes usadas/m.png")
        op_2=btn_resultado("Pelo dorsal oscuro, líneas de los dientes maxilares casi paralelas, peso corporal +/-20g y antebrazo de 41-45mm", preg_murc_45, "Sturnira luisi", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_44)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_46 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Antebrazo normalmente de +35mm, paladar casi circular", "Antebrazo normalmente de +35mm, paladar casi circular", preg_murc_46, preg_murc_47)
        op_2=btn_cambio("Antebrazo normalmente de -35mm, paladar anteriormente estrechado", "Antebrazo normalmente de -35mm, paladar anteriormente estrechado", preg_murc_46, preg_murc_50)
        volver=btn_normal("Volver", preg_murc_44)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_47 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Color del pelo chocolate oscuro, membrana interfemoral (MI) notablemente orlada, angosta y en forma de 'V', herradura de la hoja de la nariz ventralmente doblada para abajo, incisivos interiores superiores no bilobados, líneas faciales presentes, amarillas, angostas, líneas medianas dorsales ausentes, incisivos interiores superiores truncados, no lobados, márgenes de las orejas y tragus blancos o de color crema, peso corporal +/-17g y antebrazo de 37-43mm", preg_murc_47, "Enchistenes hartii", "Imagenes usadas/m.png")
        op_2=btn_cambio("Color del pelo gris-chocolate, membrana interfemoral (MI) desnuda o escasamente orlada, ancha y en forma de 'U',  herradura ventralmente libre, incisivos interiores superiores bilobados", "Color del pelo gris-chocolate, membrana interfemoral (MI) desnuda o escasamente orlada, ancha y en forma de 'U',  herradura ventralmente libre, incisivos interiores superiores bilobados", preg_murc_47, preg_murc_48)
        volver=btn_normal("Volver", preg_murc_46)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_48 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Márgenes de las orejas amarillas y amarillas en la base, hoja de la nariz más larga y ancha, M3 ausente, líneas faciales siempre presentes, líneas blancas brillantes y anchas, línea mediana dorsal ausente, incisivos interiores superiores truncados  y bilobados, peso corporal +/-11g, antebrazo de 35-40mm y pelo de 4-6mm", preg_murc_48, "Artibeus phaeotis", "Imagenes usadas/Murciélagos/Artibeus phaeotis.png")
        op_2=btn_cambio("Márgenes de las orejas no amarillas y de color crema en la base, hoja de la nariz más corta y angosta, M3 presente, líneas faciales siempre presentes, blanchas, angostas y pequeñas, incisivos interiores superiores truncados y bilobados", "Márgenes de las orejas no amarillas y de color crema en la base, hoja de la nariz más corta y angosta, M3 presente, líneas faciales siempre presentes, blanchas, angostas y pequeñas, incisivos interiores superiores truncados y bilobados", preg_murc_48, preg_murc_49)
        volver=btn_normal("Volver", preg_murc_47)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_49 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[9:]
        del clases[9:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Más pequeño, partes inferiores del cuerpo de color más claro y amarillo, frecuentemente tiene líneas faciales blancas bien definidas y prominentes, extremidades posteriores (tibia, pie y membrana interfemoral (MI)) casi desnudas, peso corporal +/-11g, antebrazo de 35-42mm y pelo velludo de 6-7mm", preg_murc_49, "Artibeus watsoni", "Imagenes usadas/m.png")
        op_2=btn_resultado("Más grande, partes inferiores del cuerpo de color más oscuro, gris-chocolate, no siempre tiene líneas faciales bien definidas, extremidades posteriores (tibia, pie y membrana interfemoral (MI)) normalmente peludas, peso corporal +/-13g y antebrazo de 40-45mm", preg_murc_49, "Artibeus incomitatus", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_48)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_50 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Líneas faciales presentes, blancas y angostas, muy pequeño, calcar (o calcáneo) recto, base de la oreja y hoja de la nariz solamente moderadamente amarillas, línea dorsal ausente, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, márgenes de las orejas y tragus de color amarillo o naranja, pelo dorsal tricolorido (banda basal a veces obscura), peso corporal +/-8g y antebrazo de 29-34mm", preg_murc_50, "Vampyressa pusilla", "Imagenes usadas/m.png")
        op_2=btn_cambio("Líneas faciales ausentes, calcar (o calcáneo) recto o falciforme, base de las orejas y hoja de la nariz de color amarillo brillante", "Líneas faciales ausentes, calcar (o calcáneo) recto o falciforme, base de las orejas y hoja de la nariz de color amarillo brillante", preg_murc_50, preg_murc_51)
        volver=btn_normal("Volver", preg_murc_46)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_51 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Dorso anterior blanquizco, dorso posterior de color tostado, calcar (o calcáneo) recto, peso corporal +/-5g y antebrazo de 23-31mm", preg_murc_51, "Ectophylla alba", "Imagenes usadas/m.png")
        op_2=btn_resultado("Dorso anterior amarillo, dorso posterior de color tostado, calcar (o calcáneo) falciforme, líneas faciales y línea dorsal siempre ausentes, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, márgenes de las orejas y tragus de color amarillo o naranja, peso corporal +/-7g y antebrazo de 29-33mm", preg_murc_51, "Mesophylla macconnelli", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_50)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_52 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        Canvas.__init__(self)
        del caracteristicas[1:]
        del clases[1:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Ausente", "Tiene cola", preg_murc_52, preg_murc_53)
        op_2=btn_cambio("Presente", "No tiene cola", preg_murc_52, preg_murc_56)
        volver=btn_normal("Volver", preg_murc_1)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Cola:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_53 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[2:]
        del clases[2:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Cara desnuda y grotescamente arrugada, mancha blanca en el hombro, membrana interfemoral (MI) ancha, peluda, en forma de 'U' y fuertemente orlada, líneas siempre ausentes, pelo dorsal tricolorido, cara muy corta básicamente sin rostro, orejas no afiladas, peso corporal +/-20g y antebrazo de 41-45mm", preg_murc_53, "Centurio senex", "Imagenes usadas/Murciélagos/Centurio senex.png")
        op_2=btn_cambio("Cara peluda con ornamentos rudimentarios en la nariz, sin manchas blancas en el hombro, membrana interfemoral (MI) angosta o ausente", "Cara peluda con ornamentos rudimentarios en la nariz, sin manchas blancas en el hombro, membrana interfemoral (MI) angosta o ausente", preg_murc_53, preg_murc_54)
        volver=btn_normal("Volver", preg_murc_52)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_54 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[3:]
        del clases[3:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Puntas de las alas blancas, peso corporal +/-36g y antebrazo de 48-54mm", preg_murc_54, "Diaemus youngi", "Imagenes usadas/m.png")
        op_2=btn_cambio("Puntas de las alas no blancas", "Puntas de las alas no blancas", preg_murc_54, preg_murc_55)
        volver=btn_normal("Volver", preg_murc_53)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_55 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[4:]
        del clases[4:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Miembro metacarpal del pulgar muy elongado, orejas de tamaño mediano y redondeadas, calcar (o calcáneo) aparentemente ausente, extremidades posteriores con pelos muy cortos, partes inferiores del cuerpo blanquizcas, peso corporal +/-34g y antebrazo de 53-65mm", preg_murc_55, "Desmodus rotundus", "Imagenes usadas/m.png")
        op_2=btn_resultado("Miembro metacarpal del pugar corto, orejas cortas y cuadradas, calcar (o calcáneo) notable, extremidades posteriores densamente peludas, partes inferiores del cuerpo gris chocolate, peso corporal +/-25g y antebrazo de 49-56mm", preg_murc_55, "Diphylla ecaudata", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_54)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_56 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[2:]
        del clases[2:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Se extiende hasta o más allá del margen de la membrana interfemoral (MI)", "La cola se extiende hasta o más allá del margen de la membrana interfemoral (MI)", preg_murc_56, preg_murc_57)
        op_2=btn_cambio("No llega gasta el margen de la membrana interfemoral (MI)", "La cola no llega gasta el margen de la membrana interfemoral (MI)", preg_murc_56, preg_murc_82)
        volver=btn_normal("Volver", preg_murc_52)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="La cola:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_57 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[3:]
        del clases[3:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Hasta el margen de la membrana interfemoral (MI) o se extiende solamente una o dos vértebras más allá", "La cola se extiende hasta el margen de la membrana interfemoral (MI) o se extiende solamente una o dos vértebras más allá", preg_murc_57, preg_murc_58)
        op_2=btn_cambio("Mucho más allá del margen de la membrana interfemoral (MI)", "La cola se extiende mucho más allá del margen de la membrana interfemoral (MI)", preg_murc_57, preg_murc_69)
        volver=btn_normal("Volver", preg_murc_56)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="La cola se extiende:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_58 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[4:]
        del clases[4:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Extensivamente peluda", "Membrana interfemoral extensivamente peluda", preg_murc_58, preg_murc_59)
        op_2=btn_cambio("Casi desnuda", "Membrana interfemoral casi desnuda", preg_murc_58, preg_murc_62)
        volver=btn_normal("Volver", preg_murc_57)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Membrana interfemoral (MI):", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_59 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("De color amarillo, alas negras, peso corporal +/-11g y antebrazo de 43-47mm", preg_murc_59, "Dasypterus ega", "Imagenes usadas/m.png")
        op_2=btn_cambio("De color rojizo", "De color rojizo", preg_murc_59, preg_murc_60)
        volver=btn_normal("Volver", preg_murc_58)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_60 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()

        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Dorso y partes inferiores del cuerpo rojos, peso corporal +/-20g y antebrazo +/-50mm", preg_murc_60, "Lasiurus egregius", "Imagenes usadas/m.png")
        op_2=btn_cambio("Partes inferiores del cuerpo de color amarillo o negruzco", "Partes inferiores del cuerpo de color amarillo o negruzco", preg_murc_60, preg_murc_61)
        volver=btn_normal("Volver", preg_murc_59)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_61 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Partes inferiores del cuerpo amarillas, dorso rojizo-naranja, banda mediana de los pelos dorsales es pálida y ancha, peso corporal +/-8g y antebrazo de 38-42mm", preg_murc_61, "Lasiurus blossevillii", "Imagenes usadas/m.png")
        op_2=btn_resultado("Partes inferiores del cuerpo negruzcas, dorso marrón, banda mediana de los pelos dorsales es pálida y angostas, peso corporal +/-13g y antebrazo de 43-46mm", preg_murc_61, "Lasiurus castaneus", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_60)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_62 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Piernas muy largas, membrana del ala muy grande y conectada muy arriba en la tibia, peso corporal +/-6g y antebrazo de 36-39mm", preg_murc_62, "Natalus stramineus", "Imagenes usadas/m.png")
        op_2=btn_cambio("Piernas cortas, membrana del ala conectada al lado del pie", "Piernas cortas, membrana del ala conectada al lado del pie", preg_murc_62, preg_murc_63)
        volver=btn_normal("Volver", preg_murc_58)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_63 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Adyacente al canino", "El primer diente post-canino alto en la parte superior está adyacente al canino", preg_murc_63, preg_murc_64)
        op_2=btn_cambio("Separado del canino por dientes pequeños y bajos", "El primer diente post-canino alto en la parte superior está separado del canino por dientes pequeños y bajos", preg_murc_63, preg_murc_67)
        volver=btn_normal("Volver", preg_murc_62)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="El primer diente post-canino alto en la parte superior está:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_64 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Bases del pelo dorsal pálido, amarillo, amarillo oscuro, peso corporal +/-5g y antebrazo de 27-31mm", preg_murc_64, "Rhogeessa tumida", "Imagenes usadas/m.png")
        op_2=btn_cambio("Bases del pelo dorsal fusco oscuro", "Bases del pelo dorsal fusco oscuro", preg_murc_64, preg_murc_65)
        volver=btn_normal("Volver", preg_murc_63)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_65 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Pequeño, pelo corto, peso corporal +/-7g y antebrazo de 37-43mm", preg_murc_65, "Eptesicus furinalis", "Imagenes usadas/m.png")
        op_2=btn_cambio("Tamaño mediano a grande, pelo largo, antebrazo +40mm", "Tamaño mediano a grande, pelo largo, antebrazo +40mm", preg_murc_65, preg_murc_66)
        volver=btn_normal("Volver", preg_murc_64)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_66 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[9:]
        del clases[9:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Tamaño mediano, negruzco, peso corporal +/-10g y antebrazo de 42-47mm", preg_murc_66, "Eptesicus brasiliensis", "Imagenes usadas/m.png")
        op_2=btn_resultado("Grande, de color chocolate oscuro, peso corporal +/-13g y antebrazo de 46-54mm", preg_murc_66, "Eptesicus fuscus", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_65)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_67 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Partes inferiores del cuerpo blanquizcas, dorso negruzco con puntas pálidas, pies más grandes, peso corporal +/-7g y antebrazo de 33-38mm", preg_murc_67, "Myotis albescens", "Imagenes usadas/m.png")
        op_2=btn_cambio("Partes inferiores del cuerpo amarillas o chocolates, dorso sin puntas pálidas, pies pequeños", "Partes inferiores del cuerpo amarillas o chocolates, dorso sin puntas pálidas, pies pequeños", preg_murc_67, preg_murc_68)
        volver=btn_normal("Volver", preg_murc_63)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_68 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Pelo dorsal lanoso, peso corporal +/-5g y antebrazo de 32-38mm", preg_murc_68, "Myotis riparius", "Imagenes usadas/m.png")
        op_2=btn_resultado("Pelo dorsal liso, peso corporal +/-4g y antebrazo de 33-38mm", preg_murc_68, "Myotis nigricans", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_67)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_69 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[4:]
        del clases[4:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Presentes", "Tiene discos de succión en el pulgar y los pies", preg_murc_69, preg_murc_70)
        op_2=btn_cambio("Ausentes", "No tiene discos de succión en el pulgar y los pies", preg_murc_69, preg_murc_71)
        volver=btn_normal("Volver", preg_murc_57)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Discos de succión en el pulgar y los pies:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_70 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Partes inferiores del cuerpo blancas o amarillas pálidas, rabo se extiende 5-8mm más allá de la membrana interfemoral (MI), membrana interfemoral (MI) casi desnuda, calcar (o calcáneo) normalmente con dos proyecciones membranosas extendiendo hasta el margen posterolateral de la membrana interfemoral (MI), peso corporal +/-4g y antebrazo de 34-38mm", preg_murc_70, "Thyroptera tricolor", "Imagenes usadas/m.png")
        op_2=btn_resultado("Partes inferiores del cuerpo chocolates o naranja-chocolates, rabo se extiende 2-4mm más allá de la membrana interfemoral (MI), membrana interfemoral (MI) con pelos largos (4mm) escasamente distribuidos, pelos finos, calcar (o calcáneo) con una proyección membranosa extendiendo hasta el margen posterolateral de la membrana interfemoral (MI), peso corporal +/-3g y antebrazo de 30-35mm", preg_murc_70, "Thyroptera discifera", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_69)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_71 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Petiolado (casi circular, pellizcado en la base)", "Antitragus petiolado (casi circular, pellizcado en la base)", preg_murc_71, preg_murc_72)
        op_2=btn_cambio("Más ancho en la base", "Antitragus más ancho en la base", preg_murc_71, preg_murc_76)
        volver=btn_normal("Volver", preg_murc_69)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Antitragus:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_72 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Pelos en cadera de 3-6mm y antebrazo +/-50mm", "Pelos en cadera de 3-6mm y antebrazo +/-50mm", preg_murc_72, preg_murc_73)
        op_2=btn_cambio("Pelos en cadera de 1-2mm y antebrazo -45mm", "Pelos en cadera de 1-2mm y antebrazo -45mm", preg_murc_72, preg_murc_75)
        volver=btn_normal("Volver", preg_murc_71)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_73 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo desnudo, incisivos interiores superiores sobresalientes, peso corporal +/-21g y antebrazo de 48-56mm", preg_murc_73, "Promops centralis", "Imagenes usadas/m.png")
        op_2=btn_cambio("Antebrazo peludo, incisivos interiores superiores no sobresalen", "Antebrazo peludo, incisivos interiores superiores no sobresalen", preg_murc_73, preg_murc_74)
        volver=btn_normal("Volver", preg_murc_72)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_74 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Pelos dorsales con bases de color blanco o gris contrastante, peso corporal +/-27g y antebrazo de 45-52mm", preg_murc_74, "Molossus sinaloae", "Imagenes usadas/m.png")
        op_2=btn_resultado("Pelos dorsales con poco contraste entre las puntas y las bases, peso corporal +/-32g y antebrazo de 46-51mm", preg_murc_74, "Molossus rufus", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_73)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_75 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Pelo +/-3mm en el centro de la espalda, banda basal de los pelos dorsales es pálida, peso corporal +/-12g y antebrazo de 36-40mm", preg_murc_75, "Molossus molossus", "Imagenes usadas/m.png")
        op_2=btn_resultado("Pelo +/-2mm en el centro de la espalda, poco o ningún contraste entre las puntas y las bases de los pelos dorsales, peso corporal +/-22g y antebrazo de 38-43mm", preg_murc_75, "Molossus bondae", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_72)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_76 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Orejas grandes, conectadas en la frente, hocico no hinchado e inflado", "Orejas grandes, conectadas en la frente, hocico no hinchado e inflado", preg_murc_76, preg_murc_77)
        op_2=btn_cambio("Orejas de tamaño moderado, no conectadas en la frente, hocico hinchado e inflado", "Orejas de tamaño moderado, no conectadas en la frente, hocico hinchado e inflado", preg_murc_76, preg_murc_81)
        volver=btn_normal("Volver", preg_murc_71)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_77 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Labios superiores grandes, sueltos y muy arrugados, peso corporal +/-10g y antebrazo de 36-46mm", preg_murc_77, "Tadarida brasiliensis", "Imagenes usadas/m.png")
        op_2=btn_cambio("Labios superiores normales", "Labios superiores normales", preg_murc_77, preg_murc_78)
        volver=btn_normal("Volver", preg_murc_76)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_78 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("+50mm", "Antebrazo de más de 50mm", preg_murc_78, preg_murc_79)
        op_2=btn_cambio("-40mm", "Antebrazo de menos de 40mm", preg_murc_78, preg_murc_80)
        volver=btn_normal("Volver", preg_murc_77)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Antebrazo:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_79 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[9:]
        del clases[9:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Tragus relativamente pequeño, agudo, pliegue anterior basal de la oreja -15mm, color en el dorso negruzco, peso corporal +/-33g y antebrazo de 66-74mm", preg_murc_79, "Eumops auripendulus", "Imagenes usadas/m.png")
        op_2=btn_resultado("Tragus relativamente grande, truncado, pliegue anterior basal de la oreja +15mm, color en el dorso gris chocolate, peso corporal +/-38g y antebrazo de 55-63mm", preg_murc_79, "Eumops glaucinus", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_78)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_80 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[9:]
        del clases[9:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Pelo dorsal corto (2mm) y terciopelado, peso corporal +/-18g y antebrazo de 36-42mm", preg_murc_80, "Eumops hansae", "Imagenes usadas/m.png")
        op_2=btn_resultado("Pelo dorsal largo (6mm) y suelto, peso corporal +/-10g y antebrazo de 38-49mm", preg_murc_80, "Eumops bonariensis", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_78)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_81 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Pequeño, pecho blanquizco, peso corporal +/-13g y antebrazo de 31-36mm", preg_murc_81, "Cynomops planirostris", "Imagenes usadas/m.png")
        op_2=btn_resultado("Grande, color del pecho no diferenciado, negruzco o chocolate, peso corporal +/-20g y antebrazo de 34-38mm", preg_murc_81, "Cynomops greenhalli", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_76)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_82 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[3:]
        del clases[3:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("De color blanco o blanquizco, membranas pálidas, peso corporal +/-16g y antebrazo de 64-66mm", preg_murc_82, "Diclidurus albus", "Imagenes usadas/m.png")
        op_2=btn_cambio("De color negruzco, chocolate o naranja, membranas negruzcas", "De color negruzco, chocolate o naranja, membranas negruzcas", preg_murc_82, preg_murc_83)
        volver=btn_normal("Volver", preg_murc_56)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_83 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[4:]
        del clases[4:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Dos líneas blanquizcas", "Dos líneas longitudinales en el dorso", preg_murc_83, preg_murc_84)
        op_2=btn_cambio("Una o ninguna línea", "Una o ninguna línea longitudinal en el dorso", preg_murc_83, preg_murc_86)
        volver=btn_normal("Volver", preg_murc_82)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Líneas longitudinales en el dorso:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_84 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Grande, de color negruzco, con saco glandular, peso corporal +/-6g y antebrazo de 40-49mm", preg_murc_84, "Saccopteryx bilineata", "Imagenes usadas/m.png")
        op_2=btn_cambio("Pequeño, de color gris o chocolate y antebrazo -45mm", "Pequeño, de color gris o chocolate y antebrazo -45mm", preg_murc_84, preg_murc_85)
        volver=btn_normal("Volver", preg_murc_83)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_85 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Antebrazo desnudo, saco glandular en membrana antebrachial, peso corporal +/-4g y antebrazo de 36-43mm", preg_murc_85, "Saccopteryx leptura", "Imagenes usadas/m.png")
        op_2=btn_resultado("Antebrazo con mechones de pelo aislados, sin saco glandular en el ala, peso corporal +/-3g y antebrazo de 34-41mm", preg_murc_85, "Rhynchonycteris naso", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_84)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_86 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[5:]
        del clases[5:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Con una línea mediana dorsal de color blanquizco o amarillo, labio leporino (hendido)", "Con una línea mediana dorsal de color blanquizco o amarillo, labio leporino (hendido)", preg_murc_86, preg_murc_87)
        op_2=btn_cambio("Dorso sin líneas, labio superior normal", "Dorso sin líneas, labio superior normal", preg_murc_86, preg_murc_88)
        volver=btn_normal("Volver", preg_murc_83)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_87 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Pequeño, pies posteriores de -21mm, garras no excesivamente grandes, peso corporal +/-30g y antebrazo de 55-59mm", preg_murc_87, "Noctilio albiventris", "Imagenes usadas/m.png")
        op_2=btn_resultado("Grande, pies posteriores excepcionalmente grandes (+25mm), garras excesivamente grandes, peso corporal +/-55g y antebrazo de 81-89mm", preg_murc_87, "Noctilio leporinus", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_86)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_88 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[6:]
        del clases[6:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("Saco en forma de bolsillo en membrana antebrachial en los machos", "Saco en forma de bolsillo en membrana antebrachial en los machos", preg_murc_88, preg_murc_89)
        op_2=btn_cambio("Sin saco glandular en las alas", "Sin saco glandular en las alas", preg_murc_88, preg_murc_91)
        volver=btn_normal("Volver", preg_murc_86)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_89 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Ala conectada cerca de la base de los dedos del pie, saco cerca de antebrazo, peso corporal +/-9g y antebrazo de 45-48mm", preg_murc_89, "Cormura brevirostris", "Imagenes usadas/Murciélagos/Cormura brevirostris.png")
        op_2=btn_cambio("Ala conectada al tobillo, saco en el margen mediano o anterior de la membrana", "Ala conectada al tobillo, saco en el margen mediano o anterior de la membrana", preg_murc_89, preg_murc_90)
        volver=btn_normal("Volver", preg_murc_88)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_90 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Grande, peso corporal +/-7g y antebrazo de 44-54mm", preg_murc_90, "Peropteryx kappleri", "Imagenes usadas/m.png")
        op_2=btn_resultado("Pequeño, peso corporal +/-5g y antebrazo de 37-44mm", preg_murc_90, "Peropteryx macrotis", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_89)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_91 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[7:]
        del clases[7:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Orejas cortas, redondeadas, formando un túnel, pelo gris, pulgares rojos, peso corporal +/-3g y antebrazo de 34-36mm", preg_murc_91, "Furipterus horrens", "Imagenes usadas/m.png")
        op_2=btn_cambio("Orejas de tamaño moderado, no forman un túnel, pelo chocolate, naranja o gris-chocolate, antebrazo +44mm", "Orejas de tamaño moderado, no forman un túnel, pelo chocolate, naranja o gris-chocolate, antebrazo +44mm", preg_murc_91, preg_murc_92)
        volver=btn_normal("Volver", preg_murc_88)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_92 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[8:]
        del clases[8:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Membranas de las alas conectadas cerca de los dedos del pie, pelo largo (9mm en la cadera) y tosco, peso corporal +/-5g y antebrazo de 42-45mm", preg_murc_92, "Centronycteris maximiliani", "Imagenes usadas/m.png")
        op_2=btn_cambio("Membranas de las alas conectadas a los tobillos o en la tibia, pelo corto (5mm en la cadera) y no tosco", "Membranas de las alas conectadas a los tobillos o en la tibia, pelo corto (5mm en la cadera) y no tosco", preg_murc_92, preg_murc_93)
        volver=btn_normal("Volver", preg_murc_91)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Selecciona la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_93 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[9:]
        del clases[9:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_cambio("La espalda (en la línea mediana dorsal), dando la apariencia de una espalda desnuda", "Alas se conectan en la espalda (en la línea mediana dorsal), dando la apariencia de una espalda desnuda", preg_murc_93, preg_murc_94)
        op_2=btn_cambio("Los lados del cuerpo, solamente un poco más arriba de lo normal", "Alas se conectan en los lados del cuerpo, solamente un poco más arriba de lo normal", preg_murc_93, preg_murc_95)
        volver=btn_normal("Volver", preg_murc_92)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Alas se conectan en:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_94 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[10:]
        del clases[10:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Grande, platopatagio cubierto con muchos pelos cortos, peso corporal +/-15g y antebrazo de 49-56mm", preg_murc_94, "Pteronotus gymnonotus", "Imagenes usadas/m.png")
        op_2=btn_resultado("Pequeño, platopatagio escasa e irregularmente cubierto con pelos largos, peso corporal +/-7g y antebrazo de 40-50mm", preg_murc_94, "Pteronotus davyi", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_93)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class preg_murc_95 (Canvas):
    def __init__(self, comand):
        Canvas.__init__(self)
        del caracteristicas[10:]
        del clases[10:]
        especie_final.clear()
        imagen_final.clear()
        
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        fondo=PhotoImage(file="Imagenes usadas/Fondo.png")
        logo=PhotoImage(file="Imagenes usadas/logo.png")
        op_1=btn_resultado("Grande, peso corporal +/-23g y antebrazo de 49-65mm", preg_murc_95, "Pteronotus parnellii", "Imagenes usadas/m.png")
        op_2=btn_resultado("Pequeño, peso corporal +/-8g y antebrazo de 40-47mm", preg_murc_95, "Pteronotus personatus", "Imagenes usadas/m.png")
        volver=btn_normal("Volver", preg_murc_93)
        volver.configure(width=10, height=1)
        self.create_image(0,0, anchor="nw", image=fondo)
        self.create_image(500, 20, anchor="n", image=logo)
        self.create_text(500, 180, text="Seleccione la opción más acertada:", font=font_1, justify=tk.CENTER, width=900)
        self.create_window(250, 215, anchor="n", window=op_1)
        self.create_window(750, 215, anchor="n", window=op_2)
        self.create_window(10, 10, window=volver, anchor="nw")
        self.fondo_ref=fondo
        self.logo_ref=logo

class confirmacion(tk.Frame):
    def __init__(self, comand):
        tk.Frame.__init__(self)
        font_1=Tkfont.Font(family="Cascadia Code", size=18)
        self.configure(background="#F6F39F")
        canvas=Canvas(self)
        canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        barra=ttk.Scrollbar(self, orient=VERTICAL, command=canvas.yview)
        barra.pack(side=tk.RIGHT, fill=Y)
        canvas.configure(background="#F6F39F", yscrollcommand=barra.set)
        canvas.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        frame_sec=tk.Frame(canvas, background="#F6F39F")
        canvas.create_window(0, 0, width=980, anchor="nw", window=frame_sec)
        
        Label(frame_sec, text="Si alguno de estos datos no es correcto seleccionelo:", font=font_1, background="#F6F39F").pack(side=tk.TOP)
        conteo_de_botones=len(caracteristicas)
        botones_creados=0
        if botones_creados < conteo_de_botones:
                boton1=botones_creados
                Button(frame_sec, text=caracteristicas[boton1], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton1])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                botones_creados+=1
                
                if botones_creados < conteo_de_botones:
                        boton2=botones_creados
                        Button(frame_sec, text=caracteristicas[boton2], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton2])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                        botones_creados+=1
                        
                        if botones_creados < conteo_de_botones:
                                boton3=botones_creados
                                Button(frame_sec, text=caracteristicas[boton3], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton3])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                                botones_creados+=1

                                if botones_creados < conteo_de_botones:
                                    boton4=botones_creados
                                    Button(frame_sec, text=caracteristicas[boton4], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton4])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                                    botones_creados+=1

                                    if botones_creados < conteo_de_botones:
                                        boton5=botones_creados
                                        Button(frame_sec, text=caracteristicas[boton5], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton5])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                                        botones_creados+=1

                                        if botones_creados < conteo_de_botones:
                                            boton6=botones_creados
                                            Button(frame_sec, text=caracteristicas[boton6], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton6])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                                            botones_creados+=1

                                            if botones_creados < conteo_de_botones:
                                                boton7=botones_creados
                                                Button(frame_sec, text=caracteristicas[boton7], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton7])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                                                botones_creados+=1

                                                if botones_creados < conteo_de_botones:
                                                    boton8=botones_creados
                                                    Button(frame_sec, text=caracteristicas[boton8], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton8])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                                                    botones_creados+=1

                                                    if botones_creados < conteo_de_botones:
                                                        boton9=botones_creados
                                                        Button(frame_sec, text=caracteristicas[boton9], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton9])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                                                        botones_creados+=1

                                                        if botones_creados < conteo_de_botones:
                                                            boton10=botones_creados
                                                            Button(frame_sec, text=caracteristicas[boton10], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton10])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                                                            botones_creados+=1

                                                            if botones_creados < conteo_de_botones:
                                                                boton11=botones_creados
                                                                Button(frame_sec, text=caracteristicas[boton11], font=font_1, bg="White", wraplength=900, command=lambda:self.master.cambio(clases[boton11])).pack(side=tk.TOP, pady=5, padx=10, expand=True, fill=tk.BOTH)
                                                                botones_creados+=1

        def respuesta():
                resp=Toplevel()
                resp.geometry("480x480")
                resp.resizable(0,0)
                resp.configure(background="#F6F39F")
                font=Tkfont.Font(family="Cascadia Code", size=18, slant="italic")
                font_2=Tkfont.Font(family="Cascadia Code", size=15)
                img_ruta=imagen_final[0]
                murc_img=tk.PhotoImage(file=img_ruta)
                tk.Label(resp, text=("Su murciélago es "+especie_final[0]), font=font, wraplength=450, background="#F6F39F").pack(side=tk.TOP, pady=20)
                tk.Label(resp, image=murc_img).pack(side=tk.TOP, pady=20)
                if urls[especie_final[0]] is not None:
                    tk.Button(resp, height=15, text="Más información", font=font_2, command=lambda:[webbrowser.open(urls[especie_final[0]])]).pack(side=tk.LEFT, anchor="s", pady=20, padx=10)
                    tk.Button(resp, height=15, text="Cerrar", font=font_2, command=lambda:[resp.destroy(), self.master.cambio(inicio)]).pack(side=tk.RIGHT, anchor="s", pady=20, padx=10)
                else:
                    tk.Button(resp, height=15, text="Cerrar", font=font_2, command=lambda:[resp.destroy(), self.master.cambio(inicio)]).pack(side=tk.BOTTOM, pady=20, padx=10)
                self.ref=murc_img
        
        Button(frame_sec, text="Continuar", font=Tkfont.Font(family="Cascadia Code", size=15), bg="White", command=lambda:[respuesta()]).pack(side=tk.BOTTOM, pady=5, padx=200, expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    app = CF()
    app.mainloop()