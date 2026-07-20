import matplotlib.pyplot as plt
def create_matrix(filmes):
    matrix = [[0 for _ in filmes] for _ in filmes]
    return matrix
    # faz uma matriz quadrada de zeros com o tamanho da lista de filmes, para ser usada nas funções abaixo

def matrix_genero(filmes):
    matrix = create_matrix(filmes)
    for i in range(len(filmes)):
        for j in range(i+1,len(filmes)):
            if filmes[i]["genero"] == filmes[j]["genero"]:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix # tem que retornar uma matrix com as relações entre os gêneros

def matrix_atores(filmes):
    matrix = create_matrix(filmes)
    for i in range(len(filmes)):
        for j in range(i + 1, len(filmes)):
            atores_i = set(filmes[i]["atores_principais"])
            atores_j = set(filmes[j]["atores_principais"])
            if atores_i.intersection(atores_j):
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix
# tem que retornar uma matrix com as relações entre os atores principais
def matrix_duracao(filmes):
    matrix = create_matrix(filmes)
    for i in range(len(filmes)):
        for j in range(i + 1, len(filmes)):
            if abs(filmes[i]["duracao"] - filmes[j]["duracao"]) <= 30:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix
# tem que retornar uma matrix com as relações entre a duração dos filmes
def matriz_geral_direta(filmes):
    n = len(filmes)
    matriz = [[0 for _ in filmes] for _ in filmes]

    for i in range(n):
        for j in range(i+1,n):

            atores_i = set(filmes[i]["atores_principais"])
            atores_j = set(filmes[j]["atores_principais"])
            peso = 0

            if filmes[i]["genero"] == filmes[j]["genero"]:
                peso += 1

            if atores_i.intersection(atores_j):
                peso += 1

            if abs(filmes[i]["duracao"] - filmes[j]["duracao"]) <= 30:
                peso += 1

            matriz[i][j] = peso
            matriz[j][i] = peso

    return matriz
# aqui tem que retornar uma matriz com as relações entre os filmes, considerando gênero, atores e duração
def draw_matrix(filmes1, matrix):

    filmes = [filme["nome"] for filme in filmes1]
    
    # Matriz simétrica baseada na regra dos 30 minutos
    matriz = matrix

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Matriz de Adjacência dos Filmes", fontsize=17, pad=18)
# aqui cria a figura e o eixo do gráfico, define o título e o tamanho da fonte
    
    cax = ax.imshow(matriz, cmap='Blues', interpolation='none')
# desenhando a matriz (cmap='Blues' para tons de azul)
    
    ax.set_xticks(range(len(filmes)))
    ax.set_yticks(range(len(filmes)))
    ax.set_xticklabels(filmes, rotation=45, ha="right", fontsize=12)
    ax.set_yticklabels(filmes, fontsize=12)
# configurando os ticks e labels dos eixos x e y, com rotação de 45 graus para os nomes dos filmes no eixo x, alinhamento à direita e tamanho de fonte 15, e tamanho de fonte 10 para o eixo y
    
    for i in range(len(filmes)):
        for j in range(len(filmes)):
            # Pinta de branco se for 1 (fundo escuro) e de preto se for 0 (fundo claro)
            cor = "white" if matriz[i][j] == 1 else "black"
            ax.text(j, i, str(matriz[i][j]), ha="center", va="center", color=cor, fontsize=12, fontweight='bold')
# adicionando os valores da matriz como texto dentro de cada célula, centralizados, com cor branca para 1 e preta para 0, e peso de fonte em negrito
    
    plt.tight_layout()
    plt.show()
    # Ajusta o layout para não cortar os nomes e exibe
