def roman(a):
    otvet = ""
    sot = a // 100
    if sot == 9:
        otvet += "CM"
    elif sot == 10:
        otvet += "M"
    else:
        otvet += "C" * sot
    a = a % 100
    pit = a // 10
    if pit == 9:
        otvet += "XC"
    elif pit == 5:
        otvet += "L"
    elif pit == 4:
        otvet += "XL"
    elif 6 <= pit and pit <= 8:
        otvet += "L" + "X" * (pit - 5)
    else:
        otvet += pit * "X"
    a = a % 10
    if a == 5:
        otvet += "V"
    elif a == 9:
        otvet += "IX"
    elif a == 4:
        otvet += 'IV'
    elif 6 <= a and a <= 8:
        otvet += "V" + "I" * (a - 5)
    else:
        otvet += a * "I"
    return otvet
a = int(input("Введите число: "))
print(roman(a))

#import math
#
#def solve(f):
#    a = int(f[0])
#    b = int(f[1])
#    c = int(f[2])
#    d = b**2 - 4 * a * c
#    if d > 0:
#        x1 = (-b + math.sqrt(d)) / 2 * a
#        x2 = (-b - math.sqrt(d)) / 2 * a
#        return x1, x2
#    elif d == 0:
#        x = -b / 2 * a
#        return x
#    else:
#        x3 = "Корней нет"
#        return x3
#f = input("Введите 3 числа: ")
#f = f.split()
#print(solve(f))

# a = 0
# b = []
# def partial_sums(b):
#     c = [0]
#     d = 0
#     for i in b:
#         d = i + d
#         c.append(d)
#     return c
#
# while a != "A":
#     a = input('Введите число, для окончания списка введите A: ')
#     if a == "A":
#         break
#     else:
#         a = int(a)
#         b.append(a)
# print(partial_sums(b))

# c = []
# b = set()
# a = 0
# while a != 'A':
#     a = input('Введите число: ')
#     if a == 'A':
#         break
#     else:
#         a = int(a)
#         b.add(a)
#         c.append(a)
# listt = len(c)
# sett = len(b)
# tf = False
# if listt > sett:
#     tf = True
# print(tf)

# keey = 0
# maxx = 0
# b = {}
# a = input()
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# for key, value in b.items():
#     if value > maxx:
#         maxx = value
#         keey = key
# print(keey)

# b = ""
# a = input("Введите строку: ")
# a = a.split()
# for i in a:
#     b = b + i
# b = len(b)
# print(b)

# c = 0
# b = []
# a = 0
# d = []
# while a != 'A':
#     a = input('Введите число: ')
#     if a == 'A':
#         break
#     else:
#         a = int(a)
#         b.append(a)
# for i in b:
#     if c == 0:
#         c = c + i
#     else:
#         if c != i:
#             f = c + i
#             d.append(f)
#             c = i
# print(d)

#def tyt(a):
#    f = []
#    i = 2
#    while a != 1:
#        if a % i == 0:
#            a = a / i
#            f.append(i)
#        else:
#            i = i + 1
#    return f
#
#a = int(input("Введите число: "))
#print(tyt(a))

# a = []
# b = 0
# while b != 'A':
#     b = input("Введите A для оканчания списка")
#     if b == 'A':
#         break
#     else:
#         b = int(b)
#         a.append(b)
# g = False
# for n,i in enumerate(a):
#     d = a.copy()
#     e = d.pop(n)
#     print(a)
#     print(d)
#     for f in d:
#         if f == e:
#             g = True
#             break
# print(g)
from os.path import split

#def fn(n,s):
#    for v,l in n.items():
#        if l == s:
#            return v
#n = {}
#a = input("Введите текст")
#maxs = ""
#a = a.split()
#for i in a:
#    if i in n:
#        n[i] = n[i] + 1
#    else:
#        n[i] = 1
#    f = len(i)
#    if f > len(maxs):
#        maxs = i
#print(maxs)
#print(fn(n,max(n.values())))

# nums = [0]
# c = 0
# n= 0
# while n != -1:
#     n = int(input("Введите число: "))
#     if n == -1:
#         break
#     nums.append(n)
# i = int(input('Введите число i: '))
# for f,n in enumerate(nums):
#     print(f, n)
#     if f != 0:
#         if i % f == 0:
#             n = n ** 2
#             c = c + n
# print(c)