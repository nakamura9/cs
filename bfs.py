from Graph import Graph, RandomGraph, Edge, Vertex
import time

class Q(list):
    def dequeue(self):
        return self.pop(0)

    def enqueue(self, val):
        self.append(val)


def bfs(graph, start):
    q = Q()
    discovered = [start]
    q.append(start)

    while len(q) > 0:
        v = q.dequeue()
        for w in graph.out_vertices(v):
            if not w in discovered:
                discovered.append(w)
                q.enqueue(w)

    if len(discovered) == len(list(graph.vertices())):
        print("This graph is a connected graph")
        return True

    else:
        print(f"Total number of nodes: {len(list(graph.vertices()))} \n"
                f"Number of visitable nodes: {len(discovered)}")
        return False

if __name__ == "__main__":

    vertices = [ Vertex(str(i)) for i in range(300)]
    
    p = 0.01
    histogram = {}
    while p < 0.02:
        g = RandomGraph(vs =vertices)
        for i in range(3):
            g.add_random_edges(p)
            start = time.time()
            connected = bfs(g, vertices[0])
            histogram.setdefault(p, 0)
            histogram[p] += 1 if connected else 0
        p += 0.01

    for probability, connect_count in histogram.items():
        print(f"For the probability {probability}, the connectedness count"
                f"was {connect_count}.")


    print(f"Execution time: {time.time() - start}")
    # from graphworld import GraphWorld, CircleLayout
    # layout = CircleLayout(g)
    # gw = GraphWorld()
    # gw.show_graph(g, layout)
    # gw.mainloop()
    # print(f"Execution time: {time.time() - start}")

