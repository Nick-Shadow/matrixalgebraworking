from math import sqrt
import numpy

VALID_RESPONSE_PERCENT_BARRIER = 1 - 0.25

# _Load in data, just hardcoded fn

N_MASTER = numpy.array([[1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1]])

N_HAND = numpy.array([[0, 1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 1, 1, 0, 0],
                      [0, 1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1]])

C = numpy.array([[1, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 1],
                 [1, 0.5, 0, 0, 0.5, 1],
                 [0, 1, 1, 1, 1, 0]])

n_vec_master = []
n_vec_hand = []
c_vec = []

# _Reduce Dimensions


def matrix_to_vector(m: numpy.ndarray, out: numpy.ndarray):
    for v in m:
        for s in v:
            out.append(s)


matrix_to_vector(N_MASTER, n_vec_master)
matrix_to_vector(N_HAND, n_vec_hand)
matrix_to_vector(C, c_vec)

# _Find unit Vector


def find_unit(m: numpy.ndarray, out: numpy.ndarray):
    mmag = 0
    for e in m:
        mmag += e**2
    mmag = sqrt(mmag)
    for e in m:
        out.append(e / mmag)


n_hat_master = []

find_unit(n_vec_master, n_hat_master)

# _Find all projection info


def proj_onto_x(onto: numpy.ndarray, x: numpy.ndarray, out_proj: numpy.ndarray):
    assert len(onto) is len(x)
    # numerator aka dot product
    n: int = 0
    for i in range(len(onto)):
        n += onto[i] * x[i]
    # denominator aka squared magnitude
    d: int = 0
    for e in onto:
        d += e**2
    c = n / d
    for i in range(len(onto)):
        out_proj.append(c * onto[i])
    return n / sqrt(d)


n_n_master_proj = []
n_n_hand_proj = []
n_c_proj = []

n_n_scalar = proj_onto_x(n_hat_master, n_vec_master, n_n_master_proj)
n_n_hand_scalar = proj_onto_x(n_hat_master, n_vec_hand, n_n_hand_proj)
n_c_scalar = proj_onto_x(n_hat_master, c_vec, n_c_proj)

n_master_percent = float(n_n_scalar / n_n_scalar)
n_hand_percent = float(n_n_hand_scalar / n_n_scalar)
c_percent = float(n_c_scalar / n_n_scalar)

# _Show Results

print("-" * 100)
print("Values over {:.2%} are considered to be a valid N".format(
    VALID_RESPONSE_PERCENT_BARRIER))
print("-" * 100)


def isValid(percent: float) -> str:
    return "✓ YES!" if percent >= VALID_RESPONSE_PERCENT_BARRIER else "X  NO!"


print("{:>7} | N master      onto  N master   overlap: | {:>6.2%}".format(
    isValid(n_master_percent), n_master_percent))
print("{:>7} | N hand-drawn  onto  N master   overlap: | {:>6.2%}".format(
    isValid(n_hand_percent), n_hand_percent))
print("{:>7} | C             onto  N master   overlap: | {:>6.2%}".format(
    isValid(c_percent), c_percent))
print("-" * 100)
