import numpy as np
import pandas as pd
from statistician.confidence_interval import CI


# def get_bins(df, name, bin_size, f_max=max):

class Joints():
    @staticmethod
    def get_bins(series, bin_size, f_max=np.max):
        # if df is None:
        if series is None:
            raise ('series is none')

        # max_value = int(np.ceil(f_max(df[name])))
        max_value = int(np.ceil(f_max(series)))
        bins = np.arange(0, max_value + bin_size, bin_size)
        return bins

    @staticmethod
    def calculate_freq(row, df, x_callback=None, y_callback=None):
        x = row.name[0]
        y = row.name[1]

        df_1 = df
        if x_callback is not None:
            df_1 = x_callback(df_1, x)
        df_2 = df_1
        if y_callback is not None:
            df_2 = y_callback(df_2, y)

        row['X>x'] = df_2[df_2['x'] > x].shape[0]
        # row['X<=x'] = df_2[df_2['x'] <= x].shape[0]
        # row['Y<=y'] = df_2[df_2['y'] <= y].shape[0]
        # row['Y>y'] = df_2[df_2['y'] <= y].shape[0]
        # row['X<=x, Y<=y'] = df_2[(df_2['x'] <= x) & (df_2['y'] <= y)].shape[0]
        # row['X<=x, Y>y'] = df_2[(df_2['x'] <= x) & (df_2['y'] > y)].shape[0]
        row['X>x, Y<=y'] = df_2[(df_2['x'] > x) & (df_2['y'] <= y)].shape[0]
        # row['X>x, Y>y'] = df_2[(df_2['x'] > x) & (df_2['y'] > y)].shape[0]

        return row

    @staticmethod
    def get_hist(df=None,
                 x_bins=1,
                 y_bins=1,
                 y_callback=None,
                 x_callback=None):
        if df is None:
            raise ('df is none')

        df_freq = pd.DataFrame(index=pd.MultiIndex.from_product([x_bins, y_bins], names=['X', 'Y']),
                               columns=['X>x',
                                        # 'X<=x',
                                        # 'Y<=y',
                                        # 'Y>y',
                                        # 'X<=x, Y<=y',
                                        # 'X<=x, Y>y',
                                        'X>x, Y<=y'
                                        # 'X>x, Y>y'
                                        ])

        df_freq = df_freq.apply(Joints.calculate_freq,
                                axis=1,
                                df=df,
                                x_callback=x_callback,
                                y_callback=y_callback)

        return df_freq

    @staticmethod
    def calculate_joints(df=None,
                         # x_name=None,
                         x_bin_size=1,
                         x_max=(lambda v: v.max()),
                         x_callback=None,
                         # y_name=None,
                         y_bin_size=1,
                         y_max=(lambda v: v.max()),
                         y_callback=None):
        # x_bins = get_bins(df, x_name, x_bin_size, x_max)
        # y_bins = get_bins(df, y_name, y_bin_size, y_max)

        # df['x'] = df[x_name]
        # df['y'] = df[y_name]

        x_bins = Joints.get_bins(df['x'], x_bin_size, x_max)
        y_bins = Joints.get_bins(df['y'], y_bin_size, y_max)

        df_freq = Joints.get_hist(df=df,
                                  x_bins=x_bins,
                                  x_callback=x_callback,
                                  y_bins=y_bins,
                                  y_callback=y_callback)

        #TODO make general, parameterize
        max_value = df['x'].quantile(0.99)
        df_freq = df_freq[df_freq.index.get_level_values(0) < max_value]
        df_freq = df_freq.apply(CI.calculate_ci, axis=1)

        pxy = df_freq['p_tilde']


        return pxy

# df = pd.DataFrame({'x': [1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4], 'y': [50,51,53,52,57,43,42,45,48,44,32,35,32,33,21,20]})
# df_freq = get_hist2d(df)
