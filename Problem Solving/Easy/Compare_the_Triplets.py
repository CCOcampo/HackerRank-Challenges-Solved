def compareTriplets(a, b):
    na = sum(1 for x, y in zip(a, b) if x > y)
    ba = sum(1 for x, y in zip(a, b) if x < y)
    return [na, ba]

#Example
a = [1, 2, 3]
b = [3, 2, 1]
print(compareTriplets(a, b))