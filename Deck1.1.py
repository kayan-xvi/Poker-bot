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
# MAIN EXECUTION
#---------------------

deck = make_deck()
print(deck)

p_hand = []
for i in range(5): 
    card, deck = pick_card(deck)
    p_hand.append(card)
print(p_hand)

c_hand = []
for i in range(5): 
    card, deck = pick_card(deck)
    c_hand.append(card)
print(c_hand)











