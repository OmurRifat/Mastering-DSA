import heapq

class ImprovedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, v1, v2, weight):
        """Add weighted edge. For undirected graph, add both directions."""
        self.adj_list[v1].append((v2, weight))
        self.adj_list[v2].append((v1, weight))
    
    def add_directed_edge(self, v1, v2, weight):
        """Add weighted edge for directed graph."""
        self.adj_list[v1].append((v2, weight))
    
    def dijkstra_all_paths(self, start_vertex):
        """
        Find shortest distances from start_vertex to ALL other vertices.
        
        Returns:
            dict: {vertex: shortest_distance}
        """
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start_vertex] = 0
        
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Skip if we've already processed this vertex with a better distance
            if current_distance > distances[current_vertex]:
                continue
            
            # Check all neighbors
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                
                # If we found a shorter path, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances
    
    def dijkstra_single_target(self, start_vertex, target_vertex):
        """
        Find shortest distance from start_vertex to target_vertex.
        Early termination when target is found.
        
        Returns:
            float: shortest distance to target (or inf if unreachable)
        """
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start_vertex] = 0
        
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Early termination: found the target!
            if current_vertex == target_vertex:
                return current_distance
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances[target_vertex]
    
    def dijkstra_with_path(self, start_vertex, target_vertex):
        """
        Find shortest path from start_vertex to target_vertex.
        Returns both the distance and the actual path taken.
        
        Returns:
            tuple: (distance, path_list)
        """
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start_vertex] = 0
        
        # Track the previous vertex in the optimal path
        previous = {vertex: None for vertex in self.adj_list}
        
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_vertex == target_vertex:
                break
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Reconstruct the path
        path = []
        current = target_vertex
        
        if previous[current] is None and current != start_vertex:
            # No path exists
            return float('inf'), []
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        
        return distances[target_vertex], path
    
    def print_list(self):
        """Print the adjacency list."""
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")


# ============================================
# EXAMPLE 1: Basic Shortest Path
# ============================================
print("="*50)
print("EXAMPLE 1: Simple Graph")
print("="*50)

g1 = ImprovedGraph()
for v in ["A", "B", "C", "D", "E"]:
    g1.add_vertex(v)

g1.add_edge("A", "B", 4)
g1.add_edge("A", "C", 2)
g1.add_edge("B", "C", 1)
g1.add_edge("B", "D", 5)
g1.add_edge("C", "D", 8)
g1.add_edge("C", "E", 10)
g1.add_edge("D", "E", 2)

print("\nGraph:")
g1.print_list()

print("\nAll shortest distances from A:")
distances = g1.dijkstra_all_paths("A")
for vertex, distance in sorted(distances.items()):
    print(f"A -> {vertex}: {distance}")

print("\nShortest distance from A to E:")
distance_to_e = g1.dijkstra_single_target("A", "E")
print(f"Distance: {distance_to_e}")

print("\nShortest path from A to E:")
distance, path = g1.dijkstra_with_path("A", "E")
print(f"Distance: {distance}")
print(f"Path: {' -> '.join(path)}")


# ============================================
# EXAMPLE 2: Your Original Graph (simplified)
# ============================================
print("\n" + "="*50)
print("EXAMPLE 2: Chain Graph (A to Z)")
print("="*50)

g2 = ImprovedGraph()
vertices = ["A", "B", "C", "D", "E"]
for v in vertices:
    g2.add_vertex(v)

# Create a chain: A-B-C-D-E
g2.add_edge("A", "B", 1)
g2.add_edge("B", "C", 1)
g2.add_edge("C", "D", 1)
g2.add_edge("D", "E", 1)

# Add a shortcut with higher cost
g2.add_edge("A", "E", 10)

print("\nShortest path from A to E:")
distance, path = g2.dijkstra_with_path("A", "E")
print(f"Distance: {distance}")
print(f"Path: {' -> '.join(path)}")
print(f"Note: Even though there's a direct edge A-E with cost 10,")
print(f"the path through B-C-D is shorter (total cost: {distance})")


# ============================================
# EXAMPLE 3: Directed Graph (Network Delay)
# ============================================
print("\n" + "="*50)
print("EXAMPLE 3: Network Delay Problem")
print("="*50)

g3 = ImprovedGraph()
for v in [1, 2, 3, 4]:
    g3.add_vertex(v)

# Directed edges (signal can only go one way)
g3.add_directed_edge(1, 2, 1)
g3.add_directed_edge(1, 3, 4)
g3.add_directed_edge(2, 3, 2)
g3.add_directed_edge(2, 4, 6)
g3.add_directed_edge(3, 4, 3)

print("\nDirected Graph (Network):")
g3.print_list()

print("\nTime for signal to reach all nodes from node 1:")
distances = g3.dijkstra_all_paths(1)
max_time = max(distances.values())

if max_time == float('inf'):
    print("Not all nodes are reachable!")
else:
    print(f"All nodes receive the signal in: {max_time} time units")
    print("\nTime to reach each node:")
    for node in sorted(distances.keys()):
        print(f"  Node {node}: {distances[node]} time units")
