#  Take input from User and generate factorial result
z = 1
x = int(input("Please enter your number :  - "))
while (x > 0):
    z = z * x
    x = x - 1
print("Factorial result is : " + str(z))
