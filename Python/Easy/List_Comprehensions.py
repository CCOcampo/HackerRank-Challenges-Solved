if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res = []

    for a in range(x + 1):
        for b in range(y + 1):
            for c in range(z + 1):
                if (a + b + c) != n:
                    res.append([a, b, c])
    print(res)
