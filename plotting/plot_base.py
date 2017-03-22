from itertools import cycle
import matplotlib.pyplot as plt


class PlotBase(object):


    markers = ['D', 's', 'x', '^', 'd', 'h', '+', '*', ',', 'o', '.', '1', 'p', '3', '2', '4', 'H', 'v', '8',
               '<', '>']
    colors = ['g', 'y', 'r', 'b', 'black']

    markercycler = cycle(markers)
    colorcycler = cycle(colors)


    @staticmethod
    def configure_ax(self, ax, grid_alpha=1):
        ax.grid(alpha=grid_alpha)