x = 3
print(x)

x = 4
print(x)

x = [3]
print(x)

x = (["Oranges", "Grapes"])
print(x)

x = "Oranges", "Grapes"
print(x)
# Tuples are 'lists' but without brackets, or with parentheses

x = "Oranges", "Grapes"
print(x[0])

# Note that a negative index starts from the back of the list and works from right to left, with -1 representing the last value, -2 representing the second to last value, etc...

x = [5, 8, 1, 6, 8]
print(x[2])

x = [5, 8, 1, 6, 8]
x[1] = 100
print(x)

# Tuples do not support item assignment, tuples are immutable and cannot be changed

x = (5, 8, 1, 6, 8)
print(x)

x = (6, 3, 1)
print(x)

x = []
print(x)

my_list = [4, 1, 8, 4, 1]
print(x)

for item in my_list:
    print(item)

    # for item in my_list:

my_list = [[2, 3], [4, 6], [2, 1]]
print(my_list)

for item in my_list:
    print(item)

print(my_list)

my_list = [2, 3, 4,6, 2, 1]

for i in range(6):
    print(ny_list[i])

print()

for item in my_list:
    print(item)

my_list = [2, 3, 4, 6, 2, 1, 9, 10]
print(my_list)

my_list.append("Rabbits")
my_list.append("Carrots")

print(my_list)

my_list = [3, 6, 5]
# my_list.append(3, 4)
# Note that the above will create an error
my_other_list = [3, 4]
my_list.extend(my_other_list)
print(my_list)

my_list = []

for i in range(5):
    user_input = input("Enter an integer: ")
    user_input = int(user_input)
    my_list.append(user_input)

print(my_list)

my_list = [0] * 100
print(my_list)

my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

list_total = 0

for item in my_list:
# for i in tange(len(my_list)):
# This is also acceptable, but more complicated
    list_total += item

print(list_total)

my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

for i in range(len(my_list)):
    my_list[i] += 1

print(my_list)

for item in my_list:
    item += 1

my_list = "Hello there!"

print(len(my_list))
print(my_list[-1])

print(my_list[:5])
print(my_list[5:])

my_list = "0123456789"

print(my_list[:3])
print(my_list[3:])
print(my_list[3:6])

x = "Hi!" * 5

x = "Hi!"
y = "There"
print(x * 5 + y * 2)

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))

result = months[(n - 1) * 3:(n - 1) * 3 + 3]

print(result)