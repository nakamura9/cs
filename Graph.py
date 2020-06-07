import random
import copy

class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """Creates a new graph vs is a list of vertices and es is a list of edges"""
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """add vertex to graph"""
        print(v)
        self[v]= {}

    def add_edge(self, e):
        """
        Add edge beween two vertices in both directions.
        If an edge exists between the vertices the new edge
        replaces it.
        """
        v,w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v,w):
        print("Get edge")
        if self.get(v, None):
            if self[v].get(w, None):
                return self[v][w]

        return None

    def remove_edge(self, e):
        del self[e[0]][e[1]]
        del self[e[1]][e[0]]

    def vertices(self):
        print("all vertices")
        return self.keys()

    def edges(self):
        print("all edges")
        edges = set()
        for v in self.keys():
            for w in self[v].keys():
                edges.add(self[v][w])

        return list(edges)

    def out_vertices(self, v):
        print(" all out vertices for %s" % repr(v))
        return self[v].keys()

    def out_edges(self, v):
        # print(" all out edges for %s" % repr(v))
        return self[v].values()

    def add_all_edges(self):
        edges = []
        for v in self.keys():
            for w in self.keys():
                e = Edge(v,w)
                if not e in edges and v.label != w.label:
                    edges.append(e)                  
                    self.add_edge(e)
                    
    def add_regular_edges(self, degree=4):
        unprocessed = list(self.keys())
        
        for v in unprocessed:
            options = copy.copy(unprocessed)
          
            try:
                options.remove(v)
            except ValueError:
                return
            v_edges = 0
            
            while len(self.out_edges(v)) != degree:
                v_edges = len(self.out_edges(v))
                other = random.choice(options)
                
                if len(self.out_edges(other)) == degree:
                    continue

                self.add_edge(Edge(v, other))
                options.remove(other)
                
            #unprocessed.remove(v)
            
        
class RandomGraph(Graph):
    def add_random_edges(self, p):
        edge_count = int(len(list(self.vertices())) * p)
        for v in self.vertices():
            for i in range(edge_count):
                other = list(self.vertices())
                other.remove(v)
                w = random.choice(other)
                if self[v].get(w, None) or self[w].get(v, None):
                    continue
                self.add_edge(Edge(v, w))

        
class Vertex(object):
    def __init__(self, label=''):
        self.label=label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    def __eq__(self, other):
        return self.label == other.label
    
    def __hash__(self):
        return hash(self.label)
    
    
    __str__ = __repr__


class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls,(e1,e2))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    def __eq__(self, other):
        return (self[0] == other[0] and self[1] ==other[1]) or (self[0] == other[1] and self[1] == other[0])

    __str__ = __repr__
    
def breadth_first_search(graph, start_node):
    q = [start_node]
    discovered = [start_node]
    
    
    

if __name__ == "__main__":
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')

    e = Edge(v, w)

    g = Graph([v,w,x], [e])

    # test remove edge
    f  = Edge(v, x)
    g.add_edge(f)

    g.remove_edge(f)

    # creating a fresh graph and testing all edges
    h = Graph([x,v,w])

    h.add_all_edges()

    h = RandomGraph([x,v,w])
    h.add_random_edges(0.1)
    
    
        

