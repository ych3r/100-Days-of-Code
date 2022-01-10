import random

def guess(target, difficulty):
    if difficulty == "easy":
        attempts = 10
    if difficulty == "hard":
        attempts = 5
    end = False
    while not end:
        print(f"You have {attempts} attempts remaining to guess the number.")
        num = int(input("Make a guess: "))
        if num < target:
            attempts -= 1
            print("Too low.\nGuess again.")
        if num > target:
            attempts -= 1
            print("Too high.\nGuess again.")
        if num == target and attempts >= 0:
            attempts -= 1
            print(f"You got it! The answer is {num}.")
            end = True
        if attempts < 0:
            print("You lose.")
            end = True

def main():
    print("Welcom to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    target = random.randint(1, 100)
    difficulty = input("Choos a difficulty. Type 'easy' or 'hard': ")
    guess(target, difficulty)

main()