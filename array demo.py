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
    return arr.insert(value, index)

insertion(arr1 ,9 ,2)

# extending

def extending(arr,arr2):
    return arr.extend(arr2)

extending(arr1,[9,10,11])
print(arr1)

#pop method

arr1.pop()
print(arr1)

#reverse method

arr1.reverse()
print(arr1)

#count()

def counting(arr, val):
        return arr.count(val)
print(counting(arr1, 6))

#add items from list

temp = [20,30,25]
arr1.fromlist(temp)
print(arr1)