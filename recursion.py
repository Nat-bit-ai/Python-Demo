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