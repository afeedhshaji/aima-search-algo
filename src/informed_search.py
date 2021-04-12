from constants import LAST_4_CH_GOAL_ST
from .node import Node
from .priorityq import PriorityQueue
from .utils import misplaced_tiles


class InformedSearch:
    def __init__(self, input_conf):
        self.input_conf = input_conf
        self.exp_index = 0

    def greedy_best_first(self):
        num_misplaced_tiles = misplaced_tiles(self.input_conf)
        root_node = Node(
            self.input_conf, None, 0, num_misplaced_tiles, num_misplaced_tiles
        )

        frontier = PriorityQueue()
        explored_st = []

        print(
            "\nNode is represented in the following form (Tile Value | h(n)) ::\n"
        )

        """ Push the root node to the frontier PQ """
        frontier.push(root_node, 2)

        while not frontier.is_empty():

            curr_node = frontier.top()

            """ Goal State """
            if curr_node.tile_value[3:] in LAST_4_CH_GOAL_ST:
                print("Goal state found", curr_node.tile_value)
                print("Cost : ", curr_node.g)

                print("Path : ", end="")
                curr_node.printPredecessors(2)
                print("\n")

            explored_st.append(curr_node)
            frontier.pop()

            """ Explore neighbors """
            # print("\n\nExploring : ", curr_node)
            curr_node.find_neighbors_graph(frontier, explored_st, 2)

        return
