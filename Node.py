import threading
from Percept import Percept
from Mind import Mind
from Strategy import Strategy
from Action import Action
from Request import Request
from State import State
import networkx as nx


class Node(threading.Thread):
    # The class Node represent an active agent in the system.
    def __init__(self, node_id, goal, env=None, master=None, start_x=0, start_y=0):
        super(Node, self).__init__()
        self.node_id = node_id
        self.goal = goal  # tuple(y,x)
        self.x = start_x
        self.y = start_y
        self.env = env
        self.master = master
        # self.inbox = []
        # self.terminate = 0  # signal 1 terminates node
        self.percept = None  # percept= north,east,south,west
        self.action = None
        self.mind = Mind(self, Strategy.LookUpTab)
        self.taken_turn = False  # did I move already?
        # this is the current reward, based on how far away we are from target
        self.score = None
        # self.table = [[[0, 0, 0, 0] for j in range(5)] for k in range(5)]  # action represented as [N, E, S, W]
        self.states = []

    def perceive(self):
        if self.states:
            last_state = self.states[-1]
            if last_state.score < self.score:  # we got closer
                reward = 1
            else:
                reward = -1  # we got further

            self.update_table(last_state, reward)

        cell = self.env.get_cell(self.y, self.x)
        self.percept = Percept(cell.north, cell.east, cell.south, cell.west)
        self.states.append(State(self.y, self.x, self.score))

    # Update the table for the previous cell with the previous move, and the current cell with the opposite move
    def update_table(self, last_state, reward):
        if last_state.y > self.y:  # we moved up
            self.env.update_table(last_state.y, last_state.x, 0, reward)
            self.env.update_table(self.y, self.x, 2, -reward)
            # self.table[last_state.y][last_state.x][0] = reward
            # self.table[self.y][self.x][2] = -reward
        elif last_state.y < self.y:  # we moved down
            self.env.update_table(last_state.y, last_state.x, 2, reward)
            self.env.update_table(self.y, self.x, 0, -reward)
            # self.table[last_state.y][last_state.x][2] = reward
            # self.table[self.y][self.x][0] = -reward
        elif last_state.x < self.x:  # we moved right
            self.env.update_table(last_state.y, last_state.x, 1, reward)
            self.env.update_table(self.y, self.x, 3, -reward)
            # self.table[last_state.y][last_state.x][1] = reward
            # self.table[self.y][self.x][3] = -reward
        elif last_state.x > self.x:  # we moved left
            self.env.update_table(last_state.y, last_state.x, 3, reward)
            self.env.update_table(self.y, self.x, 1, -reward)
            # self.table[last_state.y][last_state.x][3] = reward
            # self.table[self.y][self.x][1] = -reward

    def decide(self):
        self.action = self.mind.policy()

    def act(self):
        if self.action.value == 1:
            self.move_up()
        elif self.action.value == 2:
            self.move_right()
        elif self.action.value == 3:
            self.move_down()
        elif self.action.value == 4:
            self.move_left()
        elif self.action.value == 0:
            self.wait()
        else:
            print("Error: Not an existing move!")

    def move_up(self):
        self.master.requests.append(Request(self, Action.go_north))

    def move_down(self):
        self.master.requests.append(Request(self, Action.go_south))

    def move_left(self):
        self.master.requests.append(Request(self, Action.go_west))

    def move_right(self):
        self.master.requests.append(Request(self, Action.go_east))

    def wait(self):
        self.master.requests.append(Request(self, Action.wait))

    def check_msg(self):
        if self.inbox:
            msg = self.inbox.pop(0)
            print(msg)

    def evolve(self):

        while self.taken_turn:
            fg = 0
            #print(self.node_id, " is waiting")
        self.taken_turn = True
        self.perceive()
        print("Agent ", self.node_id, "(", self.y, ",", self.x, ") is ", -self.score, "steps away from" ,
              self.goal)
        self.decide()
        print("_____")
        self.act()

    def run(self):
        self.score = -(len(nx.shortest_path(self.env.graph, self.master.grid[self.y][self.x],
                               self.master.grid[self.goal[0]][self.goal[1]])) - 1)
        i = 0
        #while self.terminate == 0:
        while True:
            i += 1
            print(i)
            self.evolve()
            if self.y == self.goal[0] and self.x == self.goal[1]:
                print("agent ", self.node_id, "got out in ", i-1, "steps.")
                break
