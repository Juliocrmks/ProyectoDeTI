import tkinter as tk
import json

def cerrar(self):
    self.ventana.destroy()

class reportePedido:
    def __init__(self, id):
        self.id = id

        self.ventana = tk.Tk()
        self.ventana.title("Reporte de Pedido ")
        self.ventana.geometry('640x465')
        self.ventana.configure(background='#344e41')

        with open('jsontest.json', 'r') as f:
            data = json.load(f)


        self.texto1 = tk.Label(self.ventana, text="ID : ", bg="#344e41", fg="black", font=('Arial', 12),
                               foreground='#ffffff')
        #aqui va el ID
        self.texto2 = tk.Label(self.ventana, text=id, bg="#344e41", fg="black", font=('Arial', 12),
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

        counter = 1
        for dish in data[id]:
            if counter != len(data[id]):
                itemName = id
                itemName = dish['item'+ str(counter)]['name']
                labelDeItem = tk.Label(self.frameText, text=itemName, pady=20, padx=10, bg='#588157', foreground="#ffffff").grid(column=0, row=(counter+1), padx=10, pady=10)
                itemPrice = dish['item'+ str(counter)]['price']
                labelDePrecio = tk.Label(self.frameText, text=itemPrice, pady=20, padx=10, bg='#588157', foreground="#ffffff").grid(column=1, row=(counter+1), padx=10, pady=10)
                counter +=1

        self.botoncerrar = tk.Button(self.ventana, text="Cerrar", bg="red", fg="black", command=lambda: cerrar(self))

        self.texto1.grid(row=0, column=0, padx=30, pady=30)
        self.texto2.grid(row=0, column=2, padx=30, pady=30)
        self.frameText.grid(column=2, row=1)
        self.botoncerrar.grid(row=9, column=2, padx=30, pady=30)

        self.nombre.grid(column=0, row=0, padx=10, pady=10)
        self.precio.grid(column=1, row=0, padx=10, pady=10)
        self.frameText.grid_propagate(0)



