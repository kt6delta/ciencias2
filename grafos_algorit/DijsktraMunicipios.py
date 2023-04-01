# !/usr/bin/python3
# Dijkstra Algorithm
# Author: Jhonatan Moreno - Laura Preciado
from operator import ne


class Node:
    # Nodo
    def __init__(self, name):
        self.id = name
        self.neighbors = []
        self.isVisited = False
        self.father = None
        self.distance = float('inf')

    def add_neighbor(self, neighbor, distance):
        if neighbor not in self.neighbors:
            self.neighbors.append([neighbor, distance])


class Graphic:
    def __init__(self):
        self.Nodes = {}

    def add_node(self, id):
        if id not in self.Nodes:
            self.Nodes[id] = Node(id)

    def add_edge(self, node_a, node_b, distance):
        if node_a in self.Nodes and node_b in self.Nodes:
            self.Nodes[node_a].add_neighbor(node_b, distance)
            self.Nodes[node_b].add_neighbor(node_a, distance)

            # self.G.add_edge(node_a, node_b, weight=distance)

    def get_path(self, node_b):
        path = []
        actual = node_b
        while actual is not None:
            path.insert(0, actual)
            actual = self.Nodes[actual].father
        return [path, self.Nodes[node_b].distance]

    def min(self, list):
        if len(list) > 0:
            m = self.Nodes[list[0]].distance
            v = list[0]

            for i in list:
                if m > self.Nodes[i].distance:
                    m = self.Nodes[i].distance
                    v = i

            return v

    def dijkstra(self, node_a):
        if node_a in self.Nodes:
            self.Nodes[node_a].distance = 0
            actual = node_a
            unvisited = []

            # Se agregan todos a no visitados
            for v in self.Nodes:
                if v != node_a:
                    self.Nodes[v].distance = float('inf')
                self.Nodes[v].father = None
                unvisited.append(v)

            while len(unvisited) > 0:
                # Se evaluan los vertices vecinos y se toma el menor
                for neighbor in self.Nodes[actual].neighbors:
                    if not self.Nodes[neighbor[0]].isVisited:
                        if self.Nodes[actual].distance + neighbor[1] < self.Nodes[neighbor[0]].distance:
                            self.Nodes[neighbor[0]
                                ].distance = self.Nodes[actual].distance + neighbor[1]
                            self.Nodes[neighbor[0]].father = actual

                self.Nodes[actual].isVisited = True
                unvisited.remove(actual)

                actual = self.min(unvisited)
        else:
            return False


if __name__ == '__main__':

    gr = Graphic()
    ciudades = ['bogota', 'honda', 'girardot', 'ibague', 'armenia', 'pereira', 'manizales', 'medellin', 'villavicencio', 'tunja', 'chiquinquira', 'duitama', 'sogamoso', 'socorro', 'bucaramanga', 'barrancabermeja', 'pamplona', 'cucuta', 'tulua', 'cali']
    for i in ciudades:
        gr.add_node(i)

    # Bogotá
    gr.add_edge('bogota', 'villavicencio', 110.4)  # origen, destino, peso
    gr.add_edge('bogota', 'chiquinquira', 144.4)
    gr.add_edge('bogota', 'tunja', 151.5)
    gr.add_edge('bogota', 'honda', 161.7)
    gr.add_edge('bogota', 'girardot', 138.1)
    gr.add_edge('bogota', 'medellin', 511.8)

    # Honda
    gr.add_edge('honda', 'girardot', 136)
    gr.add_edge('honda', 'ibage', 146)
    gr.add_edge('honda', 'manizales', 137)
    gr.add_edge('honda', 'medellin', 370)
    gr.add_edge('honda', 'chiquinquira', 284)

    # Girardot
    gr.add_edge('girardot', 'ibage', 68.4)

    # Ibague
    gr.add_edge('ibague', 'armenia', 80.6)
    gr.add_edge('ibague', 'manizales', 173)
    gr.add_edge('ibague', 'barrancabermeja', 429)

    # Armenia
    gr.add_edge('armenia', 'pereira',  45.4)
    gr.add_edge('armenia', 'tulua', 87.2)

    # Pereira
    gr.add_edge('pereira', 'armenia', 45.4)
    gr.add_edge('pereira', 'manizales', 53.3)
    gr.add_edge('armenia', 'medellin', 214)

    # Manizales
    gr.add_edge('manizales', 'barramcabermeja', 427)
    gr.add_edge('manizales', 'medellin', 197)


    # Medellín
    gr.add_edge('medellin', 'barrancabermeja', 300)
    gr.add_edge('medellin', 'chiquinquira', 391)


    # Villavicencio
    gr.add_edge('villavicencio', 'tunja', 258.3)
    gr.add_edge('villavicencio', 'sogamoso', 349.3)

    # Tunja
    gr.add_edge('tunja', 'duitama', 54.3)
    gr.add_edge('tunja', 'chiquinquira', 77.2)
    gr.add_edge('tunja', 'socorro', 162)

    # Chiquinquira
    gr.add_edge('chiquinquira', 'socorro', 142)
    gr.add_edge('chiquinquira', 'barrancabermeja', 267)

    # Duitama
    gr.add_edge('duitama', 'sogamoso', 20)
    gr.add_edge('duitama', 'pamplona', 303)

    # Socorro
    gr.add_edge('socorro', 'bucaramanga', 120)

    # Bucaramanga
    gr.add_edge('bucaramanga', 'pamplona', 125)
    gr.add_edge('bucaramanga', 'cucuta', 196)
    gr.add_edge('bucaramanga', 'barrancabermeja', 115)


    # 18
    gr.add_edge('cucuta', 'barrancabermeja', 436)


    # 19
    gr.add_edge('tulua', 'cali', 94.2)

    gr.dijkstra(str(input("[+] Ingrese el nodo de inicio: ")))
    dst = str(input("[+] Ingrese el nodo destino: "))
    print("[!] Solución: ")
    print(gr.get_path(dst))

    # size = int(input("[+] Please, enter the number of vertices in the graph: "))
    # # Start in 0
    # graph = [[0 for j in range(size)] for i in range(size)]
    #
    # for i in range(size):
    #     for j in range(size):
    #         enter = input(f'Enter the element [{i}][{j}]: ')
    #         graph[i][j] = enter
    #
    # print("The graph is: ")
    # for i in range(size):
    #     for j in range(size):
    #         print(graph[i][j], end=" ")
    #     print()