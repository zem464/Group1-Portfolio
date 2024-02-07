import heapq

class Vertex:
    def __init__(self, node: str):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent]) 

    def add_neighbor(self, neighbor: 'Vertex', distance: float = 0): 
        self.adjacent[neighbor] = distance

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_distance(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        else:
            print(f"Vertex {node} not found.")
            return None

    def add_edge(self, frm, to, distance=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], distance)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], distance)

    def get_vertices(self):
        return self.vert_dict.keys()

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vert_dict.values()}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in current_vertex.adjacent.items():
                distance = current_distance + float(weight)
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    
    def total_distance(self, path):
        total_distance = 0
        for current_vertex, next_vertex in zip(path, path[1:]):
            total_distance += self.vert_dict[current_vertex].get_distance(self.vert_dict[next_vertex])

        return total_distance


    
    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.vert_dict:
            return []
        paths = []
        for vertex in self.vert_dict[start].adjacent.keys():
            if vertex.get_id() not in path:
                new_paths = self.find_all_paths(vertex.get_id(), end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def alternate_routes(self, start, end):
        all_paths = self.find_all_paths(start, end)
        alternate_routes = []

        for path in all_paths:
            total_distance = self.total_distance(path)
            alternate_routes.append((path, total_distance))

        return alternate_routes

    def shortest_path(self, start, end):
        distances = self.dijkstra(self.vert_dict[start])
        path = [end]
        current_vertex = self.vert_dict[end]

        while current_vertex != self.vert_dict[start]:
            next_vertex = min(current_vertex.adjacent.keys(), key=lambda x: distances[x])
            path.append(next_vertex.get_id())
            current_vertex = next_vertex

        return path[::-1]
    
    @staticmethod
    def print_shortest_route(all_paths):
        if not all_paths:
            print("No routes available.")
            return
        
        shortest_route = min(all_paths, key=lambda x: x[1])
        return shortest_route[0]
        
    @staticmethod
    def print_shortest_route_distance(all_paths):
        if not all_paths:
            print("No routes available.")
            return
        shortest_route = min(all_paths, key=lambda x: x[1])
        return shortest_route[1]