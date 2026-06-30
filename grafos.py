import networkx as nx
import matplotlib.pyplot as plt

def adicionar_ao_grafo(grafo, filmes):
    for i in range(len(filmes)):
        if filmes[i]["nome"] not in grafo:
            grafo.add_node(filmes[i]["nome"])    
    
def relacionar_genero(grafo, filmes):
    adicionar_ao_grafo(grafo, filmes)
    for i in range(len(filmes)):
        for j in range(i + 1, len(filmes)):
            if filmes[i]["genero"] == filmes[j]["genero"]:
                grafo.add_edge(filmes[i]["nome"], filmes[j]["nome"])
                       
def relacionar_atores(grafo, filmes):
    adicionar_ao_grafo(grafo, filmes)
    for i in range(len(filmes)):
        for j in range(i + 1, len(filmes)):
            atores_i = set(filmes[i]["atores_principais"])
            atores_j = set(filmes[j]["atores_principais"])
            if atores_i.intersection(atores_j):
                grafo.add_edge(filmes[i]["nome"], filmes[j]["nome"])
    
def relacionar_duracao(grafo, filmes):
    adicionar_ao_grafo(grafo, filmes)
    for i in range(len(filmes)):
        for j in range(i + 1, len(filmes)):
            if abs(filmes[i]["duracao"] - filmes[j]["duracao"]) <= 30:
                grafo.add_edge(filmes[i]["nome"], filmes[j]["nome"])

def mostrar_grafo(grafo):
    plt.figure(figsize=(13, 8))
    
    pos = nx.spring_layout(grafo, k=1.0, seed=42)

    
    nx.draw_networkx_nodes(
        grafo, pos,
        node_color='lightgray',
        node_size=2100
    )

    nx.draw_networkx_edges(
        grafo, pos,
        width=2
    )

    nx.draw_networkx_labels(
        grafo, pos,
        font_size=9,
        font_weight='bold'
    )

    plt.axis('off')
    plt.show()