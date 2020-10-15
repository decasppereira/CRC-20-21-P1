import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import plfit

def get_average_degree(G):
    return (nx.number_of_edges(G)*2)/nx.number_of_nodes(G)

def show_abolute_frequency(G):
    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    x_axis = [i for i in range(max_degree)]
    plt.scatter(x_axis, degree_list)
    plt.show()

def power_law(x, a, b, c):
    return (np.exp(-b * x) * a) + c

def show_distribution(G):
    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    N = nx.number_of_nodes(G)
    x_axis = [i for i in range(max_degree)]
    y_axis = [j/N for j in degree_list]
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(0.01,max_degree)
    plt.ylim(0.0001,0.05)
    
    plt.scatter(x_axis, y_axis, s=1.5)
    plt.show()
    

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
    
def get_average_path_length(G):
    return 0

def show_hist_plot(G):
    degree_list = nx.degree_histogram(G)
    ax = sns.distplot(degree_list)
    # plt.xscale('log')
    # plt.yscale('log')
    plt.show()

def show_log_scale_dist(G):
    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    N = nx.number_of_nodes(G)
    x = [i for i in range(max_degree)]
    y = [j/N for j in degree_list]
    z = np.polyfit(x, y, 3)
    plt.show()

if __name__ == '__main__':
    import graph_parser as gparser
    G = gparser.char_colab_graph()
    show_log_scale_dist(G)
    
    