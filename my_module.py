def math_formula(x):
    y = 3*x**2 + 2*x -6 
    return y
print('The value of y when x  = 3 is ',math_formula(3))

def middle_int(a,b,c): #a, b and c are integers
    A = sorted([a,b,c]) #We could also write this using conditional statements (if)
    return A[1]
print('The middle one of 8,5,1 is', middle_int(8,5,1))

def middle_int_function(a,b,c): #Learn to write a function
    A = sorted([a,b,c])
    x = A[1]
    y = 3*x**2 + 2*x -6
    return y
