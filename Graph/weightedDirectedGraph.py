class WeightedDirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2, weight):
        self.adj_list[v1].append((v2, weight))

    def print_list(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

wdg = WeightedDirectedGraph()
wdg.add_vertex("A")
wdg.add_vertex("B")
wdg.add_vertex("C")

wdg.add_edge("A", "B", 10) 
wdg.add_edge("B", "C", 5)

wdg.print_list()