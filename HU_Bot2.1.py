# The aim of this program is to play against a simple bot
'''
Suits: 
â™ 
â™¥
â™¦
â™¦
'''

#---------------------
 
def make_deck(): 
    '''
    Creates the deck of cards to use
    '''
    suits = ['♠','♣','♥','♦']
    values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    cards = []
    n = 0
    for suit in range(len(suits)): 
        for value in range(len(values)): 
            cards.append([values[value], suits[suit]])
            n += 1 
    return cards

#---------------------

def convert(person):
    '''
    Turns all of the letter values into numbers as easier to work with
    '''
    temp = person.hand
    for n in range(len(temp)): 
        #print(deck[n][0])
        if temp[n][0] == 'A': 
            temp[n][0] = 14
        if temp[n][0] == 'K': 
            temp[n][0] = 13 
        if temp[n][0] == 'Q': 
            temp[n][0] = 12
        if temp[n][0] == 'J': 
            temp[n][0] = 11  
    person.converted = temp 
    #print(deck)
    return deck
    
#---------------------
'''
def reconvert(deck):
    ''
    Turns all of the numbers into letters for visual purposes 
    shouldn't need this function to exist anymore 
    ''
    for n in range(len(deck)): 
        #print(deck[n][0])
        if deck[n][0] == 14: 
            deck[n][0] = 'A'
        if deck[n][0] == 13: 
            deck[n][0] = 'K' 
        if deck[n][0] == 12: 
            deck[n][0] = 'Q'
        if deck[n][0] == 11: 
            deck[n][0] = 'J'  
    #print(deck)
    return deck
'''
#---------------------

def pick_card(deck):
    '''
    Picks a card and removes this card from the deck, returning this card in form: [value,suit]
    '''
    card1n = 52
    card1n = random.randint(0,len(deck)-1)
    card1 = deck[card1n]
    card = [card1[0],card1[1]]
    deck.remove(card1)
    return card, deck

#---------------------

def card_data(person): 
    '''
    This turns the cards chosen into data to work with for hand classification
    '''
    #suits = []
    #values = []
    for card in range(len(person.hand)):
        person.values.append(person.hand[card][0])
        person.suits.append(person.hand[card][1])
    person.valuecount = [person.values.count(i) for i in person.values]
    person.suitcount = [person.suits.count(i) for i in person.suits]
    person.dif = max(person.values) - min (person.values)
    #return valuecount, dif, suitcount, values
    
#---------------------

def royal(person): 
    card_data(person)
    #strength = 0 
    if max(person.valuecount) == 1 and 5 in person.suitcount and person.dif == 4 and 14 in person.values:  
        person.strength = 9
        person.values.sort(reverse = True)
        for i in range(len(person.values)):
            person.strength *= 100 
            person.strength += person.values[i]
    #return strength

#---------------------

def strflu(person): 
    card_data(person)
    #strength = 0 
    if max(person.valuecount) == 1 and 5 in person.suitcount and person.dif == 4:
        #print(suitcount)
        person.strength = 8
        person.values.sort(reverse = True)
        for i in range(len(person.values)):
            person.strength *= 100 
            person.strength += person.values[i]
    #return strength

#---------------------

def strwheel(person): 
    card_data(person)
    strength = 0
    if 5 in person.suitcount and 5 in person.values and 4 in person.values and 3 in person.values and 2 in person.values and 14 in person.values:
        person.strength = 8
        person.values.sort(reverse = True)
        person.values.remove(14)
        person.values.append(14)
        for i in range(len(person.values)):
            person.strength *= 100 
            person.strength += person.values[i]
    #return strength
    
#---------------------

def quad(person): 
    card_data(person)
    #strength = 0 
    if 4 in person.valuecount: 
        person.strength = 7
        for i in range(len(person.values)): 
            if person.valuecount[i] == 4: 
                n = person.values[i]
                for j in range(4):
                    person.strength *= 100 
                    person.strength += n
                break
        person.values.sort(reverse = True)
        for k in range(len(person.values)): 
            if person.values[k] != n:
                person.strength *= 100 
                person.strength += person.values[k]
    #return strength

#---------------------

def fh(person): 
    card_data(person)
    #strength = 0 
    n = 0 
    m = 0
    if 3 in person.valuecount and 2 in person.valuecount:
        person.strength = 6
        for i in range(len(person.values)): 
            if person.valuecount[i] == 3: 
                n = person.values[i]
                for j in range(3):
                    person.strength *= 100 
                    person.strength += n
                break
        for i in range(len(person.values)): 
            if person.valuecount[i] == 2: 
                m = person.values[i]
                for j in range(2):
                    person.strength *= 100 
                    person.strength += m
                break
    #return strength

