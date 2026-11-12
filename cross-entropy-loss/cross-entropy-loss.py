import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    length_all = len(y_true)
    running_total = 0

    for i in range(length_all):
        correct_index = y_true[i]
        correct_pred = y_pred[i][correct_index] 
        running_total += -1 * np.log(correct_pred)

    average = running_total / length_all
    return float(average)