import numpy as np
import matplotlib.pyplot as plt

class HeatMap():
    @staticmethod
    def plot_mat(pxy, fig, ax): #clim=None, title=None, xlabel=None, ylabel=None, xticklabels=None, yticklabels=None):

        xs = pxy.index.get_level_values(0).unique()
        ys = pxy.index.get_level_values(1).unique()
        pxy = pxy.reshape(len(xs), len(ys))

        pxy = np.nan_to_num(pxy)
        pxy = pxy.T

        pxy_max = pxy.max()
        pxy_min = pxy.min()

        # fig, ax = plt.subplots()


        mat = ax.matshow(pxy, aspect='auto', origin='lower')  # , cmap=plt.cm.gnuplot2_r)
        # if clim:
        #     mat.set_clim(clim[0], clim[1])

        # ax.set_title(title, size=25, y=1.0)

        #Put labels on the bottom
        ax.xaxis.set_ticks_position('bottom')
        #Make labels greater
        # ax.tick_params(axis='both', which='major', labelsize=25)

        xticklabels = xs
        xticks = ax.get_xticks()
        xlabels = [0] + [xticklabels[int(xticks[i])] for i in range(len(xticks) - 1) if xticks[i] >= 0]
        ax.set_xticklabels(xlabels, rotation='horizontal', minor=False)

        yticklabels = ys
        yticks = ax.get_yticks()
        ylabels = [0] + [yticklabels[int(yticks[i])] for i in range(len(yticks) - 1) if yticks[i] >= 0]
        ax.set_yticklabels(ylabels, rotation='horizontal', minor=False)

        tick_loc = [pxy_min, (pxy_max + pxy_min) / 2, pxy_max]
        c = fig.colorbar(mat, ax=ax, ticks=tick_loc, format='%.2f')

        # c.ax.tick_params(labelsize=20)

        return fig, ax, mat

#     @staticmethod
#     def plot_mats(dfs, ax_shape, title=None, xlabel=None, ylabel=None, x_max=None, outputfile=None):
#         # organs_cycle = cycle(organs)
#
#         fig, axs = plt.subplots(ax_shape[0], ax_shape[1], sharey=True)
#
#         for i in range(ax_shape[0]):
#             for j in range(ax_shape[1]):
#                 ax = axs[i, j]
#                 df_freq = organs[organ_name][x_name][y_name][time]
#
#                 max_value = organs_df[organ_name]['df'][x_name].quantile(0.99)
#                 df_freq = df_freq[df_freq.index.get_level_values(0) < max_value]
#                 df_freq = df_freq.apply(CI.calculate_ci, axis=1)
#                 pxy = df_freq['p_tilde']
#                 #             pxy = df_freq['X>x, Y<=y'] / df_freq['X>x']
#                 xs = pxy.index.get_level_values(0).unique()
#                 ys = pxy.index.get_level_values(1).unique()
#                 pxy = pxy.reshape(len(xs), len(ys))
#
#                 pxy = np.nan_to_num(pxy)
#                 pxy = pxy.T
#
#                 pxy_max = pxy.max()
#                 pxy_min = pxy.min()
#
#                 mat = plot_mat(ax=ax,
#                                pxy=pxy,
#                                clim=(pxy_min, pxy_max),
#                                title=organ_name,
#                                xlabel=xlabel,
#                                ylabel=ylabel,
#                                xticklabels=xs
#                                )
#                 tick_loc = [pxy_min, (pxy_max + pxy_min) / 2, pxy_max]
#                 c = fig.colorbar(mat, ax=ax, ticks=tick_loc, format='%.2f')
#                 c.ax.tick_params(labelsize=20)
#
#         for i in range(axs.shape[0]):
#             ax = axs[i, 0]
#             ax.set_ylabel(ylabel, size=25)
#
#         for i in range(axs.shape[1]):
#             ax = axs[axs.shape[0] - 1, i]
#             ax.set_xlabel(xlabel, size=25)
#
#         # fig.subplots_adjust(right=0.83)
#         # #     cax,kw = mpl.colorbar.make_axes([ax for ax in axs.flat], location='bottom')
#         # #     plt.colorbar(mat, cax=cax,  **kw)
#         #     #cbar_ax = fig.add_axes([0, 0, 1, 0.1])
#         #     #c = fig.colorbar(mat, cax=cbar_ax, orientation='horizontal')
#
#         #     #
#
#         #     cbar_ax = fig.add_axes([0.85, 0.15, 0.02, 0.7])
#         #     fig.colorbar(mat, cax=cbar_ax)
#         #     cbar_ax.tick_params(labelsize=25)
#
#
#
#
#         if title:
#             fig.suptitle(title, fontsize=30, fontweight="bold")
#         fig.set_size_inches(20, 10)
#         fig.tight_layout(rect=[0, 0, 1, .95], w_pad=0.5)  # pad=1.0, h_pad=0.5, w_pad=0.5)
#         if outputfile:
#             plt.savefig(outputfile)
#
#
# # x_name = 'cold_ischemic'
# # y_name = 'survival_time'
# #
# # for organ_name in organs:
# #     organs[organ_name][x_name] = dict()
# #     organs[organ_name][x_name][y_name] = dict()
# #     path = 'hists/hist_o_%s_x%s_xbs_0001_y%s_ybs_0001.h5' % (organ_name, x_name, y_name)
# #     organs[organ_name][x_name][y_name]['short'] = pd.read_hdf(path, 'table')
# #
# #
#
#
# # x_name = 'cold_ischemic'
# # y_name = 'survival_time'
# # time = 'short'
# # title='$P(T \leq t | I > i)$'
# #
# # outputfile = 'plots/heatmaps/%s/%s_%s.pdf' %(time, x_name, y_name)
# # plot_mats(x_name,
# #           y_name, time,
# #           title=title,
# #           ylabel='Graft Failure (T) Days',
# #           xlabel='Ischemic Time (I) Hours',
# #           outputfile=outputfile)
#
#
# #
# # from statistician.joints import *
# # import pandas as pd
# # import matplotlib.pyplot as plt
# #
# # # df = pd.DataFrame({'x': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4],
# # #                    'y': [50, 51, 53, 52, 57, 43, 42, 45, 48, 44, 32, 35, 32, 33, 21, 20, 50, 51, 53, 52, 57, 43, 42, 45, 48, 44, 32, 35, 32, 33, 21, 20, 50, 51, 53, 52, 57, 43, 42, 45, 48, 44, 32, 35, 32, 33, 21, 20]})
# #
# # #
# # df = pd.DataFrame({'x': np.random.normal(10, 1, 50),
# #                    'y': np.random.normal(1, 1, 50)})
# # #
# # #
# # #
# # #
# # #
# # #
# # pxy = Joints.calculate_joints(df, x_bin_size=0.5, y_bin_size=0.5)
# # #
# # #
# # #
# # #
# # HeatMap.plot_mat(pxy)
# # #
# # plt.show()
# # #
# #
# #
# # import numpy as np
