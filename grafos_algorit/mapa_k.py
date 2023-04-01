import folium

def find(parents, vertex): #encontrar el conjunto al que pertenece un vértice
    if parents[vertex] != vertex:
        parents[vertex] = find(parents, parents[vertex])
    return parents[vertex]

def union(parents, ranks, vertex1, vertex2):#unir dos conjuntos, seleccionando uno de los dos representantes como nuevo padre del otro
    parent1 = find(parents, vertex1)
    parent2 = find(parents, vertex2)
    if parent1 != parent2:
        if ranks[parent1] < ranks[parent2]:
            parents[parent1] = parent2
        elif ranks[parent1] > ranks[parent2]:
            parents[parent2] = parent1
        else:
            parents[parent2] = parent1
            ranks[parent1] += 1
#recorre aristas ordenadas por peso, y une vértices en conjuntos hasta que todos los vértices estén en el mismo conjunto. 
# Para cada arista que une dos vértices de conjuntos diferentes, se agrega al árbol de mínima expansión y se unen los conjuntos:
def kruskal(graph):
    parents = {}
    ranks = {}
    for vertex in graph:
        parents[vertex] = vertex
        ranks[vertex] = 0
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]['neighbors'].items():
            edges.append((weight, vertex, neighbor))
    edges.sort()
    mst = []
    for edge in edges:
        weight, vertex1, vertex2 = edge
        if find(parents, vertex1) != find(parents, vertex2):
            mst.append(edge)
            union(parents, ranks, vertex1, vertex2)
        if len(set(parents.values())) == 1:
            break
    return mst


if __name__ == '__main__':
    # Ejemplo de uso
    graph = {
        'bogota': {'neighbors': {'villavicencio': 110.4, 'chiquinquira': 144.4, 'tunja': 151.5, 'honda': 161.7, 'girardot': 138.1, 'medellin': 511.8}, 'parent': None},
        'honda': {'neighbors': {'bogota': 161.7, 'girardot': 136, 'ibage': 146, 'manisalez': 137, 'medellin': 370, 'chiquinquira': 284}, 'parent': None},
        'girardot': {'neighbors': {'bogota': 138.1, 'honda': 136, 'ibage': 68.4}, 'parent': None},
        'ibage': {'neighbors': {'armenia': 80.6, 'manisalez': 173, 'barrancabermeja': 429, 'honda': 146, 'girardot': 68.4}, 'parent': None},
        'armenia': {'neighbors': {'pereira':  45.4, 'ibage': 80.6, 'tulua': 87.2}, 'parent': None},
        'pereira': {'neighbors': {'armenia': 45.4, 'medellin': 214, 'manisalez': 53.3}, 'parent': None},
        'manisalez': {'neighbors': {'pereira': 53.3, 'ibage': 173, 'honda': 137, 'bucaramanga': 427}, 'parent': None},
        'medellin': {'neighbors': {'barrancabermeja': 300, 'honda': 370, 'chiquinquira': 391, 'manisalez': 197, 'pereira': 214, 'bogota': 511.8}, 'parent': None},
        'villavicencio': {'neighbors': {'bogota': 110.4, 'tunja': 258.3, 'sogamoso': 349.3}, 'parent': None},
        'tunja': {'neighbors': {'duitama': 54.3, 'villavicencio': 258.3, 'bogota': 151.5, 'socorro': 162, 'chiquinquira': 77.2}, 'parent': None},
        'chiquinquira': {'neighbors': {'bogota': 144.4, 'tunja': 77.2, 'honda': 284, 'medellin': 391, 'barrancabermeja': 267, 'socorro': 142}, 'parent': None},
        'duitama': {'neighbors': {'sogamoso': 20, 'pamplona': 303, 'tunja': 54.3}, 'parent': None},
        'sogamoso': {'neighbors': {'duitama': 20, 'villavicencio': 349.3}, 'parent': None},
        'socorro': {'neighbors': {'chiquinquira': 142, 'tunja': 162, 'bucaramanga': 120}, 'parent': None},
        'bucaramanga': {'neighbors': {'cucuta': 196, 'pamplona': 125, 'socorro': 120, 'barrancabermeja': 115}, 'parent': None},
        'barrancabermeja': {'neighbors': {'cucuta': 436, 'bucaramanga': 115, 'chiquinquira': 267, 'ibage': 429, 'manisalez': 427, 'medellin': 300}, 'parent': None},
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
    arbol = kruskal(graph)
    rutas = [(origen, destino, {'weight': peso})
             for peso, origen, destino in arbol]

    m = folium.Map(location=[posicion['bogota']['y'],
                posicion['bogota']['x']], zoom_start=7)
    

    for o, d, w in rutas:
        o_lat, o_lon = posicion[o]['y'], posicion[o]['x']
        d_lat, d_lon = posicion[d]['y'], posicion[d]['x']
        w_num = w['weight']
        folium.Marker(location=[o_lat, o_lon], popup=o).add_to(m)
        folium.Marker(location=[d_lat, d_lon], popup=d).add_to(m)
        folium.PolyLine(locations=[(o_lat, o_lon), (d_lat, d_lon)],
                        tooltip=f'{o} - {d}: {w_num}', color='red',
                        weight=2).add_to(m)
        
    m.save('mapa_kruskal.html')