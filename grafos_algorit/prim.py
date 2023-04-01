import networkx as nx
import matplotlib.pyplot as plt
""" árbol de expansión mínima de un grafo no dirigido y conexo utilizando el algoritmo de Prim.
1.Inicializar el conjunto de nodos visitados y el conjunto de nodos no visitados.
2.Seleccionar un nodo inicial de forma arbitraria y añadirlo al conjunto de nodos visitados.
3.Mientras haya nodos sin visitar:
    a. Calcular el costo mínimo de las aristas que conectan los nodos visitados y no visitados.
    b. Añadir el nodo no visitado con el costo mínimo al conjunto de nodos visitados y añadir la arista correspondiente al árbol de expansión mínima.
4. Devolver el árbol de expansión mínima."""
def prim(graph):
    visited = set()
    unvisited = set(graph.keys())
    start = next(iter(unvisited)) # elegimos un nodo aleatorio como nodo inicial
    visited.add(start)
    unvisited.remove(start)
    tree = {}

    while unvisited:
        min_cost = float('inf')
        min_edge = None
        for visited_node in visited:
            for neighbor, cost in graph[visited_node]['neighbors'].items():
                if neighbor in unvisited and cost < min_cost:
                    min_cost = cost
                    min_edge = (visited_node, neighbor)
        if min_edge:
            tree[min_edge] = min_cost
            visited.add(min_edge[1])
            unvisited.remove(min_edge[1])

    return tree

if __name__ == '__main__':
    graph = {
        'bogota': {'neighbors': {'villavicencio': 110.4, 'chiquinquira': 144.4, 'tunja':151.5, 'honda':161.7, 'girardot':138.1, 'medellin': 511.8}, 'parent': None},
        'honda': {'neighbors': {'bogota': 161.7, 'girardot': 136,'ibage':146,'manisalez': 137,'medellin': 370,'chiquinquira': 284}, 'parent': None},
        'girardot': {'neighbors': {'bogota': 138.1, 'honda':136, 'ibage':68.4}, 'parent': None},
        'ibage': {'neighbors': {'armenia': 80.6, 'manisalez': 173,'barrancabermeja':429, 'honda': 146, 'girardot':68.4}, 'parent': None},
        'armenia': {'neighbors': {'pereira':  45.4, 'ibage': 80.6,'tulua':87.2}, 'parent': None},
        'pereira': {'neighbors': {'armenia': 45.4, 'medellin': 214, 'manisalez': 53.3}, 'parent': None},
        'manisalez': {'neighbors': {'pereira': 53.3, 'ibage': 173, 'honda':137,'bucaramanga':427}, 'parent': None},
        'medellin': {'neighbors': {'barrancabermeja': 300, 'honda': 370,'chiquinquira':391, 'manisalez': 197, 'pereira':214, 'bogota': 511.8}, 'parent': None},
        'villavicencio': {'neighbors': {'bogota': 110.4, 'tunja': 258.3, 'sogamoso':349.3}, 'parent': None},
        'tunja': {'neighbors': {'duitama':54.3, 'villavicencio': 258.3, 'bogota':151.5,'socorro':162,'chiquinquira':77.2 }, 'parent': None},
        'chiquinquira': {'neighbors': {'bogota': 144.4, 'tunja': 77.2, 'honda': 284,'medellin':391,'barrancabermeja':267,'socorro':142 }, 'parent': None},
        'duitama': {'neighbors': {'sogamoso': 20, 'pamplona': 303, 'tunja':54.3}, 'parent': None},
        'sogamoso': {'neighbors': {'duitama': 20, 'villavicencio': 349.3}, 'parent': None},
        'socorro': {'neighbors': {'chiquinquira':142 , 'tunja':162 ,'bucaramanga':120}, 'parent': None},
        'bucaramanga': {'neighbors': {'cucuta': 196,'pamplona': 125,'socorro': 120,'barrancabermeja': 115}, 'parent': None},
        'barrancabermeja': {'neighbors': {'cucuta': 436, 'bucaramanga': 115,'chiquinquira': 267,'ibage': 429, 'manisalez':427,'medellin':300}, 'parent': None},
        'pamplona': {'neighbors': {'duitama': 303, 'bucaramanga': 125}, 'parent': None},
        'cucuta': {'neighbors': {'barrancabermeja': 436, 'bucaramanga': 196}, 'parent': None},
        'tulua': {'neighbors': {'cali': 94.2, 'armenia': 87.2}, 'parent': None},
        'cali': {'neighbors': {'tulua': 94.2}, 'parent': None}
    }
    arbol = prim(graph)
    nodes=[]
    for ciudades in arbol:
        nodes.append(ciudades[0])
        nodes.append(ciudades[1])
    nodes=list(set(nodes))

    edges= [(start, end, {'weight': weight}) for (start, end), weight in arbol.items()]
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    # Dibujamos el grafo con las aristas y los pesos de las aristas
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=1)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Mostramos el grafo
    plt.axis('off')
    plt.show()
