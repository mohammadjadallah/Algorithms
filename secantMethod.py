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
    from math import e  # Until (e) expression works when we put it inside the equation

    secant_method('x ** 2 - 612', 10, 30, 1/100)  # True solution

    print('\n')

    secant_method('e**-x - x', 1, 0, 1/100)  # True solution

    print('\n')

    secant_method('x ** 3 - 2 * x ** 2 + x - 3', 4, 3, 2 / 100)  # True solution

    print('\n')

    secant_method('x**2 - 9', 10, 9, 0.00001 / 100)  # True solution

    print('\n')

    secant_method('x**3 - 4', 10, 9, 0.00001 / 100)  # True solution

    
    '''
    output:
    
        The root1 is 22.8
        The root2 is 25.609756097560975
        The root3 is 24.703748488512694
        The root4 is 24.738029754158898
        The final root5 is 24.738634179877618

        
        The root1 is 0.6126998367802821
        The root2 is 0.5638383891610742
        The root3 is 0.5671703584197446
        The final root4 is 0.5671433066049633
        
        
        The root1 is 2.625
        The root2 is 2.4390243902439024
        The root3 is 2.23626192342722
        The root4 is 2.184386342189474
        The root5 is 2.1749681981462508
        The final root6 is 2.174562197637539
        
        
        The root1 is 5.2105263157894735
        The root2 is 4.017301038062284
        The root3 is 3.2436944937833037
        The root4 is 3.0341427921844217
        The root5 is 3.0013253625538097
        The root6 is 3.00000749760865
        The root7 is 3.000000001655807
        The root8 is 3.000000000000002
        The final root9 is 3.0
        
        
        The root1 is 6.324723247232472
        The root2 is 5.099615484487135
        The root3 is 3.790653899377583
        The root4 is 2.9453768516447463
        The root5 is 2.3153749395419085
        The root6 is 1.9120045701636306
        The root7 is 1.6896085060972919
        The root8 is 1.6050741890004419
        The root9 is 1.5884840251345835
        The root10 is 1.5874130147323309
        The root11 is 1.5874010601258086
        The root12 is 1.5874010519682609
        The final root13 is 1.5874010519681994
        
    '''
