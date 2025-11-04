# Number of vertices
n = 4

# Initialize a 4*4 matrix filled with zeros
graph = [[0 for _ in range(n)] for _ in range(n)]

# Function to add an edge
def add_edge(i, j):
    graph[i][j] = 1
    graph[j][i] = 1


# Add edges
add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 3)
add_edge(2, 3)

# Print adjacency matrix
for row in graph:
    print(row)



# ----------------------------------------------


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, i, j):
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def print_matrix(self):
        for row in self.matrix:
            print(row)

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.print_matrix()