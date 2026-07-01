import networkx as nx
import matplotlib.pyplot as plt
import interface

filmes = [
    {
        "nome": "A Origem",
        "genero": "Ficção Científica",
        "atores_principais": ["Leonardo DiCaprio", "Tom Hardy", "Cillian Murphy"],
        "duracao":148
    },

    {
        "nome": "Batman Begins",
        "genero": "Ação",
        "atores_principais": ["Christian Bale", "Cillian Murphy", "Liam Neeson"],
        "duracao":140
    },
    {
        "nome": "Batman: O Cavaleiro das Trevas Ressurge",
        "genero": "Ação",
        "atores_principais": ["Christian Bale", "Tom Hardy", "Anne Hathaway"],
        "duracao":165
    },
    {
        "nome": "Interestelar",
        "genero": "Ficção Científica",
        "atores_principais": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "duracao":169
    },
    {
        "nome": "Oppenheimer",
        "genero": "Drama",
        "atores_principais": ["Cillian Murphy", "Robert Downey Jr.", "Matt Damon"],
        "duracao":180
    }
]

if __name__ == "__main__":
    interface.criar_interface(filmes)
