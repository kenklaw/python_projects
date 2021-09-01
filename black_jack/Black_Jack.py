import random

from casino_classes import *


class BlackjackHand:
    def __init__(self):
        self.hand = []

# Add card to the hand
    def add_card(self, new_card):
        self.hand.append(new_card)

# str to return hand
    def __str__(self):
        hand = ""
        for card in self.hand:
            if card == self.hand[-1]:
                hand += str(card)
            else:
                hand += str(card) + ", "
        return hand

# get value returns value of the cards
    def get_value(self):
        value = 0
        for card in self.hand:
            value += card.get_value()
        for card in self.hand:
            while card.get_rank() == Card.card_deck[0][0]and value > 21:
                value -= 10
        return value


class Blackjack:
    card_deck = []

# rebuild the deck and shuffles
    def rebuild(self):
        for i in range(51):
            card = Card(i)
            Blackjack.card_deck.append(card)
            random.shuffle(Blackjack.card_deck)

# defines the variable used in class
    def __init__(self, starting_dollars):
        self.starting_dollars = starting_dollars
        self.bank = ChipBank(starting_dollars)
        self.game = True

# draw a card
    def draw(self):
        if Blackjack.card_deck == []:
            self.rebuild()
            card = random.choice(Blackjack.card_deck)
            Blackjack.card_deck.remove(card)
            return card
        else:
            card = random.choice(Blackjack.card_deck)
            Blackjack.card_deck.remove(card)
            return card

# starts the game and gives card out to dealer and player and determines blackjack
    def start_hand(self, wager):
        self.bank.withdraw(wager)
        self.dealer = BlackjackHand()
        self.player = BlackjackHand()
        self.dealer_card = Blackjack.draw(self)
        self.dealer_card.face_down()
        self.dealer.add_card(self.dealer_card)
        self.dealer.add_card(Blackjack.draw(self))
        self.player.add_card(Blackjack.draw(self))
        self.player.add_card(Blackjack.draw(self))
        self.game = True
        print("Your Starting Hand: ", self.player)
        print("Dealer Hand: ", self.dealer)
        if self.player.get_value() and self.dealer.get_value() == 21:
            self.end_hand('push')
        elif self.player.get_value() == 21:
            self.end_hand('win')
        elif self.dealer.get_value() == 21:
            self.end_hand('lose')

# allows player to draw a card and determines the player card value
    def hit(self):
        if self.player.get_value() > 21:
            self.end_hand('lose')
        elif self.player.get_value() == 21:
            self.stand()
        elif self.player.get_value() < 21:
            p_card = Blackjack.draw(self)
            self.player.add_card(p_card)
            print("You Draw: ", p_card)
            print(self.player)
            if self.player.get_value() > 21:
                self.end_hand('bust')
            elif self.player.get_value() == 21:
                self.stand()

# Auto stands when player hit 21 or when player choose to stand
    def stand(self):
        self.dealer_card.face_up()
        print("Dealer has: ", self.dealer)
        while self.dealer.get_value() <= 16:
            a_card = Blackjack.draw(self)
            self.dealer.add_card(a_card)
            print("Dealer Draws: ", a_card)
            print("Dealer has: ", self.dealer)
        if self.dealer.get_value() == self.player.get_value() == 21:
            self.end_hand('push')
        elif self.dealer.get_value() == 21:
            self.end_hand('lose')
        elif self.dealer.get_value() > 21:
            self.end_hand('dealer bust')
        elif self.dealer.get_value() < 21 and self.dealer.get_value()\
                > self.player.get_value():
            self.end_hand('lose')
        elif self.dealer.get_value() == self.player.get_value():
            self.end_hand('push')
        elif self.dealer.get_value() < self.player.get_value():
            self.end_hand('win')

# Determines the outcome of the game with win, lose, push or bust for dealer and player
    def end_hand(self, outcome):
        if outcome == 'win':
            print("You wins \n")
            self.bank.deposit(wager * 2)
            print(self.bank)
            self.game = False
        elif outcome == 'lose':
            print("You lose \n")
            print(self.bank)
            self.game = False
        elif outcome == 'push':
            print("Push \n")
            self.bank.deposit(wager)
            self.game = False
        elif outcome == 'bust':
            print("You bust, you lose \n")
            print(self.bank)
            self.game = False
        elif outcome == 'dealer bust':
            print("Dealer bust, You win \n")
            self.bank.deposit(wager * 2)
            print(self.bank)
            self.game = False

# keep the game going or resets the game cards
    def game_active(self):
        if self.game is True:
            return True
        elif self.game is False:
            return False

# test code
if __name__ == "__main__":
    blackjack = Blackjack(250)
    while blackjack.bank.value > 0:
        print("Your remaining chips: "+str(blackjack.bank))
        wager = int(input("How much would you like to wager? "))
        blackjack.start_hand(wager)
        while blackjack.game_active():
            choice = input("STAND or HIT: ").upper()
            if choice == "STAND":
                blackjack.stand()
            elif choice == "HIT":
                blackjack.hit()
        print()
    print("Out of money! The casino wins!")
