from math import sqrt
import copy

# Project a onto b proj_b a

print()
print("Project A onto B...")
print("Hit enter without entering a number to stop entering data")
print()

a = list()
b = list()

while True:
    a = list()
    b = list()

    while True:
        readd = input("Enter next element for A: ")
        if not readd:
            print("  => A is: ", a)
            break
        a.append(int(readd))
    print()
    while True:
        readd = input("Enter next element for B: ")
        if not readd:
            print("  => B is: ", b)
            break
        b.append(int(readd))

    if len(a) == len(b):
        print("\n" * 2)
        print("Solving...")
        print("\n" * 2)
        break
    else:
        print("Vectors MUST be the same size, do it again")


a_dot_b = 0
for i in range(len(a)):
    a_dot_b += a[i] * b[i]

mag_b_sqr = 0
for i in range(len(a)):
    mag_b_sqr += b[i]**2

mag_b = sqrt(mag_b_sqr)

# Proj a unto b

projection = copy.deepcopy(a)
for i in range(len(a)):
    projection[i] = (a_dot_b / mag_b_sqr) * b[i]

print("Projection: ", projection)
print()

# Comp a unto b

projection_mag = a_dot_b / mag_b

print("Projection Magnitude: ", projection_mag)
print()

# Ortho a unto b

ortho = copy.deepcopy(a)
for i in range(len(a)):
    ortho[i] = a[i] - projection[i]

print("Orthogonal Component: ", ortho)
print("\n" * 2)
