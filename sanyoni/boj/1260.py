import sys
import collections


class GraphNode:
    def __init__(self, index):
        self.index = index
        self.is_visited = False
        self.connected_nodes = []

    def __lt__(self, other):
        return self.index < other.index

    def connect_node(self, other_node):
        if other_node in self.connected_nodes:
            return

        self.connected_nodes.append(other_node)

    def set_visited(self, value):
        self.is_visited = value

    def dfs(self):
        if self.is_visited == True:
            return

        sys.stdout.write(str(self.index) + " ")

        self.is_visited = True
        self.connected_nodes.sort()
        for node in self.connected_nodes:
            node.dfs()

    def bfs(self, waiting_queue):
        if self.is_visited == True:
            return

        sys.stdout.write(str(self.index) + " ")

        self.is_visited = True
        self.connected_nodes.sort()
        for node in self.connected_nodes:
            if node.is_visited == True:
                continue

            waiting_queue.append(node)


class Graph:
    def __init__(self, nodes_count, start_node_index):
        self.nodes = []
        for i in range(nodes_count):
            self.nodes.append(GraphNode(i + 1))

        self.start_node_index = start_node_index

    def connect_node(self, start_node_index, from_node_index):
        start_node = self.nodes[start_node_index]
        from_node = self.nodes[from_node_index]
        start_node.connect_node(from_node)
        from_node.connect_node(start_node)

    # 모든 노드의 visited 플래그를 초기화합니다
    def clear_all_node_visited(self):
        for node in self.nodes:
            node.set_visited(False)

    # DFS를 실시합니다
    def do_dfs(self):
        start_node = self.nodes[self.start_node_index]

        start_node.dfs()

    # BFS를 실시합니다
    def do_bfs(self):
        start_node = self.nodes[self.start_node_index]

        next_visit_nodes_waiting_queue = collections.deque()
        next_visit_nodes_waiting_queue.append(start_node)

        while len(next_visit_nodes_waiting_queue) > 0:
            next_node = next_visit_nodes_waiting_queue.popleft()

            next_node.bfs(next_visit_nodes_waiting_queue)


# 입력받고, 그래프를 초기화합니다
nodes_count, vertex_count, start_node_index = sys.stdin.readline().rstrip().split()
nodes_count = int(nodes_count)
vertex_count = int(vertex_count)
start_node_index = int(start_node_index) - 1

graph = Graph(nodes_count, start_node_index)

for i in range(vertex_count):
    node1_index, node2_index = sys.stdin.readline().rstrip().split()
    node1_index = int(node1_index) - 1
    node2_index = int(node2_index) - 1

    graph.connect_node(node1_index, node2_index)

# DFS와 BFS를 실시합니다
graph.do_dfs()
sys.stdout.write("\n")

graph.clear_all_node_visited()

graph.do_bfs()
sys.stdout.write("\n")