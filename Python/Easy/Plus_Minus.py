def plusMinus(arr):
    n = len(arr)
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    zer = sum(1 for x in arr if x == 0)

    pos = pos / n
    neg = neg / n
    zer = zer / n

    print(f"{pos:.6f}")
    print(f"{neg:.6f}")
    print(f"{zer:.6f}")

#Example

arr = [-4, 3, -9, 0, 4, 1]
print(plusMinus(arr))