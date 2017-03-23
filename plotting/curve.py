from plotting.plot_base import *


class Curve(object):
    @staticmethod
    def plot_curve(df, ax=None):

        # fig, ax = plt.subplots()

        ax.plot(df['x'], df['y'],
                # label='%s = %d' % (symbol, ys[s]),
                linewidth=2,
                linestyle='-',
                color=next(PlotBase.colorcycler),
                marker=next(PlotBase.markercycler), alpha=0.8)

        ax.locator_params(nbins=7)
        ax.tick_params(axis='both', which='major', labelsize=10)
        ax.legend(loc='upper left', fontsize=14)

        # PlotBase.configure_ax(ax)

        return ax

    @staticmethod
    def plot_curves(df, x_name, y_name, time, xlabel=None, ylabel=None, symbol=None, sharex=True, outputfile=None):
        organs_cycle = cycle(organs)

        fig, axs = plt.subplots(2, 3, sharey=False, sharex=sharex)

        for i in range(axs.shape[0]):
            for j in range(axs.shape[1]):

                markers = ['D', 's', 'x', '^', 'd', 'h', '+', '*', ',', 'o', '.', '1', 'p', '3', '2', '4', 'H', 'v',
                           '8',
                           '<', '>']
                colors = ['g', 'y', 'r', 'b', 'black']
                markercycler = cycle(markers)
                colorcycler = cycle(colors)

                ax = axs[i, j]
                organ_name = next(organs_cycle)
                df_freq = organs[organ_name][x_name][y_name][time]
                x_max_value = organs_df[organ_name]['df'][x_name].quantile(0.99)
                df_freq = df_freq[df_freq.index.get_level_values(0) <= x_max_value]
                df_freq = df_freq.apply(calculate_ci, axis=1)
                pxy = df_freq['p_tilde']
                #             y_max_value = organs_df[organ_name]['df'][y_name].quantile(0.99)
                #             df_freq = df_freq[df_freq.index.get_level_values(1) < y_max_value]


                #             pxy = df_freq['X>x, Y<=y'] / df_freq['X>x']
                xs = pxy.index.get_level_values(0).unique()
                #             ys = pxy.index.get_level_values(1).unique()
                #             pxy = pxy.reshape(len(xs),len(ys))

                pxy = pxy.fillna(0)
                #             pxy = np.nan_to_num(pxy)
                #             pxy = pxy.T

                #             amax = len(pxy) - 1

                b = 5.

                a1 = 0
                a2 = 1
                a3 = 7
                a4 = 15
                a5 = 30

                slices = [a1, a2, a3, a4, a5]
                # ax.set_color_cycle([plt.cm.cool(i) for i in range(len(slices))])
                ax.grid(alpha=1)
                for s in slices:
                    p = pxy[:, s]
                    ax.plot(xs, pxy.loc[:, s], label='%s = %d' % (symbol, ys[s]), linewidth=2, linestyle='-',
                            color=next(colorcycler), marker=next(markercycler), alpha=0.8)
                # xticks = ax.get_xticks()
                #                 xlabels = [xs[int(xticks[i])] for i in range(len(xticks)-1)]
                #                 ax.set_xticklabels(xlabels, rotation='horizontal', minor=False)
                ax.locator_params(nbins=7)
                ax.tick_params(axis='both', which='major', labelsize=25)
                ax.set_title(organ_name, size=35, y=1.00)
                ax.legend(loc='upper left', fontsize=14)

        for i in range(axs.shape[0]):
            ax = axs[i, 0]
            ax.set_ylabel(ylabel, size=25)

        for i in range(axs.shape[1]):
            ax = axs[axs.shape[0] - 1, i]
            ax.set_xlabel(xlabel, size=25)
        # ax.set_title('%s' % (organ_name), size=30)
        fig.set_size_inches(20, 10)
        #     fig.set_size_inches(25, 30)
        fig.tight_layout()  # pad=1.0, h_pad=0.5, w_pad=0.5)

        if outputfile:
            plt.savefig(outputfile)


            # x_name = 'distance'
            # y_name = 'survival_time'
            # time = 'short'
            #
            # xlabel = 'Distance (D) Miles'
            # ylabel = '$P(T \leq t | D > d)$'
            #
            #
            # outputfile = 'plots/curves/%s/%s_%s.pdf' %(time, x_name, y_name)
            # plot_curves(x_name,
            #           y_name, time,
            #           ylabel=ylabel,
            #           xlabel=xlabel,
            #          symbol='$t$',sharex=False,
            #           outputfile=outputfile)



            # x_name = 'cold_ischemic'
            # y_name = 'survival_time'
            # time = 'short'
            #
            # xlabel = 'Ischemic Time (I) Hours'
            # ylabel = '$P(T \leq t | I > i )$'
            #
            #
            # outputfile = 'plots/curves/%s/%s_%s.pdf' %(time, x_name, y_name)
            # plot_curves(x_name,
            #           y_name, time,
            #           ylabel=ylabel,
            #           xlabel=xlabel,
            #          symbol='$t$',sharex=False,
#             #           outputfile=outputfile)
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# df = pd.DataFrame({'x': np.arange(0, 10),
#                    'y': 2 * np.arange(0, 10)})
#
#
# fig, ax = plt.subplots()
#
# Curve.plot_curve(df, ax)