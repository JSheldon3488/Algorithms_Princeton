""" This Module is the Week 1 Assignment for doing simulations to solve for the 'percolation probability'.

Problem Statement: Write a program to estimate the value of the percolation threshold via Monte Carlo simulation.

Examples: Given a composite systems comprised of randomly distributed insulating and metallic materials: what fraction
of the materials need to be metallic so that the composite system is an electrical conductor? Given a porous landscape
with water on the surface (or oil below), under what conditions will the water be able to drain through to the bottom
(or the oil to gush through to the surface)?

Need:
    * Random Number Generator
    * Weighted Quick Union Find that works (tests needed) #TODO: Write Test Suite
    * N by M grid of sites (List or List of List or numpy array)
    * Monte Carlo simulation function
    * Follow their provided API
    * IllegalArgumentException if open(), isOpen(), isFull() is outside prescribed range, or n < 1 in constructor
"""

class Percolation:
    """ Provided API from the assignment to solve for the percolation probability. """

    def __init__(self, n: int):
        """ Creates n-by-n grid, with all sites initially blocked. """
        if n < 1:
            raise IllegalArgumentException
        else:
            self.grid = [[0 for _ in range(n)] for _ in range(n)]
            self.n = n
            self.open_count = 0
            self.total = n**2
            self.quick_union = QuickUnionExtended(self.total)

    def valid_cell(self, row: int, col: int) -> bool:
        return 0 <= row < self.n and 0 <= col < self.n

    def open(self, row: int, col: int):
        """ Opens the site (row,col) if it is not open already and update the appropriate unions """
        if not self.valid_cell(row,col):
            raise IllegalArgumentException
        elif not self.is_open(row, col):
            self.grid[row][col] = 1
            self.open_count += 1
            # Connect all the valid nearby open sites
            # Left
            if self.valid_cell(row, col-1) and self.is_open(row, col-1):
                self.quick_union.union(p=(row * self.n + col), q=(row * self.n + col - 1))
            # Right
            if self.valid_cell(row, col+1) and self.is_open(row, col+1):
                self.quick_union.union(p=(row * self.n + col), q=(row * self.n + col + 1))
            # Up
            if self.valid_cell(row-1, col) and self.is_open(row-1, col):
                self.quick_union.union(p=(row - 1) * self.n + col, q=(row - 1) * self.n + col)
            # Down
            if self.valid_cell(row+1, col) and self.is_open(row+1, col):
                self.quick_union.union(p=(row + 1) * self.n + col, q=(row + 1) * self.n + col)

    def is_open(self, row: int, col: int):
        """ returns if the position (row,col) is open """
        return self.grid[row][col]

    def is_full(self, row: int, col: int) -> bool:
        """ Returns if the position (row,col) is full.

        Note: A full site is an open site that can be connected to an open site in the top row via a chain of neighboring open sites.
        """
        if not self.valid_cell(row, col):
            raise IllegalArgumentException
        if not self.is_open(row, col):
            return False
        return self.quick_union.root((row*self.n + col)) == self.quick_union.virtual_top

    def number_of_open_sites(self) -> int:
        """ Returns the number of open sites """
        return self.open_count

    def percolates(self) -> bool:
        """ Returns if the system percolates or not """
        return self.quick_union.tree[self.quick_union.virtual_bottom] == self.quick_union.virtual_top

    def simulation(self):
        """ Run a simulation to get the percolation probability """
        # TODO


class QuickUnionExtended:
    """ Weighted Quick Union with Path Compression implementation using a list as the underlying data structure.

    Note that this is an extended Quick_Union to help solve the percolation problem.
    """

    def __init__(self, n: int):
        self.tree = [i for i in range(n)] + [n] + [n+1]    # Index n is virtual bottom, n+1 virtual top
        self.size = [1 for i in range(n)]
        self.virtual_top = n+1
        self.virtual_bottom = n

        # Point the first sqrt(n) and last sqrt(n) items at the virtual top and bottom
        sqr_root = int(n**(1/2))
        self.tree[0:sqr_root] = [n+1]*sqr_root
        self.tree[-sqr_root:] = [n]*sqr_root

    def root(self, node: int) -> int:
        """ finds and returns the root for this node """
        while self.tree[node] != node:
            self.tree[node] = self.tree[self.tree[node]]  # Path Compression
            node = self.tree[node]
        return node

    def connected(self, p: int, q: int) -> bool:
        """ Returns whether or not these two nodes are connected """
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        """ Takes two nodes and creates a union of their two trees (by root) with the smallest tree pointing to
        root of the tallest tree.
         """
        p_root = self.root(p)
        q_root = self.root(q)
        if p_root == q_root:
            return

        # If either node points at virtual top or bottom then can connect both to top or bottom and size doesnt matter anymore.
        if p_root == self.virtual_top or q_root == self.virtual_top:
            self.tree[p_root], self.tree[q_root] = self.virtual_top, self.virtual_top

        elif p_root == self.virtual_bottom or q_root == self.virtual_bottom:
            self.tree[p_root], self.tree[q_root] = self.virtual_bottom, self.virtual_bottom

        # Neither node connects to top or bottom so union as usual
        elif self.size[p_root] < self.size[q_root]:
            self.tree[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.tree[q_root] = p_root
            self.size[p_root] += self.size[q_root]


class IllegalArgumentException(Exception):
    print("Invalid Argument!")
