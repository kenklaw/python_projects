import random


class Card:

    card_deck = {(0): ['Ace', 11, 1],
                 (1): ['2', 2],
                 (2): ['3', 3],
                 (3): ['4', 4],
                 (4): ['5', 5],
                 (5): ['6', 6],
                 (6): ['7', 7],
                 (7): ['8', 8],
                 (8): ['9', 9],
                 (9): ['10', 10],
                 (10): ['Jack', 10],
                 (11): ['Queen', 10],
                 (12): ['King', 10]}
# Class member variable that all objects in Card
# lass can access

    def __init__(self, card_num):
        self.card_number = card_num
        self.face = "up"
# constructor method

    def get_suit(self):
        return Card._what_suit_(self)
# Returns the suit of a specific card

    def _what_suit_(self):
        if self.card_number < 13:
            return 'Spades'
        elif self.card_number < 26:
            return 'Hearts'
        elif self.card_number < 39:
            return 'Clubs'
        else:
            return'Diamonds'
# A helper method that references card_deck dictionary to
# determine the card suit

    def get_rank(self):
        return Card._what_rank_(self)
# Method that returns rank of card

    def _what_rank_(self):
        if self.card_number < 13:
            rank = Card.card_deck[self.card_number][0]
            return rank
        elif self.card_number < 26:
            key = self.card_number - 13
            rank = Card.card_deck[key][0]
            return rank
        elif self.card_number < 39:
            key = self.card_number - 26
            rank = Card.card_deck[key][0]
            return rank
        else:
            key = self.card_number - 39
            rank = Card.card_deck[key][0]
            return rank
# A helper method that references card_deck dictionary to
# determine the card rank

    def get_value(self):
        if self.card_number < 13:
            value = Card.card_deck[self.card_number][1]
            return value
        elif self.card_number < 26:
            key = self.card_number - 13
            value = Card.card_deck[key][1]
            return value
        elif self.card_number < 39:
            key = self.card_number - 26
            value = Card.card_deck[key][1]
            return value
        else:
            key = self.card_number - 39
            value = Card.card_deck[key][1]
            return value
# Method that returns the value of a card

    def face_down(self):
        self.face = "down"

    def face_up(self):
        self.face = "up"

    def __str__(self):
        if self.face == "down":
            return "< face down >"
        else:
            card_hand = str(Card.get_rank(self)) + " of " \
                      + str(Card.get_suit(self))
            return card_hand


class ChipBank:

    def __init__(self, value):
        self.value = value
# Constructor method

    def withdraw(self, amount):
        if amount > self.value:
            amount = self.value
            self.value = 0
            return amount
        else:
            self.value -= amount
            return amount
# Returns the amount withdrawn and changes self.value
# to reflect the money withdrawn

    def deposit(self, amount):
        self.value += amount
# Adds money to self.value

    def __str__(self):
        '''Black chips are worth 100, green chips are worth 25, red chips\
 are worth 5, and blue chips are worth of 1. This method returns the number\
 chips you have as well as the monetary value of the chips.'''
        black_chips = 0
        green_chips = 0
        red_chips = 0
        blue_chips = 0

        remaining = self.value
        if self.value // 100:
            black_chips = self.value // 100
            remaining -= (black_chips * 100)
        if remaining // 25:
            green_chips = remaining // 25
            remaining -= (green_chips * 25)
        if remaining // 5:
            red_chips = remaining // 5
            remaining -= (red_chips * 5)
        if remaining // 1:
            blue_chips = remaining // 1

        string = str(black_chips) + ' black chip(s), ' + str(green_chips)\
            + ' green chip(s), ' + str(red_chips) + ' red chip(s), ' \
            + str(blue_chips) + ' blue chip(s), - totalling $' \
            + str(self.value)
        return string

# Below is the test code
if __name__ == '__main__':
    deck = []
    for i in range(52):
        my_card = Card(i)
        deck.append(my_card)
        print(my_card)

    print(random.choice(deck))

    card = Card(37)
    print(card)

    print(card.get_value())

    print(card.get_suit())

    print(card.get_rank())

    card.face_down()
    print(card)

    card.face_up()
    print(card)

    cs = ChipBank(149)
    print(cs)

    cs.deposit(7)
    print(cs.value)

    print(cs)

    print(cs.withdraw(84))

    print(cs)

    cs.deposit(120)
    print(cs)

    print(cs.withdraw(300))
