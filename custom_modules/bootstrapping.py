import numpy as np


def bootstrap_median_difference(sample1, sample2, replications=1000):
    """
    Calculate the bootstrapped 95% confidence interval for the difference in medians between two datasets.

    Parameters:
    sample1 (array-like): First dataset for bootstrapping.
    sample2 (array-like): Second dataset for bootstrapping.
    n_iterations (int, optional): Number of bootstrap iterations (default is 1000).

    Returns:
    np.ndarray: Array containing the 2.5th and 97.5th percentiles of the bootstrapped median differences, representing
                the 95% confidence interval.
    """
    median_differences = []
    for _ in range(replications):
        resample1 = np.random.choice(sample1, size=len(sample1), replace=True)
        resample2 = np.random.choice(sample2, size=len(sample2), replace=True)
        median_difference = np.median(resample1) - np.median(resample2)
        median_differences.append(median_difference)

    return np.percentile(median_differences, [2.5, 97.5])


def bootstrap_median(original_sample, col, replications):
    """Simulate sample medians:
    original_sample: df containing the original sample data
    col: label of column containing the variable
    replications: number of bootstrap samples
    Returns array of bootstrap sample medians
    """
    medians = np.array([])
    for _ in np.arange(replications):
        bootstrap_sample = original_sample.sample(len(original_sample), replace=True)
        resampled_median = bootstrap_sample[col].median()
        medians = np.append(medians, resampled_median - theta_hat)

    return medians


def bootstrap_mean(original_sample, col, replications):
    """Simulate sample means:
    original_sample: df containing the original sample data
    col: label of column containing the variable
    replications: number of bootstrap samples
    Returns array of bootstrap sample means
    """
    means = np.array([])
    for _ in np.arange(replications):
        bootstrap_sample = original_sample.sample(len(original_sample), replace=True)
        resampled_mean = bootstrap_sample[col].mean()
        means = np.append(means, resampled_mean)

    return means
