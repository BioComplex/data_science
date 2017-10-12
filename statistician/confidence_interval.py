import numpy as np
from scipy import stats
import scipy.stats as st

class CI():

    @staticmethod
    def proportion_ci_wilson(nx, n, conf_level=0.95):
        alpha = 1 - conf_level
        nx = float(nx)
        n = float(n)
        if n == 0 or nx == 0:
            return np.nan, np.nan, np.nan
        p_hat = nx / n

        z = stats.norm.ppf(1 - alpha / 2)
        t = np.power(z, 2) / n

        p_tilde = (p_hat + t / 2.) / (1 + t)
        see = np.sqrt((p_hat * (1 - p_hat) / n) + (t / (4. * n))) / (1 + t)

        ci_l = p_tilde - z * see
        ci_u = p_tilde + z * see
        return p_tilde, ci_l, ci_u

    @staticmethod
    def calculate_ci(row, nx_index='X>x, Y<=y', n_index='X>x'):
        #TODO need to make it general
        # nx = row['X>x, Y<=y']
        # n = row['X>x']
        nx = row[nx_index]
        n = row[n_index]
        (p, l, u) = CI.proportion_ci_wilson(nx, n)
        row['p_tilde'] = p
        row['ci'] = '%.02f (%.02f, %.02f)' % (round(p * 100, 2), round(l * 100, 2), round(u * 100, 2))
        return row

    @staticmethod
    def risk_ratio_ci(x1, n1, x2, n2, confidence_level=.95):
        """ http://stats.stackexchange.com/questions/21298/confidence-interval-around-the-ratio-of-two-proportions
        This function calculates the confidence interval from the ratio between 2 proportions.

        Args:
            x1 (int): number of success cases in population 1.
            n1 (int): number of elements in population 1.
            x2 (int): number of success cases in population 2.
            n2 (int): number of elements in population 2.
            confidence_level (double): percentage of confidence (0-1), default value is 0.95.

        Returns:
            tuple: log(teta), SEM(log(teta)), teta, CI(-,+)
        """
        teta = np.divide(np.divide(x1, n1), np.divide(x2, n2))
        se_log_teta = np.sqrt(np.divide(1., x1) - np.divide(1., n1) + np.divide(1., x2) - np.divide(1., n2))
        adj = st.norm.ppf(1 - (1 - confidence_level) / 2)
        return np.log(teta), np.multiply(adj, se_log_teta), teta, (np.exp(np.subtract(np.log(teta), np.multiply(adj, se_log_teta))),np.exp(np.add(np.log(teta), np.multiply(adj, se_log_teta))))

