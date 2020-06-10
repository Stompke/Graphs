from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    all_nums = set()

    # adding unique nodes
    for pair in ancestors:
        if pair[0] not in all_nums:
            all_nums.add(pair[0])
            g.add_vertex(pair[0])
        if pair[1] not in all_nums:
            all_nums.add(pair[1])
            g.add_vertex(pair[1])

    # Adding ancestor pairs as edges
    for pair in ancestors:
        # swaped the pair to look up the tree not down the tree
        g.add_edge(pair[1], pair[0])

    # check if the starting node has no parents
    is_orphan = g.get_neighbors(starting_node)
    if len(is_orphan) == 0:
        return -1


    s = Stack()
    all_paths = []
    s.push([starting_node])
    # grab the top route off the stack and look for the next ancestor
    while s.size() > 0:
        path = s.pop()
        cur_index = path[-1]
        parents = g.get_neighbors(cur_index)
        if len(parents) > 0:
            for parent in parents:
                path_copy = list(path)
                path_copy.append(parent)
                # Add this new path to the stack
                s.push(path_copy)
        else:
            # this path has ended and will get added to a storage of all the paths
            all_paths.append(path)

    # Start with setting the first path to be the longest
    longest = all_paths[0]

    # loop through all paths and overwrite "longest" if it is longer
    for stored_path in all_paths:
        if len(stored_path) > len(longest):
            longest = stored_path
        # if it is the same length see which ending integer is smaller
        if len(stored_path) == len(longest):
            if stored_path[-1] < longest[-1]:
                longest = stored_path

    return longest[-1]

print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6))
