from random import  randint


number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range (number):
    list.append(randint(0, 9))

for i in range (len(list)):
    while  number < len(list)/2 and number > len(list)/2:
        number  = number - 1
        a = list[i] * list[number]
        list2(list.append())
        i += 1

print(list)
print(list2)