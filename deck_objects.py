import random


class Card:

    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['h','s','d','c']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank)+str(self.suit)

class Hand:
    def __init__(self):
        self.cards = []


    def add(self, card):
        self.cards.append(card)

    def show(self):
        shown_hand = ""
        for card in self.cards:
            shown_hand+=card
        print(shown_hand)

class Deck(Hand):

    def __init__(self):
        self.cards = []

    def build(self):
        for rank in Card.ranks:
            for suit in Card.suits:
                card = Card(rank, suit)
                self.cards.append(card.__str__())

    def shuffle(self):
        random.shuffle(self.cards)

    def burn_card(self):
        self.pop(0)

    def deal_card(self, hand, num):
        cards_dealt = []
        for i in range(num):
            cards_dealt.append(self.cards.pop())

        for card in cards_dealt:
            hand.add(card)



deck_object = Deck()
hand = Hand()
hand.show()
deck_object.build()
deck_object.shuffle()
deck_object.deal_card(hand, 2)
hand.show()