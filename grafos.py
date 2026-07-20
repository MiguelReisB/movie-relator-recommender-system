import networkx as nx
import matplotlib.pyplot as plt

def adicionar_ao_grafo(grafo, filmes):
    for i in range(len(filmes)):
        if filmes[i]["nome"] not in grafo:
            grafo.add_node(filmes[i]["nome"])    
    # aqui tem que adicionar os filmes como nós do grafo, se eles ainda não estiverem no grafo
def relacionar_genero(grafo, filmes):
    adicionar_ao_grafo(grafo, filmes)
    for i in range(len(filmes)):
        for j in range(i + 1, len(filmes)):
            if filmes[i]["genero"] == filmes[j]["genero"]:
                grafo.add_edge(filmes[i]["nome"], filmes[j]["nome"])
    # aqui tem que adicionar as relações entre os filmes com o mesmo gênero como arestas do grafo                   
def relacionar_atores(grafo, filmes):
    adicionar_ao_grafo(grafo, filmes)
    for i in range(len(filmes)):
        for j in range(i + 1, len(filmes)):
            atores_i = set(filmes[i]["atores_principais"])
            atores_j = set(filmes[j]["atores_principais"])
            if atores_i.intersection(atores_j):
                grafo.add_edge(filmes[i]["nome"], filmes[j]["nome"])
    # aqui tem que adicionar as relações entre os filmes com atores principais em comum como arestas do grafo
def relacionar_duracao(grafo, filmes):
    adicionar_ao_grafo(grafo, filmes)
    for i in range(len(filmes)):
        for j in range(i + 1, len(filmes)):
            if abs(filmes[i]["duracao"] - filmes[j]["duracao"]) <= 30:
                grafo.add_edge(filmes[i]["nome"], filmes[j]["nome"])
    # aqui tem que adicionar as relações entre os filmes com duração semelhante como arestas do grafo
def mostrar_grafo(grafo):
    fig, ax = plt.subplots(figsize=(10.1, 7.3))

    rotulos = {filme: str(i + 1) for i, filme in enumerate(grafo.nodes())}
# cria um dicionário de rótulos para os nós do grafo, onde a chave é o nome do filme e o valor é um número sequencial começando de 1
    legenda = "\n".join([f"{i + 1}: {filme}" for i, filme in enumerate(grafo.nodes())])
    ax.text(
        -0.18,
        1.02,
        legenda,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment='top',
        horizontalalignment='left',
        bbox=dict(
            facecolor='white',
            edgecolor='black',
            boxstyle='round,pad=0.5'
        ),
        zorder=10,
    )
    # aqui cria uma legenda com os nomes dos filmes e seus respectivos números fora do gráfico, no canto superior esquerdo
    fig.subplots_adjust(left=0.28)

    pos = nx.spring_layout(grafo, k=10, seed=11)

    nx.draw_networkx_nodes(
        grafo,
        pos,
        node_color='lightgray',
        node_size=1700,
        ax=ax
    )
# aqui desenha os nós do grafo com cor cinza claro e tamanho 1700, usando o layout de mola para posicionamento

    nx.draw_networkx_edges(
        grafo,
        pos,
        width=2,
        ax=ax
    )

# aqui desenha as arestas do grafo com largura 2, usando o mesmo layout de mola para posicionamento
    nx.draw_networkx_labels(
        grafo,
        pos,
        labels=rotulos,
        font_size=12,
        font_weight='bold',
        ax=ax
    )
# aqui desenha os rótulos dos nós do grafo com tamanho de fonte 12 e peso de fonte em negrito, usando o mesmo layout de mola para posicionamento
    ax.axis('off')
    ax.set_title("Relação entre os Filmes", fontsize=14, pad=15)
    plt.show()
    # aqui desliga os eixos do gráfico, adiciona um título ao gráfico e exibe o gráfico
