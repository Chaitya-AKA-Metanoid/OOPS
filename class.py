import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def print_info(self):
        print(f"'{self.name}' stats \n-------------- \nhealth = {self.health} \nattack power = {self.attack} \ndefense = {self.defense}\n")

    def attack_enemy(self, enemy):
        attack = random.randint(1, self.attack)  # Random attack value
        damage = max(attack - enemy.defense, 0)  # Ensure damage can't be negative
        enemy.health = max(enemy.health, 0)  # Ensure enemy health can't go below 0
        enemy.health -= damage  # Apply damage to enemy
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        print(f"{enemy.name}'s health is now {enemy.health}\n")

    def is_alive(self):
        return self.health > 0  # Return True if the character is alive

# Create characters
wizard = Character("Oz", 110, 10, 6)
knight = Character("Metanoid", 80, 15, 3)

# Fight loop
while wizard.is_alive() and knight.is_alive():
    wizard.attack_enemy(knight)
    if knight.is_alive():  # Knight only attacks if still alive
        knight.attack_enemy(wizard)

# After the fight
if wizard.is_alive():
    print("\n\nYou have Won!")
else:
    print("\n\nYou have Lost!")

# Print final stats
wizard.print_info()
knight.print_info()