#---------------------

def flu(person): 
    card_data(person)
    #strength = 0 
    if 5 in person.suitcount:
        person.strength = 5
        person.values.sort(reverse = True)
        for i in range(len(person.values)):
            person.strength *= 100 
            person.strength += person.values[i]
    #return strength

#---------------------

def stra(person): 
    card_data(person)
    #strength = 0 
    if max(person.valuecount) == 1 and person.dif == 4: 
        person.strength = 4
        person.values.sort(reverse = True)
        for i in range(len(person.values)):
            person.strength *= 100 
            person.strength += person.values[i]
    #return strength 

#---------------------

def wheel(person): 
    card_data(person)
    #strength = 0
    if 5 in person.values and 4 in person.values and 3 in person.values and 2 in person.values and 14 in person.values:
        person.strength = 4
        person.values.sort(reverse = True)
        person.values.remove(14)
        person.values.append(14)
        for i in range(len(person.values)):
            person.strength *= 100 
            person.strength += person.values[i]
    #return strength
    
#---------------------

def trip(person): 
    card_data(person)
    #strength = 0 
    if 3 in person.valuecount: 
        person.strength = 3
        for i in range(len(person.values)): 
            if person.valuecount[i] == 3: 
                n = person.values[i]
                for j in range(3):
                    person.strength *= 100 
                    person.strength += n
                break
        person.values.sort(reverse = True)
        for k in range(len(person.values)): 
            if person.values[k] != n:
                person.strength *= 100 
                person.strength += person.values[k]
    #return strength 
    
#---------------------

def twopair(person): 
    card_data(person)
    #strength = 0 
    n = 0 
    m = 0 
    pairs = []
    if person.valuecount.count(2) == 4: 
        person.strength = 2
        for i in range(len(person.values)): 
            if person.valuecount[i] == 2: 
                n = person.values[i]
                break
        for i in range(len(person.values)):
            if person.valuecount[i] == 2 and person.values[i] != n: 
                m = person.values[i]
                break
        pairs.append(n)
        pairs.append(m)
        pairs.sort(reverse = True)
        for j in range(2): 
            for l in range(2):
                person.strength *= 100 
                person.strength += pairs[j]
        person.values.sort(reverse = True)
        for k in range(len(values)): 
            if person.values[k] != n and person.values[k] != m :
                person.strength *= 100 
                person.strength += person.values[k]
    #return strength
    
#---------------------

def pair(person): 
    card_data(person)
    #strength = 0 
    n = 0
    if 2 in person.valuecount: 
        person.strength = 1
        for i in range(len(person.values)): 
            if person.valuecount[i] == 2: 
                n = person.values[i]
                for j in range(2):
                    person.strength *= 100 
                    person.strength += n
                break
        person.values.sort(reverse = True)
        for k in range(len(person.values)): 
            if person.values[k] != n:
                person.strength *= 100 
                person.strength += person.values[k]
    #return strength

#---------------------

def high(person): 
    card_data(person)
    # This autogives a strength of 00
    person.strength = 0 
    person.values.sort(reverse = True)
    for i in range(len(person.valuecount)):
        person.strength *= 100 
        person.strength += person.values[i]
    return strength
    
#---------------------

def hand_value(person): 
    '''
    This applies the classification of the hand to the strength
    '''
    #strength = 0
    high(person)
    pair(person)
    twopair(person)
    trip(person)
    wheel(person)
    stra(person)
    flu(person)
    fh(person)
    quad(person)
    strwheel(person)
    strflu(person)
    royal(person)
    #return strength

#---------------------

def hand_type(person):
    power = person.strength//(10**10)
    #print(strength)
    #person.handtype = ''
    if power == 0: 
        person.handtype = 'High card'
    if power == 1: 
        person.handtype = 'Pair'
    if power == 2: 
        person.handtype = 'Two pair'
    if power == 3: 
        person.handtype = 'Three of a kind'
    if power == 4: 
        person.handtype = 'Straight'
    if power == 5: 
        person.handtype = 'Flush'
    if power == 6: 
        person.handtype = 'Full house'
    if power == 7: 
        person.handtype = 'Four of a kind'
    if power == 8: 
        person.handtype = 'Straight flush'
    if power == 9: 
        person.handtype = 'Royal flush'
    #return classif, power

#---------------------

