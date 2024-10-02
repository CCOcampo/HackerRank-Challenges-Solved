def evenForest(t_nodes, t_edges, t_from, t_to):
    #Crear una lista de listas según el numero de nodos
    tree = [[] for _ in range(t_nodes + 1)] 

    #Construcción del arbol teniendo en cuenta aristas de cada lista
    for u, v in zip(t_from, t_to):
        tree[u].append(v)
        tree[v].append(u)
    
    #Variables para crear el arbol
    subtree_size = [0] * (t_nodes + 1)
    visited = [False] * (t_nodes + 1)
    
    def dfs(node):
        visited[node] = True
        subtree_size[node] = 1
        for neighbor in tree[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                subtree_size[node] += subtree_size[neighbor]
    
    dfs(1)
    
    #Aristas que se pueden eliminar manteniendo la estructura del subarbol
    removable_edges = 0
    for i in range(2, t_nodes + 1):
        if subtree_size[i] % 2 == 0:
            removable_edges += 1
    
    return removable_edges

#Example
t_nodes = 10
t_edges = 9
t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
t_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]

print(evenForest(t_nodes, t_edges, t_from, t_to))
