# Poker-bot

This is a collection into what I'e done so far with my poker work using python 
Poker is a great game for this due to having to deal with decisions, statistics and there being many different games to play 

The coding style over the course of the documents have chnaged mainly due to me learning: 
- OOP 
- Functions 

The categories of the files' progress is as follows: 

- Deck1.0 - Deck2.6
  - Starts as creating a deck of cards with a function that picks a single card 
  - Ends with a hand being chosen, and judging the hand's value - displaying the type of hand present (i.e. pair, flush etc.) 
  - Handstrength 2.6 is the final version of this working 

- Hand+board1.2
  - This creates hands for each the player and computer, then deals a flop, turn and river 

- HU_Handstrength3.1 - HU_Handstrength3.2
  - This uses a combination of the 2 above and compares the strengths of the player and computer hands throughout a full hand, ending on showdown 

- Five_card_draw5.1 and All_possible4.1
  - This takes all of the possible cominations of hands and puts it into a dictionary of the types: {type(as a number as per my sorting system) : occurances} 
  - The main problem with this is the max number for my dictionary storage being 1,098,240 (at least ins VSCode) 
  - And it takes a little while to run 

- HU_Bot1.1 - HU_Bot2.1 
  - This is a current work in progress 
  - This is where I have a full dealing of a hand and comparison from start to end in a single function 
  - It plays out hands, and by HU_Bot1.5 the computer makes decisions on whether to fold based on simple logic - due to it being heads-up, if the current strength of the computer hand is weaker than half of all other possible hands it folds 
  - By HU_Bot1.6 I have began to add in the betting architecture using OOP 
  - To the end of HU_bot1.x it begins to use the architecture and create the space for actual betting to occur 
  - HU_Bot2.1 is a mess - I have started to transition all of my variabled to an object so have found some complications which will need resolving 
  - HU_Bot
