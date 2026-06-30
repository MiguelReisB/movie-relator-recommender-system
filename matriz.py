import matplotlib.pyplot as plt
def create_matrix(filmes):
    matrix = [[0 for _ in filmes] for _ in filmes]
    return matrix

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

def matrix_duracao(filmes):
    matrix = create_matrix(filmes)
    for i in range(len(filmes)):
        for j in range(i + 1, len(filmes)):
            if abs(filmes[i]["duracao"] - filmes[j]["duracao"]) <= 30:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix

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

def draw_matrix(filmes1, matrix):

    filmes = [filme["nome"] for filme in filmes1]
    
    # Matriz simétrica baseada na regra dos 30 minutos
    matriz = matrix

    # 2. Criando o Quadro da Matriz
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Matriz de Adjacência dos Filmes", fontsize=14, pad=15)

    # Desenhando a matriz (cmap='Blues' para tons de azul)
    cax = ax.imshow(matriz, cmap='Blues', interpolation='none')

    # 3. Configurando os nomes nos eixos X e Y
    ax.set_xticks(range(len(filmes)))
    ax.set_yticks(range(len(filmes)))
    ax.set_xticklabels(filmes, rotation=45, ha="right", fontsize=10)
    ax.set_yticklabels(filmes, fontsize=10)

    # 4. Escrevendo os números (0 e 1) dentro de cada quadradinho
    for i in range(len(filmes)):
        for j in range(len(filmes)):
            # Pinta de branco se for 1 (fundo escuro) e de preto se for 0 (fundo claro)
            cor = "white" if matriz[i][j] == 1 else "black"
            ax.text(j, i, str(matriz[i][j]), ha="center", va="center", color=cor, fontweight='bold')

    # Ajusta o layout para não cortar os nomes e exibe
    plt.tight_layout()
    plt.show()