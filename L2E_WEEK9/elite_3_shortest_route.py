# Why queue.pop(0) would be slow:
# A Python list stores items in contiguous memory, so removing index 0 via pop(0)
# forces Python to shift every remaining element one slot left, costing O(n) per removal.
# Advancing an integer index pointer (head += 1) takes O(1) time instead.


# Time: O(V + E), Space: O(V) where V is the number of nodes and E is the number of edges.
# Reasoning: BFS explores each reachable node and directed edge once using an O(1) index-pointer queue and a parent dictionary of size O(V).
def shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return []
    if start == goal:
        return [start]
    
    queue = [start]
    head = 0
    came_from = {start: None}

    while head < len(queue):
        current = queue[head]
        head += 1

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbour in graph.get(current, []):
            if neighbour not in came_from:
                came_from[neighbour] = current
                queue.append(neighbour)

    return []


# Time: O(V + E), Space: O(V) where V is the number of nodes and E is the number of edges.
# Reasoning: Starting from start, BFS visits every reachable node and outgoing edge once while storing visited nodes in a set of up to V items.
def reachable(graph, start):
    if start not in graph:
        return 0
    queue = [start]
    head = 0
    visited = {start}

    while head < len(queue):
        current = queue[head]
        head += 1

        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return len(visited)


# Time: O(V + E), Space: O(V) where V is the number of nodes and E is the number of edges.
# Reasoning: Three-state DFS inspects every node and directed edge at most once while tracking active recursion states in a dictionary of size O(V).
def has_cycle(graph):
    state = {}

    def dfs(node):
        state[node] = 1
        for neighbour in graph.get(node, []):
            if state.get(neighbour, 0) == 1:
                return True
            if state.get(neighbour, 0) == 0:
                if dfs(neighbour) is True:
                    return True
        state[node] = 2
        return False

    for node in graph:
        if state.get(node, 0) == 0:
            if dfs(node) is True:
                return True
    return False


# Bonus: Returns every shortest path from start to goal
# Time: O(V + E + P * L) where P is the number of shortest paths and L is path length; Space: O(V + E + P * L).
# Reasoning: Level-by-level BFS records all parents at the shortest distance for each node, and backtracking rebuilds every valid shortest path.
def all_shortest_paths(graph, start, goal):
    if start not in graph or goal not in graph:
        return []
    if start == goal:
        return [[start]]

    dist = {start: 0}
    parents = {start: []}
    queue = [start]
    head = 0

    while head < len(queue):
        current = queue[head]
        head += 1

        if goal in dist and dist[current] >= dist[goal]:
            continue

        for neighbour in graph.get(current, []):
            next_dist = dist[current] + 1
            if neighbour not in dist:
                dist[neighbour] = next_dist
                parents[neighbour] = [current]
                queue.append(neighbour)
            elif dist[neighbour] == next_dist:
                parents[neighbour].append(current)

    if goal not in dist:
        return []

    results = []

    def backtrack(node, path):
        if node == start:
            full_path = path + [start]
            full_path.reverse()
            results.append(full_path)
            return
        for p in parents[node]:
            backtrack(p, path + [node])

    backtrack(goal, [])
    return results


# --- Main Section (Testing) ---
if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["F"],
        "E": ["F"],
        "F": []
    }

    # 1. Prompt examples
    print("shortest_path A -> F:", shortest_path(graph, "A", "F"))      # ['A', 'B', 'D', 'F']
    print("shortest_path A -> A:", shortest_path(graph, "A", "A"))      # ['A']
    print("shortest_path F -> A:", shortest_path(graph, "F", "A"))      # []
    print("reachable A:", reachable(graph, "A"))                        # 6
    print("reachable C:", reachable(graph, "C"))                        # 4
    print("has_cycle(graph):", has_cycle(graph))                        # False
    print("has_cycle(X <-> Y):", has_cycle({"X": ["Y"], "Y": ["X"]}))   # True

    # 2. Custom Test 1 (Edge Case): Unknown start or goal node
    print("Unknown start:", shortest_path(graph, "Z", "F"), reachable(graph, "Z"))  # [], 0
    print("Unknown goal:", shortest_path(graph, "A", "Z"))                          # []

    # 3. Custom Test 2 (Edge Case): Self-loop cycle
    self_loop_graph = {"A": ["B"], "B": ["B"]}
    print("Self-loop has_cycle:", has_cycle(self_loop_graph))                       # True
    print("Self-loop reachable B:", reachable(self_loop_graph, "B"))                # 1

    # 4. Custom Test 3: Disconnected components & dead-end node
    disconnected = {"1": ["2"], "2": [], "3": ["4"], "4": ["3"]}
    print("Disconnected path 1 -> 4:", shortest_path(disconnected, "1", "4"))       # []
    print("Disconnected has_cycle:", has_cycle(disconnected))                       # True

    # 5. Bonus Test: All shortest paths from A to F
    print("All shortest paths A -> F:", all_shortest_paths(graph, "A", "F"))
    # [['A', 'B', 'D', 'F'], ['A', 'C', 'D', 'F'], ['A', 'C', 'E', 'F']]
