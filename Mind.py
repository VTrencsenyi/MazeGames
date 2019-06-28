from Strategy import Strategy
from Action import Action
import random
from operator import itemgetter

class Mind:
    def __init__(self, owner, strategy=Strategy.Random):
        self.strategy = strategy  # an integer denoting the corresponding strategy, 0 is random
        self.owner = owner

    def policy(self):
        node = self.owner
        action_set = []  # the list of actions we can do based on percept and rules
        p = node.percept
        up = None
        right = None
        down = None
        left = None
        # compose list of available actions
        if p.north == 0:
            up = node.env.table[node.y][node.x][0]
            action_set.append((Action.go_north, up))
        if p.east == 0:
            # action_set.append(Action.go_east)
            right = node.env.table[node.y][node.x][1]
            action_set.append((Action.go_east, right))
        if p.south == 0:
            # action_set.append(Action.go_south)
            down = node.env.table[node.y][node.x][2]
            action_set.append((Action.go_south, down))
        if p.west == 0:
            # action_set.append(Action.go_west)
            left = node.env.table[node.y][node.x][3]
            action_set.append((Action.go_west, left))

        # use strategy to decide which action to take
        if self.strategy.value == 0:
            r = random.choice(action_set)
            return r[0]
        elif self.strategy.value == 1:
            move = max(action_set, key=itemgetter(1))
            print(move)
            return move[0]





