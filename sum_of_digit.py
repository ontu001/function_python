# Write a function that takes a number a parameter and return the sum of digits.
ds = int(input("Drop your digit = "))

print("\n")


def sum(a):
    summ = 0
    while a > 0:
        d = a % 10
        summ = summ + d
        a = a // 10
    return summ


value = sum(ds)
print("Sum of your digit is  = ", value)

print("\n") 