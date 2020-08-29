# This Module contains the Quick Union Data Structure and Algorithm for solving the Dynamic Connectivity Problem

class Quick_Union():
    """ Weighted Quick Union with Path Compression implementation using a list as the underlying data structure

    Note that self.tree is a List but actually represents a tree data structure where each value in the array tells
    us who that nodes parent is. self.size is used for the weighted union so that we can always combine the root of the
    smaller tree with the root of the larger tree. N + Mlg*(N) running time for N objects and M union-find operations (almost linear).
    10^9 union and find with 10^9 objects using WQUPC (Weighted Quick-Union with Path Compression) reduces the time
    from 30 years to 6 seconds!
    """

    def __init__(self, n: int):
        self.tree = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def _root(self, node: int) -> int:
        """ finds and returns the root for this node """
        while self.tree[node] != node:
            self.tree[node] = self.tree[self.tree[node]]    # Path Compression
            node = self.tree[node]
        return node

    def connected(self, p: int, q: int) -> bool:
        """ Returns whether or not these two nodes are connected """
        return self._root(p) == self._root(q)

    def union(self, p: int, q: int):
        """ Takes two nodes and creates a union of their two trees (by root) with the smallest tree pointing to
        root of the tallest tree.
         """
        p_root = self._root(p)
        q_root = self._root(q)
        if p_root == q_root:
            return

        if self.size[p_root] < self.size[q_root]:
            self.tree[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.tree[q_root] = p_root
            self.size[p_root] += self.size[q_root]
