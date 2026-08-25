# Build a number guessing game - computer picks a random number, user keeps guessing until correct.

import random
comp = random.randint(1,100)
tries = 0

while True:
    tries = tries + 1
    huma = int(input("Guess your number between 1 - 100 -: "))

    if huma == comp:
        print(f"Congratulations you have won in {tries} tries ! ")
        break
    elif huma > comp:
        print("Sorry wrong guess go lower ! ")

    elif huma < comp:
        print("Sorry wrong guess go higher ! ")