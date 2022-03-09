#Programming Question 2:
#Take name of the User
#Take Marks of Maths, Science and English from User
#Find percentage of given marks, Display,
#User name is <NAME>, Scored <PERCENTAGE>  % in exams

#Solution

# Take Name from User
name= input("Please enter your name : -  ")

# Take Math marks from User
maths= input("Please enter your Maths marks : -  ")

# Take Science marks from User
science= input("Please enter your Science marks : -  ")

# Take English marks from User
english= input("Please enter your English marks : -  ")

percentage = (int(maths) + int(science) + int(english))/3
print( "User name is " + name + ", Scored " + str(percentage) +"% in exams" )