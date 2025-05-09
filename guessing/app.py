import random

rand_a = 1
rand_b = 10

random_number = random.randint(rand_a, rand_b)
attempts = 0
while True:
    user_input = int(input("Your choice: "))

    if user_input < random_number:
        print("A little higher.")
        attempts += 1
    elif user_input > random_number:
        print("A little lower.")
        attempts += 1
    elif user_input == random_number:
        print(f"Correct! You did it in {attempts+1} attempts.")
        print(f"Your guess: {user_input}\nComputer guess: {random_number}")
        break


