import tkinter as tk


def cerrar(self):
    self.ventana.destroy()



class list:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Lista de Precios")
        self.ventana.geometry('570x780')
        self.ventana.configure(background='#344e41')

        # linea de arriba
        self.texto0 = tk.Label(self.ventana, text="PLATILLOS", bg="#344e41", fg="black", font=('Arial', 12),
                               foreground='#ffffff', relief='raised',)
        self.texto1 = tk.Label(self.ventana, text="SUBTOTAL", bg="#344e41", fg="black", font=('Arial', 12),
                               foreground='#ffffff', relief='raised',)
        self.texto2 = tk.Label(self.ventana, text="TOTAL", bg="#344e41", fg="black", font=('Arial', 12),
                               foreground='#ffffff', relief='raised',)
        # posicion de linea de arriba
        self.texto0.grid(row=0, column=0, padx=20, pady=20)
        self.texto1.grid(row=0, column=2, padx=20, pady=20)
        self.texto2.grid(row=0, column=4, padx=20, pady=20)
        # platillos
        self.platillo0 = tk.Label(self.ventana, text="Cemita", bg="#344e41", fg="white")
        self.platillo1 = tk.Label(self.ventana, text="Chile En Nogada", bg="#344e41", fg="white")
        self.platillo2 = tk.Label(self.ventana, text="Chalupa", bg="#344e41", fg="white")
        self.platillo3 = tk.Label(self.ventana, text="Mole Poblano", bg="#344e41", fg="white")
        self.platillo4 = tk.Label(self.ventana, text="Taco Arabe", bg="#344e41", fg="white")
        self.platillo5 = tk.Label(self.ventana, text="Molotes", bg="#344e41", fg="white")
        self.platillo6 = tk.Label(self.ventana, text="Enchiladas De Pipian", bg="#344e41", fg="white")
        self.platillo7 = tk.Label(self.ventana, text="Tortitas De Santa Clara", bg="#344e41", fg="white")
        self.platillo8 = tk.Label(self.ventana, text="Refresco", bg="#344e41", fg="white")
        self.platillo9 = tk.Label(self.ventana, text="Agua De Sabor", bg="#344e41", fg="white")
        # posicion de platillos
        self.platillo0.grid(row=1, column=0, padx=20, pady=20)
        self.platillo1.grid(row=2, column=0, padx=20, pady=20)
        self.platillo2.grid(row=3, column=0, padx=20, pady=20)
        self.platillo3.grid(row=4, column=0, padx=20, pady=20)
        self.platillo4.grid(row=5, column=0, padx=20, pady=20)
        self.platillo5.grid(row=6, column=0, padx=20, pady=20)
        self.platillo6.grid(row=7, column=0, padx=20, pady=20)
        self.platillo7.grid(row=8, column=0, padx=20, pady=20)
        self.platillo8.grid(row=9, column=0, padx=20, pady=20)
        self.platillo9.grid(row=10, column=0, padx=20, pady=20)
        # subtotal
        self.subtotal0 = tk.Label(self.ventana, text="$59.84", bg="#344e41", fg="white")
        self.subtotal1 = tk.Label(self.ventana, text="$249.84", bg="#344e41", fg="white")
        self.subtotal2 = tk.Label(self.ventana, text="$34.84", bg="#344e41", fg="white")
        self.subtotal3 = tk.Label(self.ventana, text="$59.84", bg="#344e41", fg="white")
        self.subtotal4 = tk.Label(self.ventana, text="$19.84", bg="#344e41", fg="white")
        self.subtotal5 = tk.Label(self.ventana, text="$54.84", bg="#344e41", fg="white")
        self.subtotal6 = tk.Label(self.ventana, text="$39.84", bg="#344e41", fg="white")
        self.subtotal7 = tk.Label(self.ventana, text="$14.84", bg="#344e41", fg="white")
        self.subtotal8 = tk.Label(self.ventana, text="$19.84", bg="#344e41", fg="white")
        self.subtotal9 = tk.Label(self.ventana, text="$14.84", bg="#344e41", fg="white")
        # posicion de subtotal
        self.subtotal0.grid(row=1, column=2, padx=20, pady=20)
        self.subtotal1.grid(row=2, column=2, padx=20, pady=20)
        self.subtotal2.grid(row=3, column=2, padx=20, pady=20)
        self.subtotal3.grid(row=4, column=2, padx=20, pady=20)
        self.subtotal4.grid(row=5, column=2, padx=20, pady=20)
        self.subtotal5.grid(row=6, column=2, padx=20, pady=20)
        self.subtotal6.grid(row=7, column=2, padx=20, pady=20)
        self.subtotal7.grid(row=8, column=2, padx=20, pady=20)
        self.subtotal8.grid(row=9, column=2, padx=20, pady=20)
        self.subtotal9.grid(row=10, column=2, padx=20, pady=20)
        # total
        self.total0 = tk.Label(self.ventana, text="$60", bg="#344e41", fg="white")
        self.total1 = tk.Label(self.ventana, text="$250", bg="#344e41", fg="white")
        self.total2 = tk.Label(self.ventana, text="$35", bg="#344e41", fg="white")
        self.total3 = tk.Label(self.ventana, text="$60", bg="#344e41", fg="white")
        self.total4 = tk.Label(self.ventana, text="$20", bg="#344e41", fg="white")
        self.total5 = tk.Label(self.ventana, text="$55", bg="#344e41", fg="white")
        self.total6 = tk.Label(self.ventana, text="$40", bg="#344e41", fg="white")
        self.total7 = tk.Label(self.ventana, text="$15", bg="#344e41", fg="white")
        self.total8 = tk.Label(self.ventana, text="$20", bg="#344e41", fg="white")
        self.total9 = tk.Label(self.ventana, text="$15", bg="#344e41", fg="white")
        # posicion de total
        self.total0.grid(row=1, column=4, padx=20, pady=20)
        self.total1.grid(row=2, column=4, padx=20, pady=20)
        self.total2.grid(row=3, column=4, padx=20, pady=20)
        self.total3.grid(row=4, column=4, padx=20, pady=20)
        self.total4.grid(row=5, column=4, padx=20, pady=20)
        self.total5.grid(row=6, column=4, padx=20, pady=20)
        self.total6.grid(row=7, column=4, padx=20, pady=20)
        self.total7.grid(row=8, column=4, padx=20, pady=20)
        self.total8.grid(row=9, column=4, padx=20, pady=20)
        self.total9.grid(row=10, column=4, padx=20, pady=20)
        # boton
        self.botoncerrar = tk.Button(self.ventana, text="Cerrar", bg="red", fg="black", command=lambda: cerrar(self))
        self.botoncerrar.grid(row=11, column=3, padx=20, pady=20)
        self.botonatras = tk.Button(self.ventana, text="Atras", fg="black", command=lambda: cerrar(self))
        self.botonatras.grid(row=11, column=1, padx=20, pady=20)
