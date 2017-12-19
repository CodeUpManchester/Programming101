from cards import Card
from cards import Deck
from cards import Player

def twist(player):
    card = deck.deal()
    #print 'Card: ' + card.toString()
    player.hand.append(card)
    #print player.toString()
    
def waitForAction(player):
    action = raw_input("Stick or twist? ")
    if action.lower()[0] == 's':
        player.isStuck = True
    else:        
        twist(player)

name = raw_input('What is your name? ')

play = 'y'
while play.lower()[0] == 'y': 
    dealer = Player('Dealer')
    player = Player(name)
    deck = Deck()

    #for card in deck.cards:
    #    print card.toString()

    #Deal cards
    for i in range(2):
        twist(player)
        twist(dealer)

    while not(player.isStuck or player.isBust()):
        print player.toString()
        waitForAction(player)

    print
    
    while not(dealer.isBust() or player.isBust()) and (player.getTotal() > dealer.getTotal() or dealer.getTotal() <= 17):
        twist(dealer)

    print player.toString()
    print
    print dealer.toString()
    print
    
    if not dealer.isBust() and (player.isBust() or dealer.getTotal() >= player.getTotal()):
        winner = 'Dealer'
    else:
        winner = player.name

    print winner + ' wins!'
    play = raw_input('Play again? (y/n)')

print 'Goodbye!'
