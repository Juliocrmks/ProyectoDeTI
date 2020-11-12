import tkinter as tk
import json
import datetime


# funcion para cerrar
def cerrar(self):
    self.ventana.destroy()


# funcion para reportar el pedido
class reportePedido:
    def __init__(self, id):
        self.id = id

        self.ventana = tk.Tk()
        self.ventana.title("Reporte de Pedido ")
        self.ventana.geometry('490x700')
        self.ventana.configure(background='#344e41')

        today = datetime.datetime.now()
        x = today.strftime("%Y")
        if x == "2020":
            filename = "2020.json"
        elif x == "2021":
            filename = "2021.json"
        elif x == "2022":
            filename = "2022.json"
        elif x == "2023":
            filename = "2023.json"
        elif x == "2024":
            filename = "2024.json"
        elif x == "2025":
            filename = "2025.json"
        elif x == "2026":
            filename = "2026.json"
        with open(filename, 'r') as f:
            data = json.load(f)

        self.texto1 = tk.Label(self.ventana, text="ID : ", bg="#344e41", fg="black", font=('Arial', 12),
                               foreground='#ffffff')
        # aqui va el ID
        self.texto2 = tk.Label(self.ventana, text=id, bg="#344e41", fg="black", font=('Arial', 12),
                               foreground='#ffffff')

        self.frameText = tk.Frame(self.ventana, relief="ridge", width=300, height=525, bg="#000000")
        self.frameText.columnconfigure(3)
        self.frameText.rowconfigure(15)

        # asi es como vas metiendo la informacion
        self.nombre = tk.Label(self.frameText, text="  NOMBRE  ", pady=10, padx=10, bg='#000000', foreground="#ffffff",
                               font=('Arial', 12))
        self.precio = tk.Label(self.frameText, text="  PRECIO  ", pady=10, padx=10, bg='#000000', foreground="#ffffff",
                               font=('Arial', 12))

        self.botoncerrar = tk.Button(self.ventana, text="Cerrar", bg="red", fg="black", command=lambda: cerrar(self))

        self.texto1.grid(row=0, column=0, padx=30, pady=30)
        self.texto2.grid(row=0, column=2, padx=30, pady=30)
        self.frameText.grid(column=2, row=1)
        self.botoncerrar.grid(row=9, column=2, padx=30, pady=30)

        self.nombre.grid(column=0, row=0, padx=10, pady=5)
        self.precio.grid(column=1, row=0, padx=10, pady=5)
        self.frameText.grid_propagate(0)

        counter = 1
        for dish in data[id]:
            for item in range(len(dish)):
                if counter <= len(dish):
                    itemName = id
                    itemName = dish['item' + str(counter)]['name']
                    labelDeItem = tk.Label(self.frameText, text=itemName, pady=5, padx=10, bg='#000000',
                                           foreground="#ffffff").grid(column=0, row=(counter + 1), padx=10, pady=1)
                    itemPrice = dish['item' + str(counter)]['price']
                    labelDePrecio = tk.Label(self.frameText, text=itemPrice, pady=5, padx=10, bg='#000000',
                                            foreground="#ffffff").grid(column=1, row=(counter + 1), padx=10, pady=1)
                    counter += 1
        self.labelTotalNombre = tk.Label(self.frameText, text="Total", pady=5, padx=10, bg='#000000',
                                   foreground="#ffffff").grid(column=0, row=(counter + 1), padx=10, pady=1)
        self.itemTotal = data[id][1]['total']
        self.labelTotal = tk.Label(self.frameText, text=self.itemTotal, pady=5, padx=10, bg='#000000',
                                   foreground="#ffffff").grid(column=1, row=(counter + 1), padx=10, pady=1)
