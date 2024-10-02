def diagonalDifference(arr):
    n = len(arr)
    diag = 0
    diagl = 0
    for i in range(n):
        diag += arr[i][i]
        diagl += arr[i][n-i-1]
    diagonal = abs(diag - diagl)
    return diagonal

#Example
arr = [
    [11, 2, 4],
[4, 5, 6],
[10, 8, -12]
]

print(diagonalDifference(arr))