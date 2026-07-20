import tkinter as tk
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
    # funções para gerar as matrizes e os grafos, chamando as funções do arquivo matriz.py e grafos.py, respectivamente
def criar_interface(filmes):
    janela = tk.Tk()
    janela.title("Sistema de recomendação de Filmes")
    janela.geometry("500x420")
    janela.config(bg="#1e1e2f")

    titulo = tk.Label(
        janela,
        text="Sistema de recomendação de Filmes",
        font=("Arial", 16),
        bg="#1e1e2f",
        fg="white"
        )
    titulo.pack(pady=15)

    frame_botoes = tk.Frame(
        janela,
        bg="#303058",
        width=300,
        height=200
        )
    frame_botoes.pack(pady=10)
    frame_botoes.pack_propagate(False)

    espaco_topo = tk.Frame(
        frame_botoes,
        height=30,
        bg="#303058"
        )
    espaco_topo.pack()
    
    btn1 = tk.Button(
        frame_botoes,
        text="Relação Geral",
        width=30,
        command=lambda: geral(filmes),
        bg="#4a90e2",
        fg="white",
        bd=0
        )
    btn1.pack(pady=6)

    btn2 = tk.Button(
        frame_botoes,
        text="Por Gênero",
        width=30,
        command=lambda: genero(filmes),
        bg="#4a90e2",
        fg="white",
        bd=0
        )
    btn2.pack(pady=6)

    btn3 = tk.Button(
        frame_botoes,
        text="Por Atores",
        width=30,
        command=lambda: atores(filmes),
        bg="#4a90e2",
        fg="white",
        bd=0
        )
    btn3.pack(pady=6)

    btn4 = tk.Button(
        frame_botoes,
        text="Por Duração",
        width=30,
        command=lambda: duracao(filmes),
        bg="#4a90e2",
        fg="white",
        bd=0
        )
    btn4.pack(pady=6)

    espaco_baixo = tk.Frame(
        frame_botoes,
        height=20,
        bg="#303058"
        )
    espaco_baixo.pack(side="bottom")


    btn_sair = tk.Button(
        janela,
        text="Sair",
        width=10,
        command=janela.quit,
        bg="#e74c3c",
        fg="white",
        bd=0
        )
    btn_sair.pack(pady=30)

    janela.mainloop()
# aqui cria a interface gráfica com os botões para cada tipo de relação, chamando as funções correspondentes ao clicar nos botões, e um botão para sair do programa
