import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import graph_parser as gparser
from scipy.optimize import curve_fit


def get_average_degree(G):
    return (nx.number_of_edges(G)*2)/nx.number_of_nodes(G)

def show_abolute_frequency(G):

    """
    Shows a chart with the corresponding absolute frequency of each character appearence in a book
    """

    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    x_axis = [i for i in range(max_degree)]
    plt.scatter(x_axis, degree_list)
    plt.show()

def power_law(x, C, a):
    return C * x ** (-a)

def linear_funct(x, lN, a):
    return a * x + lN

def show_linear_scale_dist(G):

    """
    Shows a chart with the degrees of a node and its probability
    """

    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    N = nx.number_of_nodes(G)
    y_aux = [j/N for j in degree_list]

    x_axis = list(filter(lambda i: y_aux[i] != 0, range(max_degree)))
    y_axis = list(filter(lambda y: y!=0, y_aux))

    plt.xlabel('Degree (k)')
    plt.ylabel('Probability of a Node with Degree k (Pk)')
    plt.scatter(x_axis,y_axis, s=1)
    plt.show()

def show_log_scale_dist(G):

    """
    Shows a chart with the degrees of a node and its probability in a log-scale
    """

    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    N = nx.number_of_nodes(G)
    x = [np.log10(i) for i in range(max_degree)]
    y = [np.log10(j/N) for j in degree_list]
    plt.xlabel('Degree (k)')
    plt.ylabel('Probability of a Node having degree k (Pk)')
    plt.scatter(x,y, s=1)
    plt.show()

def show_power_law(G):

    """Shows a chart with the degrees of a node and its probability plus its power law"""

    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    N = nx.number_of_nodes(G)

    y_aux = [j/N for j in degree_list]

    x = list(filter(lambda i: y_aux[i] != 0, range(max_degree)))
    y = list(filter(lambda y: y!=0, y_aux))

    popt, pcov = curve_fit(power_law, x[1:], y[1:])

    plt.xlabel('Degree (k)')
    plt.ylabel('Probability of a Node with Degree k (Pk)')
    plt.ylim((0, 0.045))
    plt.scatter(x, y, s=1)
    plt.plot(x[1:], power_law(x[1:], *popt), 'r')

    plt.show()
    print('Power law: Pk= '+ str(popt[0])+' * k** -'+ str(popt[1]))

def get_local_clustering(G, n):
    node_neighbors = list(nx.neighbors(G, n))
    Li = 0
    ki = len(node_neighbors)
    if ki <= 1:
        print('Impossible to calculate clustering. Node has too few neighbors.')
        return 0
    for nd in node_neighbors:
        for i in nx.neighbors(G, nd):
            if i in node_neighbors:
                Li += 1
    return Li / (ki * (ki-1))

def get_average_clustering(G):
    sum = 0
    N = nx.number_of_nodes(G)
    print(G.nodes())
    for n in G.nodes():
        print(n)
        sum += get_local_clustering(G,n)
    return sum/N

def get_largest_component(G):
    largest_cc =  max(nx.connected_components(G), key=len)
    print("Size of the largest connected component: " + str(len(largest_cc)))
    return G.subgraph(largest_cc).copy()

def get_degree_centrality(G):
    return nx.degree_centrality(G)

def get_closeness_centrality(G):
    return nx.closeness_centrality(G)

def get_betweenness_centrality(G):
    return nx.betweenness_centrality(G)


######## Auxiliar functions ###############

def print_names(n_name_dic, nodes):
    for node in nodes:
        print(n_name_dic[node])

def get_3_best_nodes(dic_node_cent):
    best3 = {}

    for i in range(3):
        max_c = 0
        max_n = 0
        for node in dic_node_cent:
            if dic_node_cent[node] > max_c and node not in best3.keys():
                max_c = dic_node_cent[node]
                max_n = node
        best3[max_n] = max_c

    return best3

###########################################

if __name__ == '__main__':
    G = gparser.char_colab_graph()

