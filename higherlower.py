from art_higherlower import logo, vs
from game_data import data
import random

again = False

def hl():
    data_list = data
    score = 0
    game = False
    first_item = random.choice(data_list)
    while not game:
        print(logo)
        print(f"Score: {score}")
        data_list.remove(first_item)
        first_number = first_item['follower_count']
        print(f"Compare A : {first_item['name']}, {first_item['description']}, from {first_item['country']} has {first_item['follower_count']} followers.")
        print(vs)
        second_item = random.choice(data)
        print(f"Against B : {second_item['name']}, {second_item['description']}, from {second_item['country']}")
        second_number = second_item['follower_count']
        decision = input(f"Do you think {second_item['name']} 'higher' or 'lower' followers?: ").lower()
        if first_number < second_number and decision == 'higher':
            result = True
        elif first_number < second_number and decision == 'lower':
            result = False
        elif first_number > second_number and decision == 'higher':
            result = False
        elif first_number > second_number and decision == 'lower':
            result = True
        if result:
            score += 1
            print(f"You are correct!")
            data_list.append(first_item)
            first_item = second_item
        else:
            print(f"Your guess is wrong. You lose with Score: {score}")
            return

while not again:
    hl()
    if not input("Do you want to play again? Type 'y' or 'n': ").lower() == 'y':
        again = True
