def make_deck(): 
    '''
    Creates the deck of cards to use
    '''
    suits = ['♠','♣','♥','♦']
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    cards = {}
    n = 0
    for suit in range(len(suits)): 
        for value in range(len(values)): 
            cards[n] = (values[value] + suits[suit])
            #print(cards[n])
            n += 1 
    #print(cards) 
    return cards

#---------------------

def pick_card(deck):
    '''
    Picks a random card and removes it from the deck 
    '''
    #print('hand initiated')
    #print(deck)
    import random
    card1n = 52
    hand = []
    while card1n not in deck:  
        card1n = random.randint(0,51)
        #print(card2n)
    #print('card1n = {}, card2n = {}'.format(card1n,card2n))
    card1 = deck[card1n]
    #print(deck[card1n])
    #print('card1 = {}, card2 = {}'.format(card1,card2))
    hand.append(card1)
    del deck[card1n]
    #print(len(deck))
    return card1, deck

#---------------------
# MAIN EXECUTION
#---------------------

deck = make_deck()
print(deck)

# Making your hand 

p_hand = []
for i in range(2): 
    card, deck = pick_card(deck)
    p_hand.append(card)
#print(p_hand)
print('Your hand is: {}'.format(p_hand))
print('Number of cards left in deck: {}'.format(len(deck)))

# Making comp hand

c_hand = []
for i in range(2): 
    card, deck = pick_card(deck)
    c_hand.append(card)
#print(c_hand)
print('Comp hand is: {}'.format(c_hand))
print('Number of cards left in deck: {}'.format(len(deck)))

# Making flop 

board = []
for i in range(3): 
    card, deck = pick_card(deck)
    board.append(card)
#print(board)
print('Flop is: {}'.format(board))
print('Number of cards left in deck: {}'.format(len(deck)))

# Adding turn 
for i in range(1): 
    card, deck = pick_card(deck)
    board.append(card)
#print(board)
print('Turn is: {}'.format(board))
print('Number of cards left in deck: {}'.format(len(deck)))

# Adding river

for i in range(1): 
    card, deck = pick_card(deck)
    board.append(card)
#print(board)
print('River is: {}'.format(board))
print('Number of cards left in deck: {}'.format(len(deck)))







