"""
Dijkstra's Algorithm - Practice Problems
Each problem includes:
1. Problem statement
2. Example
3. Solution with explanation
4. Test cases
"""

import heapq

# ============================================
# PROBLEM 1: Network Delay Time (LeetCode 743)
# ============================================

def network_delay_time(times, n, k):
    """
    You are given a network of n nodes, labeled from 1 to n.
    You are also given times, a list of travel times as directed edges.
    times[i] = (u, v, w) where u is the source node, v is the target node,
    and w is the time it takes for a signal to travel from source to target.
    
    We will send a signal from node k.
    Return the MINIMUM time it takes for ALL n nodes to receive the signal.
    If it's impossible for all nodes to receive the signal, return -1.
    
    Example:
        times = [[2,1,1], [2,3,1], [3,4,1]]
        n = 4, k = 2
        
        Graph:  2 --1--> 1
                |
                1
                |
                v
                3 --1--> 4
        
        Answer: 2 (node 4 takes the longest at 2 time units)
    """
    # Build adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Dijkstra's algorithm
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0
    
    pq = [(0, k)]
    
    while pq:
        current_time, node = heapq.heappop(pq)
        
        if current_time > distances[node]:
            continue
        
        for neighbor, time in graph[node]:
            new_time = current_time + time
            if new_time < distances[neighbor]:
                distances[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    
    # Find maximum time (when the last node receives the signal)
    max_time = max(distances.values())
    return max_time if max_time != float('inf') else -1


print("="*60)
print("PROBLEM 1: Network Delay Time")
print("="*60)
print("\nTest Case 1:")
times1 = [[2,1,1], [2,3,1], [3,4,1]]
result1 = network_delay_time(times1, 4, 2)
print(f"times = {times1}, n = 4, k = 2")
print(f"Result: {result1}")
print(f"Expected: 2\n")

print("Test Case 2:")
times2 = [[1,2,1]]
result2 = network_delay_time(times2, 2, 1)
print(f"times = {times2}, n = 2, k = 1")
print(f"Result: {result2}")
print(f"Expected: 1\n")

print("Test Case 3 (Impossible case):")
times3 = [[1,2,1]]
result3 = network_delay_time(times3, 2, 2)
print(f"times = {times3}, n = 2, k = 2")
print(f"Result: {result3}")
print(f"Expected: -1 (node 1 is unreachable from node 2)\n")


# ============================================
# PROBLEM 2: Cheapest Flights Within K Stops (LeetCode 787)
# ============================================

def find_cheapest_price(n, flights, src, dst, k):
    """
    There are n cities connected by flights.
    Each flight is [from, to, price].
    Find the cheapest price from src to dst with at most k stops.
    Return -1 if there's no such route.
    
    This is a VARIATION of Dijkstra where we track (cost, city, stops_left).
    
    Example:
        n = 4
        flights = [[0,1,100], [1,2,100], [2,0,100], [1,3,600], [2,3,200]]
        src = 0, dst = 3, k = 1
        
        Cheapest path with at most 1 stop: 0 -> 1 -> 3 = 700
    """
    # Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v, price in flights:
        graph[u].append((v, price))
    
    # (cost, city, stops_used)
    pq = [(0, src, 0)]
    
    # Track minimum cost to reach each city with specific number of stops
    visited = {}
    
    while pq:
        cost, city, stops = heapq.heappop(pq)
        
        # Found destination
        if city == dst:
            return cost
        
        # Too many stops
        if stops > k:
            continue
        
        # Skip if we've visited this (city, stops) combination with lower cost
        if (city, stops) in visited and visited[(city, stops)] <= cost:
            continue
        
        visited[(city, stops)] = cost
        
        # Explore neighbors
        for neighbor, price in graph[city]:
            new_cost = cost + price
            heapq.heappush(pq, (new_cost, neighbor, stops + 1))
    
    return -1


print("\n" + "="*60)
print("PROBLEM 2: Cheapest Flights Within K Stops")
print("="*60)
print("\nTest Case 1:")
flights1 = [[0,1,100], [1,2,100], [2,0,100], [1,3,600], [2,3,200]]
result1 = find_cheapest_price(4, flights1, 0, 3, 1)
print(f"n = 4, flights = {flights1}")
print(f"src = 0, dst = 3, k = 1")
print(f"Result: {result1}")
print(f"Expected: 700 (path: 0 -> 1 -> 3)\n")

print("Test Case 2:")
flights2 = [[0,1,100], [1,2,100], [0,2,500]]
result2 = find_cheapest_price(3, flights2, 0, 2, 1)
print(f"n = 3, flights = {flights2}")
print(f"src = 0, dst = 2, k = 1")
print(f"Result: {result2}")
print(f"Expected: 200 (path: 0 -> 1 -> 2)\n")


# ============================================
# PROBLEM 3: Path with Minimum Effort (LeetCode 1631)
# ============================================

def minimum_effort_path(heights):
    """
    You are a hiker on a 2D grid (heights matrix).
    You start at top-left (0,0) and want to reach bottom-right.
    
    A route's effort is the maximum absolute difference in heights
    between two consecutive cells in the route.
    
    Find the minimum effort required.
    
    Example:
        heights = [[1,2,2],
                   [3,8,2],
                   [5,3,5]]
        
        Answer: 2 (path: 1->3->5->3->5, max diff = 2)
    """
    if not heights or not heights[0]:
        return 0
    
    rows, cols = len(heights), len(heights[0])
    
    # Minimum effort to reach each cell
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0
    
    # (effort, row, col)
    pq = [(0, 0, 0)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while pq:
        effort, row, col = heapq.heappop(pq)
        
        # Reached destination
        if row == rows - 1 and col == cols - 1:
            return effort
        
        # Skip if we've found a better path
        if effort > efforts[row][col]:
            continue
        
        # Check all 4 neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                # Effort is the max difference along the path
                new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                
                if new_effort < efforts[new_row][new_col]:
                    efforts[new_row][new_col] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_col))
    
    return efforts[rows - 1][cols - 1]


