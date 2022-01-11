from Higher_Lower_data import data
import random
from replit import clear

A = random.choice(data)
B = random.choice(data)

current_score = 0
end = False
while not end:
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    ans = input("Who has more followers? Type 'A' or 'B': ")
    if ans == 'A' and A['follower_count'] > B['follower_count']:
        clear()
        current_score += 1
        print(f"You're right. Current score: {current_score}")
        B = random.choice(data)
    elif ans == 'B' and B['follower_count'] > A['follower_count']:
        clear()
        current_score += 1
        print(f"You're right. Current score: {current_score}")
        A = random.choice(data)
    else:
        print("You're wrong.")
        end = True