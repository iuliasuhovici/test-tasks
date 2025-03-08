# Фиббоначи

def fibbonacci(n):
    if n <= 1:
        return n
    return fibbonacci(n-1) + fibbonacci(n-2)

print (fibbonacci(6))
