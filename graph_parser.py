import matplotlib.pyplot as plt
import networkx as nx

def char_book_graph():
    G = nx.Graph()

    f = open("marvel_collaborations_dataset.txt", "r")

    lines = f.readlines()[1:]
    f.close()
    book_app = [ line.split() for line in lines ]
    
    for book in book_app:
        print(book[0])
        for chara in book[1:]:
            G.add_edge(book[0], chara)
    return G

def char_colab_graph():
    G = nx.Graph()

    f = open("marvel_collaborations_dataset.txt", "r")

    lines = f.readlines()[1:]
    f.close()
    marvel_appear = [ line.split() for line in lines ]

    dic_book_colabs = {}

    for char_books in marvel_appear:
        char = char_books[0]
        for book in char_books[1:]:
            if book in dic_book_colabs:
                dic_book_colabs[book] += [int(char)]
            else:
                dic_book_colabs[book] = [int(char)]

    for book in dic_book_colabs:
        char_colabs = dic_book_colabs[book]
        if len(char_colabs) == 1:
            G.add_node(char_colabs[0])
            continue
        for i in range(len(char_colabs)):
            for j in range(i+1, len(char_colabs)):
                G.add_edge(char_colabs[i], char_colabs[j])

    return G


if __name__ == '__main__':
    char_colab_graph()
