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
        self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not exist")

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

        # keep track of visited nodes
        visited = set()

        # Repeat until queue is empty
        while q.size() > 0:

            # Dequeue first vert
            v = q.dequeue()

            # if its not visited:
            if v not in visited:
                print(v)

                # Mark visited
                visited.add(v)

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

            # Remove first item from stack
            v = s.pop()

            # If its not visited
            if v not in visited:
                print(v)
                # Mark visited
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        path = self.get_neighbors(starting_vertex)

        visited.add(starting_vertex)

        print(starting_vertex)

        for n in path - visited:
            # print(
            #     n,
            #     "Next",
            #     path,
            #     "path",
            #     path -
            #     visited,
            #     "sub")
            self.dft_recursive(n, visited)
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        # push the first path into the queue
        q.enqueue([starting_vertex])
        while q.size() > 0:
            # get the first path from the queue
            path = q.dequeue()
            # v = q.dequeue()
            # get the last node from the path
            node = path[-1]
            # path found
            if node == destination_vertex:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into
            # the queue
            for adjacent in self.get_neighbors(node):
                new_path = list(path)
                new_path.append(adjacent)
                q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        lst = []
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:

            # Remove first item from stack
            v = s.pop()

            # If its not visited
            if v not in visited:
                print(v)
                # Mark visited
                visited.add(v)
                lst.append(v)
                if v == destination_vertex:
                    return lst
                    break

                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=[]):
        """
          Return a list containing a path from Return a list containing a path from
          starting_vertex to destination_vertex in starting_vertex to destination_vertex in
          depth - first order.	        depth - first order.
          This should be done using recursion.	        This should be done using recursion.
          """
        if starting_vertex == destination_vertex:
            return visited + [starting_vertex]
        else:
            visited.append(starting_vertex)
            for edge in self.get_neighbors(starting_vertex):
                if edge not in visited:
                    path = self.dfs_recursive(
                        edge, destination_vertex, visited)
                    if path:
                        return path
            visited.remove(starting_vertex)


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
    print(graph.get_neighbors(2), "Neighbors")
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

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
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
    # print(list(graph.dfs_recursive(1, 6)))
