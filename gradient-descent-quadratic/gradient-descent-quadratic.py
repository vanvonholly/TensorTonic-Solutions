def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # f'(x) = 2ax +b = 0 --> optimal x
    # find gradient at each x -> if negative, update position + step
    # keep doing it until you get x closest to optimal x
    x = x0

    for i in range(steps):
        gradient = 2*a*x + b
        x += -(lr) * gradient
    
    return float(x)