def judge_value(person):
    '''
    This function judges the value of any hand put into it in format [[value,suit], ...]
    '''
    convert(person)
    hand_value(person)
    #print('This is your hands value:')
    #print(handstrength)
    #print('This is your type of hand:')
    #print(hand_type(handstrength))
    #return handstrength
    
#---------------------

def make_hand(deck, person, size): 
    '''
    This function creates a hand of size, size or adds size cards to a hand from deck
    '''
    person.printout = ''
    reconvert(person.hand)
    for i in range(size): 
        card, deck = pick_card(deck)
        person.hand.append(card)
    for i in range(len(person.hand)):
        for j in range(2):
            person.printout += str(person.hand[i][j]) 
        person.printout += '  '
    #return hand, printout, deck

#---------------------

def make_printout(hand): 
    '''
    This function makes a prinout in the appropriate form for front end display
    '''
    #printout = ''
    for i in range(len(person.hand)):
            for j in range(2):
                person.printout += str(person.hand[i][j]) 
            person.printout += '  '
    #return printout

#---------------------

def single_hand(person, size): 
    '''
    This function finds the best hand of size 5 possible from all given cards 
    '''
    possible = [] 
    maxstrength = 0
    maxhand = []
    typecount = {}
    for i in range(1,10): 
        typecount[i] = 0
        #print(typecount)
    for single in itertools.combinations(hand,5): 
        #print('single')
        #print(list(single))
        possible.append(list(single))
    #print(len(possible))
    #print('TEST1')
    for hands in possible: 
        #print(hand)
        handstrength = judge_value(hands)
        classif, power = hand_type(handstrength)
        #print(power)
        #if power == 8: 
                #print(hands)
        for i in range(1,10):
            if power == i:
                typecount[i] += 1 
            
        #print('\n')
        #print(2)
        if handstrength > maxstrength:
            maxstrength = handstrength
            #print('TEST: {}'.format(hands))
            #print(typecount)
            maxhand = hands
            #print(hands)
    #print('TEST2')
    #print('Best possible hand:')
    #print(maxhand)
    #print(hand_type(maxstrength))
    #print(maxstrength)
    return maxhand, maxstrength, typecount

#---------------------

def blinds(sb, bb, big): 
    '''
    This function sets up the blinds for the hand 
    '''
    if sb.chips >= big//2: 
        sb.chips -= big//2
        sb.inter += big//2
    if sb.chips < big//2: 
        sb.inter = sb.chips 
        sb.chips = 0
        
    if bb.chips >= big: 
        bb.chips -= big
        bb.inter += big
    if bb.chips < big: 
        bb.inter = bb.chips 
        bb.chips = 0
    bb.chips 
    #print(sb.chips)
    #print(bb.chips)

#---------------------

def betting(sb, bb, pot, ): 
    '''
    This function deals with the betting of the player each time they have a decision 
    It leads down 2 paths - one if the player is sb, one if player is not sb 
    '''
    if sb.name == 'player': 
        while sb.inter != bb.inter:
            # Player decision 
            decision = input('What would you like to do (fold/ int(amount))?\n')
            decision = decision.strip()
            decision = decision.lower() 
        
            if decision == 'fold': 
                print('Player has folded - you lose')
                exit() 
        
            if decision.isdigit(): 
                number = str(decision)
                if sb.chips >= number: #Bet/ call/ raise
                    sb.chips -= number
                    sb.inter += number
                else: #All in 
                    sb.inter = sb.chips 
                    sb.chips = 0 
            
            
            # Computer response 
            # Should slightly randomise - raise 1 in 5 calls 
            # Calling when stronger/ total > (comp.inter - p.inter)/ pot + 2*p.inter 
    if sb.name == 'comp': 
        pass
    
#---------------------

def position(c_hand, board, remaining): 
    temp = []
    c_hand, c_strength, typecount = single_hand(c_hand, 5)
    #print(board)
    #temp = board
    for card in board: 
            temp.append(card)
    #print(temp)
    possible = []
    for hands in itertools.combinations(remaining,2): 
        temp.clear()
        #print('Board: {}'.format(board))
        for card in board: 
            temp.append(card)
        #temp = board
        #print(temp)
        for card in list(hands):
            temp.append(card)
        #print(temp)
        possible.append(list(temp))
        #print(possible)
        #for card in board: 
            #print(card)
            #possible[i].append(card)
            #i += 1
    
    stronger = 0 
    weaker = 0 
    same = 0
    #print('This is the number of possible combinations left: {}'.format(len(possible)))
    #print(c_strength)
    for hand in possible: 
        tophand, tophandstrength, count = single_hand(hand,5)
        #print(judge_value(hand))
        if c_strength > tophandstrength: 
            stronger += 1 
        if c_strength < tophandstrength: 
            weaker += 1 
            #print(hand_type(judge_value(hand)))
        if c_strength == tophandstrength: 
            same += 1 
    #print(stronger)
    #print(weaker)
    #print(same)
    if weaker > stronger: 
        print('The computer folds - you win')
        #exit()
    return stronger, weaker, same

