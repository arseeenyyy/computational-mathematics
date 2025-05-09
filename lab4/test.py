import numpy as np

def f(x): 
    return (4 * x) / (x ** 4 + 12)

def phi(x): 
    return -0.019 + 0.487 * x - 0.165 * (x ** 2)

# for i in np.arange(0, 2.2, 0.2): 
#     print(f'x_i: {i:.1f}  f(x_i): {f(i)}\n----')

sum = 0
for i in np.arange(0, 2.2, 0.2):
    sum += (phi(i) - f(i)) ** 2
print(sum / 11)