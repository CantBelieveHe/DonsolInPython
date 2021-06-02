import os

from Donsol.Game import Game
from Donsol.Deck import Deck
from Donsol.Display import Display
# handles the input loop, prints additional game state info

gameOver = False # flag marking if the game has ended, does not say if the player won or not
canEscape = False # flag marking if the player is allowed the escape the current room
escapedLast = False # flag tracking if the player escaped from the last room without clearing it 
turnNumber = 0
game = Game()
deck = Deck()
display = Display()

# create our first room
if os.name == 'posix':
  _ = os.system('clear')
else: # for windows platfrom
  _ = os.system('cls')
display.Opening()
game.currRoom = deck.createRoom()
game.incRoomNo() # increment room number to 1
# the room then gets printed in the input loop

# Start game loop
while gameOver == False:
  turnNumber+=1
  print("---- Turn %d ----" %(turnNumber))

  # if the is only 1 card left, or the room is full and the player can escape and this isnt the first move of the game
  if game.getRoomSize() == 1 or (game.getRoomSize() == 4 and escapedLast == False):
    canEscape = True
  else:
    canEscape = False

  # -- printing section --
  # print game info
  # show deck, health, and shield status
  display.showStats(deck.cardsLeft(),game.getStats())
  
  # print alerts
  display.showAlerts(escapedLast,game.getAlerts())

  # print room
  display.displayRoom(game.getRoom(), game.getRoomNo())

  # print possible actions
  display.showActions(game.getRoomSize(),deck.cardsLeft(),canEscape)

  # -- input section --
  # take/validate input
  command = input()
  # if deck is full and room is full then the player hasnt made a move yet and can reshuffle
  if command.lower() == 'q':
    gameOver = True
    break
  if deck.cardsLeft()==50 and game.getRoomSize()==4 and command.lower() == 'r':
    print("Reshuffling...")
    deck.escapeRoom(game.currRoom) # return the cards in the room to the deck
    game.currRoom = deck.createRoom() # draw a new room

  elif canEscape and command.lower() == 'e': # if the player can escape and chooses to
    if game.getRoomSize() != 1: # if the room has more than card left
      escapedLast = True # block the player from escaping the next room
    else:
      escapedLast = False # allow the player to escape the next room

    # print message based on what type of escape the player just did
    display.escapeMessage(escapedLast,game.monsterCheck())

    deck.escapeRoom(game.getRoom()) # return the remaining cards to the deck
    game.setRoom(deck.createRoom()) # draw a new room
    game.incRoomNo() # increment the room counter

  # if the player inputs a number and the number is <= the number of cards in the room
  elif (command.isnumeric() and int(command)<=game.getRoomSize()): 
    game.selectCard(int(command)-1) # adjust the input since the array is base 0 and activate that card  

  # else the input is invalid
  else:
    print("bad input! :(")

  # check if the player has won/lost the game
  if (deck.containsMonsters() == False and game.monsterCheck() == False) or game.health <= 0:
    gameOver = True # we test if the player has won outside of the main game loop

  # if the player just activated the 3rd card in the rooom
  if game.getRoomSize()==1:
    print("A way out of the room becomes clear.")

  # check if player has cleared room
  if game.emptyRoom(): # if the room is empty
    print("The room is empty, you move on.")
    game.setRoom(deck.createRoom()) # draw new room
    game.incRoomNo() # increment the room counter
    escapedLast = False # allow the player to escape the next room

  # -- end of game loop --

# print out the final screen
display.finalScreen(deck.containsMonsters(),game.monsterCheck(),game.checkHealth())