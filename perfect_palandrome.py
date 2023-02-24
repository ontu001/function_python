# Write a function that checks if a number is prime or not. If the number is prime the functions return true, otherwise false. Also try functions for checking perfect numbers and palindromes.
a = int(input("Input your digit to check if prime or not = "))

print("\n")


def prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
            break
    else:
        return True


v = prime(a)
print("Prime number = ", v)


def perfect(a):
    s = 0
    for i in range(1, a, 1):
        if a % i == 0:
            s = s + i
    if s == a:
        return True
    else:
        return False


p = perfect(a)
if p:
    print(a, "Is a perfect number")
else:
    print(a, "Is not a perfect number")


def pal(a):
    temp = a
    reverse = 0

    while a > 0:
        d = a % 10
        reverse = reverse * 10 + d
        a = a // 10
    if temp == reverse:
        return True
    else:
        return False


pl = pal(a)
print("palindrome =", pl)

print("\n")