#---------------------

def preposition(c_hand, remaining): 
    temp = []
    c_hand, c_strength, typecount = single_hand(c_hand, 2)
    #print(board)
    #temp = board
    #print(temp)
    possible = []
    for hands in itertools.combinations(remaining,2): 
        possible.append(hands)
        #print(possible)
        #for card in board: 
            #print(card)
            #possible[i].append(card)
            #i += 1
    
    stronger = 0 
    weaker = 0 
    same = 0
    #print('This is the number of possible combinations left: {}'.format(len(possible)))
    #print(c_strength)
    for hand in possible: 
        prestrength = hand_value(c_hand)
        #tophand, tophandstrength, count = single_hand(hand,2)
        #print(judge_value(hand))
        if c_strength > prestrength: 
            stronger += 1 
        if c_strength < prestrength: 
            weaker += 1 
            #print(hand_type(judge_value(hand)))
        if c_strength == prestrength: 
            same += 1 
    #print(stronger)
    #print(weaker)
    #print(same)
        #exit()
    return stronger, weaker, same
#---------------------

def board_cards(p_hand, c_hand, board, deck, remaining, stage, number): 
    '''
    This function creates the board depending on input
    '''
    board, b_print, deck = make_hand(deck, board, number)
    convert(board)
    print('This is the {}:'.format(stage))
    print(b_print)
    print('\n')
    for card in board: 
        if card not in p_hand:
            p_hand.append(card)
        if card not in c_hand:
            c_hand.append(card)
        if card in remaining:
            remaining.remove(card)
            #print(True)
    #print('Comp number of cards reminaing: {}'.format(len(remaining)))

    #print('\nYour hand:')
    p_hand, p_strength, typecount = single_hand(p_hand, 5)
    #print(make_printout(reconvert(p_hand)))
    #print(hand_type(p_strength))
    #print('Comp hand:')
    c_hand, c_strength, typecount = single_hand(c_hand, 5)
    #print(make_printout(reconvert(c_hand)))
    #print(hand_type(c_strength))
    #print('\n')
    
    #print(c_hand)
    #print(board)
    #print(len(remaining))
    stronger, weaker, same = position(c_hand, board, remaining)
    return p_hand, c_hand, board, deck, remaining, p_strength, c_strength
    
#---------------------

def old_heads_up_prob(sb, bb): 
    '''
    This function allows the comp to make moves depending on probabilities of future cards  
    '''
    # Setup for the game 
    deck = make_deck()
    board = []
    pot = 0
    remaining = make_deck()
    
    # Blinds
    blinds(sb, bb, 100)
    
    # Preflop 
    p_hand = []
    p_hand, p_print, deck = make_hand(deck, p_hand, 2)
    print('This is your hand:')
    print(p_print)
    print('\n')
    p_strength = judge_value(p_hand)
    c_hand = []
    c_hand, c_print, deck = make_hand(deck, c_hand, 2)
    print('This is comp hand:')
    print(c_print)
    for card in c_hand: 
        remaining.remove(card)
    #print('Comp number of cards reminaing: {}'.format(len(remaining)))
    print('\n')

    #p_strength = judge_value(p_hand)
    #print(p_strength)
    
    # Preflop
    prestroger, preweaker, presame = preposition(c_hand, remaining)
    #betting(sb, bb, pot)
    
    # Flop
    p_hand, c_hand, board, deck, remaining, p_strength, c_strength = board_cards(p_hand, c_hand, board, deck, remaining, 'flop', 3)
    
    # Turn
    p_hand, c_hand, board, deck, remaining, p_strength, c_strength = board_cards(p_hand, c_hand, board, deck, remaining, 'turn', 1)
    
    # River
    p_hand, c_hand, board, deck, remaining, p_strength, c_strength = board_cards(p_hand, c_hand, board, deck, remaining, 'river', 1)
    
    # Showdown
    print('Your hand: {} {}'.format(make_printout(reconvert(p_hand)), hand_type(p_strength)))
    print('Comp hand: {} {}'.format(make_printout(reconvert(c_hand)), hand_type(c_strength)))
    if p_strength > c_strength: 
        print('You won')
        player.chips += pot
        pot = 0
    elif p_strength < c_strength:
        print('You lose')
        comp.chips += pot
        pot = 0
    else: 
        print('You tied')
        player.chips += pot/2 
        comp.chips += pot/2
        pot = 0
    print(player.chips)
    print(comp.chips)
    # Returns the opposite of this hand so it is the input of the next hand 
    return bb, sb

