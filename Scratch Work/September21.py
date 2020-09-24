# # Lists
# my_list = [3, 8, 1, 0]
# print(my_list[-1])
#
# my_list = 3, 8, 1, 0
# for my_item in my_list:
#     print(my_item)
#
# for i in range(len(my_list)):
#     print(my_item[i])

# Secret codes
plain_text = "This is a test. ABCD abcd"

for character in plain_text:
    # print(character)
    my_val = ord(character)
    my_val += 1
    my_char = chr(my_val)
    print(my_char, end=' ')

print()
encrypted_text = "U i j t ! j t ! b ! u f t u / ! B C D E ! b c d e "

for character in encrypted_text:
    # print(character)
    my_val = ord(character)
    my_val -= 1
    my_char = chr(my_val)
    print(my_char, end=' ')

class Character:
    """This describes the class."""

    def __init__(self):
        """ This is a method auto-called when created"""

        # Create attribute
        self.name = ""
        self.outfit = ""
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.armor_amount = 0
        self.max_speed = 0