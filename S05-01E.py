C=[0, 1]
    F = int(input('enter a number '))
    for i in range(2,F):
    C.append(C[i-1]+C[i-2])
    return F

print(C)
