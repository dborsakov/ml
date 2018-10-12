import math

def fac(x):
    result = 1
    i=1
    while i<x+1:
        result *= i
        i+=1
    return result

def fib(n):
    if (n==0): return 0
    if (n==1): return 1

    return(fib(n-1)+fib(n-2))

print( fac(8)/fib(17)* math.pi)
