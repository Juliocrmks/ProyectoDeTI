import tkinter as tk
import json 
from reportePedido import reportePedido


# funcion para abrir la pagina de la orden
def open_order_resp(self, id):
    pedidoEspecifico = reportePedido(id)
    pedidoEspecifico.ventana.mainloop()


# funcion para crear ventana del 2020
def create_window_2020(self):
    root = tk.Tk()
    root.title("2020")
    container = tk.Frame(root)
    canvas = tk.Canvas(container, bg="#344e41")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#344e41")
    canvas.config(width = 180)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    with open('2020.json','r') as f:
        data = json.load(f)
        for item in data:
            id = item
            buttonAbrirPedidos = tk.Button(scrollable_frame, text=item, pady=20, padx=10, bg='#588157',
                                           foreground="#ffffff", command=lambda i=item: open_order_resp(self, i)).pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


# funcion para crear ventana del 2021
def create_window_2021(self):
    root = tk.Tk()
    root.title("2021")
    container = tk.Frame(root)
    canvas = tk.Canvas(container, bg="#344e41")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#344e41")
    canvas.config(width=180)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    with open('2021.json', 'r') as f:
        data = json.load(f)
        for item in data:
            id = item
            buttonAbrirPedidos = tk.Button(scrollable_frame, text=item, pady=20, padx=10, bg='#588157',
                                           foreground="#ffffff", command=lambda i=item: open_order_resp(self, i)).pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


# funcion para crear ventana del 2022
def create_window_2022(self):
    root = tk.Tk()
    root.title("2022")
    container = tk.Frame(root)
    canvas = tk.Canvas(container, bg="#344e41")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#344e41")
    canvas.config(width=180)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    with open('2022.json', 'r') as f:
        data = json.load(f)
        for item in data:
            id = item
            buttonAbrirPedidos = tk.Button(scrollable_frame, text=item, pady=20, padx=10, bg='#588157',
                                           foreground="#ffffff", command=lambda i=item: open_order_resp(self, i)).pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


# funcion para crear ventana del 2023
def create_window_2023(self):
    root = tk.Tk()
    root.title("2023")
    container = tk.Frame(root)
    canvas = tk.Canvas(container, bg="#344e41")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#344e41")
    canvas.config(width=180)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    with open('2023.json', 'r') as f:
        data = json.load(f)
        for item in data:
            id = item
            buttonAbrirPedidos = tk.Button(scrollable_frame, text=item, pady=20, padx=10, bg='#588157',
                                           foreground="#ffffff", command=lambda i=item: open_order_resp(self, i)).pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


# funcion para crear ventana del 2024
def create_window_2024(self):
    root = tk.Tk()
    root.title("2024")
    container = tk.Frame(root)
    canvas = tk.Canvas(container, bg="#344e41")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#344e41")
    canvas.config(width=180)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    with open('2024.json', 'r') as f:
        data = json.load(f)
        for item in data:
            id = item
            buttonAbrirPedidos = tk.Button(scrollable_frame, text=item, pady=20, padx=10, bg='#588157',
                                           foreground="#ffffff", command=lambda i=item: open_order_resp(self, i)).pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


# funcion para crear ventana del 2025
def create_window_2025(self):
    root = tk.Tk()
    root.title("2025")
    container = tk.Frame(root)
    canvas = tk.Canvas(container, bg="#344e41")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#344e41")
    canvas.config(width=180)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    with open('2025.json', 'r') as f:
        data = json.load(f)
        for item in data:
            id = item
            buttonAbrirPedidos = tk.Button(scrollable_frame, text=item, pady=20, padx=10, bg='#588157',
                                           foreground="#ffffff", command=lambda i=item: open_order_resp(self, i)).pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


# funcion para crear ventana del 2026
def create_window_2026(self):
    root = tk.Tk()
    root.title("2026")
    container = tk.Frame(root)
    canvas = tk.Canvas(container, bg="#344e41")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#344e41")
    canvas.config(width=180)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    with open('2026.json', 'r') as f:
        data = json.load(f)
        for item in data:
            id = item
            buttonAbrirPedidos = tk.Button(scrollable_frame, text=item, pady=20, padx=10, bg='#588157',
                                           foreground="#ffffff", command=lambda i=item: open_order_resp(self, i)).pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


# clase de registro
class Register:
    def __init__(self):

        self.screen = tk.Tk()
        self.screen.title("Registro")
        self.screen.geometry('237x370')
        self.screen.configure(background='#344e41')

        self.text = tk.Label(self.screen, text="Selcciona año", fg="white", bg="#344e41")
        self.text.grid(row=0, column=0, padx=20, pady=20)

        # botones de los años
        self.button1 = tk.Button(self.screen, text="2020", padx=20, pady=20,
                                 command=lambda: create_window_2020(self), fg="white", bg="#588157")
        self.button2 = tk.Button(self.screen, text="2021", padx=20, pady=20,
                                 command=lambda: create_window_2021(self), fg="white", bg="#588157")
        self.button3 = tk.Button(self.screen, text="2022", padx=20, pady=20,
                                 command=lambda: create_window_2022(self), fg="white", bg="#588157")
        self.button4 = tk.Button(self.screen, text="2023", padx=20, pady=20,
                                 command=lambda: create_window_2023(self), fg="white", bg="#588157")
        self.button5 = tk.Button(self.screen, text="2024", padx=20, pady=20,
                                 command=lambda: create_window_2024(self), fg="white", bg="#588157")
        self.button6 = tk.Button(self.screen, text="2025", padx=20, pady=20,
                                 command=lambda: create_window_2025(self), fg="white", bg="#588157")
        self.button7 = tk.Button(self.screen, text="2026", padx=20, pady=20,
                                 command=lambda: create_window_2026(self), fg="white", bg="#588157")

        self.button1.grid(row=2, column=0, padx=20, pady=20)
        self.button2.grid(row=2, column=1, padx=20, pady=20)
        self.button3.grid(row=3, column=0, padx=20, pady=20)
        self.button4.grid(row=3, column=1, padx=20, pady=20)
        self.button5.grid(row=4, column=0, padx=20, pady=20)
        self.button6.grid(row=4, column=1, padx=20, pady=20)