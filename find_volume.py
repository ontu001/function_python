# Write a function that takes the radius of a sphere as a parameter and returns its volume.
rad = float(input("Enter your radius = "))

print(" \n ")


def res(x):
    pi = 3.141592653589793238
    volume = 4 / 3 * (pi * x * x * x)

    return volume


result = res(rad)
print("Volume of the sphere = ", result)

print(" \n ")