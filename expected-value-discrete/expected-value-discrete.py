import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    running_total = 0
    num_inputs = len(x)

    for i in range(num_inputs):
        running_total += x[i]*p[i]

    
    return float(running_total)