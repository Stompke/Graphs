"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                visited.add(v)
                print(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)




    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                visited.add(v)
                print(v)

                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)



    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        def dft_recursive_inner(starting_point, path_so_far = [], visited = set(), all_paths = [] ):


            if starting_point in visited or self.get_neighbors(starting_point) == set():
                all_paths.append(path_so_far)
                return None
            
            visited.add(starting_point)
            path_so_far.append(starting_point)
            print(starting_point)
            # print(path_so_far)
            for neighbor in self.get_neighbors(starting_point):
                dft_recursive_inner(neighbor, path_so_far, visited)

        return dft_recursive_inner(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        routes = {}
        best_route = []
        while q.size() > 0:
            v = q.dequeue()
            
            if v not in visited:
                if v == destination_vertex:
                    # return routes
                    cur = destination_vertex
                    while cur != starting_vertex:
                        for v in visited:
                            if cur in routes[v]:
                                best_route.insert(0, v)
                                cur = v
                    best_route.append(destination_vertex)
                    return best_route
                visited.add(v)
                neighbors = set()
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
                    neighbors.add(next_vert)
                routes[v] = neighbors


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        routes = {}
        best_route = []
        while s.size() > 0:
            v = s.pop()
            
            if v not in visited:
                if v == destination_vertex:
                    # return routes
                    cur = destination_vertex
                    print(routes)
                    print(visited)
                    while cur != starting_vertex:
                        # print(cur)
                        for v in visited:
                            if cur in routes[v]:
                                best_route.insert(0, v)
                                cur = v
                                break
                    best_route.append(destination_vertex)
                    return best_route
                visited.add(v)
                neighbors = set()
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)
                    neighbors.add(next_vert)
                routes[v] = neighbors

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def dfs_recursive_inner(starting_point, ending_point, visited = set() ):
            if starting_point == ending_point:
                return [starting_point]
            if starting_point not in visited:
                visited.add(starting_point)
                neighbors = [node for node in self.get_neighbors(starting_point) if node not in visited]
                if len(neighbors) == 0:
                    return None
                for neighbor_node in neighbors:
                    path = dfs_recursive_inner(neighbor_node, ending_point, visited)
                    if path:
                        return [starting_point, *path]


        return dfs_recursive_inner(starting_vertex, destination_vertex)
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    graph.add_edge(4, 6)


    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    graph.add_vertex(222)
    print('get neighbors', graph.get_neighbors(222))
    if(graph.get_neighbors(222) == set()):
        print('it is esual YO')

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print('dft_recursive: ', graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('breadth first search: ', graph.bfs( 1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('dfs', graph.dfs(1, 6))
    print('dfs recursive: ', graph.dfs_recursive(1, 3))
