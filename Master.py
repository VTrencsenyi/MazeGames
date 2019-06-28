import threading
import random
import networkx as nx


class Master(threading.Thread):
    # The master node handles node movement requests
    def __init__(self, env, nodes, grid):
        super(Master, self).__init__()
        self.node_id = 0  # Master node is always with id 0
        self.env = env
        self.grid = grid  # all cells
        self.nodes = nodes
        self.requests = []
        # self.terminate = 0  # signal 1 terminates node

    def validate_moves(self):
        while len(self.requests) != len(self.nodes):
            # wait to receive requests from everyone, thus eliminating racing conditions
            asd = 1

        # Randomize order of requests, to decrease racing conditions
        random.shuffle(self.requests)
        while self.requests:
            req = self.requests.pop()
            node_loc = self.grid[req.owner.y][req.owner.x]

            if req.action.value == 1:
                if node_loc.north == 0:  # There is no wall in the direction node wants to go
                    new_loc = self.grid[req.owner.y-1][req.owner.x]
                    if new_loc.occupied is None:  # No one occupies target cell
                        req.owner.y = req.owner.y - 1
                        #print("Master validate -move up- for", req.owner.node_id)
                else:
                    print("Move is invalid!", req.owner.node_id)

            elif req.action.value == 2:
                if node_loc.east == 0:  # There is no wall in the direction node wants to go
                    new_loc = self.grid[req.owner.y][req.owner.x+1]
                    if new_loc.occupied is None:  # No one occupies target cell
                        req.owner.x = req.owner.x + 1
                        #print("Master validate -move right- for", req.owner.node_id)
                else:
                    print("Move is invalid!", req.owner.node_id)

            elif req.action.value == 3:
                if node_loc.south == 0:  # There is no wall in the direction node wants to go
                    new_loc = self.grid[req.owner.y+1][req.owner.x]
                    if new_loc.occupied is None:  # No one occupies target cell
                        req.owner.y = req.owner.y + 1
                        #print("Master validate -move down- for", req.owner.node_id)
                else:
                    print("Move is invalid!", req.owner.node_id)

            elif req.action.value == 4:
                if node_loc.west == 0:  # There is no wall in the direction node wants to go
                    new_loc = self.grid[req.owner.y][req.owner.x-1]
                    if new_loc.occupied is None:  # No one occupies target cell
                        req.owner.x = req.owner.x - 1
                        #print("Master validate -move left- for", req.owner.node_id)
                else:
                    print("Move is invalid!", req.owner.node_id)

        # Reset node flags to generate new turn and apply rewards
        for i in range(len(self.nodes)):
            node = self.nodes[i]
            node.score = -(len(nx.shortest_path(self.env.graph, self.grid[node.y][node.x],
                                                self.grid[node.goal[0]][node.goal[1]]))-1)
            node.taken_turn = False

    def run(self):
        i = 0
        while True:
            self.validate_moves()
            i = i+1
            node = self.nodes[0]
            if node.y == node.goal[0] and node.x == node.goal[1]:
                break


