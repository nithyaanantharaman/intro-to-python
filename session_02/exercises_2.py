# Session 2 Exercises
#name = input("Whats your name")
#print (("Hello ") + name)

#age = int(input("whats your age"))
#age_in_10_years =age + 10
#print ("Your age in 10 years: "+ #str(age_in_10_years))

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
#length = float(input("what is the length"))
#breadth =float(input("what is the breadth")) 
#area = length * breadth
#print ("Area of the rectangle:" + str(area))


# 2. Write code that prints the length of the string, 'python'.
#print (len("python"))


# 3. Print out the first and third letter of the word 'python'.
#print ("python"[0])
#print ("python"[2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.
#name = input("whats your name")
#print ("Hello " + name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
#age = int(input("whats your age"))
#age_in_15_years =age + 15
#print ("Your age in 15 years: "+ #str(age_in_15_years))


# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
#name = input("whats your name")
#age = int(input("whats your age"))
#print ("Hello " + str (name) + "You are currently " + str(age) + "years old")
#age_in_15_years =age + 15
#print ("In 15 years you will be " + str(age_in_15_years))

# 7. Ask the user to enter their hometown, print it out in uppercase letters.
#hometown = input("enter your hometown")
#print (hometown.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
#fav = input("enter your fav colour")
#print(len(fav))


# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
#weather = input("whats the weather today")
#month = input ("whats the month")
#print("It is month " + month + "and the weather today is " + weather)



# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
#month = input("What month is it?\n")
#temp1 = int(input("What was the temperature on Monday?\n"))
#temp2 = int(input("What was the temperature on Tuesday?\n"))
#temp3 = int(input("What was the temperature on Wednesday?\n"))
#temp4 = int(input("What was the temperature on Thursday?\n"))
#temp5 = int(input("What was the temperature on Friday ?\n"))
#avg = (temp1 + temp2 + temp3 + temp4 + temp5)/5
#print("It is month" + month + "and the aveg temp is " + str(avg))

# 11. Print out the above sentence but make the month upper case.
#print("It is month" + month.upper() + "and the aveg temp is " + str(avg))


# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
#favanimals ="My favourite animals:\n\tCats,\n\tDogs"
#print(favanimals)

# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
#name = input("What is your name?\n")
#number = int(input("Enter a number:\n"))
#print(name[number].upper())

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
string = "WelcometoPython"
print(len(string))
print(string[1:14:2])