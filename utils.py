import numpy as np



def get_binary_representation_positive(x):
    x = abs(x)
    binary_string = bin(x)[2:]
    k = len(binary_string)

    representation  = []
    for i, d in enumerate(binary_string):
        if d == "1":
            representation.append(k - 1 - i)

    return representation

def regular_exponentiation(x,k):

    if k == 0:
        return 1

    x_r = x

    for i in range(k - 1):
        x_r *= x
    return x_r

def fast_exponentiation(x,k):
    if k == 0:
        return 1
    nb_mult = 0
    result = 1
    binary_repr_pos = get_binary_representation_positive(k)

    x_current = x
    i = 0

    while len(binary_repr_pos) > 0:
        target = binary_repr_pos.pop(-1)
        while i != target:
            x_current *= x_current
            i += 1
            nb_mult += 1
        result *= x_current

        nb_mult += 1

    return result,nb_mult


if __name__ == "__main__":
    print(fast_exponentiation(10,100))
    print(np.log2(100))