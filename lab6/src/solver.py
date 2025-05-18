import numpy as np

def euler_method(f, xi, y0): 
    yi = [y0]
    h = xi[1] - xi[0] 
    for i in range(len(xi)):
        y_next = yi[i] + h * f(xi[i], yi[i])
        yi.append(y_next)
    return yi


def main(): 
    f = lambda x, y: x + y
    xi = np.arange(0, 1.0, 0.1).tolist()
    y0 = 1
    yi = euler_method(f, xi, y0);
    print(yi)

if __name__ == "__main__": 
    main()