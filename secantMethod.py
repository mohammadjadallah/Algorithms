# Secant Method

def secant_method(equation, a, b, given_error):

    def f(x):
        F = eval(equation)
        return F

    before_c = 0
    Xi = a
    X_i_minus1 = b
    Xr = Xi - ((f(Xi) * (Xi-X_i_minus1)) / (f(Xi) - f(X_i_minus1)))
    Ea = abs((Xr - before_c) / Xr) * 100
    count = 1
    while Ea/100 > given_error:

        Xr = Xi - ((f(Xi) * (Xi - X_i_minus1)) / (f(Xi) - f(X_i_minus1)))

        Ea = abs((Xr - Xi) / Xr) * 100
        X_i_minus1, Xi = Xi, Xr

        print(f'The root{count} is {Xr}')
        count += 1

    else:
        Xr = Xi - ((f(Xi) * (Xi - X_i_minus1)) / (f(Xi) - f(X_i_minus1)))
        print(f'The final root{count} is {Xr}')


if __name__ == '__main__':
    from math import e

    secant_method('x ** 2 - 612', 10, 30, 1/100)  # True solution

    print('\n')

    secant_method('e**-x - x', 1, 0, 1/100)  # True solution

    print('\n')

    secant_method('x ** 3 - 2 * x ** 2 + x - 3', 4, 3, 2 / 100)  # True solution

    print('\n')

    secant_method('x**2 - 9', 10, 9, 0.00001 / 100)  # True solution

    print('\n')

    secant_method('x**3 - 4', 10, 9, 0.00001 / 100)  # True solution

