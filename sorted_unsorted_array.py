'''
Write a function that sorts an array of numbers. I the main function , first create and print the unsorted array ,then
use
the
function
to
sort
the
array, then
prin
the
sorted
array. '''

n = int(input("How many value do you want = "))
arr =[]
for i in range(1, n+1):
    v = int(input("Inter your value = "))
    arr.append(v)


def list(a):
    print("Unsorted array = ", a)

    y = sorted(a)  # here i sorted the array in decending order
    print("Sorted array = ", y)


list(arr)
