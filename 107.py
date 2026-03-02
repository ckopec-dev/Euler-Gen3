"""
Problem 107: Minimal network

A weighted graph problem where we need to find the minimum spanning tree.
The input file contains edge weights and we need to find the minimum total weight
to connect all vertices.
"""

def kruskal_mst(n, edges):
    """
    Find minimum spanning tree using Kruskal's algorithm
    n: number of vertices
    edges: list of (weight, u, v)
    """
    # Sort edges by weight
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    mst_weight = 0
    edges_used = 0
    
    for weight, u, v in edges:
        if union(u, v):
            mst_weight += weight
            edges_used += 1
            if edges_used == n - 1:
                break
    
    return mst_weight

def solve():
    # Parse the network.txt file
    edges = []
    with open('network.txt', 'r') as f:
        for i, line in enumerate(f):
            values = line.strip().split(',')
            for j, val in enumerate(values):
                if val:
                    weight = int(val)
                    if j > i:  # only upper triangle to avoid duplicates
                        edges.append((weight, i, j))
    
    n = 40  # 40 vertices in the original network
    full_weight = sum(w for w, _, _ in edges)
    mst_weight = kruskal_mst(n, edges)
    saved = full_weight - mst_weight
    
    return saved

if __name__ == '__main__':
    result = solve()
    print(f"Answer: {result}")
