from itertools import cycle
import matplotlib.pyplot as plt


class PlotBase(object):


    markers = ['D', 's', 'x', '^', 'd', 'h', '+', '*', ',', 'o', '.', '1', 'p', '3', '2', '4', 'H', 'v', '8',
               '<', '>']
    colors = ['g', 'y', 'r', 'b', 'black']

    @staticmethod
    def configure_ax(ax, par_plot):
        PlotBase.get_par_plot(par_plot)
        PlotBase.set_par(ax.set_xlabel, par_plot, 'x_label')
        PlotBase.set_par(ax.set_ylabel, par_plot, 'y_label')

        # ax.set_title(par_plot['title'])
        # ax.grid(alpha=grid_alpha)

    @staticmethod
    def get_par_plot(par_plot):
        pass
        # PlotBase.__get_par__(par_plot, 'x_label', 'X')
        # PlotBase.__get_par__(par_plot, 'y_label', 'Y')
        # PlotBase.__get_par__(par_plot, 'title', 'title')

    @staticmethod
    def set_par(func, par_plot, name):
        if par_plot.keys().__contains__(name):
            func(par_plot[name])


    @staticmethod
    def __get_par__(par_plot, par, default=None):
        if not par_plot.keys().__contains__(par):
            par_plot[par] = default

    @staticmethod
    def __set_par__(par_plot, par, func):
        if par_plot.keys().__contains__(par):
            par_plot[par] = func(par_plot[par])

    @staticmethod
    def get_par(par_plot, name, default=None, transform=None):
        if not par_plot.keys().__contains__(name) and default is None:
            return None
        param = None
        if par_plot.keys().__contains__(name):
            param = par_plot[name]
        elif not par_plot.keys().__contains__(name) and default is not None:
            param = default

        if transform is not None:
            param = transform(param)

        return param
