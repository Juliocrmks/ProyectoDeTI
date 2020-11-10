import tkinter as tk

def boton_Cerrar(self):
    self.ventana.destroy()

class oki:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Confirmacion")
        self.ventana.geometry('300x110')
        self.ventana.configure(background='#344e41')


        self.text = tk.Label(self.ventana, text="Reporte guardado exitosamente.", bg="#344e41", fg="white")
        self.text.grid(row=1, column=0, padx=20, pady=20)
        self.buttonok = tk.Button(self.ventana, text="  Aceptar  ", pady=5, padx=5,
                                   command=lambda: boton_Cerrar(self), bg='#588157', foreground="#ffffff")
        self.buttonok.grid(row=2, column=1, padx=5, pady=5)