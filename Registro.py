import tkinter as tk


def create_window_2020(self):
    root = tk.Tk()
    root.title("Registro")
    container = tk.Frame(root)
    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient= "vertical", command= canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

   # with open('jsontest.json', 'r') as read_file:
        #data = json.load(read_file)

    # for item in data:
    #     textforButton = item
    #     labeltotal = data[item][-1]['total']
    #     button = Button(text=textforButton).grid

    for i in range(50):
        tk.Label(scrollable_frame, text="Sample scrolling label").pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()

def create_window_2021(self):
    toplevel = tk.Toplevel()
    toplevel.title('2021')
    toplevel.geometry('400x400')
    toplevel.focus_set()
    toplevel.configure(background='#344e41')
    toplevel.scrollbar = tk.Scrollbar(toplevel, orient="vertical")
    toplevel.scrollbar.grid(row="0", column="1", sticky="E")

def create_window_2022(self):
    toplevel = tk.Toplevel()
    toplevel.title('2022')
    toplevel.geometry('400x400')
    toplevel.focus_set()
    toplevel.configure(background='#344e41')
    toplevel.scrollbar = tk.Scrollbar(toplevel, orient="vertical")
    toplevel.scrollbar.grid(row="0", column="1", sticky="E")

def create_window_2023(self):
    toplevel = tk.Toplevel()
    toplevel.title('2023')
    toplevel.geometry('400x400')
    toplevel.focus_set()
    toplevel.configure(background='#344e41')
    toplevel.scrollbar = tk.Scrollbar(toplevel, orient="vertical")
    toplevel.scrollbar.grid(row="0", column="1", sticky="E")

def create_window_2024(self):
    toplevel = tk.Toplevel()
    toplevel.title('2024')
    toplevel.geometry('400x400')
    toplevel.focus_set()
    toplevel.configure(background='#344e41')
    toplevel.scrollbar = tk.Scrollbar(toplevel, orient="vertical")
    toplevel.scrollbar.grid(row="0", column="1", sticky="E")

def create_window_2025(self):
    toplevel = tk.Toplevel()
    toplevel.title('2025')
    toplevel.geometry('400x400')
    toplevel.focus_set()
    toplevel.configure(background='#344e41')
    toplevel.scrollbar = tk.Scrollbar(toplevel, orient="vertical")
    toplevel.scrollbar.grid(row="0", column="1", sticky="E")

def create_window_2026(self):
    toplevel = tk.Toplevel()
    toplevel.title('2026')
    toplevel.geometry('400x400')
    toplevel.focus_set()
    toplevel.configure(background='#344e41')
    toplevel.scrollbar = tk.Scrollbar(toplevel, orient="vertical")
    toplevel.scrollbar.grid(row="0", column="1", sticky="E")

def cerrar(self):
    self.screen.destroy()

class Register:
    def __init__(self):

        self.screen = tk.Tk()
        self.screen.title("Registro de pedidos")
        self.screen.geometry('225x400')
        self.screen.configure(background='#344e41')

        self.text = tk.Label(self.screen, text="Selcciona año", fg="white", bg="#344e41")
        self.text.grid(row=0, column=0, padx=20, pady=20)

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


