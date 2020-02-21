# DonsolInPython
Designed by John Eternal, Donsol is a game where you explore a dungeon made out of a standard 54-card deck. You win the game by elimnating all monsters from the deck.
Remade in python to run in the command line by me.
Check out the original here:
https://100r.co/site/donsol.html#what_is_donsol?
https://wiki.xxiivv.com/site/donsol.html

# How To Play:
Download this repo,
Open up the folder in your CLI
Type: 'python main.py'
Enjoy!

# Game Rules:
Diamonds are shields and are used to defeat monsters.
Hearts are health potions.
The other half of the deck is made up of monsters, with jesters (Donsols) being the strongest.

Diamonds/Shields:
  Shields absorb their value in damage and defeat the selected monster, the difference between the shield and monster's strengths is dealt as damage to the player. Face cards have a strength of 11.
  Once a shield is used for the first time it is damaged, and it can only withstand an attack from a monster of lesser strength to the last. If a monster attacks a damaged shield of lesser strength, that shield will break and the player will take full damage.

Hearts/Health:
  The player has a max health of 21 hp.
  Health potions restore their value in hp, with face cards being worth 11 hp.
  Drinking more than one health potion in a row will not heal you.
  Should the player's health >= 0 then the game is lost.

Monsters:
  Monsters have strength equal to their value with face cards having the following values: J: 11, Q:13, K: 15, and jesters (or Donsols): 21
  monsters can be defeated in any order, and once every monster has been defeated the game has been won.

Rooms:
  Each room contains four random cards.
  The player will automatically leave the room if there are no cards left. If there is only one card left then the player can leave without penalty. If there is more than one card left in the room then the player can escape, but only if they did not escape the last room.
