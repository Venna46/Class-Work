from typing import Hashable, List, Set

class Graph:
    def __init__(self, directed: bool = False) -> None:
        self.directed = directed
        self.adj_list: dict[Hashable, set] = {}


    def insert(self):
        pass

    def __repr__(self) -> str:
        graph_str = ""

        for node, neighbours in self.adj_list.items():
           graph_str += f"{node} -> {neighbours} \n"

        return  graph_str

    def get_nodes(self) -> list:
        return list(self.adj_list.keys())


    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())


    def adj_matrix(self):
        nodes = self.get_nodes()

        index = {node: i for i, node in enumerate(nodes)}
        size = len(nodes)
        matrix = [[0 for _ in range(size)] for _ in range (size)]
        for from_node, neighbours in self.adj_list.items():
            for to_node in neighbours:
                if isinstance(to_node, tuple):
                    to, weight = to_node
                    matrix[index[from_node]][index[to]] = weight
                else:
                    matrix[index[from_node]][index[to_node]] = 1
        return matrix


    def add_node(self, node) -> None:
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already created")



    def add_edge(self, from_node, to_node, weight=None) ->None:
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)

        else:
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def depth_first_search(self, start):
        visited, stack, order = set(), [start], []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for nb in reversed(list(self.obtain_neighbours(node))):
                    nb = nb[0] if isinstance(nb, tuple) else nb
                    if nb not in visited:
                        stack.append(nb)
        return order

    def breadth_first_search(self, start):
        visited, queue, order = set(), [start], []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                for nb in self.obtain_neighbours(node):
                    nb = nb[0] if isinstance(nb, tuple) else nb
                    if nb not in visited and nb not in queue:
                        queue.append(nb)
        return order


if __name__ == '__main__':
    g = Graph(directed=True)
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 24)
    g.add_edge("B", "D")

    print("Adjacency list:")
    print(g)
    print("\nDFS from A: ", g.depth_first_search("A"))
    print("BFS from A: ", g.breadth_first_search("A"))
    print("\nAdjacency matrix:")
    for row in g.adj_matrix():
        print(row)



