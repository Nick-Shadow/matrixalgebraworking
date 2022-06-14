from math import sqrt


def add_vecs(a, b):
    """Add two same size vectors

    Args:
        a (num array): vector part
        b (num array): vector part

    Returns:
        num array: vector whole
    """
    assert len(a) == len(b)
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c


def sub_vecs(a, b):
    """Subtract two same size vectors (a - b)

    Args:
        a (num array): vector whole
        b (num array): vector part

    Returns:
        num array: vector part
    """
    assert len(a) == len(b)
    c = []
    for i in range(len(a)):
        c.append(a[i] - b[i])
    return c


def dot_product(a, b) -> float:
    """Makes dot product of a and b

    Args:
            a (num array): factor a
            b (num array): factor b

    Returns:
            float: inner product
    """
    assert len(a) == len(b)
    d: float = 0
    for i in range(len(a)):
        d += a[i] * b[i]
    return d


def scalar_product(c: float, a):
    """Preforms scalar multiplication on array

    Args:
            c (float): scalar factor
            a (num array): vector factor

    Returns:
            num array: product
    """
    b = []
    for i in range(len(a)):
        b.append(c * a[i])
    return b


def scalar_div(c: float, a):
    """Preforms scalar division on array

    Args:
            c (float): scalar dividend!
            a (num array): vector

    Returns:
            num array: product
    """
    r = 1 / c
    return scalar_product(r, a)


def magnitude(a):
    """Finds magnitude of vector

    Args:
            a (num array): vector

    Returns:
            float: magnitude scalar
    """
    m = 0
    for i in range(len(a)):
        m += a[i]**2
    m = sqrt(m)
    return m


def unit_vector(a):
    """Finds unit vector of a

    Args:
      a (num array): vector with nonunit length

    Returns:
      num array: unit vector in direction of a
    """
    m = magnitude(a)
    b = scalar_div(m, a)
    return b

##############################################################################
##############################################################################
##############################################################################


A = [[2, 1, 0, 1],
     [1, -1, 3, 1],
     [0, 1, 1, 1]]
"""
Input vectors
"""

u = [unit_vector(A[0])]
"""
Unit vectors
"""

for k in range(len(A) - 1):
    u_k1 = A[k + 1]
    for i in range(k + 1):  # ! noninclusive range(), must add 1 to k
        u_k1 = sub_vecs(u_k1, scalar_product(
            dot_product(A[k + 1], u[i]), u[i]))
    u.append(unit_vector(u_k1))

print()
for x in u:
    print(x)
print()
