# Write a function that takes a number a parameter and return its factorial.
input_number = int(input("Drop a positive number to check factorial = "))

print("\n")


def fct(n):
    iv = 1
    for i in range(1, n + 1):
        iv = iv * i
    return iv


p = fct(input_number)

print("The factorial of ", input_number, "is =", p)
print("\n")

