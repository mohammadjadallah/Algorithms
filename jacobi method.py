from sympy import Eq, symbols, solve

def jacobi_method():
    '''
    Jacobi method

    we wanna create algorithm to solve linear equation

    the use will give three equation and these equations have symbol like x1, x2, x3

    then will give initial guess like 0, 1, 0. Now we wanna take number iteration from user

    to find the last values of x1, x2, x3

    now run program and see the result

    '''

    x1, x2, x3 = symbols('x1 x2 x3')

    initial_guess1, initial_guess2, initial_guess3 = map(int, input('Enter initial guesses respectively: ').split())

    li_e1 = list()
    li_e2 = list()
    li_e3 = list()

    iterations = int(input('Enter numbers iterations: '))

    eq1 = Eq(12*x1 + 3 * initial_guess2 - 5 * initial_guess3, 1)  # x2 = initial_guess2 , x3 = initial_guess3

    li_e1.append(*eval(f'{solve(eq1)}'))

    eq2 = Eq(initial_guess1 + 5 * x2 + 3 * initial_guess3, 28)  # x1 = initial_guess1, x3 = initial_guess3

    li_e2.append(*eval(f'{solve(eq2)}'))

    eq3 = Eq(3*initial_guess1 + 7 * initial_guess2 + 13 * x3, 76)  # x1 = initial_guess1, x2 = initial_guess2

    li_e3.append(*eval(f'{solve(eq3)}'))

    for i in range(iterations - 1):
        eq1 = Eq(12 * x1 + 3 * li_e2[i] - 5 * li_e3[i], 1)  # x2 = initial_guess2 , x3 = initial_guess3
        eq2 = Eq(li_e1[i] + 5 * x2 + 3 * li_e3[i], 28)  # x1 = initial_guess1, x3 = initial_guess3
        eq3 = Eq(3 * li_e1[i] + 7 * li_e2[i] + 13 * x3, 76)  # x1 = initial_guess1, x2 = initial_guess2
        li_e1.append(*eval(f'{solve(eq1)}'))
        li_e2.append(*eval(f'{solve(eq2)}'))
        li_e3.append(*eval(f'{solve(eq3)}'))

    print('x1', li_e1)
    print('x2', li_e2)
    print('x3', li_e3)


print(jacobi_method.__doc__)
jacobi_method()
