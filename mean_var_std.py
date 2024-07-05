import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    y = [list[0:3], list[3:6], list[6:10]]
    x = np.asarray(y)
    print(x)
    mean = [x.mean(axis=0).tolist(), x.mean(axis=1).tolist(), x.mean()]
    variance = [x.var(axis=0).tolist(), x.var(axis=1).tolist(), x.var()]
    standard_deviation = [x.std(axis=0).tolist(), x.std(axis=1).tolist(), x.std()]
    _max = [x.max(axis=0).tolist(), x.max(axis=1).tolist(), x.max()]
    _min = [x.min(axis=0).tolist(), x.min(axis=1).tolist(), x.min()]
    _sum = [x.sum(axis=0).tolist(), x.sum(axis=1).tolist(), x.sum()]

    calculations = {'mean': mean, 'variance': variance, 'standard deviation': standard_deviation, 'max': _max, 'min': _min, 'sum': _sum}

    return calculations