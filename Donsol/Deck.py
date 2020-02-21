import random
class Deck:
  # contains 'deck' of cards and handles drawing/returning cards for rooms
  def __init__(self):
    self.cards = ['S.1','S.2','S.3','S.4','S.5','S.6','S.7','S.8','S.9','S.10','S.J','S.Q','S.K','H.1','H.2','H.3','H.4','H.5','H.6','H.7','H.8','H.9','H.10','H.J','H.Q','H.K','M.1','M.2','M.3','M.4','M.5','M.6','M.7','M.8','M.9','M.10','M.J','M.Q','M.K','B.1','B.2','B.3','B.4','B.5','B.6','B.7','B.8','B.9','B.10','B.J','B.Q','B.K','D.R','D.W']

  def cardsLeft(self):
    return len(self.cards)

  def containsMonsters(self): # should this return true, the game has been won
    monster = 'M'
    beast = 'B'
    donsol = "D"
    rMonster = [i for i in self.cards if monster in i]
    rBeast = [i for i in self.cards if beast in i]
    rDonsol = [i for i in self.cards if donsol in i]
    if(len(rMonster)==0 and len(rBeast)==0 and len(rDonsol)==0):
      return False
    else:
      return True

  def createRoom(self): # creates a new room with 4 random cards
    roomCards = []
    roomSize = 0
    if len(self.cards) >= 4:
      roomSize = 4
    else:
      roomSize = len(self.cards)
    for i in range(roomSize):
      if len(self.cards) == 0:
        return
      cardIndex = random.randint(0,len(self.cards)-1)
      roomCards.append(self.cards.pop(cardIndex))
    return roomCards

  def escapeRoom(self, roomCards): # returns cards remaining in room to the deck
    self.cards = self.cards + roomCards