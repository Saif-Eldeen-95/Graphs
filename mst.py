import heapq

def prims_mst(graph, start):
    """
    Prim's Algorithm using a min-heap (priority queue).
    
    graph: adjacency list → {node: [(neighbor, weight), ...]}
    start: source vertex s
    
    Returns: (mst_edges, total_weight)
    """
    visited    = set()
    min_heap   = [(0, start, None)]  # (weight, current_node, parent_node)
    mst_edges  = []
    total_weight = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_weight += weight

        if parent is not None:
            mst_edges.append((parent, node, weight))

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    return mst_edges, total_weight


# ── Visualization ─────────────────────────────────────────────────────────────
def print_mst(mst_edges, total_weight):
    print("MST Edges:")
    print(f"  {'From':>4} {'To':>4}   {'Weight':>6}")
    print("  " + "-" * 20)
    for u, v, w in mst_edges:
        print(f"  {u:>4} {'→':>2} {v:<4}  weight: {w}")
    print(f"\n  Total MST weight: {total_weight}")


# ── Example Graph ─────────────────────────────────────────────────────────────

graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('D', 8), ('E', 5)],
    'C': [('B', 3), ('F', 7)],
    'D': [('A', 6), ('B', 8), ('E', 9)],
    'E': [('B', 5), ('D', 9), ('F', 4)],
    'F': [('C', 7), ('E', 4)],
}

mst_edges, total_weight = prims_mst(graph, start='A')
print_mst(mst_edges, total_weight)