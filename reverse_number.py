
# Write a function that takes a number a parameter and return the reverse number.

x = int(input("Drop your digit to Reverse = "))

print("\n")


def rev(a):
    d = 0
    r = 0
    while a > 0:
        d = a % 10
        a = int(a / 10)
        r = r * 10 + d
    return r


value = rev(x)
print("Your input digit is = ", x)
print("Reverse value is  = ", value)

print("\n")

