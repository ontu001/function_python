# Write a function that returns the minimum , maximum and the avarage value  of an array passed as a parameter.

n = int(input("How many value do you want = "))
arr =[]
for i in range(1, n+1):
    v = int(input("Inter your value = "))
    arr.append(v)


def cal(i):
    a = max(i)
    b = min(i)


    return a, b

c = cal(arr)

print(" So the maximum and minimum value is = ", c)