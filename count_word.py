# Write a function that takes a string as parameter and returns the number of words in that string.

a = input("Enter your sentence = ")


def count(a):
    s = 0
    for i in a:
        if i == ' ':
            s = s + 1
    return s


res = count(a)
print("Number of word in that string = ", res + 1)
