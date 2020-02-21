from Donsol.Game import Game
from Donsol.Deck import Deck
from Donsol.Display import Display
# a terrible, hideous file that handles the input loop and prints additional game state info
gameOver = False
firstMove = True
canEscape = False
escapedLast = False
game = Game()
deck = Deck()
display = Display()
# create our first room
print("You stand at the ruined entrance of the dungeon,\nthe bones and broken weapons of those who tried before you litter the ground.\nArmed with nothing but your wits,\nyou press forward to defeat the darkness.")
game.currRoom = deck.createRoom()
display.addRoom()
# Start input loop
while gameOver == False:
  # print status
  print('Cards Left: %d' % (deck.cardsLeft()))
  stat = ''
  if escapedLast and len(game.currRoom)!=1:
    stat = stat+"There's no escape!  "
  game.showStats()
  if game.shield == 0:
    stat = stat+'No Shield!  '
  if game.broken and game.shield != 0:
    stat = stat+'Shield damaged!  '
  if game.poisoned:
    stat = stat+'Healing!'
  if stat != '':
    print(stat)
  # print room
  display.displayRoom(game.currRoom)
  # print actions
  print('Select card#: 1-%d' % (len(game.currRoom)))
  if firstMove:
    print("Or enter 'r' to reshuffle the deck")
  if len(game.currRoom) == 1 or (len(game.currRoom) == 4 and escapedLast == False and firstMove == False):
    print("or enter 'e' to escape")
    canEscape = True
  else:
    canEscape = False
  # take/validate input
  command = input()
  if firstMove and command.lower() == 'r':
    deck.escapeRoom(game.currRoom)
    game.currRoom = deck.createRoom()
  if canEscape and command.lower() == 'e':
    if len(game.currRoom) != 1:
      escapedLast = True
    else:
      escapedLast = False
    if escapedLast:
      print("You decide to leave that room alone.")
    else:
      if game.monsterCheck():
        print("You dash past the creature and out of the room,\nits cries of anger the only thing chasing you.")
      else:
        print("You leave the items to rust.")
    deck.escapeRoom(game.currRoom)
    game.currRoom = deck.createRoom()
    display.addRoom()
  if (command.isnumeric() and int(command)<=len(game.currRoom)):
    game.selectCard(int(command)-1)
    firstMove = False
  elif firstMove == False and canEscape == False:
    print('bad input')
  # check if player has cleared room
  if game.emptyRoom():
    print("The room is empty, you move on.")
    game.currRoom = deck.createRoom()
    display.addRoom()
    escapedLast = False
  # check if player has won the game
  if (deck.containsMonsters() == False and game.monsterCheck() == False) or game.health <= 0:
    gameOver = True
  # newline for formatting
  print()
# print out the final screen
if(deck.containsMonsters() == False and game.monsterCheck() == False):
  print("You emerge bloody and beaten from the dungeon,\nbut the Donsols have been defeated, the evil rests for now.")
print('Game Over!')
