import random

class Character:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
    
    def attack_enemy(self, target):
        damage = max(1, self.attack)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
    
    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack=25, speed=5)
    
    def attack_enemy(self, target):
        if self.health < 30:
            print(f"{self.name} enters Berserk Mode! Attack power doubled!")
            damage = self.attack * 2
        else:
            damage = self.attack
        target.health -= damage
        print(f"{self.name} swings a sword! Deals {damage} damage.")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack=40, speed=7)
        self.mana = 50
    
    def attack_enemy(self, target):
        if self.mana >= 10:
            self.mana -= 10
            damage = self.attack
            print(f"{self.name} casts Fireball! Deals {damage} damage but loses 5 health.")
            self.health -= 5
        else:
            damage = self.attack
            print(f"{self.name} is out of mana! Casting regular attack.")
        target.health -= damage

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack=22, speed=10)
        self.critical_chance = 0.3
    
    def attack_enemy(self, target):
        if random.random() < self.critical_chance:
            damage = self.attack * 2
            print(f"{self.name} lands a Critical Hit! Deals {damage} damage.")
        else:
            damage = self.attack
            print(f"{self.name} shoots an arrow! Deals {damage} damage.")
        target.health -= damage

def battle(char1, char2):
    print(f"{char1.name} vs {char2.name} - Battle Start!")
    if char2.speed > char1.speed:
        char1, char2 = char2, char1
    
    while char1.is_alive() and char2.is_alive():
        char1.attack_enemy(char2)
        if char2.is_alive():
            char2.attack_enemy(char1)
    winner = char1 if char1.is_alive() else char2
    print(f"{winner.name} wins!")

warrior = Warrior("Thor")
mage = Mage("Gandalf")
archer = Archer("Alex")

battle(archer, warrior)
