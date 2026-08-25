# Build a number guessing game - computer picks a random number, user keeps guessing until correct.

import random
comp = random.randint(1,100)

while True:
    huma = int(input("Guess your number between 1 - 100 -: "))

    if huma == comp:
        print("Congratulations you have won ! ")
        break
    elif huma > comp:
        print("Sorry wrong guess go lower ! ")

    elif huma < comp:
        print("Sorry wrong guess go higher ! ")