import numpy as np


def best_square_size(x, y, n):
    '''
    Given a rectangle with width and height, fill it with n squares of equal size such 
    that the squares cover as much of the rectangle's area as possible. 
    The size of a single square should be returned.
    Source: https://math.stackexchange.com/questions/466198/algorithm-to-get-the-maximum-size-of-n-squares-that-fit-into-a-rectangle-with-a
    '''
    x, y, n = float(x), float(y), float(n)
    px = np.ceil(np.sqrt(n * x / y))
    if np.floor(px * y / x) * px  < n:
            sx = y / np.ceil(px * y / x)
    else:
            sx = x/px
    py = np.ceil(np.sqrt(n * y / x))
    if np.floor(py * x / y) * py < n:
            sy = x / np.ceil(x * py / y)
    else:
            sy = y / py
    return max(sx,sy)


def best_layout(w, h, n):
    ''' Find the best layout of multiple subplots for a given screen size'''
    a = best_square_size(w, h, n)
    return [int(w/a), int(h/a)]