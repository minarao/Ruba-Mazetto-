# CS1210 HW3
# Mina Rao
# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.
from random import randint
from time import time
import matplotlib.pyplot as plt
######################################################################
# Some functions you will need to use.
# Returns a random 40-element string from (0, 1) that represents
# left-right when shuffling a deck of 40 cards.
 
def bits(l=40):
    return( [ randint(0,1) for i in range(l) ] )
def createDeck():
    deck=[]
    suit=["spades","hearts","diamonds","clubs"]
    for x in suit:
        for y in range(1,11):
            deck.append((y,x))
    return deck
             
def riffle(D = createDeck(), r = 5):
    count=0
    bit=bits()
    riffledeck=[]
    left=D[:20]
    right=D[20:]    
    while count<r:       
        for x in range(len(bit)):
            if left==[]: #checks if bits is all ones
                riffledeck=riffledeck+right
                break
            if right==[]:#checks if bits is all zeros
                riffledeck=riffledeck+left
                break
            if bit[x]==0:
                riffledeck.append(left.pop(0))
            elif bit[x]==1:
                riffledeck.append(right.pop(0))
            else:
                pass
        count=count+1 #counts the number of times deck is shuffled
        #reorders deck in shuffled order
        left=riffledeck[:20]
        right=riffledeck[20:]
    #accounts for an error of continuously appending list onto deck
    riffled=riffledeck[len(riffledeck)-40:len(riffledeck)]
    return riffled
def entropy(D):
    count=0 
    for x in range(1,len(D)):
        # checks if deck order doesn't ascend by one
        if D[x-1][0]!=D[x][0]-1 and D[x-1][1]==D[x][1]:
            count=count+1
        # accounts for if cards are not in same suit
        elif D[x-1][0]!=10 and D[x-1][0]!=D[x][0]-1:
            count=count+1 #counts number of times deck is out of order
    return count
def testEntropy(r=range(0, 1000,10),m=100):
    plt.title("Entropy values for riffle")
    plt.xlabel( "Trial")
    plt.ylabel( "Average number of Entropy Values")
    # each bar represents the average of 100 riffled entropy values
    plt.bar(r,[sum([entropy(riffle(createDeck(),i))for k in range(0,m)]) for i in r]) #k=range for y axis, i for x-axis
    plt.show()
def testRunTime(r=range(0,1000,10), m=100):
    start=time()
    [riffle(createDeck(),i)for k in range(0,m) for i in r] 
    print(format(time()- start))
     
# Fisher-Yates-Knuth fair shuffle.
def shuffle(D = createDeck()):
    i = len(D)-1
    while i > 0:
     j = randint(0, i)
     D[i], D[j] = D[j], D[i]
     i = i-1
    return(D)
##################################################################
