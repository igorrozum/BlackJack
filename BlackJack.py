'''
This is a Black Jack game
'''

import random
import time

minimal_bet = 1
dealer_balance = 1000

class Card():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Player():
    def __init__(self, name='default_name', balance=0, bet=0, card_set=[]):
        self.name = name
        self.balance = balance
        self.bet = bet
        self.card_set = card_set
    
    def add_money(self, amount):
        self.balance += amount

    def take_money(self, amount):
        self.balance -= amount



two = Card('2', 2)
three = Card('3', 3)
four = Card('4', 4)
five = Card('5', 5)
six = Card('6', 6)
seven = Card('7', 7)
eitht = Card('8', 8)
nine = Card('9', 9)
ten = Card('10', 10)
jack = Card('Jack', 10)
queen = Card('Queen', 10)
king = Card('King', 10)
ace = Card('Ace', 11)

def add_card():
    card = random.choice(deck)
    deck.remove(card)
    return card

def cards_value(card_set):
    value = 0
    for card in card_set:
        value += card.value
    return value

def display_cards(player, cards_set):
    print(f'{player}, has {cards_value(cards_set)} points:', end=" ")
    for card in cards_set:
        if (card != cards_set[-1]):
            print('\033[31m' + card.name + '\033[0m', end=', ')
        else:
            print('\033[31m' + card.name + '\033[0m', end="")

def check_cards(player, cards_set):
    value = cards_value(cards_set)
    choice = 0
    while True:
        if value < 21:
            print('1. Stand')
            print('2. Hit')
            choice = int(input(player.name + ', please choose your next move: '))
            if choice == 1:
                print('You chose to stand\n')
                break
            elif choice == 2:
                card = add_card()
                cards_set.append(card)
                print("You've got a " + card.name)
                display_cards(player.name, cards_set)
                print('\n---   ---   ---   ---   ---\n')
                value = cards_value(cards_set)  
        elif value == 21:
            if len(cards_set) == 2:
                print("Congratulations! You've got Blac Jack")
                break
            else:
                print("Congratulations! You've got 21")
                break
        else:
            print("The value is more than 21. It's a bust")
            break


print('\n*** Welcome to Black Jack! ***\n')

num_of_players = int(input('How many players are gonna be playing? '))
players = [Player()]*(num_of_players+1)
players[0] = Player('Dealer', dealer_balance)

for i in range(1,num_of_players+1):
    # Get user's name
    players[i].name = input(f'Player{i}, please enter your name: ')
    # Get users's balance
    try:
        new_balance = int(input(players[i].name + ', set your balance: '))
    except:
        print('This is not a number. Please enter a correct one')
    else:
        if new_balance >= minimal_bet:
            print(f'Your balance is: ${new_balance}')
        else:
            print(f'Please enter a number bigger than {minimal_bet}')
    players[i] = Player(players[i].name, new_balance)

