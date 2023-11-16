import numpy as np
def arf(*args):
    return sum(args) / len(args)

x = int(input())
y = int(input())
z = int(input())

d = np.arange(x, y, z)
print(arf(d))