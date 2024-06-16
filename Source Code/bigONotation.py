def addUp1(n):
    sum = n * (n + 1) / 2
    return sum

def addUp2(n):
    sum = 0
    for i in n:
        sum += i
    return sum

print(addUp1(1234567))
print(addUp2(range(1234567)))