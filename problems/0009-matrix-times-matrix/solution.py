def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    
    b_t = list(zip(*b))
    
    return [[sum(x * y for x, y in zip(row_a, col_b)) for col_b in b_t] for row_a in a]