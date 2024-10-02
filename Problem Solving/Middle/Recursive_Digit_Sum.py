'''En este ejercicio utilize time.time para buscar un codigo 
que fuera mas recursivo teniendo en cuenta el tiempo necesario
para su ejecución 
'''

import time
start_time = time.time()

def superDigit(n, k):
    def digit_sum(x):
        return sum(int(digit) for digit in x)
    initial_sum = digit_sum(str(n))
    initial_sum *= k
    def super_digit(x):
        while x >= 10:
            x = digit_sum(str(x))
        return x
    return super_digit(initial_sum)


#Example
n=5231048538923
k=33
print(superDigit(n,k)) 

end_time = time.time()
elap = end_time - start_time
print(f"tiempo requerido para ejecutar el codigo es de {elap} sec")