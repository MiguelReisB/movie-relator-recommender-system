import networkx as nx
import matplotlib.pyplot as plt
import interface

filmes = [
    {
        "nome": "Following",
        "genero": "Thriller",
        "atores_principais": ["Jeremy Theobald", "John Nolan", "Lucy Thackeray"],
        "duracao":69
    },
    {
        "nome": "Memento",
        "genero": "Thriller",
        "atores_principais": ["Guy Pearce", "Carrie-Anne Moss", "Joe Pantoliano"],
        "duracao":113
    },
    {
        "nome": "Insônia",
        "genero": "Thriller",
        "atores_principais": ["Al Pacino", "Robin Williams", "Hilary Swank"],
        "duracao":118
    },
    {
        "nome": "Batman Begins",
        "genero": "Ação",
        "atores_principais": ["Christian Bale", "Cillian Murphy", "Liam Neeson"],
        "duracao":140
    },
    {
        "nome": "O Grande Truque",
        "genero": "Thriller",
        "atores_principais": ["Christian Bale", "Hugh Jackman", "Scarlett Johansson"],
        "duracao":130
    },
    {
        "nome": "Batman: O Cavaleiro das Trevas",
        "genero": "Ação",
        "atores_principais": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "duracao":152
    },
    {
        "nome": "A Origem",
        "genero": "Ficção Científica",
        "atores_principais": ["Leonardo DiCaprio", "Tom Hardy", "Cillian Murphy"],
        "duracao":148
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
        "nome": "Dunkirk",
        "genero": "Guerra",
        "atores_principais": ["Tom Hardy", "Cillian Murphy", "Kenneth Branagh"],
        "duracao":106
    },
    {
        "nome": "Tenet",
        "genero": "Ficção Científica",
        "atores_principais": ["John David Washington", "Robert Pattinson", "Elizabeth Debicki"],
        "duracao":150
    },
    {
        "nome": "Oppenheimer",
        "genero": "Drama",
        "atores_principais": ["Cillian Murphy", "Robert Downey Jr.", "Matt Damon"],
        "duracao":180
    },
    {
        "nome": "A Odisseia",
        "genero": "Fantasia",
        "atores_principais": ["Matt Damon", "Tom Holland", "Anne Hathaway"],
        "duracao":173
    }
]

if __name__ == "__main__":
    interface.criar_interface(filmes)
