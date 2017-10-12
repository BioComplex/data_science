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

        assert fig is not None, "fig is none"
        par_titles = PlotBase.get_par(par_subplots, 'title', transform=cycle)
        par_titlesize = PlotBase.get_par(par_subplots, 'title.size')

        axs = np.ravel(np.array(axs))
        for i in range(len(axs)):
            ax = axs[i]
            sub_dfs = dfs[i]
            ax = Curve.plot_curves(sub_dfs, par_plot, fig, ax)
            if par_titles:
                ax.set_title(next(par_titles), fontsize=par_titlesize)


        par_legend = PlotBase.get_par(par_subplots, 'legend')
        if par_legend:
            par_legend_fontsize = PlotBase.get_par(par_subplots, 'legend.fontsize')
            par_legend_loc = PlotBase.get_par(par_subplots, 'legend.loc')
            par_legend_pos = int(PlotBase.get_par(par_subplots, 'legend.pos', default=0))
            axs[par_legend_pos].legend(labels=par_legend, loc=par_legend_loc, fontsize=par_legend_fontsize)

        par_xlabel = PlotBase.get_par(par_subplots, 'x_label')
        par_xlabel_pos = PlotBase.get_par(par_subplots, 'x_label.pos', [0])
        if par_xlabel:
            [axs[i].set_xlabel(par_xlabel) for i in par_xlabel_pos]

        par_ylabel = PlotBase.get_par(par_subplots, 'y_label')
        par_ylabel_pos = PlotBase.get_par(par_subplots, 'y_label.pos', [0])
        if par_ylabel:
            [axs[i].set_ylabel(par_ylabel) for i in par_ylabel_pos]

        PlotBase.configure_fig(fig, par_subplots)
        # PlotBase.configure_ax(ax, par_subplots)

        # TODO parameterize
        # plt.tight_layout()
        # fig.tight_layout(rect=par_figrect, w_pad=par_figwpad, h_pad=par_fighpad, pad=par_figpad)  # pad=1.0, h_pad=0.5, w_pad=0.5)


        PlotBase.configure_fig(fig, par_plot)

        # figsize = PlotBase.get_par(par_plot, 'figsize')
        # if figsize:
        #     fig.set_size_inches(figsize)

        plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Arial'], 'size': 12})

        return fig, axs

    @staticmethod
    def plot_curves(dfs, par_plot, fig=None, ax=None):

        if ax is None:
            fig, ax = plt.subplots(1, 1)

        #Parameters
        par_linewidth = PlotBase.get_par(par_plot, 'linewidth', 2)
        par_linestyle = PlotBase.get_par(par_plot, 'linestyle', '-')
        par_alpha = PlotBase.get_par(par_plot, 'alpha', .8)
        par_color = PlotBase.get_par(par_plot, 'color', default=PlotBase.colors, transform=cycle)
        par_marker = PlotBase.get_par(par_plot, 'marker', default=PlotBase.markers, transform=cycle)
        par_legend = PlotBase.get_par(par_plot, 'legend', transform=cycle)




        for df in dfs:

            label = None
            if par_legend:
                label = next(par_legend)

            ax.plot(df['x'], df['y'],
                    linewidth=par_linewidth,
                    linestyle=par_linestyle,
                    alpha=par_alpha,
                    color=next(par_color),
                    marker=next(par_marker),
                    label=label)


            PlotBase.configure_ax(ax, par_plot)

            PlotBase.configure_fig(fig, par_plot)

            # figsize = PlotBase.get_par(par_plot, 'figsize')
            # if figsize:
            #     fig.set_size_inches(figsize)

            # TODO parameterize

        # plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Arial'], 'size': 12})

        return ax