print("\n" + "="*60)
print("PROBLEM 3: Path with Minimum Effort")
print("="*60)
print("\nTest Case 1:")
heights1 = [[1,2,2], [3,8,2], [5,3,5]]
result1 = minimum_effort_path(heights1)
print(f"heights = {heights1}")
print(f"Result: {result1}")
print(f"Expected: 2\n")

print("Test Case 2:")
heights2 = [[1,2,3], [3,8,4], [5,3,5]]
result2 = minimum_effort_path(heights2)
print(f"heights = {heights2}")
print(f"Result: {result2}")
print(f"Expected: 1\n")


# ============================================
# PROBLEM 4: Shortest Path in Binary Matrix (LeetCode 1091)
# ============================================

def shortest_path_binary_matrix(grid):
    """
    Given an n x n binary matrix, return the length of the shortest
    clear path in the matrix. If there is no clear path, return -1.
    
    A clear path is from top-left (0,0) to bottom-right (n-1, n-1):
    - All visited cells are 0
    - All adjacent cells are 8-directionally connected
    
    Example:
        grid = [[0,0,0],
                [1,1,0],
                [1,1,0]]
        
        Answer: 4 (path length, not distance)
    """
    if not grid or grid[0][0] == 1:
        return -1
    
    n = len(grid)
    if n == 1:
        return 1 if grid[0][0] == 0 else -1
    
    # 8 directions
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    # (distance, row, col)
    pq = [(1, 0, 0)]  # Start with distance 1
    visited = {(0, 0)}
    
    while pq:
        dist, row, col = heapq.heappop(pq)
        
        # Reached destination
        if row == n - 1 and col == n - 1:
            return dist
        
        # Check all 8 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check bounds and validity
            if (0 <= new_row < n and 0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                heapq.heappush(pq, (dist + 1, new_row, new_col))
    
    return -1


print("\n" + "="*60)
print("PROBLEM 4: Shortest Path in Binary Matrix")
print("="*60)
print("\nTest Case 1:")
grid1 = [[0,0,0], [1,1,0], [1,1,0]]
result1 = shortest_path_binary_matrix(grid1)
print(f"grid = {grid1}")
print(f"Result: {result1}")
print(f"Expected: 4\n")

print("Test Case 2:")
grid2 = [[0,1], [1,0]]
result2 = shortest_path_binary_matrix(grid2)
print(f"grid = {grid2}")
print(f"Result: {result2}")
print(f"Expected: -1 (no clear path)\n")


# ============================================
# YOUR PRACTICE EXERCISES
# ============================================

print("\n" + "="*60)
print("PRACTICE EXERCISES FOR YOU TO TRY")
print("="*60)

print("""
1. PATH WITH MAXIMUM PROBABILITY (LeetCode 1514)
   - Given edges with success probabilities
   - Find path with maximum probability of success
   - Hint: Use Dijkstra with max-heap (negate probabilities)

2. SWIM IN RISING WATER (LeetCode 778)
   - Grid where each cell has elevation
   - Water level rises over time
   - Find minimum time to reach bottom-right
   - Hint: Similar to minimum effort problem

3. MINIMUM COST TO MAKE AT LEAST ONE VALID PATH (LeetCode 1368)
   - Grid with directional arrows
   - Can change direction with cost 1
   - Find minimum cost to reach bottom-right
   - Hint: Use Dijkstra where cost is number of direction changes

4. THE MAZE II (LeetCode 505)
   - Ball rolls in a maze until hitting a wall
   - Find shortest distance to destination
   - Hint: State is (row, col), edges are "roll until wall"

Try implementing these on your own!
Each one is a variation of Dijkstra's algorithm.
""")
