from collections import deque
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
        
    def remove_edges(self, v1, v2):
        if v1 in self.adj_list.key() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False
        
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
        
        
    def all_path(self, start, destination, path=None):
        if path is None:
            path = [start]
        if start == destination:
            return [path]
        paths = []
        for neighbor in self.adj_list[start]:
            if neighbor not in path:
                paths.extend(self.all_path(neighbor, destination, path + [neighbor]))
                
        return paths
        
my_graph = Graph()
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
print('all paths: ')
print(my_graph.all_path('Muthiripparamba', 'Manjeri'))