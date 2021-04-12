from constants import MAX_HOPS, GOAL_STATE, MAX_LEN


class Node:
    # Initialize the class
    def __init__(self, tile_value="", parent=None, g=0, h=0, f=0):
        self.tile_value = tile_value
        self.parent = parent
        self.g = g  # Distance to start node
        self.h = h  # Distance to goal node
        self.f = f  # Total cost

    def __repr__(self):
        return "({} {} {} {})".format(self.tile_value, self.g, self.h, self.f)

    @staticmethod
    def heuristic(node):
        misplaced = 0
        tile_value = node.tile_value.replace("_", "")
        for i in range(MAX_LEN - 1):
            if tile_value[i] != GOAL_STATE[i]:
                misplaced += 1
        return misplaced

    def find_neighbors_graph(self, frontier, explored_st, search_type):

        # print("Exploring", self.tile_value)
        pos = self.tile_value.find("_")
        curr_node = -1
        curr_pos = pos
        child_nodes = []

        """ Initialize child nodes """
        for _ in range(6):
            child_nodes.append(
                Node(self.tile_value, self.parent, self.g, self.h, self.f)
            )

        curr_pos_start = curr_pos - MAX_HOPS
        curr_pos_end = pos + MAX_HOPS + 1

        """ Explore the 6 possible children """
        for curr_pos in range(curr_pos_start, curr_pos_end, 1):
            exp_found = 0
            frontier_found = 0

            # print(curr_pos)

            """ Main If loop """
            if curr_pos != pos and (curr_pos >= 0 and curr_pos <= 6):
                curr_node += 1
                child_node = child_nodes[curr_node]

                child_node.tile_value = list(child_node.tile_value)
                """ Swap tiles tp get the child states """
                (
                    child_node.tile_value[curr_pos],
                    child_node.tile_value[pos],
                ) = (
                    child_node.tile_value[pos],
                    child_node.tile_value[curr_pos],
                )

                child_node.tile_value = "".join(child_node.tile_value)

                # print(child_nodes)

                child_node.h = Node.heuristic(child_node)
                child_node.g += abs(pos - curr_pos)
                child_node.f = child_node.g + child_node.h

                """ Loop through explored and frontier """
                for i in range(len(explored_st)):
                    if explored_st[i].tile_value == child_node.tile_value:
                        exp_found = 1

                for i in range(frontier.qsize()):
                    if frontier.atIdx(i).tile_value == child_node.tile_value:
                        frontier_found = 1

                if not exp_found and not frontier_found:
                    # print("Pushing", child_node)
                    child_node.parent = self
                    frontier.push(child_node, search_type)
                    # frontier.printNodes()

                    # EXP_INDX += 1

    def find_neighbors_graph_mod(self, frontier, explored_st, search_type):

        # print("Exploring", self.tile_value)
        pos = self.tile_value.find("_")
        curr_node = -1
        curr_pos = pos
        child_nodes = []

        """ Initialize child nodes """
        for _ in range(6):
            child_nodes.append(
                Node(self.tile_value, self.parent, self.g, self.h, self.f)
            )

        curr_pos_start = curr_pos - MAX_HOPS
        curr_pos_end = pos + MAX_HOPS + 1

        """ Explore the 6 possible children """
        for curr_pos in range(curr_pos_start, curr_pos_end, 1):
            exp_found = 0
            frontier_found = 0

            # print(curr_pos)

            """ Main If loop """
            if curr_pos != pos and (curr_pos >= 0 and curr_pos <= 6):
                curr_node += 1
                child_node = child_nodes[curr_node]

                child_node.tile_value = list(child_node.tile_value)
                """ Swap tiles tp get the child states """
                (
                    child_node.tile_value[curr_pos],
                    child_node.tile_value[pos],
                ) = (
                    child_node.tile_value[pos],
                    child_node.tile_value[curr_pos],
                )

                child_node.tile_value = "".join(child_node.tile_value)

                # print(child_nodes)

                child_node.h = Node.heuristic(child_node)
                child_node.g += abs(pos - curr_pos)
                child_node.f = child_node.g + child_node.h

                """ Loop through explored and frontier """
                for i in range(len(explored_st)):
                    if explored_st[i].tile_value == child_node.tile_value:
                        exp_found = 1

                for i in range(frontier.qsize()):
                    if frontier.atIdx(i).tile_value == child_node.tile_value:
                        frontier_found = 1

                if not exp_found and not frontier_found:
                    # print("Pushing", child_node)
                    child_node.parent = self
                    frontier.push(child_node, search_type)
                    # frontier.printNodes()

                    # EXP_INDX += 1

                elif frontier_found:
                    for i in range(frontier.qsize()):
                        if (
                            frontier.atIdx(i).tile_value
                            == child_node.tile_value
                            and frontier.atIdx(i).f > child_node.f
                        ):
                            child_node.parent = self
                            frontier.deleteIdx(i)
                            frontier.push(child_node, search_type)
                            # print("Pushing", child_node)
                            # frontier.printNodes()

    def printPredecessors(self, search_type):
        curr_node = self
        path = []
        i = 0
        while curr_node is not None:
            path.append(curr_node)
            curr_node = curr_node.parent

        for i in path[::-1]:
            if i != path[0]:
                if search_type == 1:
                    print("({} | {}) ->".format(i.tile_value, i.g), end="")
                elif search_type == 2:
                    print("({} | {}) ->".format(i.tile_value, i.f), end="")
            else:
                if search_type == 1:
                    print("({} | {})\n".format(i.tile_value, i.g))
                elif search_type == 2:
                    print("({} | {}) \n".format(i.tile_value, i.h))
