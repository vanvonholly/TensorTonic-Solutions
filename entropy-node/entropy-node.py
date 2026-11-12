import numpy as np
import math

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    seen = set()
    total_length = len(y)
    running_total = 0

    for i in y:
        if i not in seen:
            freqfrac = y.count(i) / total_length
            running_total += -1 * freqfrac * math.log2(freqfrac)
        seen.add(i)

    if len(set(y)) == 1:
        running_total = 0
            
    return float(running_total)