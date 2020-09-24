# I love text based games and I'm super excited to make this one! We didn't get to make this type of game in Professor's Brodie's class last semester, but this seems really up my alley!
# Honestly, I wanted to make a text-based game for my final project in that class, but the game had to be animated, so I wasn't able to make a game like this for the class and we never really covered text adventures..

import random


def main():
    print("Welcome to Celadon City!")
    print("You've found Team Rocket's base of operations and have freed the captured Pokemon. HOORAY!!")
    print("Unfortunately as you are just escaping, a Team Rocket Grunt alerts the hideout and you must flee"
          " lest they catch you! ")
    print("One Rocket Grunt may be enough to handle, but a whole hideout? Ride atop Arcanine and make it to safety!!!")
    # done = False


main()


done = False
milesTraveled = 0
nativesTraveled = -20
arcanineTiredness = 0
thirst = 0
canteen = 3
oasis = -1

while done is False:
    print("A. Drink a bottle of Fresh Water.")
    # Please don't dock points for the apparent random capitalization, 'Fresh Water' is in in-game item in the Pokemon video game series.
    print("S. Use Quick Attack!")
    print("D. Use Extreme Speed!")
    print("Z. Use a Max Elixir.")
    print("X. Status Check")
    print("C. Quit the game.")
    print()

input("What is your choice? ")
