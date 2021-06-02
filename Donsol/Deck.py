import random
class Deck:
  # contains 'deck' of cards and handles drawing/returning cards to/from rooms
  def __init__(self):
    self.cards = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK','M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','MJ','MQ','MK','G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','GJ','GQ','GK','DR','DW']

  def cardsLeft(self):
    return len(self.cards)

  def containsMonsters(self): # should this return false, the game has been won
    bad = ['M','G','D']
    enemies = False
    for i in range(len(self.cards)):
      if any(j in self.cards[i] for j in bad):
        enemies = True
    return enemies

  def createRoom(self): # creates a new room with 4 random cards
    roomCards = [] # array that holds the cards in the current room
    roomSize = 0
    if len(self.cards) == 0: # if the deck runs out 
        print("this shouldnt happen")
        return
    if len(self.cards) >= 4: # if there are 4 or more cards left in the deck
      roomSize = 4 # add 4 cards to the room
    else: # else add whatever cards are left in the deck
      roomSize = len(self.cards)
    for i in range(roomSize): # for each card in the room
      if len(self.cards) == 0: # if the deck runs out 
        print("this shouldnt happen")
        return
      cardIndex = random.randint(0,len(self.cards)-1) # pick a random card from the deck
      roomCards.append(self.cards.pop(cardIndex)) # remove the card from the deck array and add it to the room array
    return roomCards

  def escapeRoom(self, roomCards): # returns cards remaining in room to the deck
    self.cards = self.cards + roomCards