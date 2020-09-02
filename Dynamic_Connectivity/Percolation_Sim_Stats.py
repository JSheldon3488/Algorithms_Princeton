""" This module contains the simulation method for performing multiple percolation simulations and presenting
a suite of statistics about the simulation results. """

from Percolation import Percolation
import numpy as np
from tqdm import tqdm
from typing import List


class PercolationStats:
    """ This class provides a driver for running a simulation and printing out detailed statistics about a specific simulation. """

    def __init__(self, row_col_size: int):
        self.size = row_col_size
        self.mean = None
        self.stddev = None
        self.ci_low = None
        self.ci_high = None

    def run(self, num_sims: int):
        """ Run a percolation simulation num_sims times and save the results in object attributes """
        results = []
        percolator = Percolation(self.size)

        for _ in tqdm(range(num_sims)):
            results.append(percolator.simulation())
            percolator.reset()

        result = np.asarray(results)
        self.mean = np.mean(results)
        self.stddev = np.std(results)
        self.ci_low = self.mean - 1.96 * self.stddev * (1 / (self.size ** (1 / 2)))
        self.ci_high = self.mean + 1.96 * self.stddev * (1 / (self.size ** (1 / 2)))

    def print_stat_summary(self):
        """ Prints out a report of the results of the simulation """
        print(f'Simulation Mean: {self.mean:.5}, Simulation Std_Dev: {self.stddev:.5}')
        print(f'95% Confidence Interval: ({self.ci_low:.5} - {self.ci_high:.5})')

    def time_sim(self, sizes: List[int]):
        # TODO: Write time simulation function with plotting
        pass


def main():
    sim = PercolationStats(row_col_size=500)
    sim.run(num_sims=100)
    sim.print_stat_summary()


if __name__ == '__main__':
    main()
