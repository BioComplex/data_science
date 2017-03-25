from plotting.plot_base import *
import numpy as np


class Curve(object):
    @staticmethod
    def plot_curves_subplots(dfs, par_plot=None):

        assert dfs is not None and type(dfs) is list, "df is none or not list"

        par_subplots = par_plot['subplots']
        nrows, ncols, sharex, sharey = par_subplots['nrows'], par_subplots['ncols'], par_subplots['sharex'], \
                                       par_subplots['sharey']

        fig, axs = plt.subplots(nrows=nrows, ncols=ncols, sharex=sharex, sharey=sharey)

        par_figtitle = PlotBase.get_par(par_subplots, 'fig.title')

        # par_plot['title'] = PlotBase.get_par(par_subplots, 'title', transform=cycle)

        par_titles = PlotBase.get_par(par_subplots, 'title', transform=cycle)



        axs = np.ravel(np.array(axs))
        for i in range(len(axs)):
            ax = axs[i]
            sub_dfs = dfs[i]
            ax = Curve.plot_curves(sub_dfs, par_plot, ax)

            if par_figtitle:
                fig.suptitle(par_figtitle, fontsize=30, fontweight="bold")

            if par_titles:
                ax.set_title(next(par_titles))
        # PlotBase.configure_ax(ax, par_subplots)

        # TODO parameterize
        # plt.tight_layout()




        figsize = PlotBase.get_par(par_plot, 'figsize')
        if figsize:
            fig.set_size_inches(figsize)

        plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Arial'], 'size': 12})

        return fig, axs

    @staticmethod
    def plot_curves(dfs, par_plot, ax=None):

        if ax is None:
            fig, ax = plt.subplots(1, 1)

        #Parameters
        par_linewidth = PlotBase.get_par(par_plot, 'linewidth', 2)
        par_linestyle = PlotBase.get_par(par_plot, 'linestyle', '-')
        par_alpha = PlotBase.get_par(par_plot, 'alpha', .8)
        par_color = PlotBase.get_par(par_plot, 'color', default=PlotBase.colors, transform=cycle)
        par_marker = PlotBase.get_par(par_plot, 'marker', default=PlotBase.markers, transform=cycle)
        par_legends = PlotBase.get_par(par_plot, 'legends', transform=cycle)




        for df in dfs:

            label = None
            if par_legends:
                label = next(par_legends)

            ax.plot(df['x'], df['y'],
                    linewidth=par_linewidth,
                    linestyle=par_linestyle,
                    alpha=par_alpha,
                    color=next(par_color),
                    marker=next(par_marker),
                    label=label)


            PlotBase.configure_ax(ax, par_plot)

            # TODO parameterize
            ax.grid()

        return ax


    # @staticmethod
    # def get_par_plot_subplots(par_plot):
    #     if not par_plot:
    #         par_plot = dict()
    #
    #     PlotBase.__get_par__(par_plot, 'nrows', 1)
    #     PlotBase.__get_par__(par_plot, 'ncols', 1)
    #     PlotBase.__get_par__(par_plot, 'sharey', False)
    #     PlotBase.__get_par__(par_plot, 'sharex', False)
    #
    #     PlotBase.__get_par__(par_plot, 'loc', 2)
    #     PlotBase.__get_par__(par_plot, 'linewidth', 2)
    #
    #     return par_plot


    # @staticmethod
    # def __get_par_curve(par_plot):
    #     PlotBase.__get_par__(par_plot, 'linestyle', '-')
    #     PlotBase.__get_par__(par_plot, 'alpha', .8)
    #     PlotBase.__get_par__(par_plot, 'color', cycle(PlotBase.colors))
    #     PlotBase.__get_par__(par_plot, 'marker', cycle(PlotBase.markers))
    #
    #     PlotBase.__set_par__(par_plot, 'label', cycle)


    # def test():
    #     par_plot = {
    #         'subplots': {
    #             'title': ['title 1', 'title 2'],
    #             'nrows': 2,
    #             'ncols': 1,
    #             'sharex': True,
    #             'sharey': True,
    #         },
    #
    #         'x_label': 'Community Size ($c$)',
    #         'y_label': '$P(C \leq c)$',
    #         'linewidth': 2,
    #         'loc': 4,
    #         'label': ['a', 'b']
    #
    #     }
    #     import pandas as pd
    #     curves1 = []
    #     curves1.append({'x': [1, 2, 3, 4], 'y': [4, 3, 2, 1]})
    #     curves1.append({'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4]})
    #     curves2 = []
    #     curves2.append({'x': [1, 2, 3, 4], 'y': [4, 3, 2, 1]})
    #     curves2.append({'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4]})
    #
    #     Curve.plot_curves_subplots([curves1, curves2], par_plot)
    #
    #
    # test()
