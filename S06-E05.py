N = int(input('which fibbo number? '))
def F(X):
    if X == 1:
        return 0
    if X == 2:
        return 1
    else:

        Result = F(X - 1) + F(X - 2)
        return Result

print(F(N))


# 0, 1,1,2,3,5,8,13,21,34, 55, 89, 144
