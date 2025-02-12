from tkinter import *
import json
import datetime
from OK import oki


# Agrega cemita al json
def agregar_cemita(self):

    c = {"name": "Cemita",
         "price": 60,
         "id": 000
    }
    self.total += 60
    self.orden.append(c)
    imprimir_orden(self)


# Agrega chile en nogada al json
def agregar_chile_en_nogada(self):
    ch = {'name': 'Chile En Nogada',
          'price': 250,
          'id': 100
    }
    self.total += 250
    self.orden.append(ch)
    imprimir_orden(self)


# Agrega chalupa al json
def agregar_chalupa(self):
    cha = {'name': 'Chalupa',
           'price': 35,
           'id': 200
    }
    self.total += 35
    self.orden.append(cha)
    imprimir_orden(self)


# Agrega mole poblano al json
def agregar_mole_poblano(self):
    mp = {'name': 'Mole Poblano',
          'price': 60,
          'id': 300
         }
    self.total += 60
    self.orden.append(mp)
    imprimir_orden(self)


# Agrega taco arabe al json
def agregar_taco_arabe(self):
    ta = {'name': 'Taco Arabe',
          'price': 20,
          'id': 400
         }
    self.total += 20
    self.orden.append(ta)
    imprimir_orden(self)


# Agrega molotes al json
def agregar_molotes(self):
    m = {'name': 'Molotes',
         'price': 55,
         'id': 500
         }
    self.total += 55
    self.orden.append(m)
    imprimir_orden(self)


# Agrega enchiladas de pipian al json
def agregar_enchiladas_de_pipian(self):
    edp = {'name': 'Enchiladas De Pipian',
           'price': 40,
           'id': 600
         }
    self.total += 40
    self.orden.append(edp)
    imprimir_orden(self)


# Agrega tortitas de santa clara al json
def agregar_tortitas_de_santa_clara(self):
    tdsc = {'name': 'Tortitas De Santa Clara',
            'price': 15,
            'id': 700
         }
    self.total += 15
    self.orden.append(tdsc)
    imprimir_orden(self)


# Agrega refresco al json
def agregar_refrescos(self):
    r = {'name': 'Refrescos',
         'price': 20,
         'id': 800
         }
    self.total += 20
    self.orden.append(r)
    imprimir_orden(self)


# Agrega agua de sabor al json
def agregar_agua_de_sabor(self):
    ads = {'name': 'Agua De Sabor',
           'price': 15,
           'id': 900
         }
    self.total += 15
    self.orden.append(ads)
    imprimir_orden(self)


# funcion de aceptar la orden
def accept(self):
    imprimir_orden(self)
    saveToJson(self)
    self.root.destroy()
    ventanaoki = oki()
    ventanaoki.ventana.mainloop()


# funcion de cancelar la orden
def cancel(self):
    self.root.destroy()
    rootgenerepo=geneRepo()
    rootgenerepo.root.mainloop()


# funcion de imprimir la orden
def imprimir_orden(self):
    self.labelNumTotal.configure(text=str(self.total))
    n = len(self.orden)
    i = 0
    self.frameText.rowconfigure(n)
    self.frameText.columnconfigure(3)
    self.frameText.grid_propagate(0)
    for item in self.orden:
        label_name = Label(self.frameText, text=item['name'], foreground='#ffffff', bg='#000000', justify='left')
        label_price = Label(self.frameText, text=item['price'], foreground='#ffffff', bg='#000000', justify='right')
        label_name.grid(column=0, row=i, sticky='w')
        label_price.grid(column=1, row=i, sticky='e')
        i += 1


# funcion que genera el id en el json
def generate_id(self):
    today = datetime.datetime.now()
    return today.strftime("%d/%m/%Y_%H:%M.%S")


# funcion que guarda al json
def saveToJson(self):
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
    id = generate_id(self)
    platillo = {}
    pedido = {}
    lista =[]
    i = 1
    for item in self.orden:
        platillo['item' + str(i)] = item
        i=i+1
    lista.append(platillo)   
    totalDict = {'total':self.total}
    self.orden[-1] = totalDict
    lista.append(totalDict)
    print(totalDict)

    pedido[id] = lista
    with open(filename,'r+') as read_file:
        data = json.load(read_file)
        data.update(pedido)
        read_file.seek(0)
        json.dump(data, read_file, indent=4)


