# CS1210 HW4
# Mina Rao

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.
from random import randint
import matplotlib.pyplot as plt

######################################################################
# Search this file for the hashtag #TODO to see what you need to
# complete for HW4.
######################################################################
# Some functions you will need to use.

# createDeck() produces a new, cannonically ordered, 40 card deck.
# Uses a nested comprehension; deviates a bit from the specification
# because it allows one to specify a different size deck. In other
# words, createDeck(13) would create a standard 52-card deck (with J,
# Q, K denoted 11, 12, 13).
def createDeck(N=10, S=('spades', 'hearts', 'clubs', 'diamonds')):
    return([ (v, s) for s in S for v in range(1, N+1) ])

# Fisher-Yates-Knuth fair shuffle. Faster and fairer than riffle(), so
# we may as well use that here.
def shuffle(D = createDeck()):
    i = len(D)-1
    while i > 0:
        j = randint(0, i)
        D[i], D[j] = D[j], D[i]
        i = i-1
    return(D)
    
######################################################################
# Construct the representation of a given card using special unicode
# characters for hearts, diamonds, clubs, and spades. Uses special
# unicode encodings of the card suits.
def displayCard(c):
    suits = {'spades':'\u2660', 'hearts':'\u2661', 'diamonds':'\u2662', 'clubs':'\u2663'}
    return "".join((str(c[0]),str(suits[c[1]])))

######################################################################
# Print out an indexed list of the cards in input list H. Used to
# print out the hand of cards, suitable for picking from by the human
# player.
def showHand(H):
    print('\nMy hand: {}'.format(', '.join([ "[{}] {}".format(i, displayCard(H[i])) for i in range(len(H)) ] )))

# Print out the state of the table, including any player stashes. It's
# important that the indexes used identify the player number (0
# through N-1, inclusive, but only if the player has a stash) and the
# cards on the table (N through N+len(T)-1, inclusive).
def showTable(N, T, P):
	for i in range(len(P)):
		if P!={}: 
			stash=["[Player ",str(i)+"]",str(displayCard(P[i][-1])),"(","*",str(len(P[i])),")"]
			stash=" ".join(stash) #formats the elements within stash
		else: 
			a=[]
	print("Stash: ", "".join(str(stash)),"\nTable: ")#joins all the elements in the stash
	for i in range(len(T)): #adds N so that index aligns with the number of hands or players
		print([i+N],displayCard(T[i]))		
def deal(N,D,T,H):
	counter=4-len(T)#keeps track of how many cards need to be added to the table
	count=0 #keeps teack of how many times a round of cards is dealt out
	try:
		while count<3:
			for i in range(len(H)):
				H[i].append(D.pop())
			count=count+1
		while counter>0:
			T.append(D.pop(0)) 
			counter=counter-1
	except:
		print("Ooops! ran out of cards.")
	return (D, T, H)
def getMove(i, H, T, P):
	if P!={}:
		for x in P:
			for y in range(len(H[i])):
				if x!=i:
					if H[i][y][0]==P[x][-1]:#checks if automated hand matches user's current hand
						return(y,x)
						continue				
		for t in range(len(T)):
			for c in range(len(H[i])):
				if H[i][c][0] == T[t][0]:
					return(c, t)
		return((randint(1, len(H[i]))-1, None))
def pickCard(prompt, L):
    i = int(input(prompt))
    while i < 0 or i > len(L):
        i = int(input('Try again: {}'.format(prompt)))          
    return(i)

# Solicit a match from the table, including other player stashes, or
# specify a discard by entering the character 'x'. Recall player
# stashes are indexed by the player number (0 to N-1, inclusive),
# while cards on the table are indexed from N to N+len(T)-1,
# inclusive. Also note that not every player will have a stash, and
# that player 0 (the only player who gets to use pickMove() in the
# first place) can never capture his or her own stash.
def pickMove(prompt, i, N, T, P):
    while True:
        j = input(prompt)
        if j == 'x':
            return(None)
        j = int(j)
        if j <= 0 or j>= len(T)+N or j==i or (j < N and j not in P.keys()):
            continue
        return(j)

def play(N=2):
   D = shuffle()                  # Create a deck.
   T = []                         # Table top
   H = [ [] for i in range(N) ]   # Player hands
   P = { }                        # Player stash i:[c_bottom...c_top]
   # Play a game.
   while D:
      # Deal cards and (re)populate the table
      deal()
      D, T, H = deal(N, D, T, H)
      print("\n=========\nDealing...{} cards remain".format(len(D)))

      # Repeat while you (player 0) have cards in your hand.
      
      	
      while H[0]:
         # Show the state of the game from player 0 perspective.
         print("\n=========\nMy turn:")
         showTable(N, T, P)
         showHand(H[0])
         # Until you get a valid move. Will need to extend to sums in HW5.
         while True:
             # Return index of card player selects from hand.
             c = pickCard("Select a card to play from your hand (by index): ", H[0])
             # Return player stash to steal or card to match from table.
             t = pickMove("Select match (by index; x to discard): ", 0, N, T, P)

             # Make the play and break out of the while True loop. If
             # the specified play isn't legal, just continue and let
             # the while loop try again.
             if t == None:
                 T.append(H[0])
                 H.remove(H[0])
								 


             elif t < N and t in P.keys() and P[t][-1][0] == H[0][c][0]:
                 H[0][c].append(P[t])
                 P.pop(t)
								 



             elif t >= N and H[0][c][0] == T[t-N][0]:
                 H.pop([0][c][0])
                 P[t].append(H[0][c][0])
                 H[0][c].append(T[t-N][0])
                 T.pop([t-N][0])
								 



             else:
                 # Illegal move; try again.
                 print("Not a match: try again.")

         # Other players' turn.
         for i in range(1, N):
            # Show the state of the game from player i perspective.
            print("\n=========\nPlayer {}:".format(i))
            showTable(N, T, P)

            # Select move for player i. Note that getMove() is overly
            # simplistic and only picks matches from the table.
            (c, t) = getMove(i, H, T, P)

            # Make the play generated by getMove().
            #
            
            if t != None:
               # getMove() returns (c, t), meaning match card c
               # from player i's hand to cart t on the table.
               print("Took {} with {}".format(displayCard(T[t]), displayCard(H[i][c])))
               if i in P:
                  P[i].append(T.pop(t))
               else:
                  P[i] = [T.pop(t)]
               P[i].append(H[i].pop(c))
            else:
               # getMove() returns (c, None) meaning discard card c,
               # adding it to the cards currently on the table.
               print("Added {} to table".format(displayCard(H[i][c])))
               T.append(H[i].pop(c))

   # Game over. Figure out each player's score and return it as a dictionary.
   return({ p:sum([ l[0] for l in P[p] ]) for p in P.keys() })
		
	