#---------------------

def heads_up_prob(sb, bb): 
    '''
    This function allows the comp to make moves depending on probabilities of future cards  
    '''
    # Setup for the game 
    deck = make_deck()
    board = []
    pot = 0
    remaining = make_deck()
    
    # Blinds
    blinds(sb, bb, 100)
    
    # Preflop 
    #p_hand = []
    make_hand(deck, player, 2)
    print('This is your hand:')
    print(player.printout)
    print('\n')
    p_strength = judge_value(p_hand)
    #c_hand = []
    make_hand(deck, comp, 2)
    print('This is comp hand:')
    print(comp.printout)
    for card in comp.hand: 
        remaining.remove(card)
    #print('Comp number of cards reminaing: {}'.format(len(remaining)))
    print('\n')

    #p_strength = judge_value(p_hand)
    #print(p_strength)
    
    # Preflop
    prestroger, preweaker, presame = preposition(c_hand, remaining)
    #betting(sb, bb, pot)
    
    # Flop
    p_hand, c_hand, board, deck, remaining, p_strength, c_strength = board_cards(p_hand, c_hand, board, deck, remaining, 'flop', 3)
    
    # Turn
    p_hand, c_hand, board, deck, remaining, p_strength, c_strength = board_cards(p_hand, c_hand, board, deck, remaining, 'turn', 1)
    
    # River
    p_hand, c_hand, board, deck, remaining, p_strength, c_strength = board_cards(p_hand, c_hand, board, deck, remaining, 'river', 1)
    
    # Showdown
    print('Your hand: {} {}'.format(make_printout(reconvert(p_hand)), hand_type(p_strength)))
    print('Comp hand: {} {}'.format(make_printout(reconvert(c_hand)), hand_type(c_strength)))
    if p_strength > c_strength: 
        print('You won')
        player.chips += pot
        pot = 0
    elif p_strength < c_strength:
        print('You lose')
        comp.chips += pot
        pot = 0
    else: 
        print('You tied')
        player.chips += pot/2 
        comp.chips += pot/2
        pot = 0
    print(player.chips)
    print(comp.chips)
    # Returns the opposite of this hand so it is the input of the next hand 
    return bb, sb

#---------------------

#print(
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
'''
#)
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
# MAIN EXECUTION
#---------------------

import itertools
import random

# Setup of match variables 
class Person: 
    def __init__(self, name):
        self.name = name
        # Betting 
        self.chips = 1000
        self.inter = 0
        # Hand 
        self.hand = []
        self.printout = ''
        self.handtype = []
        # Hand data for analysis
        self.cards = []
        self.converted = []
        self.handstrength = 0
        self.suits = []
        self.valuecount = []
        self.values = []
        self.suitcount = [] 
        self.dif = 0
player = Person('player')
#print(player.name)
#print(player.chips)
comp = Person('comp')
#print(comp.name)
#print(comp.chips)

blinddecider = random.randint(0,1)
if blinddecider == 0: 
    heads_up_prob(comp, player)
    #print(player.chips)
    #print(comp.chips)

#while p_chips != 0 and c_chips != 0: 
for i in range(2):
    heads_up_prob(player, comp)
    #print(player.chips)
    #print(comp.chips)
    heads_up_prob(comp, player)
    #print(player.chips)
    #print(comp.chips)
#betting(p_chips, c_chips, p_inter, c_inter, pot)

'''
player-comp 
intital chip stacks 
---- should be defined outside of the individual game 

def full_game(sb, bb, sb_chips, bb_chips): 
    
    sb/bb  == player/comp 
    chips of each
    
    make deck /
    make p hand /
    make c hand /
    
    blind - betting while inter != inter 
        sb(button) then bb 
    flop /
    = betting while inter != inter 
        bb then sb(button)
    turn /
    = betting while inter != inter 
        bb then sb(button)
    river /
    = betting while inter != inter 
        bb then sb(button)
    compare strength / 
    return sb, bb, sb_chips, bb_chips
    

comp should not fold if stronger+same/(stronger+same+weaker) >= pot odds  
'''
















