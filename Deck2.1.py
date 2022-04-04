# The aim of this program is to tell you what your chance of winning the hand is  
'''
Suits: 
♠
♥
♦
♣
'''

#---------------------
 
def make_deck(): 
    '''
    Creates the deck of cards to use
    '''
    suits = ['S','H','D','C']
    values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    cards = []
    n = 0
    for suit in range(len(suits)): 
        for value in range(len(values)): 
            cards.append([values[value], suits[suit]])
            n += 1 
    return cards

#---------------------

def convert(deck):
    '''
    Turns all of the letter values into numbers as easier to work with
    '''
    for n in range(len(deck)): 
        #print(deck[n][0])
        if deck[n][0] == 'A': 
            deck[n][0] = 14
        if deck[n][0] == 'K': 
            deck[n][0] = 13 
        if deck[n][0] == 'Q': 
            deck[n][0] = 12
        if deck[n][0] == 'J': 
            deck[n][0] = 11  
    print(deck)
    
#---------------------

def pick_card(deck):
    '''
    Picks a card and removes this card from the deck, returning this card in form: [value,suit]
    '''
    #print('hand initiated')
    #print(deck)
    import random
    card1n = 52
    #while card1n not in deck: 
     #   pass
    #print(card1n)
    #print('lendeck = {}'.format(len(deck)))
    card1n = random.randint(0,len(deck)-1)
    #print(card1n)
        #print(card2n)
    #print('card1n = {}, card2n = {}'.format(card1n,card2n))
    card1 = deck[card1n]
    #print(card1)
    #print(deck[card1n])
    #print('card1 = {}, card2 = {}'.format(card1,card2))
    card = [card1[0],card1[1]]
    deck.remove(card1)
    #print(len(deck))
    return card, deck

#---------------------

def card_data(cards): 
    '''
    This turns the cards chosen into data to work with for hand classification
    '''
    suits = []
    values = []
    for card in range(len(cards)):
        values.append(cards[card][0])
        suits.append(cards[card][1])
    valuecount = [values.count(i) for i in values]
    suitcount = [suits.count(i) for i in suits]
    dif = max(values) - min (values)
    return valuecount, dif, suitcount, values
    
#---------------------

def royal(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if max(valuecount) == 1 and 5 in suitcount and dif == 4 and 14 in cards:  
        strength = 9
    return strength

#---------------------

def strflu(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if max(valuecount) == 1 and 5 in suitcount and dif == 4 or [14,2,3,4,5] in values:
        strength = 8
    return strength
    
#---------------------

def quad(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if 4 in valuecount: 
        strength = 7
    return strength

#---------------------

def fh(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if 3 in valuecount and 2 in valuecount:
        strength = 6
    return strength

#---------------------

def flu(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if 5 in suitcount:
        strength = 5
    return strength

#---------------------

def stra(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if max(valuecount) == 1 and dif == 4 or [14,2,3,4,5] in values: 
        strength = 4
    return strength 
    
#---------------------

def trip(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if 3 in valuecount: 
        strength = 3
    return strength 
    
#---------------------

def twopair(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if valuecount.count(2) == 4: 
        strength = 2
    return strength
    
#---------------------

def pair(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if 2 in valuecount: 
        strength = 1
    return strength

#---------------------

def high(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    # This autogives a strength of 0 
    strength = 0 
    return strength
    
#---------------------

def handtype(cards): 
    '''
    This applies the classification of the hand to the strength
    '''
    strength = 0
    if strength == 0: 
        strength = royal(cards)
    if strength == 0:
        strength = strflu(cards)
    if strength == 0:
        strength = quad(cards)
    if strength == 0:
        strength = fh(cards)
    if strength == 0:
        strength = flu(cards)
    if strength == 0:
        strength = stra(cards)
    if strength == 0:
        strength = trip(cards)
    if strength == 0: 
        strength = twopair(cards)
    if strength == 0: 
        strength = pair(cards)
    if strength == 0: 
        strength = high(cards)
    return strength

#---------------------

def handvalues(cards): 
    '''
    This creates the full value of the hand
    '''
    strength = handtype(cards)
    valuecount, dif, suitcount, values = card_data(cards)
    
#---------------------
# MAIN EXECUTION
#---------------------
print(
'''
Hand strength: 
Type-highest-high-middle-low-lowest

Hand type : 
royal = 09 = Royal flush 
strflu = 08 = Straight flush
quad = 07 = Four of a kind
fh = 06 = Full house 
flu = 05 = Flush
stra = 04 = Straight
trip = 03 = Three of a kind 
twopair = 02 = Two pair 
pair = 01 = Pair
high = 00 = High card
''')
#print(
'''
Hand cards: 
14 Ace 
13 King 
12 Queen 
11 Jack 
10 
09 
08 
07
06
05
04
03
02
'''
#)
#---------------------

deck = make_deck()
print(deck)

p_hand = []
for i in range(5): 
    card, deck = pick_card(deck)
    p_hand.append(card)
print(p_hand)
'''
c_hand = []
for i in range(5): 
    card, deck = pick_card(deck)
    c_hand.append(card)
print(c_hand)
'''
convert(p_hand)

print(handtype(p_hand))











