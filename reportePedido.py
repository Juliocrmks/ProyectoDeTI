import tkinter as tk


def cerrar(self):
    self.ventana.destroy()

class reportePedido:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reporte de Pedido ")
        self.ventana.geometry('640x465')
        self.ventana.configure(background='#344e41')

        self.texto1 = tk.Label(self.ventana, text="ID : ", bg="#344e41", fg="black", font=('Arial', 12),
                               foreground='#ffffff')
        #aqui va el ID
        self.texto2 = tk.Label(self.ventana, text="899-999-000", bg="#344e41", fg="black", font=('Arial', 12),
                               foreground='#ffffff')

        self.frameText = tk.Label(self.ventana, relief="ridge", width=50, height=20,
                               bg="#000000")
        #esto es del cuadro negro donde van los datos son 2 columnas y puse extra filas
        self.frameLabels = tk.Label(self.ventana, width=400, bg="#344e41")
        self.frameLabels.columnconfigure(1)
        self.frameLabels.rowconfigure(15)

        #asi es como vas metiendo la informacion
        self.nombre = tk.Label(self.frameText, text="  NOMBRE  ", pady=10, padx=5,width=28,
                           bg='#000000', foreground="#ffffff",font=('Arial', 12))
        self.precio = tk.Label(self.frameText, text="  PRECIO  ", pady=10, padx=5,width=28,
                           bg='#000000', foreground="#ffffff",font=('Arial', 12))


        self.botoncerrar = tk.Button(self.ventana, text="Cerrar", bg="red", fg="black", command=lambda: cerrar(self))



        self.texto1.grid(row=0, column=0, padx=30, pady=30)
        self.texto2.grid(row=0, column=2, padx=30, pady=30)
        self.frameText.grid(column=2, row=1)
        self.botoncerrar.grid(row=9, column=2, padx=30, pady=30)

        self.nombre.grid(column=0, row=1, padx=10, pady=10)
        self.precio.grid(column=1, row=1, padx=10, pady=10)
        self.frameText.grid_propagate(0)



