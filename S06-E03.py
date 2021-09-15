names =[]
while True:
    name = input('please entre 6 of your collugues: ')
    names.append(name)
    if len(names) > 5:
        break

print (names)
index = names.index('Mehrnaz')
print('Mehnaz index is {}' .format(index))
name = input('please entre new name; ')
if name not in names:
    print('-1')
