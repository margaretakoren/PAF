import numpy as np

def derivative_at_point(func, x, epsilon=0.01, method='three-step'):
    if method == 'two-step':
        return (func(x + epsilon) - func(x)) / epsilon
    elif method == 'three-step':
        return (func(x + epsilon) - func(x - epsilon)) / (2 * epsilon)
    else:
        raise ValueError("Nevažeća metoda")

def derivative_over_range(func, lower_bound, upper_bound, epsilon=0.01, method='three-step'):
    x_values = np.arange(lower_bound, upper_bound, epsilon)
    dfx = [derivative_at_point(func, x, epsilon, method) for x in x_values]
    return dfx, x_values

def integrate(func, lower_bound, upper_bound, Nstep):
    dx = abs(upper_bound - lower_bound) / Nstep
    return sum(func(i * dx) + func((i + 1) * dx) for i in range(Nstep)) * dx / 2

def integrate_up_dn(f, a, b, N):
    dx = (b - a) / N
    lower_sum = 0
    upper_sum = 0
    for i in range(N):
        lower_sum += f(a + i*dx) * dx
        upper_sum += f(a + (i+1)*dx) * dx
    return lower_sum, upper_sum


