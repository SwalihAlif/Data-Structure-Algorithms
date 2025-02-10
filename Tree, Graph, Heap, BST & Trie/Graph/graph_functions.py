from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        for vertex in self.adj_list.keys():
            print(vertex, ':', self.adj_list[vertex])
            
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] =[]
            
            return True 
        return False
        
    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"Error: Cannot add self-loop for vertex {v1}")
            return False
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
        
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
        
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                try:

                    visited.add(vertex)
                    result.append(vertex)
                    queue.extend([neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited])
                except KeyError:
                    pass
        
        return result
    
    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend([neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited])
        
        return result

    def shortest_path(self, start_vertex, end_vertex):
        queue = [(start_vertex, [start_vertex])]
        visited = set()
        
        while queue:
            current, path = queue.pop(0)
            if current == end_vertex:
                return path
            
            if current not in visited:
                visited.add(current)
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        
        return None  # No path found

    def all_paths(self, start_vertex, end_vertex, path=None):
        if path is None:
            path = [start_vertex]
        
        if start_vertex == end_vertex:
            return [path]
        
        paths = []
        for neighbor in self.adj_list[start_vertex]:
            if neighbor not in path:
                new_paths = self.all_paths(neighbor, end_vertex, path + [neighbor])
                paths.extend(new_paths)
        
        return paths

# another way of shortest_path and all path

    def shortest_path(self, start_vertex, end_vertex):
        if start_vertex == end_vertex:
            return [start_vertex]

        visited = set()
        queue = deque([(start_vertex, [start_vertex])])

        while queue:
            (vertex, path) = queue.popleft()
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    if neighbor == end_vertex:
                        return path + [neighbor]
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def all_paths(self, start_vertex, end_vertex):
        paths = []
        visited = set()

        def dfs_all_paths(vertex, path):
            visited.add(vertex)
            if vertex == end_vertex:
                paths.append(path)
            else:
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        dfs_all_paths(neighbor, path + [neighbor])
            visited.remove(vertex)

        dfs_all_paths(start_vertex, [start_vertex])
        return paths
        
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')


my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

print('Graph before remove_vertex():')
my_graph.print_graph()
print('-------------------------------------')
print('BFS Traversal:',my_graph.bfs('A'))
print('BFS Traversal:',my_graph.bfs('B'))
print('BFS Traversal:',my_graph.bfs('C'))
print('BFS Traversal:',my_graph.bfs('g'))
print('-------------------------------------')
print('-------------------------------------')
print('DFS Traversal:',my_graph.dfs('A'))
print('DFS Traversal:',my_graph.dfs('B'))
print('DFS Traversal:',my_graph.dfs('C'))
print('DFS Traversal:',my_graph.dfs('D'))
print('-------------------------------------')
my_graph.remove_edge('A', 'D')
my_graph.print_graph()

my_graph.remove_vertex('D')

print('\nGraph after remove_vertex():')
my_graph.print_graph()
print('-------------------------------------')
print('BFS Traversal:',my_graph.bfs('A'))
print('BFS Traversal:',my_graph.bfs('B'))
print('BFS Traversal:',my_graph.bfs('C'))
print('BFS Traversal:',my_graph.bfs('D'))
print('-------------------------------------')

print(my_graph.shortest_path('A', 'D'))  # Output: ['A', 'D']
print(my_graph.shortest_path('A', 'B'))  # Output: ['A', 'B']
print(my_graph.shortest_path('B', 'C'))  # Output: ['B', 'D', 'C']

start_vertex = 'A'
end_vertex = 'D'
paths = my_graph.all_paths(start_vertex, end_vertex)

print(f"All paths from {start_vertex} to {end_vertex}: {paths}")

