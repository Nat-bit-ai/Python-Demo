# sum of digits base k
def sumOfDigits( n, k):
    assert n>=0 and int(n) == n , 'integer input only'
    if n == 0:
        return 0
    return n%k + sumOfDigits(n//k , k)
print(sumOfDigits(7,2))
