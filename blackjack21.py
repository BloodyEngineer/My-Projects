import random
from art_blackjack import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def again():
    play = input("Type 'y' if you want to play again. 'n' if you want to quit playing. ")
    if play == "y":
        return True
    else:
        print("Good Bye.")
        return False

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(the_list):
    total = sum(the_list)
    print(f"Your total is {total}")
    if total == 21:
        return 0
    elif total > 21:
        if the_list.count(11) == 0:
            return 1
        else:
            the_list.remove(11)
            the_list.append(1)
            calculate_score(the_list)
    elif total < 21:
        return 2


game = True
dealer_bust = False
dealer_win = False
while game is True:
    print(logo)
    user_cards = []
    dealer_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
    resume = False
    while not resume:
        print(f"Your cards: {user_cards} \nDealer's cards: {dealer_cards}")
        value = calculate_score(user_cards)
        if value == 0:
            print("Blackjack! You win.")
            resume = True
            game = again()
            continue
        elif value == 1:
            print("You are over 21. Bust!")
            resume = True
            game = again()
            continue
        else:
            hit_stand = input("Hit 'h' or Stand 's'?: ")
            if hit_stand == "h":
                user_cards.append(deal_card())
                continue
            elif hit_stand == "s":
                resume = True
                continue
    if hit_stand != "s":
        continue
    total_user = sum(user_cards)
    dealer_deals = False
    while not dealer_deals:
        dealer_cards.append(deal_card())
        total_dealer = sum(dealer_cards)
        print(f"Your cards: {user_cards} \nDealer's cards: {dealer_cards}")
        print(f"Your total: {total_user} \nDealer's total: {total_dealer}")
        if total_dealer == 21:
            print("Dealer wins.")
            dealer_deals = True
            dealer_win = True
            continue
        elif total_dealer < 17:
            continue
        elif total_dealer >= 17 and total_dealer < 21:
            dealer_deals = True
            dealer_bust = False
            dealer_win = False
            continue
        else:
            if dealer_cards.count(11) == 0:
                dealer_bust = True
                dealer_deals = True
                print("Dealer Bust!")
                print("You win.")
                continue
            else:
                dealer_cards.remove(11)
                dealer_cards.append(1)
                continue


    if dealer_bust or dealer_win:
        game = again()
        continue
    else:
        if total_dealer == total_user:
            print("It is a draw")
            game = again()
            continue
        elif total_dealer < total_user:
            print("You win!")
            game = again()
            continue
        else:
            print("Dealer wins.")
            game = again()
            continue
