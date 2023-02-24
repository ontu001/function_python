# Write a function that takes a number a parameter and returns their HCF.
a = int(input("Input your 1st number = "))
b = int(input("Input your 2nd number = "))

print("\n")


def hcf(a, b):
    if a > b:
        s = a
    else:
        s = b

    for i in range(1, s + 1):
        if (a % i == 0) and (b % i == 0):
            h = i
    return h


v = hcf(a, b)

print("Height common factor = ", v)
print("\n")


