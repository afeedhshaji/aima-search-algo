class PriorityQueue:
    def __init__(self):
        self.queue = list()
        # if you want you can set a maximum size for the queue

    def printNodes(self):
        print("Frontier Nodes :", end=" ")
        for i in range(len(self.queue)):
            print(self.queue[i], end=" ")
        print("\n")

    def qsize(self):
        return len(self.queue)

    def is_empty(self):
        if self.qsize() == 0:
            return True
        else:
            return False

    def priority(self, node, search_type):
        if search_type == 1:
            return node.g
        if search_type == 2:
            return node.h

    def atIdx(self, i):
        return self.queue[i]

    def deleteIdx(self, i):
        return self.queue.pop(i)

    def push(self, node, search_type):
        if self.qsize() == 0:
            self.queue.append(node)
        else:
            for x in range(0, self.qsize()):
                # if the priority of new node is greater
                if self.priority(node, search_type) >= self.priority(
                    self.queue[x], search_type
                ):
                    # if we have traversed the complete queue
                    if x == (self.qsize() - 1):
                        # add new node at the end
                        self.queue.insert(x + 1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)
                    return True

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]
