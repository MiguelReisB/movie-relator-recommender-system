import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

import grafos
import matriz

def geral(filmes):
    matriz.draw_matrix(filmes, matriz.matriz_geral_direta(filmes))
    grafo = nx.Graph()
    grafos.relacionar_genero(grafo, filmes)
    grafos.relacionar_atores(grafo, filmes)
    grafos.relacionar_duracao(grafo, filmes)
    grafos.mostrar_grafo(grafo)
    grafos.clear()

def genero(filmes):
    matriz.draw_matrix(filmes, matriz.matrix_genero(filmes))
    grafo = nx.Graph()
    grafos.relacionar_genero(grafo, filmes)
    grafos.mostrar_grafo(grafo)
    grafos.clear()

def atores(filmes):
    matriz.draw_matrix(filmes, matriz.matrix_atores(filmes))
    grafo = nx.Graph()
    grafos.relacionar_atores(grafo, filmes)
    grafos.mostrar_grafo(grafo)
    grafos.clear()
    
def duracao(filmes):
    matriz.draw_matrix(filmes, matriz.matrix_duracao(filmes))
    grafo = nx.Graph()
    grafos.relacionar_duracao(grafo, filmes)
    grafos.mostrar_grafo(grafo)
    grafos.clear()
    matriz.matrix_duracao(filmes)
    
# Interface
def criar_interface(filmes):
    janela = tk.Tk()
    janela.title("Sistema de Filmes")
    janela.geometry("400x300")

    titulo = tk.Label(janela, text="Sistema de Relação de Filmes", font=("Arial", 14))
    titulo.pack(pady=10)

    btn1 = tk.Button(janela, text="Relação Geral", width=25, command=lambda: geral(filmes))
    btn1.pack(pady=5)

    btn2 = tk.Button(janela, text="Por Gênero", width=25, command=lambda: genero(filmes))
    btn2.pack(pady=5)

    btn3 = tk.Button(janela, text="Por Atores", width=25, command=lambda: atores(filmes))
    btn3.pack(pady=5)

    btn4 = tk.Button(janela, text="Por Duração", width=25, command=lambda: duracao(filmes))
    btn4.pack(pady=5)

    btn_sair = tk.Button(janela, text="Sair", width=25, command=janela.quit)
    btn_sair.pack(pady=10)

    janela.mainloop()