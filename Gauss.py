import numpy as np
#Gaussian Elimination
#Not Works TT

def Solve(A, B, output=True):
    """A=[x₁, y₁, c₁], B=[x₂, y₂, c₂]"""
    A = np.array(A)
    B = np.array(B)

    B = A - (B[1] / A[1]) * B
    A = B - (B[0] / A[0]) * A

    y = A[2] / A[1]
    x = B[2] / B[0]
    if output:
        print(f"x : {x}\t y : {y}")
    return (x, y)


Solve([3, 2, 12], [8, 5, 31])