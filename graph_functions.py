import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def get_average_degree(G):
    return (nx.number_of_edges(G)*2)/nx.number_of_nodes(G)

def show_abolute_frequency(G):
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
    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    N = nx.number_of_nodes(G)
    x_axis = [i for i in range(max_degree)]
    y_axis = [j/N for j in degree_list]
        
    plt.scatter(x_axis, y_axis, s=1.5)
    plt.show()

def show_log_scale_dist(G):
    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    N = nx.number_of_nodes(G)
    x = [np.log10(i) for i in range(max_degree)]
    y = [np.log10(j/N) for j in degree_list]
    plt.scatter(x,y, s=1)
    plt.show()

def show_power_law(G):
    degree_list = nx.degree_histogram(G)
    max_degree = len(degree_list)
    N = nx.number_of_nodes(G)

    x = [i for i in range(max_degree)]
    y = [j/N for j in degree_list]
    
    popt, pcov = curve_fit(power_law, x[2:], y[2:])

    plt.scatter(x, y)
    plt.plot(x, power_law(x, *popt), 'r')
    
    plt.xscale('log')
    plt.yscale('log')
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


#TODO 
def get_betweeness_centrality(G):
    return 0

if __name__ == '__main__':
    import graph_parser as gparser
    G = gparser.char_colab_graph()
    #print("Average Degree: " + get_average_degree(G))
    largest_component = get_largest_component(G)
    print("Average Path Length: " + str(nx.average_shortest_path_length(largest_component)))
    print("Diameter: " + str(nx.diameter(largest_component)))
    