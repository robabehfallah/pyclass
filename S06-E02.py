def fibonacci():

    X1 = 0
    X2 = 1
    Fibbo = int(input('enter a number '))
    for i  in range(Fibbo - 2):
        X3 = X1 + X2
        X1 = X2
        X2 = X3
    return X3
print(fibonacci())



# 0, 1,1,2,3,5,8,13,21,34, 55, 89, 144
