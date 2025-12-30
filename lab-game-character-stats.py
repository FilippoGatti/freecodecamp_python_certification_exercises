class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        self._health = value
        if self._health < 0:
            self._health = 0
        if self._health > 100:
            self._health = 100
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, value):
        self._mana = value
        if self._mana < 0:
            self._mana = 0
        if self._mana > 50:
            self._mana = 50

    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")
    
    def __str__(self):
        return f"Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}\n"
