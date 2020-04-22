import random

suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
values = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
hands_in_play = []
dealer_hand = []
player_hand = []

# Deals two random cards not already in play to the player
def get_player_hand():
    global suits, values, hands_in_play, player_hand
    hand = []
    i = 0
    while i < 2:
        value = random.choice(values)
        suit = random.choice(suits)
        if value + ' ' + suit not in hands_in_play:
            hands_in_play.append(value + ' ' + suit)
            card =  value + ' of ' + suit
            player_hand.append(card)
            i += 1
        else: # Card has already been dealt
            continue
    return player_hand

# Deals two random cards not already in play to the dealer
def get_dealer_hand():
    global suits, values, hands_in_play, dealer_hand
    hand = []
    i = 0
    while i < 2:
        value = random.choice(values)
        suit = random.choice(suits)
        if value + ' ' + suit not in hands_in_play:
            hands_in_play.append(value + ' ' + suit)
            card = value + ' of ' + suit
            dealer_hand.append(card)
            i += 1
        else:
            continue
    return dealer_hand

# Input: hand of cards
# Determines value of cards in hand
def get_value(hand):
    total = 0
    ace = False
    num_aces = 0
    for x in range(len(hand)): # Loop through each item in list
        spl = hand[x].split()
        num = spl[0]
        if num == 'Ace':
            ace = True
            num_aces += 1
        elif num == 'King' or num == 'Queen' or num == 'Jack':
            total += 10
        else:
            total += int(num)
    if ace == True:
        for a in range(num_aces):
            if total + 11 <= 21: # Check if ace can be set to 11 instead of 1
                total += 11
            else: # If not make ace 1
                total += 1
    return total

# Deals new cards to player
def deal_player():
    global hands_in_play
    value = random.choice(values)
    suit = random.choice(suits)
    while value + ' ' + suit in hands_in_play:
        value = random.choice(values)
        suit = random.choice(suits)
    hands_in_play.append(value + ' ' + suit)
    return value + ' of ' + suit

# Automatically plays dealer
# Stands on 17+
def deal_dealer():
    dealer_total = get_value(dealer_hand)
    player_total = get_value(player_hand)
    while dealer_total < 17:
        new_card = deal_player()
        dealer_hand.append(new_card)
        dealer_total = get_value(dealer_hand)
        print('Dealer pulled {}'.format(new_card))
        print_dealer_hand()

def print_player_hand():
    global player_hand
    print('Player showing: {} | Value: {}'.format(player_hand, get_value(player_hand)))

# Seperate print for dealers initial cards on table
def print_dealer_start_hand():
    global dealer_hand
    print('Dealer face up card: {}'.format(dealer_hand[0]))

def print_dealer_hand():
    global dealer_hand
    print('Dealer showing: {} | Value: {}\n'.format(dealer_hand, get_value(dealer_hand)))

def main():
    global hands_in_play, dealer_hand, player_hand
    get_player_hand()
    get_dealer_hand()
    player_value = get_value(player_hand)
    dealer_value = get_value(dealer_hand)
    print('*** Welcome to Python Blackjack ***\n')
    print_player_hand()
    if player_value == 21:
        print('BLACKJACK! YOU WIN!')
        quit()
    else:
        print_dealer_start_hand()

    choice = input('(h)it or (s)tand? ')
    while choice != 'h' and choice != 's': 
        print('Invalid input. Try Again.')
        choice = input('(h)it or (s)tand? ')
    while choice != 's':
        new_card = deal_player()
        print('You drew {}'.format(new_card))
        player_hand.append(new_card)
        print_player_hand()
        if get_value(player_hand) > 21: # BUST
            print('BUST! You lose.')
            quit()
        else:
            choice = input('(h)it or (s)tand? ')
            while choice != 'h' and choice != 's': 
                print('Invalid input. Try Again.')
                choice = input('(h)it or (s)tand? ')
    
    print()
    print_dealer_hand()
    deal_dealer()
    player_value = get_value(player_hand)
    dealer_value = get_value(dealer_hand)
    if player_value == dealer_value:
        print('PUSH')
    elif player_value > dealer_value or dealer_value > 21:
        print('YOU WIN!')
    else:
        print('You Lose.')

main()