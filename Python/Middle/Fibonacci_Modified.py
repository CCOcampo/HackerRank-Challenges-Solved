import sys
def fibonacciModified(t1, t2, n):

    sys.set_int_max_str_digits(10**6)
    for i in range(n-2):
        t3 = t1 + (t2**2)
        t1=t2
        t2=t3

    return t2

#Example
t1=1
t2=2
n=20
print(fibonacciModified(t1, t2, n))