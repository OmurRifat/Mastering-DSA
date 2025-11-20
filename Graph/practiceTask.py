class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, v1, v2, weight):
        self.adj_list[v1].append((v2, weight))
        self.adj_list[v2].append((v1, weight))

    def dfs_iterative(self, start_vertex):
        visited = set()
        stack = []
        stack.append(start_vertex)
        visited.add(start_vertex)
        cycle = False
        # print("DFS Traversal:", end="")

        while stack:
            vertex = stack.pop()
            # print(vertex, end=" ")
            for neighbor, _ in self.adj_list[vertex]:
                if neighbor in stack:
                    cycle = True
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        return {"length": len(visited), "cycle": cycle}  

    def determine_connectivity(self, start_vertex):
        return self.dfs_iterative(start_vertex)["length"] == len(self.adj_list)

    def determine_cycle_existence(self, start_vertex):
        return self.dfs_iterative(start_vertex)["cycle"]

    def print_list(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")
g.add_vertex("H")
g.add_vertex("I")
g.add_vertex("J")
g.add_vertex("K")
g.add_vertex("L")
g.add_vertex("M")
g.add_vertex("N")
g.add_vertex("O")
g.add_vertex("P")
g.add_vertex("Q")
g.add_vertex("R")
g.add_vertex("S")
g.add_vertex("T")
g.add_vertex("U")
g.add_vertex("V")
g.add_vertex("W")
g.add_vertex("X")
g.add_vertex("Y")
g.add_vertex("Z")
g.add_edge("A", "B", 1)
g.add_edge("B", "C", 1)
g.add_edge("C", "D", 1)
g.add_edge("D", "E", 1)
g.add_edge("E", "F", 1)
g.add_edge("F", "G", 1)
g.add_edge("G", "H", 1)
g.add_edge("H", "I", 1)
g.add_edge("I", "J", 1)
g.add_edge("J", "K", 1)
g.add_edge("K", "L", 1)
g.add_edge("L", "M", 1)
g.add_edge("M", "N", 1)
g.add_edge("N", "O", 1)
g.add_edge("O", "P", 1)
g.add_edge("P", "Q", 1)
g.add_edge("Q", "R", 1)
g.add_edge("R", "S", 1)
g.add_edge("S", "T", 1)
g.add_edge("T", "U", 1)
g.add_edge("U", "V", 1)
g.add_edge("V", "W", 1)
g.add_edge("W", "X", 1)
g.add_edge("X", "Y", 1)
g.add_edge("Y", "Z", 1)
# g.print_list()
# g.dfs_iterative("A")
# g.determine_connectivity("A")
g.determine_cycle_existence("A")