"""2nd GRADE EQUATION

(-b+-((b**2) - (4*a)*c)**2) / 2*a || Equation Formula

"""

"""DISCRIMINANT aka DELTA

'\u0394' --> DISCRIMINANT / DELTA unicode

When using discriminant:
    If DISC > 0 --> 2 different real solutions
    If DISC = 0 --> 2 equal real solutions
    If DISC < 0 --> 2 no real solutions, just 2 complex solutions

"""

def second_grade_equation(a,b,c,disc=False):

    if disc == True:

        discGrade_eq = int((b**2) - (4 * a) * c)

        if discGrade_eq > 0:
            rs = 'Equation has 2 different real solutions'
        elif discGrade_eq == 0:
            rs = 'Equation has 2 equal real solutions'
        elif discGrade_eq < 0:
            rs = 'Equation has no real solutions, it has 2 complex solutions'

        return f'DISCRIMINANT \u0394 is equal to {discGrade_eq}\n{rs}'
    else:

        secGrade_eq_pos = int((-b + ((b**2) - (4 * a) * c)**2) / 2 * a)
        secGrade_eq_neg = int((-b - ((b**2) - (4 * a) * c)**2) / 2 * a)

        return f'The first result is {secGrade_eq_pos} and the second result is {secGrade_eq_neg}'
    
# TRY THE CODE:
a = 3
b = -5
c = 1

# 3x² - 5x + 1 = 0

print(second_grade_equation(a,b,c))