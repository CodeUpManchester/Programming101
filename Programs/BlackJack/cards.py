import random

suits = {
    1:'Hearts',
    2:'Clubs',
    3:'Diamonds',
    4:'Spades'
}

ranks = {
    1:'Ace',
    2:'Two',
    3:'Three',
    4:'Four',
    5:'Five',
    6:'Six',
    7:'Seven',
    8:'Eight',
    9:'Nine',
    10:'Ten',
    11:'Jack',
    12:'Queen',
    13:'King'
}

class Card():
    def __init__(self, suit, rank, isFaceUp = False):
        self.suit = suit
        self.rank = rank
        self.isFaceUp = isFaceUp

    def toString(self):
        return ranks[self.rank] + ' of ' + suits[self.suit]
    
class Deck():
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.isStuck = False

    def toString(self):
        cardText = self.hand[0].toString()
        for card in self.hand[1:]:
            cardText += ', ' + card.toString()
        return self.name + "'s Hand: " + cardText + ' (Score: ' + str(self.getTotal()) + ')'

    def isBust(self):
        return self.getTotal() > 21

    def getTotal(self):
        # Calculate as if ace = 1
        total = sum([card.rank for card in self.hand if card.rank < 11])
        total += sum([10 for card in self.hand if card.rank >= 11])
        if total > 21:
            return total
        
        aces = [card for card in self.hand if card.rank == 1]
        for ace in aces:
            if total + 10 <= 21:
                total += 10
        return total
