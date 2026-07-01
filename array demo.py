#1 create an array and traverse

from array import *
arr1 = array('i', [1,2,3,4,5,6])

def traverse(arr):
    for i in arr:
        print(i)
traverse(arr1)

 #accessing elements through index

def access(arr , value):
    for i in arr:
        if i == value:
            print(arr.index(value))
access(arr1 , 3)

#appending value

def appends(arr , val):
    return arr.append(val)

appends(arr1,7)

# insertion

def insertion(arr, value, index):
    return arr.insert(index, value)

insertion(arr1 ,9 ,2)