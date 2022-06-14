from copy import deepcopy
from math import sqrt
# todo make sympy work


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


def transpose(a):
    # todo fix this stupid little thing w/out using deepcopy for square arrays
    r = deepcopy(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            r[j][i] = a[i][j]
    return r

##############################################################################
##############################################################################


def gram__schmidt(a):
    """Preforms Gram-Schmidt proceedure on a

    Args:
        a (num matrix): matrix input

    Returns:
        num matrix: matrix representing orthonormal vectors
    """
    unit_vecs = [unit_vector(a[0])]
    for k in range(len(a) - 1):
        u_k1 = a[k + 1]
        for i in range(k + 1):  # ! noninclusive range(), must add 1 to k
            u_k1 = sub_vecs(u_k1, scalar_product(
                dot_product(a[k + 1], unit_vecs[i]), unit_vecs[i]))
        unit_vecs.append(unit_vector(u_k1))

    return unit_vecs


def qr_decomp(a):
    """Finds QR decomposition or factorization of matrix a

    Args:
        a (num matrix): input matrix

    Returns:
        num matrix: orthagonal matrix
        num matrix: upper triangular matrix
    """
    e = gram__schmidt(a)
    r = []
    for i in range(len(a)):
        r.append([])
        for j in range(len(a[0])):
            if (j < i + 1):
                r[i].append(dot_product(a[i], e[j]))
            else:
                r[i].append(0)
    return e, r


##############################################################################

# todo make look nice
def print_matrix(a, label: str = ""):
    if (label == ""):
        print()
    else:
        print(f"\n{label}: ")
    for x in transpose(a):
        print(x)
    print()


##############################################################################


a_in = [[1, 2, 1],
        [2, -1, 0],
        [1, 3, 0]]

print_matrix(gram__schmidt(a_in))

# q, r = qr_decomp(a_in)

# print_matrix(q, "Q")
# print_matrix(r, "R")
