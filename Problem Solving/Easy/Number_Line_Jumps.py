def kangaroo(x1, v1, x2, v2):
    if (x1 < x2 and v1 <= v2) or (x1 > x2 and v1 >= v2):
        return 'NO'
    if v1 != v2 and (x2-x1) % (v1-v2) == 0:
        return 'YES' 
    else:
        return 'NO'

#Example

print(kangaroo(0, 2, 5, 3))