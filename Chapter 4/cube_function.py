The cube function is missing a return statement. It computes x ** 3 but throws the result away, so cube(2) returns None.

def cube(x):
    Calculate the cube of x.
    return x ** 3 
