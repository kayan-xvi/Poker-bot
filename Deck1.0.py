def make_deck(): 
    '''
    Creates the deck of cards to use
    '''
    suits = ['♠','♥','♦','♣']
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

def hand(deck):
    '''
    Creates the hand of the player 
    '''
    #print('hand initiated')
    #print(deck)
    import random
    card1n = 52
    hand = []
    while card1n not in deck:  
        card1n = random.randint(0,51)
    card2n = card1n
    #print('Card1 = {}, Card2 = {}'.format(card1n,card2n))
    while card1n == card2n or card2n not in deck:
        card2n = random.randint(0,51)
        #print(card2n)
    #print('card1n = {}, card2n = {}'.format(card1n,card2n))
    card1 = deck[card1n]
    card2 = deck[card2n]
    #print(deck[card1n])
    #print('card1 = {}, card2 = {}'.format(card1,card2))
    hand.append(card1)
    hand.append(card2)
    del deck[card1n]
    del deck[card2n]
    #print(len(deck))
    return hand, deck

#---------------------

def pick_card(deck):
    '''
    Creates the hand of the player 
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

#---------------------
# MAIN EXECUTION
#---------------------
dict = {1,'2'}
deck = make_deck()
print(deck)
'''
p_hand, deck = hand(deck)
#print(deck)
print('Your hand is: {}'.format(p_hand))
print('Cards in deck after your hand: {}'.format(len(deck)))

c_hand, deck = hand(deck)
print('Comp hand is: {}'.format(c_hand))
print('Cards in deck after comp hand: {}'.format(len(deck)))
'''
p_hand = []
for i in range(2): 
    card, deck = pick_card(deck)
    p_hand.append(card)
print(p_hand)

c_hand = []
for i in range(2): 
    card, deck = pick_card(deck)
    c_hand.append(card)
print(c_hand)











