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