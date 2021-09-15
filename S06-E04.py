Adad = []
while True:
    y = int(input('please entre 4 numbers: '))
    Adad.append(y)
    if len(Adad) >= 4:
        break

print (Adad)
list_num = len(Adad)
list_num2 = len(Adad)
temp = []
for k in range(list_num2):
    MAX = Adad[0]
    for i  in range(list_num):
        if MAX < Adad[i]:
            MAX = Adad[i]
        #print(MAX)

    temp.append(MAX)
    Adad.remove(MAX)
    list_num = list_num - 1


print(temp)
