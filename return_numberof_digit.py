# Write a function that takes a number a parameter and return the number of digits.
input_number = int(input("input your digit = "))

print("\n")


def count(a):
    c = 0
    while a != 0:
        a = a // 10
        c += 1
    return c


value = count(input_number)
print("The number of digit is = ", value)

print("\n") 