# Clase para generar reporte
class geneRepo:
    def __init__(self):
        self.root = Tk()
        self.root.title("Generar Reporte")
        self.total = 0

        # Marco principal de la pantalla
        self.frameMain = Frame(self.root, height=400, width=800, bg="#344e41")
        # Marco de texto negro
        self.frameText = Frame(self.frameMain, borderwidth=10, relief="ridge", width=300, height=340,
                               bg="#000000")
        # Marco de botones
        self.frameButtons1 = Frame(self.frameMain, bg='#344e41')
        self.frameButtons1.columnconfigure(2)
        self.frameButtons1.rowconfigure(3)
        # marco de botones 2
        self.frameButtons2 = Frame(self.frameMain, width=400, bg="#344e41")
        self.frameButtons2.columnconfigure(4)
        self.frameButtons2.rowconfigure(1)

        self.frameMain.grid(column=0, row=0)
        self.frameText.grid(column=1, row=0)
        self.frameText.grid_propagate(0)
        self.frameButtons1.grid(column=0, row=0, columnspan=1, rowspan=2)
        self.frameButtons2.grid(column=1, row=1)

        # Botones de comidas
        self.buttonCemita = Button(self.frameButtons1, text="  Cemita  ", pady=20, padx=10,
                                   command=lambda: agregar_cemita(self), bg='#588157', foreground="#ffffff")
        self.buttonTacoArabe = Button(self.frameButtons1, text="Taco Arabe", pady=20, padx=10,
                                      command=lambda: agregar_taco_arabe(self), bg='#588157', foreground="#ffffff")
        self.buttonChilesEnNogada = Button(self.frameButtons1, text="Chiles en \nNogada", pady=10, padx=10,
                                           command=lambda: agregar_chile_en_nogada(self), bg='#588157',
                                           foreground="#ffffff")
        self.buttonChalupas = Button(self.frameButtons1, text="Chalupas", pady=20, padx=10,
                                     command=lambda: agregar_chalupa(self), bg='#588157', foreground="#ffffff")
        self. buttonMolotes = Button(self.frameButtons1, text="Molotes", pady=20, padx=10,
                                     command=lambda: agregar_molotes(self), bg='#588157', foreground="#ffffff")
        self. buttonMolePoblano = Button(self.frameButtons1, text="Mole\nPoblano", pady=10, padx=10,
                                         command=lambda: agregar_mole_poblano(self), bg='#588157', foreground="#ffffff")
        self.buttonEnchiladasDePipian = Button(self.frameButtons1, text="Enchiladas \nDe Pipian", pady=10, padx=10,
                                               command=lambda: agregar_enchiladas_de_pipian(self), bg='#588157',
                                               foreground="#ffffff")
        self.buttonTortitasDeSantaClara = Button(self.frameButtons1, text="Tortitas De\nSanta Clara", pady=10, padx=10,
                                                 command=lambda: agregar_tortitas_de_santa_clara(self), bg='#588157',
                                                 foreground="#ffffff")
        self.buttonRefresco = Button(self.frameButtons1, text="Refresco", pady=10, padx=10,
                                     command=lambda: agregar_refrescos(self), bg='#588157', foreground="#ffffff")
        self.buttonAguaDeSabor = Button(self.frameButtons1, text="Agua De\nSabor", pady=10, padx=10,
                                        command=lambda: agregar_agua_de_sabor(self), bg='#588157', foreground="#ffffff")
        self.labeltotal = Label(self.frameButtons2, text="Total: ", pady=10, padx=10, bg="#344e41", foreground="#ffffff")
        self.labelNumTotal = Label(self.frameButtons2, text=str(self.total), bg="#344e41", foreground="#ffffff")
        self.buttonAccept = Button(self.frameButtons2, text="  Aceptar  ", pady=10, padx=5, command=lambda: accept(self),
                                   bg='#109401', foreground="#ffffff")
        self.buttonCancel = Button(self.frameButtons2, text="  Borrar  ", pady=10, padx=5, command=lambda: cancel(self),
                                   bg='#ad0205', foreground="#ffffff")
        # Cuadricula los botones
        self.buttonCemita.grid(row=0, column=0, padx=10, pady=10)
        self.buttonTacoArabe.grid(row=0, column=1, padx=10, pady=10)
        self.buttonChilesEnNogada.grid(row=1, column=0, padx=10, pady=10)
        self.buttonChalupas.grid(row=1, column=1, padx=10, pady=10)
        self.buttonMolotes.grid(row=2, column=0, padx=10, pady=10)
        self.buttonMolePoblano.grid(row=2, column=1, padx=10, pady=10)
        self.buttonEnchiladasDePipian.grid(row=3, column=0, padx=10, pady=10)
        self.buttonTortitasDeSantaClara.grid(row=3, column=1, padx=10, pady=10)
        self.buttonRefresco.grid(row=4, column=0, padx=10, pady=10)
        self.buttonAguaDeSabor.grid(row=4, column=1, padx=10, pady=10)

        self.labeltotal.grid(column=0, row=0, padx=10, pady=10)
        self.labelNumTotal.grid(column=1, row=0, padx=10, pady=10)
        self.buttonAccept.grid(column=2, row=0, padx=10, pady=10)
        self.buttonCancel.grid(column=3, row=0, padx=10, pady=10)
        
        self.orden = []
