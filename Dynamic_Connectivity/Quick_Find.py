# This Module contains the Quick Find Data Structure and Algorithm for solving the Dynamic Connectivity Problem

class Quick_Find():
    """ Quick-Find implementation using a List to solve the dynamic connectivity problem.

    Note that the index's in the list will represent that nodes vertex number and the value stored at that index
    will represent that nodes group.
    """

    def __init__(self, N):
        """ Initialize the list as every node is in its own group. """
        self.groupings = [i for i in range(N)]

    def connected(self, p: int, q: int) -> bool:
        """ Returns True if two nodes are in the same group, else False """
        return self.groupings[p] == self.groupings[q]

    def union(self, p: int, q: int):
        """ Moves every node in group p to group q """
        p_group = self.groupings[p]
        q_group = self.groupings[q]
        for index, group in enumerate(self.groupings):
            if group == p_group:
                self.groupings[index] = q_group

