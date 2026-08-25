import random 

lowest_num = 1
highest_num = 10
guesses = 0
answer = random.randint(lowest_num, highest_num)

while True:
    guess = input("Guess the number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
     
        if guess >= 0:
            if guess == answer:
                print("Congrats you won!!!")
                break
            elif guess < answer:
                print("Low!, Try again!")
            elif guess > answer:
                 print("High!, Try again!")
    else:
            print("Invalid guess")
            print("please select between 1 to 10")
print("Thank you")
print(f"You guessed the right number in {guesses} attempts!")