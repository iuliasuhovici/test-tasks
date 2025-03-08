# НОД чисел
'''
def nod(a, b):
    while b:
        a, b = b, a%b
    return a

print(nod(56,98))
'''

# Простое число
import math

def check(n):
    if n <=1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

print(check(2))
print(check(29))
print(check(93))

