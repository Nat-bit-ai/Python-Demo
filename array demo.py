#1 create an array and traverse

from array import *
arr1 = array('i', [1,2,3,4,5,6])

def traverse(arr):
    for i in arr:
        print(i)
traverse(arr1)

def access(arr , value):
    for i in arr:
        if i == value:
            print(arr.index(value))
access(arr1 , 3)