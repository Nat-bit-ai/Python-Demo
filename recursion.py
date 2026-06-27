# sum of digits base k
def sumOfDigits( n, k):
    assert n>=0 and int(n) == n , 'integer input only'
    if n == 0:
        return 0
    return n%k + sumOfDigits(n//k , k)
print(sumOfDigits(7,2))
# Decimal to Binary
def decToBin(n):
    assert n >= 0 and int(n) == n, 'integer input only'
    if n == 0:
        return 0
    return n%2 + 10*decToBin(n//2)
print(decToBin(10))
#Factorial
def fac(n):
    assert n > 0 and int(n) == n, 'integer input only'
    if n==0 or n==1:
        return 1
    return n*fac(n-1)
print(fac(5))
#fibonacci
def fib(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))
#GCD
def GCD(a,b):
    if b == 0:
        return a
    return GCD(b, a%b)
print(GCD(48,18))
#power of 2
def pow2(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return pow2(n // 2)

print(pow2(8))
#power of 3
def pow3(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return pow3(n // 3)

print(pow3(8))

#power of 4
def pow4(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 != 0:
        return False
    return pow4(n // 4)

print(pow4(8))


