# False position method used to numerical analysis it is a finding-root method
# it is better than bisection method and fastest as well as it is find the root with a littel iteration than bisection method


from tabulate import tabulate # to create a pretty table
from collections import deque # because deque is faster than the regular list []


def false_position_method(equation, a, b, given_error):

    Xl = deque()
    Xu = deque()
    Xr = deque()
    f_Xl = deque()
    f_Xu = deque()
    f_Xr = deque()
    Ea = deque()

    data = {
        'Xl': Xl,
        'Xu': Xu,
        'Xr': Xr,
        'f(Xl)': f_Xl,
        'f(Xu)': f_Xu,
        'f(Xr)': f_Xr,
        'Ea': Ea
    }

    def f(x):
        F = eval(equation)
        return F

    # the first root is zero
    c_before = 0
    # the general rule in false position to find the root
    c = b - ((f(b))*(a - b) / (f(a) - f(b)))  # first iteration has this root

    # estimated_error = ((current root - old root)/current root) * 100
    estimated_error = abs(((c - c_before)/c))*100

    while estimated_error/100 > given_error:

        new_c = b - ((f(b))*(a - b) / (f(a) - f(b)))

        Xl.append(a)
        Xu.append(b)
        Xr.append(new_c)
        f_Xl.append(f(a))
        f_Xu.append(f(b))
        f_Xr.append(f(c))
        Ea.append(None if estimated_error == 100 else ('%.5f' % estimated_error + '%'))

        if f(a) * f(b) >= 0:
            print("False position is fail")
            break

        elif f(a) * f(new_c) < 0:
            b = new_c
            c2 = b - ((f(b))*(a - b) / (f(a) - f(b)))
            estimated_error = abs(((c2 - new_c)/c2))*100

        elif f(b) * f(new_c) < 0:
            a = new_c
            c2 = b - ((f(b)) * (a - b) / (f(a) - f(b)))
            estimated_error = abs(((c2 - new_c) / c2)) * 100

        else:
            print("something is wrong!")
    else:
        new_c = b - ((f(b)) * (a - b) / (f(a) - f(b)))
        Xl.append(a)
        Xu.append(b)
        Xr.append(new_c)
        f_Xl.append(f(a))
        f_Xu.append(f(b))
        f_Xr.append(f(new_c))
        Ea.append('%.5f' % estimated_error + '%')

    print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=1))


print("The first trial: \n")
false_position_method("-25 + 82*x - 90*x**2 + 44*x**3 - 8*x**4 +0.7*x**5", 0.5, 1.0, 0.2/100)

print('\n-------------------------------------------------------\n')

print("The second trial: \n")
false_position_method("-0.4*x**2+2.2*x+4.7", 5, 10, 5/100)

print('\n-------------------------------------------------------\n')

print("The 3rd trial: \n")
false_position_method("x**2 - 3", 1, 2, 0.01/100)

print('\n-------------------------------------------------------\n')

print("The four trial: \n")
false_position_method("-2*x**3+2*x**2+20*x+10", 2.5, 5, 5/100)



