from constants import GOAL_STATE, MAX_LEN, LAST_4_CH_GOAL_ST
from .node import Node
from .priorityq import PriorityQueue
from .utils import misplaced_tiles


class UninformedSearch:
    def __init__(self, input_conf):
        self.input_conf = input_conf
        self.exp_index = 0

    @staticmethod
    def misplaced_tiles(tile_value):
        misplaced = 0
        tile_value = tile_value.replace("_", "")
        for i in range(MAX_LEN - 1):
            if tile_value[i] != GOAL_STATE[i]:
                misplaced += 1

        return misplaced

    def uniform_cost(self):

        num_misplaced_tiles = misplaced_tiles(self.input_conf)
        root_node = Node(
            self.input_conf, None, 0, num_misplaced_tiles, num_misplaced_tiles
        )

        frontier = PriorityQueue()
        explored_st = []

        print("\nNodes being traversed are (Tile Value | g(n) ) ::\n")

        """ Push the root node to the frontier PQ """
        frontier.push(root_node, 1)

        while not frontier.is_empty():

            curr_node = frontier.top()

            """ Goal State """
            if curr_node.tile_value[3:] in LAST_4_CH_GOAL_ST:
                # frontier.pop()
                print("Goal state found", curr_node.tile_value)
                print("Cost : ", curr_node.g)

                print("Path : ", end="")
                curr_node.printPredecessors(1)
                print("\n")

            explored_st.append(curr_node)
            frontier.pop()

            """ Explore neighbors """
            # print("\n\nExploring : ", curr_node)
            curr_node.find_neighbors_graph(frontier, explored_st, 1)

        return
