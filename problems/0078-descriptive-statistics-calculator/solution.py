import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    arr = np.array(data, dtype=float)
    vals, counts = np.unique(arr, return_counts=True)
    mode_val = float(vals[np.argmax(counts)])
    
    q25 = float(np.percentile(arr, 25))
    q50 = float(np.percentile(arr, 50))
    q75 = float(np.percentile(arr, 75))
    
    return {
        'mean': float(np.mean(arr)),
        'median': float(np.median(arr)),
        'mode': mode_val,
        'variance': float(np.var(arr)),
        'standard_deviation': float(np.std(arr)),
        '25th_percentile': q25,
        '50th_percentile': q50,
        '75th_percentile': q75,
        'interquartile_range': float(q75 - q25)
    }