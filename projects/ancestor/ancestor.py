from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    all_nums = set()
    for pair in ancestors:
        if pair[0] not in all_nums:
            all_nums.add(pair[0])
            g.add_vertex(pair[0])
        if pair[1] not in all_nums:
            all_nums.add(pair[1])
            g.add_vertex(pair[1])
    for pair in ancestors:
        g.add_edge(pair[1], pair[0])

    # get neighbors gets the parents
    print( g.get_neighbors(6))
    print( g.get_neighbors(11))

    s = Stack()
    all_paths = []
    s.push([starting_node])
    while s.size() > 0:
        path = s.pop()
        cur_index = path[-1]
        parents = g.get_neighbors(cur_index)
        if len(parents) > 0:
            for parent in parents:
                path_copy = list(path)
                path_copy.append(parent)
                s.push(path_copy)
        else:
            all_paths.append(path)
    return all_paths
            
            


print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6))
