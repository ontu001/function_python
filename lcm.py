
# Write a function that takes a number a parameter and returns their LCM.
a = int(input("Input your 1st number = "))
b = int(input("Input your 2nd number = "))

print("\n")


def lcm(a, b):
    if a > b:
        g = a
    else:
        g = b

    while (True):
        if (g % a == 0) and (g % b == 0):
            l = g
            break
        g += 1
    return l


v = lcm(a, b)

print("Least common multiple = ", v)
print("\n") 