while True:
    deck = [two, three, four, five, six, seven, eitht, nine, ten, jack, queen, king, ace]*4

    for i in range(1,num_of_players+1):
        try:
            players[i].bet = int(input(f'{players[i].name}, enter your bet please (up to {players[i].balance}): '))
        except:
            print('This is not a number. Please enter a correct one')
        else:
            if players[i].bet >= minimal_bet and players[i].bet <= players[i].balance:
                print(f'Your bet is: ${players[i].bet}\n')
            else:
                print(f'The bet should be more than {minimal_bet} and less than your balance {players[i].balance}')

    print('Dealer gives out the cards . . .\n')
    time.sleep(2)

    player0_cards = [add_card(), add_card()]
    player1_cards = [add_card(), add_card()]
    player2_cards = [add_card(), add_card()]
    

    #for i in range(1,num_of_players+1):
    display_cards(players[1].name, player1_cards)
    print('\n---   ---   ---   ---   ---')
    time.sleep(2)
    display_cards(players[2].name, player2_cards)
    print('\n---   ---   ---   ---   ---')
    time.sleep(2)
    print(f'{players[0].name}, has {player0_cards[0].name} and hidden card\n')
    time.sleep(2)

    check_cards(players[1], player1_cards)
    check_cards(players[2], player2_cards)
    print('---   ---   ---   ---   ---')

    

    if cards_value(player1_cards) <=21 or cards_value(player2_cards) <=21:
        print(players[0].name + "s checking the cards . . .")
        time.sleep(2)
        print("The second " + players[0].name + "'s card is " + player0_cards[1].name)
        while cards_value(player0_cards) < 17:
            new_card = add_card()
            player0_cards.append(new_card)
            print(players[0].name + ' is adding ' + new_card.name)
        display_cards(players[0].name, player0_cards)
        print('\n---   ---   ---   ---   ---')

    print('Processing results . . .\n')
    time.sleep(2)

    if cards_value(player1_cards) > 21 and cards_value(player2_cards) > 21:
        print('All players lost')
        for player in players:
            player.balance -= player.bet
            players[0].balance += player.bet
    else:
        if cards_value(player0_cards) <= 21:
            if cards_value(player1_cards) <= 21:
                if cards_value(player1_cards) == 21:
                    if cards_value(player1_cards) == cards_value(player0_cards):
                        print(players[1].name + ", it's a draw. You get your bet back!")
                    elif cards_value(player1_cards) == 21 and len(player1_cards) == 2:
                        print("Congratulations, " + players[1].name + ", it's a BlackJack")
                        players[1].balance += players[1].bet*1.5
                        players[0].balance -= players[1].bet*1.5
                    else:
                        print("Congratulations, " + players[1].name + ", it's 21")
                        players[1].balance += players[1].bet
                        players[0].balance -= players[1].bet
                else:
                    if cards_value(player1_cards) == cards_value(player0_cards):
                        print(players[1].name + ", it's a draw. You get your bet back!")
                    elif cards_value(player1_cards) < cards_value(player0_cards):
                        print(players[1].name + ", you have less points. You lose your bet!")
                        players[1].balance -= players[1].bet
                        players[0].balance += players[1].bet
                    else:
                        print(players[1].name + ", you have more points. You win!")
                        players[1].balance += players[1].bet
                        players[0].balance -= players[1].bet
            else:
                print(players[1].name + ", you have a bust. You lose your bet!")


            if cards_value(player2_cards) <= 21:
                if cards_value(player2_cards) == 21:
                    if cards_value(player2_cards) == cards_value(player0_cards):
                        print(players[2].name + ", it's a draw. You get your bet back!")
                    elif cards_value(player2_cards) == 21 and len(player2_cards) == 2:
                        print("Congratulations, " + players[2].name + ", it's a BlackJack")
                        players[2].balance += players[2].bet*1.5
                        players[0].balance -= players[2].bet*1.5
                    else:
                        print("Congratulations, " + players[2].name + ", it's 21")
                        players[2].balance += players[2].bet
                        players[0].balance -= players[2].bet
                else:
                    if cards_value(player2_cards) == cards_value(player0_cards):
                        print(players[2].name + ", it's a draw. You get your bet back!")
                    elif cards_value(player2_cards) < cards_value(player0_cards):
                        print(players[2].name + ", you have less points. You lose your bet!")
                        players[2].balance -= players[2].bet
                        players[0].balance += players[2].bet
                    else:
                        print(players[2].name + ", you have more points. You win!")
                        players[2].balance += players[2].bet
                        players[0].balance -= players[2].bet
            else:
                print(players[2].name + ", you have a bust. You lose your bet!")
                players[2].balance -= players[2].bet
                players[0].balance += players[2].bet
    
    for i in range(1, num_of_players+1):
        print(f'{players[i].name}, your balance is {players[i].balance}')
    play_again = input("Want to play again? Enter 'Yes' or 'No' ")
    if play_again[0].lower() != 'y':
        break