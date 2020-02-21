class Game:
  # handles game state and card interactions
  def __init__(self):
    self.health = 21
    self.shield = 0
    self.broken = False
    self.poisoned = False
    self.canEscape = True
    self.currRoom = []
    self.lastEnemy = 0

  def monsterCheck(self):
    bad = ['M','B','D']
    enemies = False
    for i in range(len(self.currRoom)):
      if any(j in self.currRoom[i] for j in bad):
        enemies = True
    return enemies

  def showStats(self):
    print('Health: %d | Shield: %d | Last Enemy: %d' % (self.health, self.shield, self.lastEnemy))

  def emptyRoom(self):
    return len(self.currRoom)==0

  def getShield(self, val):
    print("You grab a shield off the dungeon floor.")
    self.shield = val
    self.broken = False
    self.poisoned = False
    self.lastEnemy = 0
    
  def getHealth(self, val):
    if(self.poisoned == False):
      print("You feel strength swell within you.")
      self.health += val
      if (self.health > 21):
          self.health = 21
      self.poisoned = True
    else:
      print("You're unable to keep the potion down, it has no effect.")

  def attackMonster(self, val):
    if self.shield == 0:
      print("You attack the creature with your bare hands!")
    else:
      print("You bash the creature with your shield!")
    if(val < self.shield): # if attacking a weaker monster
      self.shield = val
      self.lastEnemy = val
      self.poisoned = False
      self.broken = True
      return # weaken shield
    if(val == self.shield): # if attacking a monster of equal strength
      if self.broken and val >= self.lastEnemy: 
        # if shield is already damaged
        self.shield = 0
        print("Your shield splinters and the full force of the creature's attack lands on you!")
      else:
        self.broken = True # damage shield
        self.lastEnemy = val
        self.poisoned = False
        return
    if(val > self.lastEnemy and self.broken): # if attacking a stronger monster and shield is damaged
      self.shield = 0
      print("Your shield splinters and the full force of the creature's attack lands on you!")
    self.health -= val-self.shield # calc damage to player
    self.lastEnemy = val
    self.poisoned = False
    self.broken = True


  def setRoom(self,room):
    self.currRoom = room

  def showRoom(self):
    print(self.currRoom)

  def calcVal(self,toCheck):
    if 'J' == toCheck:
      return 11
    if 'Q' == toCheck:
      return 13
    if 'K' == toCheck:
      return 15

  def selectCard(self, index):
    temp = self.currRoom.pop(index)
    val = temp[2:]
    number = val.isnumeric()
    bad = ['M','B']

    if 'S' in temp: # if shield
      if number:
        self.getShield(int(val))
      else:
        self.getShield(11)

    if 'H' in temp: # if health
      if number:
        self.getHealth(int(val))
      else:
        self.getHealth(11)

    if any(i in temp for i in bad): # if monster
      if number:
        self.attackMonster(int(val))
      else:
        self.attackMonster(self.calcVal(val))

    if 'D' in temp: # if Donsol
      self.attackMonster(21)
      print("The Donsol expires with a brilliant flash of energy.")
    if len(self.currRoom)==1:
      print("A way out of the room becomes clear.")