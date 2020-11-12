from tkinter import *
from GenerateReport import geneRepo
from PriceList import list
from Registro import Register


# funcion para abrir el registro
def openRegistro():
    Registro = Register()
    Registro.screen.mainloop


# funcion para abrir el generador de reportes
def openGenerate():
    generate = geneRepo()
    generate.root.mainloop


# funcion para abrir la lista de comidas
def openList():
    open = list()
    open.ventana.mainloop


# main
if __name__ == '__main__':
    root = Tk()
    root.title("Proyecto V0.9.5")

    # Marco principal de la pantalla
    frameMain = Frame(root, height=400, width=800, bg="#344e41")
    frameMain.rowconfigure(3)
    frameMain.columnconfigure(3)

    frameTitle = Frame(frameMain, bg="#344e41")

    labelTitle = Label(frameTitle, text="Antojitos\nPoblanos", bg='#344e41', foreground='#ffffff', relief='raised',
                       font=('Arial', 22))

    frameButtons = Frame(frameMain, bg="#344e41")
    frameButtons.columnconfigure(3)

    frameMain.grid()
    frameTitle.grid(row=0, column=1, sticky='n', columnspan=3, pady=15)
    labelTitle.grid()
    frameButtons.grid(row=1, column=1, columnspan=3, sticky='nswe')

    # Botones para escoger
    buttonList = Button(frameButtons, text="Lista de precios", pady=30, padx=15, bg="#588157", foreground='#ffffff'
                        , font=('Arial', 12), command=lambda: openList())
    buttonOrders = Button(frameButtons, text="Registro de pedidos", pady=30, padx=15, bg='#588157', foreground='#ffffff'
                          , font=('Arial', 12), command=lambda: openRegistro())
    buttonGenerate = Button(frameButtons, text="Generar pedido", pady=30, padx=15, bg='#588157', foreground='#ffffff'
                            , font=('Arial', 12), command=lambda: openGenerate())

    buttonList.grid(row=0, column=0, padx=10, pady=10)
    buttonOrders.grid(row=0, column=1, padx=10, pady=10)
    buttonGenerate.grid(row=0, column=2, padx=10, pady=10)

    root.mainloop()
