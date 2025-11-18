from collections import deque

class Graph: 
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def print_list(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def bfs(self, start_vertex):
        visited = set()
        queue = deque()

        queue.append(start_vertex)
        visited.add(start_vertex)

        print("BFS Traversal:")

        while queue: 
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print()

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
            print("DFS Traversal:", end=" ")

        visited.add(start_vertex)
        print(start_vertex, end=" ")

        for neighbor in self.adj_list[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def dfs_iterative(self, start_vertex):
        visited = set()
        stack = []

        stack.append(start_vertex)

        print("Iterative DFS Traversal:", end=" ")

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        print()

g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.print_list()

g.bfs(0)
g.dfs(0)
g.dfs_iterative(0)