# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
#name = input("Enter your name")
#if name =="Bob":
# print ("Welcome Bob!")



# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
#name = input("Enter your name")
#if name !="Alice":
  #print ("You are not Alice!")


# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
#password = input("Enter your password")
#if password =="qwerty123":
#  print ("You have successfully logged in")


# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".



# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
#num1 = int(input("enter first number\n"))
#num2 =int(input("enter second number\n"))
#total = num1+num2
#if (total>21):
 # print("Bust")
#else:
  #  print("Safe")


# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
#length = int(input("enter length \n"))
#breadth = int(input("enter breadth \n"))
#if (length==breadth):
#  print ("square")
#else:
 # print("not a square")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
#sal = int(input("your current sal"))
#yrs = int(input("how long is your current service"))
#if yrs>=3:
 # print ("you are getting a bonus")


# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
#whole = int(input("your whole number"))
#if (whole>=0):
  #print (whole**3)
#else:
 # print(whole/2)
  



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
#name = input("What is your name?\n")

#if name == "Alice":
   # print("Hello, Alice!")
#elif name == "Bob":
    #print("You're not Bob! I'm Bob..")
#else:
    #print("You must be Charlie!")


# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
#age = int(input("How old are you?\n"))

#if age == 0:
 # print ("You're not born yet!")
#elif age < 11:
# print("You're too young to go to this school")
#elif age >= 11 and age <= 16:
  #print ("You can can come to this school")
#elif age > 16:
  #print ("You're too old for school")
#else: 
  #print("You have not entered your age...")


# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
#month = input("Pick a month:\n")

#if month == "March" or month == "April" or month == "May":
 #   print(month + " is in Spring")
#elif month == "June" or month == "July" or month == "August":
 #   print(month + " is in Summer")
#elif month == "September" or month == "October" or month == "November":
#    print(month + " is in Autumn")
#elif month == "December" or month == "January" or month == "February":
#    print(month + " is in Winter")
#else:
 #   print("I don't know")


# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
#number_1 = int(input("Input a number:\n"))
#number_2 = int(input("Input another number:\n"))

#if (number_1 % 2 == 0 and number_2 % 2 == 0):
#    print("Both numbers are even.")
#elif (number_1 % 2 == 1 and number_2 % 2 == 1):
 #   print("Both numbers are odd.")
#else:
#    print(number_1 * number_2)


# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
#number1 = int(input("Please input a number:\n"))
#number2 = int(input("Please input another number:\n"))

#if number1 > number2:
 # print(str(number1) + " has the highest value")
#else: 
 # print(str(number2) + " has the highest value")


# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
#salary = int(input("What is your current salary?\n"))
#years_of_service = int(input("How many years have you worked here?\n"))

#if years_of_service > 7:
#  print("Your current salary is " + str(salary)+ ", your bonus is " + str(salary*0.2))
#elif years_of_service > 5:
#  print("Your current salary is " + str(salary)+ ", your bonus is " + str(salary*0.15))
#elif years_of_service >= 3 and years_of_service <= 5:
 # print("Your current salary is " + str(salary)+ ", your bonus is " + str(salary*0.1))
#else:
 # print("Your current salary is " + str(salary)+ ", you get no bonus.")


# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.
#name1 = input("What is your name?\n")
#age1 = int(input("How old are you?\n"))
#name2 = input("What is your name?\n")
#age2 = int(input("How old are you?\n"))
#name3 = input("What is your name?\n")
#age3 = int(input("How old are you?\n"))

#Oldest
#if age1 > age2 and age1 > age3:
 # print(name1 + "is the oldest and is " + str(age1) + "years old.")
#elif age2 > age1 and age2 > age3:
 # print(name2 + "is the oldest and is " + str(age2) + "years old.")
#elif age3 > age1 and age3> age2:
 # print(name3 + "is the oldest and is " + str(age3) + "years old.")
#else:
#  print("You are all the same age")

#Youngest
#if age1 < age2 and age1 < age3:
#  print(name1 + "is the youngest and is " + str(age1) + "years old.")
#elif age2 < age1 and age2 < age3:
 # print(name2 + "is the youngest and is " + str(age2) + "years old.")
#elif age3 < age1 and age3 < age2:
#  print(name3 + "is the youngest and is " + str(age3) + "years old.")
#else:
#  print("You are all the same age")



# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
lesson1 = input("Input your lesson:\n")
mark1 = int(input("Input your mark:\n"))
lesson2 = input("Input your lesson:\n")
mark2 = int(input("Input your mark:\n"))
lesson3 = input("Input your lesson:\n")
mark3 = int(input("Input your mark:\n"))

print("REPORT CARD:")

#Lesson 1
if mark1 > 80:
  print(lesson1 + " - A grade")
elif mark1 <= 80 and mark1 > 60:
  print(lesson1 + " - B grade")
elif mark1 <= 60 and mark1 > 50:
  print(lesson1 + " - C grade")
elif mark1 <= 50 and mark1 > 45:
  print(lesson1 + " - D grade")
elif mark1 <= 45 and mark1 > 25:
  print(lesson1 + " - E grade")
elif mark1 < 25:
  print(lesson1 + " - F grade")
else:
  print("Go to see your teacher")

#Lesson 2
if mark2 > 80:
  print(lesson2 + " - A grade")
elif mark2 <= 80 and mark2 > 60:
  print(lesson2 + " - B grade")
elif mark2 <= 60 and mark2 > 50:
  print(lesson2 + " - C grade")
elif mark2 <= 50 and mark2 > 45:
  print(lesson2 + " - D grade")
elif mark2 <= 45 and mark2 > 25:
  print(lesson2 + " - E grade")
elif mark2 < 25:
  print(lesson2 + " - F grade")
else:
  print("Go to see your teacher")

#Lesson 3
if mark3 > 80:
  print(lesson3 + " - A grade")
elif mark3 <= 80 and mark3 > 60:
  print(lesson3 + " - B grade")
elif mark3 <= 60 and mark3 > 50:
  print(lesson3 + " - C grade")
elif mark3 <= 50 and mark3 > 45:
  print(lesson3 + " - D grade")
elif mark3 <= 45 and mark3 > 25:
  print(lesson3 + " - E grade")
elif mark3 < 25:
  print(lesson3 + " - F grade")
else:
  print("Go to see your teacher")