import math
# find all prime numbers below 20
list1 = []
list2 = []
list3 = []
n = int(input('Enter a number'))


def prime(n):
    global list1
    for i in range(1, n+1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            list1.append(i)


prime(n)
print('all prime numbers upto n', list1)

# find all powers of 2 and 3 below 20
for i in range(2, n):
    p2 = i**2
    p3 = i**3
    if(p2 < n):
        list2.append(p2)
        if (p3 < n):
            list2.append(p3)

print('powers less than n', list2)

print(list2)

list1 = list1+list2
print('list with prime and power', list1)

# calclate which terms to remove
if (i > 1):
    for i in list2:
        s = int(math.sqrt(i))
        c = int(i**(1/3))

        list3.append(s)
        list3.append(c)

print(list3)

# remove all duplicates
res = []
for i in list3:
    if i not in res:
        res.append(i)
print(res)

print("The list after removing duplicates : " + str(res))

# from list 1 if there are common lcm of any of elemets remove it
for i in range(len(res)):
    list1.remove(res[i])

# multiply all the prime numbers and powers
print('final list ', list1)


def answer(list1):
    result = 1
    for x in list1:
        result = result*x
    return result


print(answer(list1))
