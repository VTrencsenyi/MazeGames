from Node import Node
from Environment import Environment
from graphics import *
from Cell import Cell
from Maze import Maze
import time
import networkx as nx


def construct_maze():

    maze = [[None for x in range(5)] for y in range(5)]
    maze[0][0] = Cell(0, 0, 1, 0, 0, 1)
    maze[0][1] = Cell(0, 1, 1, 0, 0, 0)
    maze[0][2] = Cell(0, 2, 1, 0, 1, 0)
    maze[0][3] = Cell(0, 3, 1, 1, 0, 0)
    maze[0][4] = Cell(0, 4, 1, 1, 0, 1)

    maze[1][0] = Cell(1, 0, 0, 1, 0, 1)
    maze[1][1] = Cell(1, 1, 0, 0, 1, 1)
    maze[1][2] = Cell(1, 2, 1, 0, 0, 0)
    maze[1][3] = Cell(1, 3, 0, 0, 0, 0)
    maze[1][4] = Cell(1, 4, 0, 1, 1, 0)

    maze[2][0] = Cell(2, 0, 0, 0, 0, 1)
    maze[2][1] = Cell(2, 1, 1, 0, 0, 0)
    maze[2][2] = Cell(2, 2, 0, 1, 1, 0)
    maze[2][3] = Cell(2, 3, 0, 0, 0, 1)
    maze[2][4] = Cell(2, 4, 1, 1, 0, 0)

    maze[3][0] = Cell(3, 0, 0, 1, 0, 1)
    maze[3][1] = Cell(3, 1, 0, 0, 1, 1)
    maze[3][2] = Cell(3, 2, 1, 0, 0, 0)
    maze[3][3] = Cell(3, 3, 0, 1, 0, 0)
    maze[3][4] = Cell(3, 4, 0, 1, 0, 1)

    maze[4][0] = Cell(4, 0, 0, 0, 1, 1)
    maze[4][1] = Cell(4, 1, 1, 0, 1, 0)
    maze[4][2] = Cell(4, 2, 0, 0, 1, 0)
    maze[4][3] = Cell(4, 3, 0, 1, 1, 0)
    maze[4][4] = Cell(4, 4, 0, 1, 1, 1)

    return maze


def add_neighbours(cells):
    for y in range(5):
        for x in range(5):
            c = cells[y][x]
            if c.north == 0:
                c.neighbours.append(cells[y-1][x])
            if c.south == 0:
                c.neighbours.append(cells[y+1][x])
            if c.east == 0:
                c.neighbours.append(cells[y][x+1])
            if c.west == 0:
                c.neighbours.append(cells[y][x-1])


def construct_graph(grid):
    graph = nx.Graph()
    for y in range(5):
        for x in range(5):
            cell = grid[y][x]
            for n in cell.neighbours:
                graph.add_edge(cell, n)
    return graph


if __name__ == '__main__':

    nodes = []
    nodes.append(Node(node_id=1, goal=(0, 4), start_y=2, start_x=0))
    #nodes.append(Node(node_id=2, start_x=0, start_y=4))

    grid = construct_maze()  # list of cells
    add_neighbours(grid)
    graph = construct_graph(grid)

    env = Environment(nodes, grid, graph)  # the environment creates the Master

    #n_cells = 5
    #m = Maze(grid, n_cells)

    # lines = m.build_maze()
    # window = GraphWin("Maze", 50 * n_cells + 10, 50 * n_cells + 10)
    # for j in range(5):
    #     for l in lines:
    #         window.addItem(l)
    #     for i in range(len(nodes)):
    #         n = nodes[i]
    #         x = 50*n.location_history[j][0]+25
    #         y = 50 * n.location_history[j][1]+25
    #         c = Circle(Point(x, y), 5)
    #         window.addItem(c)
    #     window.redraw()
    #     window.getKey()
    #     window.items = []






