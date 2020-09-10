# # Chapter 10 - If statements
#
# a = 5
# b = 5
#
# if a < b:
#     print("a is less than b.")
#
# if a > b:
#     print("a is greater than b")
#
# if a <= b:
#     print("a is less than or equal to b")
#
# if a >= b:
#     print("a is greater than or equal to b")
#
# if a == b:
#     print("a is equal to b")
#
# if a != b:
#     print("a is not equal to b")
#
# if not a == b:
#     print("AAAA")
#
# print("Done")
#
# a = 5
# b = 5
#
# if a == 5:
#     print("Do something")
#     print("Do something 2")
#
#     if b == 5:
#         print("Do something 3")
#
# print("Done")
#
# if a == 5 and b == 5:
#     print("They are the same")
#
# if a ==5 or b == 5 or c == 5:
#     print ("Do something")
#
# # if a > 5 and < 15:
# if a > 5 and a < 15:
#
# #Wednesday September 9
# a = 5
# b = 4
#
# if a > b:
#     print("A is bigger than b")
#
# if a == b:
#
# a = True
#
# if a:
#     print("A is true")
#
# a = True
# b = True
#
# if a and b:
#     print("Yes")
#
# a = 3
# b = 3
# c = a == b
#
# print(c)
#
# if 1:
#     print("True")
#
# if 100:
#     print("Ture")
#
# if "A":
#     print("True")
#
# Any character or string of characters is considered true.
# Note that 0 is not a value, so it is not true. Also, an empty string "", and None, are considered false

# The input function

# temperature = input ("What is the temperature in Fahrenheit? ")
# temperature = float(temperature)
# print("The temp is", temperature)
#
# if temperature > 90:
#     print("It is hot outside!")

# Convert what the user types in into a number

# temperature = float(input("What is the temperature in Fahrenheit? "))
#
# print("The temp is", temperature)

# if temperature > 90:
#     print("It is hot outside!")
# # elif temperature > 110
# #   print("You can fry eggs on the sidewalk!")
# elif temperature < 30:
#     print("It is cold outside.")
# else:
#     print("It is not so hot outside.")

# Note that either of the above methods would work

# if temperature > 30:
#     print("A")
# if temperature <= 30:
#     print("B")

#  note that the following is the same as:

# if temperature > 30:
#     print("A")
# else:
#     print("B")

# this code saves a bit of time

# user_name = input("What is your name? ")
#
# if user_name.lower() == "paul" or user_name.lower() == "pauline":
#     # it is very important that you restate the function otherwise the right side will mean true and that any ture input will return the true response
#     print("You have a nice name.")
# else:
#     print("Your name is ok, I guess.")

# Note the two equal signs and the quotation marks

# Looping

repeat = int(input("How many pleases? "))
for i in range(repeat):
    # print("I will not chew gum in class.")
    print("Please,")
print("... can I get the new Lego Hogwarts set.")