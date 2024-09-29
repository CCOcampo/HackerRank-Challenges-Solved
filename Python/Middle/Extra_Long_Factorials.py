import sys
def extraLongFactorials(n):
    mult = 1
    sys.set_int_max_str_digits(100000)  
    while n != 1:
        mult *= n
        n -= 1
    print (mult)

# Example
print(extraLongFactorials(25))
    