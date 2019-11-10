from disco import Disco
from memoriaFisica import Memoria 
from memoriaVirtual import MemoriaVirtual 
import random
import time
import threading
import sys
import tkinter as tk
from tkinter import ttk


memoriaVirtual = MemoriaVirtual(4)

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_widgets()

    def set_widgets(self):
        # Inicia o Treeview com as seguintes colunas:
        self.dataCols = ('BitR', 'Time', 'index','Process Pid')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)


        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        # Dados:
        self.data = memoriaVirtual.getMemoriaVirtual()

        # Insere cada item dos dados
        for item in self.data:
            self.tree.insert('', 'end', values=item)

if __name__ == '__main__':
    root = tk.Tk()

    app = Application(master=root)
    app.mainloop()