import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def get_average_degree(G):
    return (nx.number_of_edges(G)*2)/nx.number_of_nodes(G)

def show_abolute_frequency(G):
    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    x_axis = [i for i in range(max_degree)]
    plt.scatter(x_axis, degree_list)
    plt.show()

def show_distribution(G):
    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    N = nx.number_of_nodes(G)
    x_axis = [i for i in range(max_degree)]
    y_axis = [j/N for j in degree_list]
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(0.01,max_degree)
    plt.ylim(0.0001,0.5)
    plt.scatter(x_axis, y_axis)
    plt.show()


if __name__ == '__main__':
    import graph_parser as gparser
    G = gparser.char_colab_graph()
    show_distribution(G)
    