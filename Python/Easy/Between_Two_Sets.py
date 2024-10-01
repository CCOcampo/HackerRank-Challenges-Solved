def getTotalX(a, b):
    res = 0
    for i in range(max(a), min(b) + 1):
        is_multiple_of_a = all(i % aa == 0 for aa in a)
        is_divisor_of_b = all(bb % i == 0 for bb in b)
        if is_multiple_of_a and is_divisor_of_b:
            res += 1
            
    return res