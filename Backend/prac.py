from random import randint
n = int(input("Enter number of elements:"))
list1 = []
for i in range(n):
    list1.append(int(input("Enter element:")))

val = True

while val:
    i = randint(0, n-1)
    j = randint(0, n-1)
    list1[i] , list1[j] = list1[j], list1[i]
    for k in range(0, n-1):
        if list1[k] > list1[k+1]:
            val = False

    if val:
        break
    else:
        val = True

print(list1)


    