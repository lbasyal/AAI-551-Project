#Project: Card Game #LOCHAN BASYAL #20009277
#EE 551 Engineering Programming: Python
"""
****************************************************************************************************************
This is the Gaming project "Best Card" 
The highest priority of the card is "King of Spades" and the lowest priority of the card is "Ace of Clubs"
Spades > Hearts > Diamonds > Clubs
King > Queen > Jack > Ace
****************************************************************************************************************
Spades => 3
Hearts => 2
Diamonds =>1
Clubs => 0

Ace => 1
Jack => 11
Queen => 12
King => 13
****************************************************************************************************************
"""
import random
import math  
class Card: #class Card 
    #suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
    suit_list = ["Clubs0", "Diamonds1", "Hearts2", "Spades3"]
    rank_list = ["None", "Ace1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack11", "Queen12", "King13"]
    #rank_list = ["None", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    
    def __init__(self, suit = 0, rank = 2): #initialization 
        self.suit = suit
        self.rank = rank
    
    def __str__(self): #Printing the string 
        return (self.rank_list[self.rank] + " of " + self.suit_list[self.suit])
    
    def __eq__(self, other): #function to check equality
        return(self.rank == other.rank and self.suit == other.suit)
    
    def __gt__(self, other): #function for greater than 
        if self.suit > other.suit:
            return True
        elif self.suit == other.suit:
            if self.rank > other.rank:
                return True
        return False
#c = Card(3,13)
#print(c)
class Deck:  #class Deck
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
                
    def __str__(self):  #Printing the string
        s = ""
        for i in range(len(self.cards)):
            s += i * " " + str(self.cards[i]) + "\n"
        return s
    
    def shuffle(self):  #Shuffling the card
        n_cards = len(self.cards)
        for i in range(n_cards):
            j = random.randrange(0, n_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
            
    def pop_card(self):  #popping the card
        return self.cards.pop()
    
    def is_empty(self):  #check the isimpty
        return len(self.cards) == 0
    
    def deal(self, hands, n_cards = 52): #dealing the card
        n_players = len(hands)
        for i in range(n_cards):
            if self.is_empty():
                break
            card = self.pop_card()
            current_player = i % n_players
            hands[current_player].add_card(card)   
            
#Checking the operation (execution of the program) is it goes as per the expectation?
#d = Deck()
#d.shuffle()
#print(d)
#d.pop_card()
#len(d.cards)

class Hand(Deck):  #class Hand derived from the Deck
    def __init__(self, name = ""):
        self.cards = []
        self.name = name
    
    def add_card(self, card):  #add card function
        self.cards.append(card)
    
    def __str__(self):  #Printing the string
        s = "Hand " + self.name
        if self.is_empty():
            return s + "is empty"
        s += " contains \n" + Deck.__str__(self)
        return s
    
    
  #execution of the program starts from here by calling the appropriate function
d = Deck()   
print("Deck of cards\n")
print(d)
d.shuffle() #shuffling the card
print("After Shuffled Deck\n")
print(d)
print("\n")
hand = Hand("Lochan")
hand1 = Hand("Anish")
hand2 = Hand("Binita")
players = [hand, hand1, hand2]
d.deal(players, 9)
#this concept will help to distribute the shuffled cards to all the payers with
#any number of cards in each players hand
#print(hand, hand1, hand2)
print(hand)
print(hand1)
print(hand2)
""" 
*********************************************************************************************************************
The unique specialty of my project: 
I implemented this concept for those players who wish to play with their own rules and decide who wins the game.
Here, I can distribute an equal number of cards to each player, just changing the value "d.deal(players, 9)" in 
place of 9 in the code.

Spades => 3
Hearts => 2
Diamonds =>1
Clubs => 0

Ace => 1
Jack => 11
Queen => 12
King => 13)
*******************************************************************************************************************
"""
#import math

d = Deck()
print(d)
d.shuffle()
print(d)
a = d.pop_card()
print("Lochan:", a)
b = d.pop_card()
print("Jonas:", b)
c = d.pop_card()
print("Anish:", c)
e = d.pop_card()
print("Samita:", e)
f = d.pop_card()
print("Anil:", f)
g = d.pop_card()
print("Santosh:", g)


h = max (a, b, c, e, f, g)
print("\nThe maximum value between six:",h)
print("\n")
#print("In this project, the maximum value is calculated in such a way that the lowest value starting 
# from clubs of Ace to the highest val Spades of King")
if h == a:
    print("Congratulations! Lochan, you win the game")
    print("\n")
elif h == b:
    print("Congratulations! Jonas, you win the game")
    print("\n")
elif h == c:
    print("Congratulations! Anish, you win the game")
    print("\n")
elif h == e:
    print("Congratulations! Samita, you win the game")
    print("\n")
elif h == f:
    print("Congratulations! Anil, you win the game")
    print("\n")
else:
    print("Congratulations! Santosh, you win the game")
    print("\n")

"""
In this project, the player who has the highest priority wins the game. It is simple to play and not more time consuming for players to win the game.  
The priority of the card is setup in such a way that, 
Spades => 3
Hearts => 2
Diamonds =>1
Clubs => 0

Ace => 1
Jack => 11
Queen => 12
King => 13
***(King of spades) is in the higher priority and (Clubs of Ace) is in the lowest priority.

***Features:
***This project calculated the maximum value of card between the players
***Easy to understand the game rules and play with less time consuming
***Also provide the equal number of shuffled card to all the players for playing the game as 
per their rules and regulations. By doing this, players can decide any gaming approach.

"""