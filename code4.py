from collections import deque, defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.adj_list = defaultdict(list)  # Adjacency list representation

    def add_edge(self, u, v, bidirectional=True):
        """Add edge from u to v. Set bidirectional=False for directed graph."""
        self.adj_list[u].append(v)
        if bidirectional:
            self.adj_list[v].append(u)

    def bfs(self, start):
        """Perform BFS traversal from the start node."""
        visited = [False] * self.V
        parent = [-1] * self.V
        level = [-1] * self.V  # Distance from the start node
        traversal_order = []

        queue = deque()
        queue.append(start)
        visited[start] = True
        level[start] = 0

        while queue:
            current = queue.popleft()
            traversal_order.append(current)
            for neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = current
                    level[neighbor] = level[current] + 1
                    queue.append(neighbor)

        return traversal_order, level, parent

    def bfs_all_components(self):
        """BFS for disconnected graphs (all components)."""
        visited = [False] * self.V
        all_components = []

        for i in range(self.V):
            if not visited[i]:
                queue = deque()
                component = []

                queue.append(i)
                visited[i] = True

                while queue:
                    current = queue.popleft()
                    component.append(current)

                    for neighbor in self.adj_list[current]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

                all_components.append(component)

        return all_components

    def reconstruct_path(self, start, end, parent):
        """Reconstruct shortest path using parent array after BFS."""
        path = []
        while end != -1:
            path.append(end)
            end = parent[end]
        path.reverse()

        if path[0] == start:
            return path
        else:
            return []  # No path found

    def print_graph(self):
        """Print adjacency list of the graph."""
        print("Graph Adjacency List:")
        for node in range(self.V):
            print(f"{node} -> {self.adj_list[node]}")

# ---------- Example Usage -------------

if __name__ == "__main__":
    g = Graph(8)
    
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(5, 6)
    g.add_edge(6, 7)

    g.print_graph()

    print("\nBFS Traversal from node 0:")
    traversal, levels, parents = g.bfs(0)
    print("Traversal Order:", traversal)
    print("Levels:", levels)
    print("Parents:", parents)

    print("\nAll Connected Components (BFS on disconnected graph):")
    components = g.bfs_all_components()
    for idx, comp in enumerate(components):
        print(f"Component {idx + 1}: {comp}")

    print("\nPath from 0 to 4:")
    path = g.reconstruct_path(0, 4, parents)
    print("Shortest Path:", path)

    print("\nPath from 0 to 7 (should be empty as disconnected):")
    path = g.reconstruct_path(0, 7, parents)
    print("Shortest Path:", path)
