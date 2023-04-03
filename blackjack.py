import random

# Function to calculate the total value of a hand
def hand_value(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)
    total += aces
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

# Function to play the game
def play_game():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    player_hand = []
    dealer_hand = []
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    print(f"Player's hand: {player_hand}")
    print(f"Dealer's hand: ['?', '{dealer_hand[1]}']")
    while True:
        choice = input("Do you want to hit or stand? e/q\n")
        if choice.lower() == 'hit' or choice.lower()=='e':
            player_hand.append(deck.pop())
            print(f"Player's hand: {player_hand}")
            if hand_value(player_hand) > 21:
                print("Bust! Dealer wins.")
                return False
        elif choice.lower() == 'stand' or choice.lower()=='q':
            break
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print(f"Player's hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand}")
    if hand_value(dealer_hand) > 21:
        print("Dealer busts! Player wins.")
        return True
    elif hand_value(dealer_hand) > hand_value(player_hand):
        print("Dealer wins.\n")
        return False
    elif hand_value(player_hand) > hand_value(dealer_hand):
        print("Player wins.\n")
        return True
    else:
        print("Push (tie).\n")
        return None

# Main loop
money = 10000
while money > 0:
    print(f"Your current balance is {money}.\n")
    bet = int(input("How much do you want to bet?\n"))
    if bet > money:
        print("You don't have enough money for that bet.\n")
        continue
    result = play_game()
    if result == True:
        money += bet
    elif result == False:
        money -= bet
    else:
        continue
