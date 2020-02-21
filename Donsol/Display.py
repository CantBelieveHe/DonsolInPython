class Display:
  # translates the cards out of shorthand and prints the room
  def __init__(self):
     self.roomNo = 0
  
  def displayRoom(self,room):
    cardno = 1
    print('Room #%d:' % (self.roomNo))
    for i in room:
      ret = self.changeName(i)
      print("#%d: %s" % (cardno,ret))
      cardno += 1

  def changeName(self,card):
    # if shield
    if card[0] == 'S':
      if card[2].isalpha():
        ret = "Shield lvl: 11"
      else:
        ret = "Shield lvl: "+card[2:]
      return ret
    # if health
    if card[0] == 'H':
      if card[2].isalpha():
        ret = "Health lvl: 11"
      else:
        ret = "Health lvl: "+card[2:]
      return ret
    # if face card
    if card[2].isalpha():
      if card[2] == 'J':
        ret2 = '11'
      if card[2] == 'Q':
        ret2 = '13'
      if card[2] == 'K':
        ret2 = '15'
    # if beast
    if card[0] == 'B':
      if card[2].isalpha():
        ret = "Beast lvl: "+ret2
      else:
        ret = "Beast lvl: "+card[2:]
      return ret
    # if monster
    if card[0] == 'M':
      if card[2].isalpha():
        ret = "Monster lvl: "+ret2
      else:
        ret = "Monster lvl: "+card[2:]
      return ret
    # if Donsol
    if card == 'D.W':
      return 'The White Donsol'
    if card == 'D.R':
      return 'The Red Donsol'

  def addRoom(self):
    self.roomNo += 1

  def resetRoom(self):
    self.roomNo = 0