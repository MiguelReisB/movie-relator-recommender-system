<h1 align="center">🎬 Sistema de Recomendação de Filmes</h1> 
 
Projeto acadêmico desenvolvido para a disciplina de **Matemática Computacional Aplicada**, com o objetivo de demonstrar a aplicabilidade prática de estruturas matemáticas discretas na construção de um sistema de recomendação de filmes.
 
---
 
## 📋 Sobre o projeto
 
O sistema modela as relações entre filmes a partir de três critérios:
 
- **Gênero** — filmes do mesmo gênero são considerados relacionados;
- **Elenco** — filmes com atores em comum são conectados;
- **Duração** — filmes com diferença de até 30 minutos são agrupados.
<p>Essas relações são representadas por meio de <b>grafos</b> e <b>matrizes de adjacência</b>, e a consistência lógica do modelo é verificada com <b>Lógica Booleana</b> <br>(expressão `R = G ∨ A ∨ D`). O sistema também gera uma visualização ponderada geral, indicando o grau de similaridade entre cada par de filmes com base na quantidade de critérios em comum.</p>
 
---
 
## 🛠️ Tecnologias utilizadas
 
- [Python 3](https://www.python.org/);
- [NetworkX](https://networkx.org/) — criação e manipulação dos grafos;
- [Matplotlib](https://matplotlib.org/) — visualização dos grafos e matrizes;
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — interface gráfica.
