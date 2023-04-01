import heapq
import math


def heuristic(pos1, pos2):
    # Distancia Euclidiana entre posiciones
    x1, y1 = pos1['x'], pos1['y']
    x2, y2 = pos2['x'], pos2['y']
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def a_plus(start, goal, graph, positions):
    open_set = [(0, start)]
    closed_set = set()
    while open_set:
        f, current_node = heapq.heappop(open_set)
        if current_node == goal:
            # Reconstruimos la ruta a través de los padres
            path = [current_node]
            while graph[current_node]['parent']:
                path.append(graph[current_node]['parent'])
                current_node = graph[current_node]['parent']
            path.reverse()
            return path
        closed_set.add(current_node)
        for neighbor in graph[current_node]['neighbors']:
            if neighbor in closed_set:
                continue
            neighbor_g = graph[current_node]['g'] + \
                graph[current_node]['neighbors'][neighbor]
            if neighbor not in [n[1] for n in open_set]:
                # Agregamos el vecino a la lista de nodos abiertos
                graph[neighbor]['parent'] = current_node
                graph[neighbor]['g'] = neighbor_g
                graph[neighbor]['f'] = neighbor_g + \
                    heuristic(positions[neighbor], positions[goal])
                heapq.heappush(open_set, (graph[neighbor]['f'], neighbor))
            else:
                # El vecino ya esta en la lista de nodos abiertos
                # actualizamos sus valores si el nuevo camino es mejor
                for i, node in enumerate(open_set):
                    if neighbor == node[1]:
                        if neighbor_g < graph[neighbor]['g']:
                            graph[neighbor]['parent'] = current_node
                            graph[neighbor]['g'] = neighbor_g
                            graph[neighbor]['f'] = neighbor_g + \
                                heuristic(positions[neighbor], positions[goal])
                            open_set[i] = (graph[neighbor]['f'], neighbor)
                            heapq.heapify(open_set)
                        break
    return None


if __name__ == '__main__':
    graph = {
        'bogota': {'neighbors': {'villavicencio': 110.4, 'chiquinquira': 144.4, 'tunja':151.5, 'honda':161.7, 'girardot':138.1, 'medellin': 511.8}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'honda': {'neighbors': {'bogota': 161.7, 'girardot': 136,'ibage':146,'manisalez': 137,'medellin': 370,'chiquinquira': 284}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'girardot': {'neighbors': {'bogota': 138.1, 'honda':136, 'ibage':68.4}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'ibage': {'neighbors': {'armenia': 80.6, 'manisalez': 173,'barrancabermeja':429, 'honda': 146, 'girardot':68.4}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'armenia': {'neighbors': {'pereira':  45.4, 'ibage': 80.6,'tulua':87.2}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'pereira': {'neighbors': {'armenia': 45.4, 'medellin': 214, 'manisalez': 53.3}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'manisalez': {'neighbors': {'pereira': 53.3, 'ibage': 173, 'honda':137,'bucaramanga':427}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'medellin': {'neighbors': {'barrancabermeja': 300, 'honda': 370,'chiquinquira':391, 'manisalez': 197, 'pereira':214, 'bogota': 511.8}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'villavicencio': {'neighbors': {'bogota': 110.4, 'tunja': 258.3, 'sogamoso':349.3}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'tunja': {'neighbors': {'duitama':54.3, 'villavicencio': 258.3, 'bogota':151.5,'socorro':162,'chiquinquira':77.2 }, 'parent': None, 'g': math.inf, 'f': math.inf},
        'chiquinquira': {'neighbors': {'bogota': 144.4, 'tunja': 77.2, 'honda': 284,'medellin':391,'barrancabermeja':267,'socorro':142 }, 'parent': None, 'g': math.inf, 'f': math.inf},
        'duitama': {'neighbors': {'sogamoso': 20, 'pamplona': 303, 'tunja':54.3}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'sogamoso': {'neighbors': {'duitama': 20, 'villavicencio': 349.3}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'socorro': {'neighbors': {'chiquinquira':142 , 'tunja':162 ,'bucaramanga':120}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'bucaramanga': {'neighbors': {'cucuta': 196,'pamplona': 125,'socorro': 120,'barrancabermeja': 115}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'barrancabermeja': {'neighbors': {'cucuta': 436, 'bucaramanga': 115,'chiquinquira': 267,'ibage': 429, 'manisalez':427,'medellin':300}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'pamplona': {'neighbors': {'duitama': 303, 'bucaramanga': 125}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'cucuta': {'neighbors': {'barrancabermeja': 436, 'bucaramanga': 196}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'tulua': {'neighbors': {'cali': 94.2, 'armenia': 87.2}, 'parent': None, 'g': math.inf, 'f': math.inf},
        'cali': {'neighbors': {'tulua': 94.2}, 'parent': None, 'g': math.inf, 'f': math.inf}
    }        
    posicion = {
        'bogota': {'x': -74.07712164430839, 'y': 4.71680699877015},
        'honda': {'x': -73.35826317154614, 'y': 5.544321975003336},
        'girardot': {'x': -74.7958661049945, 'y': 4.302467009809488},
        'ibage': {'x': -75.2187342985274, 'y': 4.436544192225768},
        'armenia': {'x': -75.67792974170058, 'y': 4.536753809271931},
        'pereira': {'x': -75.71543466177089, 'y': 4.808753007545216},
        'manisalez': {'x': -75.50447803297618, 'y': -5.063494173940785},
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
    ruta_optima = a_plus(start_node, goal_node, graph, posicion)
    print('La mejor ruta es:', ruta_optima)

