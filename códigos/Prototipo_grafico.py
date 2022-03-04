from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk

raiz=Tk()
raiz.title("Taxonomía Programada")
raiz.resizable(True,True)

indice=ttk.Frame(raiz, relief="raised",borderwidth=2, padding=(10,10))
indice.pack(padx=5, pady=5)

murcielago_icono=PhotoImage(file="murcielago-boton.png").subsample(4,4)
felino_icono=PhotoImage(file="felino-boton.png").subsample(4,4)
mariposa_icono=PhotoImage(file="mariposa-boton.png").subsample(4,4)

titulo=Label(indice, text="Taxonomía Programada", font=("Gagalin", 25), fg="green").grid(column=2, row=0)
msg_slc=Label(indice, text="Seleccione el animal que está estudiando:"). grid(column=2, row=1)

boton_murcielago=Button(indice, text="Murciélagos", image=murcielago_icono, compound=TOP).grid(column=1, row=3, ipadx=10)
boton_felino=Button(indice, text="Felinos", image=felino_icono, compound=TOP).grid(column=2, row=3, ipadx=10)
boton_mariposa=Button(indice, text="Mariposas", image=mariposa_icono, compound=TOP).grid(column=3, row=3, ipadx=10)

raiz.mainloop()