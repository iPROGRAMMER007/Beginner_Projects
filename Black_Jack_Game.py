#Black Jack Game

import random

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two','Three','Four','Five','Six',
         'Seven','Eight','Nine','Ten',
         'Three','Jack','Queen','King','Ace')

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,
         'Seven':7,'Eight':8,'Nine':9,'Ten':10,
         'Jack':10,'Queen':10,'King':10,
         'Ace':11}

playing = True

#1 Create Card class

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):

        return self.rank + ' of ' + self.suit

test_card = Card('Ace','Two')

print(test_card)

#2 Create Deck Class

class Deck():

    def __init__(self):

        self.deck = []
        for suit in suits:
            for rank in ranks:

                self.deck.append(Card(suit,rank))

    def __str__(self):

        deck_comp = ''
        for card in self.deck:

            deck_comp+= '\n' + card.__str__()

        return 'The deck has :' + deck_comp

    def shuffale(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

test_deck = Deck()
test_deck.shuffale()

print(test_deck)

#3 Hand Class

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces

        if card.rank == "Ace":

            self.aces += 1

    def got_aces(self):
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -= 1

#Player

test_player = Hand()
get_card = test_deck.deal()
print(get_card)
test_player.add_card(get_card)
print(test_player.value)


#4 Chip Class

class Chips():
    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# 5 Function for game : function to take bet


def take_bet(bet):

    while True:

        try:
            Chips.bet = int(input("How much would you like to place : "))

        except:
            print("Please provide an integer")
        else:
            if Chips.bet > Chips.total:
                print("You don't have chips")

            else:
                break


def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.got_access()


def  hit_or_stand(deck,hand):
    global playing

    while True:

        x = input("Hit or Stand? enter h or s")
        if x[0].lower == 'h':
            hit(deck,hand)

        elif x[0].lower == 's':
            print("Player wants to stand deal turn")
            playing = False

        else:
            print("I don't understand,Please enter h or s")
            continue

        break

# Show some or all Crads

def show_some(player,dealer):
    print("\n Dealer's hand : ")
    print('<Card Hidden > ')
    print('',dealer.cards[1])
    print("\n Player's Han:",*player.cards,sep = '\n')


def show_all(player,dealer):
    print("\nDealer,s Hand : ",*dealer.cards,sep = '\n')
    print("Dealer,s Hand = ",dealer.value)
    print("\nPlayer's hand : ",*player.cards,sep= '\n')
    print("Player's hand = ",player.value)

#Win lose criteria

def player_win(player,dealer,chips):
    print("Player Busted")
    chips.lose_bet()

def player_lose(player,dealer,chips):
    print("Player wins Yeyye")
    chips.win_bet()


def dealer_win(player,dealer,chips):
    print("Dealer win Yeyye")
    chips.win_bet()

def dealer_lose(player,dealer,chips):
    print("Dealer lose Yeyye")
    chips.lose_bet()

def push(player,dealer):
    print("It's a push")


while True:
    print("Welcome to the club")

    #Create and shuffle

    deck = Deck()
    deck.shuffale()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

     # setup player chips

    player_chips = Chips()

    #ask fro bet

    take_bet(player_chips)

    # Show cards
    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)

# Criteria for 21 num check

        if player_hand.value > 21:
            player_lose(player_hand,dealer_hand,player_chips)

            break

    #If player has not lose ,ask dealer to play

        if player_hand.value >= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck,dealer_hand)

    # Show all cards
        show_all(player_hand,dealer_hand)

        # code different winning scenarios
        if dealer_hand.value < 21:
            dealer_lose(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_win(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

# Inform the player about their situation

        print(f'\n Player total chips are {player_chips.total}')

# Ask trhe player to play again

    new_game = input("Would you like to play [y/n]")
    if new_game[0].lower == 'y':
        playing = True

    else:
        print("Thanks you for the playing please don't come again ")
        break





