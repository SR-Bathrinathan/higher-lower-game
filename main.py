from art import logo, vs
from game_data import data
from random import choice

def select_options():
    option_a = choice(data)
    option_b = choice(data)
    while option_b == option_a:
        option_b = choice(data)
    return option_a, option_b

def follower_check(usr_choice, a, b):
    a_count = a["follower_count"]
    b_count = b["follower_count"]
    if a_count >= b_count and usr_choice == 'a':
        return 1
    elif b_count >= a_count and usr_choice == 'b':
        return 1
    else:
        return 0

def game(current_score = 0):
    a, b = select_options()
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.")
    print(vs)
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.")
    user_choice = input("Who has more followers? Type \'A\' or \'B\': ").strip().lower()
    check = follower_check(user_choice, a, b)
    if check == 1:
        current_score +=1
        print("\n" * 20)
        print(logo)
        print(f"You're right! Current score: {current_score}")
        game(current_score)
    elif check == 0:
        print("\n" * 20)
        print(f"Sorry, that's wrong. Final score: {current_score}")
        return

print("\n" * 20)
print(logo)
game()

