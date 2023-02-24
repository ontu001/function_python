'''
Write a function that takes a number and a
character as a parameter and prints a triangle of that size using the specified character.
'''

#method1
shape_number= int(input("Drop your value for the triangle ="))
shape_character= input("Drop any character for the shape design = ")


def triangle(x,y):
    k=0
    for i in range (1,x+1):
        for space in range(1,(x-i)+1):
            print(end=" ")
        while k!=(2*i-1):
            print(y , end="")
            k+=1
        k =0
        print()




triangle(shape_number,shape_character)


#method 2


a=int(input("Drop your value for triangle range ="))
b=input("Drop your character for design/shape = ")
def triangle(size, character):
    for i in range(size):
        print((size-i-1) * " " + (2*i+1) * character)

        
triangle(a,b)




#method3

digit = int(input("Input a number for your triangle = "))
character = input("Input any character = ")

print(" \n ")


def add(x, y):
    for a in range(x):
        for b in range(x - a - 1):
            print(" ", end="")
        for b in range(a + 1):
            print(y, end=" ")
        print()


add(digit, character)

print(" \n ")