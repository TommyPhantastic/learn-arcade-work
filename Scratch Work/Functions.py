# Create functions

# Why create functions?
# Make code easier to read
# Abstract our code
# Re-use
# Divide complex problem into small one
# Make code easier to maintain


def print_hello():
    print("Hello!")


def print_goodbye():
    print("Goodbye!")


def print_number(my_number):
    print(my_number)


def add_numbers(a, b):
    # print(a + b)
    return a + b

def main():
    # print_hello()
    # print_hello()
    # print_goodbye()
    # print_number(6)
    # print_number(12)
    # add_numbers(12, 5)
    # result = add_numbers(12, 5)
    # print(result)

if __name__ == "__main__":
    main()

def volume_cylinder(radius, height):
    pi = 3.14159265
    volume = pi * radius ** 2 * height
    return volume

result = volume_cylinder(3, 6) * 6
print(result)