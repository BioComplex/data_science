from itertools import cycle
import matplotlib.pyplot as plt


class PlotBase(object):


    markers = ['D', 'o', 'x','s', '^', 'd', 'h', '+', '*', ',', '.', '1', 'p', '3', '2', '4', 'H', 'v', '8',
               '<', '>']
    colors = ['g', 'y', 'r', 'b', 'black']

    @staticmethod
    def configure_ax(ax, par_plot):
        PlotBase.set_par(par_plot, 'x_label', ax.set_xlabel)
        PlotBase.set_par(par_plot, 'y_label', ax.set_ylabel)

        # par_grid = PlotBase.get_par(par_plot, 'grid')
        # if par_grid and par_grid == True:
        #     ax.grid(zorder=1)

        par_titles = PlotBase.get_par(par_plot, 'title')
        par_titlesize = PlotBase.get_par(par_plot, 'title.size', default=16)

        if par_titles:
            if type(par_titles) is cycle:
                ax.set_title(next(par_titles), fontsize=par_titlesize)
            else:
                ax.set_title(par_titles, fontsize=par_titlesize)

        par_legend = PlotBase.get_par(par_plot, 'legend', transform=cycle)
        if par_legend:
            par_loc = PlotBase.get_par(par_plot, 'legend.loc', default=4)
            par_fontsize = PlotBase.get_par(par_plot, 'legend.fontsize', default=8)
            ax.legend(loc=par_loc, fontsize=par_fontsize)

    @staticmethod
    def set_par(par_plot, name, func, default=None, transform=None):
        par = PlotBase.get_par(par_plot, name, default, transform)
        if par:
            func(par)

    @staticmethod
    def get_par(par_plot, name, default=None, transform=None):
        param = None
        if par_plot.keys().__contains__(name):
            param = par_plot[name]
        elif not par_plot.keys().__contains__(name) and default is not None:
            param = default
        if param and transform:
            param = transform(param)
        return param

    @staticmethod
    def configure_fig(fig, par_plot):
        # Figure params

        par_figtitle = PlotBase.get_par(par_plot, 'fig.suptitle')
        par_figtitle_fontsize = PlotBase.get_par(par_plot, 'fig.suptitle.fontsize', 14)
        par_figtitle_fontweight = PlotBase.get_par(par_plot, 'fig.suptitle.fontweight', 'normal')
        if par_figtitle:
            fig.suptitle(par_figtitle, fontsize=par_figtitle_fontsize)

        par_figtight_layout = PlotBase.get_par(par_plot, 'fig.tight_layout')
        par_figrect = PlotBase.get_par(par_plot, 'fig.tight_layout.rect')
        par_figwpad = PlotBase.get_par(par_plot, 'fig.tight_layout.w_pad')
        par_fighpad = PlotBase.get_par(par_plot, 'fig.tight_layout.h_pad')
        par_figpad = PlotBase.get_par(par_plot, 'fig.tight_layout.pad', 0)
        # TODO parameterize

        if par_figtight_layout:
            # plt.tight_layout(rect=par_figrect, w_pad=par_figwpad, h_pad=par_fighpad,
            #                  pad=par_figpad)
            fig.tight_layout(rect=par_figrect, w_pad=par_figwpad, h_pad=par_fighpad,
                             pad=par_figpad)

        par_figsize = PlotBase.get_par(par_plot, 'fig.figsize', (5, 5))
        fig.set_size_inches(par_figsize)
