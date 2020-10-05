import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

f = open("marvel_collaborations_dataset.txt", "r")

lines = f.readlines()[1:]

book_app = [ line.split() for line in lines ]

for book in book_app:
    print(book[0])
    for chara in book[1:]:
        G.add_edge(book[0], chara)

nx.draw(G)
plt.show()