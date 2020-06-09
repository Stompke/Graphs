from graph import Graph

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
        g.add_edge(pair[0], pair[1])
    return g.vertices

print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 7))
