
# usando algoritmo a* hallar el camino mas corto entre dos nodos en un multigrafo de 20 nodos
import heapq


def a_star(start_node, goal_node, graph, posicion):
    # Inicializar listas abierta y cerrada
    open_list = []
    closed_list = set()

    # Inicializar costos G y H de cada nodo
    g_costs = {node: float('inf') for node in graph}
    h_costs = {node: heuristic(node, goal_node, posicion) for node in graph}
    g_costs[start_node] = 0

    # Agregar nodo inicial a lista abierta
    heapq.heappush(
        open_list, (g_costs[start_node] + h_costs[start_node], start_node))

    while open_list:
        # Seleccionar nodo con menor costo total estimado
        current_node = heapq.heappop(open_list)[1]

        # Si se alcanza el nodo objetivo, devolver la ruta
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = graph[current_node]['parent']
            path.append(start_node)
            return path[::-1]#, g_costs[goal_node]

        # Agregar nodo actual a lista cerrada
        closed_list.add(current_node)

        # Explorar nodos vecinos
        for neighbor, cost in graph[current_node]['neighbors'].items():
            if neighbor in closed_list:
                continue

            tentative_g_cost = g_costs[current_node] + cost
            if tentative_g_cost < g_costs[neighbor]:
                # Actualizar costos G y H del vecino
                g_costs[neighbor] = tentative_g_cost
                h_costs[neighbor] = heuristic(neighbor, goal_node, posicion)
                graph[neighbor]['parent'] = current_node

                # Agregar vecino a lista abierta
                heapq.heappush(
                    open_list, (g_costs[neighbor] + h_costs[neighbor], neighbor))

    # No se encontró una ruta, devolver None
    return None


def heuristic(node1, node2, posicion):  # estimar la distancia desde node1 hasta node2
    # distancia euclidiana entre nodos
    return ((posicion[node1]['x']-posicion[node2]['x'])**2 + (posicion[node1]['y']-posicion[node2]['y'])**2)**0.5


if __name__ == '__main__':
    # Ejemplo de uso
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
    posicion = {
        'bogota': {'x': -74.07712164430839, 'y': 4.71680699877015},
        'honda': {'x': -73.35826317154614, 'y': 5.544321975003336},
        'girardot': {'x': -74.7958661049945, 'y': 4.302467009809488},
        'ibage': {'x': -75.2187342985274, 'y': 4.436544192225768},
        'armenia': {'x': -75.67792974170058, 'y': 4.536753809271931},
        'pereira': {'x': -75.71543466177089, 'y': 4.808753007545216},
        'manisalez': {'x': -75.49926502755311, 'y': 5.0642504941713655},
        'medellin': {'x': -75.57415231646641, 'y': 6.248510832573867},
        'villavicencio': {'x': -73.63011975960507, 'y': 4.142392322596742},
        'tunja': {'x': -73.35742472062627, 'y': 5.546417295764618},
        'chiquinquira': {'x': -73.81909544117212, 'y': 5.615380197634371},
        'duitama': {'x': -73.03273352921018, 'y': 5.818867673301295},
        'sogamoso': {'x': -72.93415412259586, 'y': 5.7330073415246225},
        'socorro': {'x': -73.26149010368579, 'y': 6.466968543443632},
        'bucaramanga': {'x': -73.1210824454418, 'y': 7.114418231090902},
        'barrancabermeja': {'x': -73.85381991118179, 'y': 7.065605455029154},
        'pamplona': {'x': -72.64737546901327, 'y': 7.376320370129446},
        'cucuta': {'x': -72.50413531753063, 'y': 7.896783318632543},
        'tulua': {'x': -76.19577077601726, 'y': 4.0907450610592395},
        'cali': {'x': -76.52367405741018, 'y': 3.428418853721823}
    }
    start_node = 'bogota'
    goal_node = 'barrancabermeja'
    print('La mejor ruta es: ',a_star(start_node, goal_node, graph, posicion))