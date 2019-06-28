import threading
from Master import Master


class Environment:
    # The static environment in which the games take place and nodes interact.
    def __init__(self, nodes, grid, graph):
        self._lock = threading.Lock()
        self.nodes = nodes
        self.grid = grid
        self.table = [[[0, 0, 0, 0] for j in range(5)] for k in range(5)]  # action represented as [N, E, S, W]
        self.master = Master(self, nodes, grid)
        self.graph = graph
        self.set_node_env()
        self.start_threads()

    def get_cell(self, y, x):
        return self.grid[y][x]

    def set_node_env(self):
        for node in self.nodes:
            node.env = self
            node.master = self.master

    def start_threads(self):
        for node in self.nodes:
            node.start()
        self.master.start()

    def update_table(self, y, x, direction, value):
        with self._lock:
            self.table[y][x][direction] = value

