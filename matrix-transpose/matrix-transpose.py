import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # get shape of np array
    A = np.array(A)
    size = A.shape
    n = size[0]
    m = size[1]
    # maybe initialise (m,n)
    output = np.zeros((m,n))
    # then get values for each row -> fill out per column
    for i in range(n):
        new_column = A[i]
        output[:,i] = new_column
        
    return output
