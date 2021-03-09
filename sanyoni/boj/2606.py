# 감염된 컴퓨터의 총 개수입니다
infected_nodes_count = 0

# 컴퓨터 객체입니다
# 이 컴퓨터는 이웃된 컴퓨터, 그리고 감염 여부를 저장합니다
class GraphNode:
    def __init__(self, number):
        self.number = number
        self.neighbour_nodes = []
        self.is_infected = False

    def __str__(self):
        return str(self.number)

    # 이웃한 컴퓨터를 등록합니다
    # 추가하려는 대상 컴퓨터 역시도 나를 이웃한 컴퓨터로 등록합니다
    def connect_node(self, other):
        if self.neighbour_nodes.__contains__(other):
            return

        self.neighbour_nodes.append(other)
        other.connect_node(self)

    # 이 컴퓨터를 감염시킵니다
    # 이 컴퓨터가 감염되면 이웃한 컴퓨터 역시 전부 감염되고, 이는 계속 재귀되어 호출됩니다
    def make_it_infected(self):
        global infected_nodes_count

        if self.is_infected is True:
            return

        self.is_infected = True
        infected_nodes_count += 1

        for node in self.neighbour_nodes:
            node.make_it_infected()


computers_count = int(input())
connections_count = int(input())

graphnode_list = [None] * computers_count
for i in range(0, computers_count):
    graphnode_list[i] = GraphNode(i + 1)

for i in range(0, connections_count):
    row_splitted = input().split()
    from_node_number = int(row_splitted[0])
    to_node_number = int(row_splitted[1])

    # 서로 이웃한 컴퓨터로 등록합니다
    from_node = graphnode_list[from_node_number - 1]
    to_node = graphnode_list[to_node_number - 1]

    from_node.connect_node(to_node)

# 1번 컴퓨터를 감염시킵니다
graphnode_list[0].make_it_infected()

# 1번 컴퓨터로 통해 바이러스에 걸린 컴퓨터 수를 구하기 때문에
# 감염된 전체 컴퓨터 개수에서 1번 컴퓨터 한 개를 제외한 값을 출력해야 합니다
print(infected_nodes_count - 1)