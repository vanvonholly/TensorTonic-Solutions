import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    running_total = 0
    total_length = len(p)

    for i in range(total_length):
        if p[i] == 0:
            running_total += 0

        else: 
            if q[i] < eps:
                q[i] = eps
            running_total += p[i] * np.log(p[i] / q[i])
    
    return float(running_total)