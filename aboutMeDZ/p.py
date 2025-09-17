a = list(range(1, 1001))
b = 0
for i in a:
    if i == 0:
        i = 0
    elif i > 0 and i / 2 == i // 2:
        i = i / 2
        if i == 3:
            b = b + 1
    else:
        i = 1 + (i - 1)
        if i == 3:
            b = b + 1
print(b)