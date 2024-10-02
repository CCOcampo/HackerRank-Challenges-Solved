def miniMaxSum(arr):
    suma=0
    for i in range(len(arr)):
        suma += arr[i]
    print(suma-max(arr), suma-min(arr))
#Example
arr = [-4, 3, -9, 0, 4, 1]
print(miniMaxSum(arr))