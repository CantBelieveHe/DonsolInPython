class Display:
  # translates the cards out of shorthand and prints the room

  def Opening(self):
    print("DONSOL, designed by John Eternal, ported by Carson Elmer")
    print("Enter 'q' to quit at any time")
    print("\nYou awaken in a dungeon wearing strange robes,\nthe cries of dreadful beasts echoing through the halls.\nTwo stars burn unbearably bright in your mind's eye,\nyou must find them, you must kill them.\n")

  def showStats(self,count,stats):
    print('Health: %d | Shield: %d | Last Enemy: %d | Cards Left: %d' %(stats[0], stats[1], stats[2], count))

  def showAlerts(self,escapedLast,alerts): # alerts[ 0: roomSize(int), 1: shield(int), 2: broken(bool), 3: poisoned(bool)]
    stat = ''
    if escapedLast and alerts[0]!=1:
      stat = stat+"There's no escape!  "

    if alerts[1] == 0:
      stat = stat+'No Shield!  '
    elif alerts[2]==True:
      stat = stat+'Shield damaged!  '

    if alerts[3]==True:
      stat = stat+'Healing!'
    if stat != '': # only print this line if there is something to print
      print(stat)

  def showActions(self,roomSize,cardsLeft,canEscape):
    print('Select card#: 1-%d' % (roomSize))
    if cardsLeft==50 and roomSize==4:
      print("Or enter 'r' to reshuffle the dungeon")
    elif roomSize==1 or (roomSize==4 and canEscape==True):
      print("or enter 'e' to escape")

  def escapeMessage(self,escapedLast,monster):
    if escapedLast: # if the player wont be able to escape again
      print("You double back and decide to try a different room.")
    else: # if the player will be able to escape again
      if monster:
        print("You dash past the creature and out of the room.")
      else:
        print("You leave the item for someone else.")

  def finalScreen(self,deckCheck,roomCheck,health):
    if(deckCheck == False and roomCheck() == False): # there are no monsters left, the player has won the game
      print("You emerge bloody and beaten from the dungeon,\nthe Donsols have been defeated, evil rests for now.")
    elif health <= 0: # the player is out of health and has lost the game
      print("You succumb to your wounds, joining the nameless dead of the dungeon.")
    print("Game Over! Thanks for Playing!")

  def displayRoom(self,room,roomNo):
    cardno = 1
    print("Room #%d:" %(roomNo))
    for i in room:
      ret = self.changeName(i)
      print("#%d: %s" % (cardno,ret))
      cardno += 1

  def changeName(self,card):
    # if shield
    if card[0] == 'S':
      if card[1].isalpha():
        ret = "Shield lvl: 11"
      else:
        ret = "Shield lvl: "+card[1:]
      return ret
    # if health
    if card[0] == 'H':
      if card[1].isalpha():
        ret = "Health lvl: 11"
      else:
        ret = "Health lvl: "+card[1:]
      return ret
    # if face card
    if card[1].isalpha():
      if card[1] == 'J':
        ret2 = '11'
      if card[1] == 'Q':
        ret2 = '13'
      if card[1] == 'K':
        ret2 = '15'
    # if beast
    if card[0] == 'G':
      if card[1].isalpha():
        ret = "Goblin lvl: "+ret2
      else:
        ret = "Goblin lvl: "+card[1:]
      return ret
    # if Minotaur
    if card[0] == 'M':
      if card[1].isalpha():
        ret = "Minotaur lvl: "+ret2
      else:
        ret = "Minotaur lvl: "+card[1:]
      return ret
    # if Donsol
    if card == 'DW':
      return 'The White Donsol'
    if card == 'DR':
      return 'The Red Donsol'
