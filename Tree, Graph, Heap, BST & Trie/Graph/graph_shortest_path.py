class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        for vertex in self.adj_list.keys():
            print(vertex, ':', self.adj_list[vertex])
        
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
        
    def add_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
        
    def remove_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    def graph_bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        result = []
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited)
        return result
    def graph_dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        result = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend(nei for nei in self.adj_list[vertex] if nei not in visited)
        return result
        
    def shortest_path(self, start, destination):
        queue = [(start, [start])]
        visited = set()
        
        while queue:
            current, path = queue.pop(0)
            if current == destination:
                return path
            if current not in visited:
                visited.add(current)
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    queue.append([neighbor, path + [neighbor]])
        return None
            
my_graph = Graph()
my_graph.add_vertex('Muthiripparamba')
my_graph.add_vertex('Aravankara')
my_graph.add_vertex('Pookkottur')
my_graph.add_vertex('Mundithodika')
my_graph.add_vertex('Pullara')
my_graph.add_vertex('Manjeri')
my_graph.print_graph()
my_graph.add_edges('Muthiripparamba', 'Aravankara')
my_graph.add_edges('Aravankara', 'Pookkottur')
my_graph.add_edges('Pookkottur', 'Mundithodika')
my_graph.add_edges('Mundithodika', 'Manjeri')
my_graph.add_edges('Muthiripparamba', 'Pullara')
my_graph.add_edges('Pullara', 'Manjeri')
my_graph.print_graph()
# my_graph.remove_edges('C', 'B')
# my_graph.print_graph()
print('-----------------------------------')
print(my_graph.graph_bfs('Muthiripparamba'))
print('-----------------------------------')
print(my_graph.graph_dfs('Manjeri'))
print('-----------------------------------')
print(my_graph.shortest_path('Muthiripparamba', 'Manjeri'))