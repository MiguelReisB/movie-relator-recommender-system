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
    plt.figure(figsize=(10.1, 7.3))

    rotulos = {filme: str(i + 1) for i, filme in enumerate(grafo.nodes())}

    legenda = "\n".join([f"{i + 1}: {filme}" for i, filme in enumerate(grafo.nodes())])
    plt.text(
        0.02,
        0.98,
        legenda,
        transform=plt.gca().transAxes,
        fontsize=8,
        verticalalignment='top',
        horizontalalignment='left',
        bbox=dict(
            facecolor='white',
            edgecolor='black',
            boxstyle='round,pad=0.5'
            )
    ) 
    
    pos = nx.spring_layout(grafo, k=10, seed=11)

    nx.draw_networkx_nodes(
        grafo, 
        pos,
        node_color='lightgray',
        node_size=1700
    )


    nx.draw_networkx_edges(
        grafo, 
        pos,
        width=2
    )


    nx.draw_networkx_labels(
        grafo, 
        pos,
        labels=rotulos,
        font_size=6,
        font_weight='bold'
    )

    plt.axis('off')
    plt.title("Relação entre os Filmes", fontsize=14, pad=15)
    plt.show()
