# Lab 04: Camel game
import random

def main():
    # Introduction
    print("Welcome to Celadon City!")
    print("You've found Team Rocket's base of operations and have freed the captured Pokemon. HOORAY!!")
    print("Unfortunately as you are just escaping, a Team Rocket Grunt alerts the hideout and you must flee"
          " lest they catch you! ")
    print("One Rocket Grunt may be enough to handle, but a whole hideout? Ride atop Arcanine and make it to safety!!!")


    done = False
    milesTraveled = 0
    nativesTraveled = -20
    arcanineTiredness = 0
    thirst = 0
    freshWater = 3
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

        userInput= input("What is your choice? ")

        # Check to see if they want to quit
        if userInput.upper() == "C":
            done = True
            print("You resigned yourself to defeat and have been captured by Team Rocket. They hold you hostage and then you beecome a Team Rcket Grunt, yourself!")

        # Status Check
        elif userInput.upper() == "X":
            print("Miles traveled:", milesTraveled)
            print("Fresh Waters in inventory:", freshWater)
            print("The Team Rocket grunts are", milesTraveled - nativesTraveled, "miles behind you.")
            print()
        # Max Elixir/Rest
        elif userInput.upper() == "Z":
            print("You stop and use a Max Elixir")
            print("Your Arcanine is happy.")
            print("Team Rocket is catching up!")
            print()
            arcanineTiredness = 0
            nativesTraveled += random.randrange(7, 15)
        # full speed ahead
        elif userInput.upper() == "D":
            miles = random.randrange(10, 21)
            milesTraveled += miles
            thirst += 1
            arcanineTiredness += random.randrange(1, 4)
            nativesTraveled += random.randrange(7, 15)
            oasis = random.randrange(20)
            if oasis == 10:
                thirst = 0
                arcanineTiredness = 0
                freshWater = 3
                print("You make a quick stop at a Pokemon Center!")
                print("You drink up and buy 3 Fresh Waters from the shop.")
                print("Your Arcanine is rested!")
                print("Team Rocket continues the chase.")
                print()
            else:
                print("Arcanine uses Extreme Speed, moving a total of", miles, "miles")
                print("Your thirst increases.")
                print("Team Rocket continues the chase.")
                print()
        # mid-speed ahead
        elif userInput.upper() == "S":
            miles = random.randrange(5, 13)
            milesTraveled += miles
            thirst += 1
            arcanineTiredness += 1
            nativesTraveled += random.randrange(7, 15)
            oasis = random.randrange(20)
            if oasis == 10:
                thirst = 0
                arcanineTiredness = 0
                freshWater = 3
                print("You make a quick stop at a Pokemon Center!")
                print("You drink up and buy 3 Fresh Waters from the shop.")
                print("Your Arcanine is rested!")
                print("Team Rocket continues the chase.")
                print()
            else:
                print("Arcanine uses Quick Attack, moving a total of", miles, "miles")
                print("Your thirst increases.")
                print("Team Rocket continues the chase.")
                print()
        # Have a Fresh Water
        elif userInput.upper() == "A":
            if freshWater > 0:
                freshWater -= 1
                thirst = 0
                print("You take a drink")
            else:
                print("You've used up all of your Fresh Waters! Oh how you wished you had some Soda Pop or Lemonade.")

        # Status updates
        # Thirst
        if thirst > 5:
            print("You blacked out from dehydration!")
            print("Team Rocket catches up to you and hold you hostage!")
            print("Game Over.")
            print()
            done = True
        elif thirst > 4:
            print("You are thirsty!")
        # Distance traveled / win check
        if milesTraveled >= 200:
            print("Congratulations! You have escaped the clutches of Team Rocket and have alerted Officer Jenny of their antics!")
            print("You win!")
            print()
            done = True
        # Camel's tiredness
        if arcanineTiredness > 8:
            print("Your Arcanine fainted of exhaustion!")
            print("With no Arcanine, Team Rocket catch up to you and hold you hostage.")
            print("Game Over.")
            print()
            done = True
        elif arcanineTiredness > 5:
            print("Your Arcanine is running low on energy.")
            print()
        # Natives distance from you
        if milesTraveled - nativesTraveled <= 0:
            print("Team Rocket has caught up with you and hold you hostage!")
            print("They convert you into a Team Rocket member.")
            print("Game Over.")
            print()
            done = True
        elif milesTraveled - nativesTraveled < 15:
            print("Team Rocket is getting uncomfortably close!")
            print()

main()

# Exit message
print("Game over.")
input("")