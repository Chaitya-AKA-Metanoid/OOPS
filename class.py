import random

def display_health_bar(character):
    bar_length = 20
    health_ratio = character.health / 110 if character.name == "Oz" else character.health / 80
    filled_length = int(bar_length * health_ratio)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    return f"{character.name}: [{bar}] {character.health} HP"

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def print_info(self):
        print(f"\n'{self.name}' stats\n--------------")
        print(f"Health       = {self.health}")
        print(f"Attack Power = {self.attack}")
        print(f"Defense      = {self.defense}\n")

    def attack_enemy(self, enemy):
        attack_value = random.randint(1, self.attack)
        damage = max(attack_value - enemy.defense, 0)
        damage = min(damage, enemy.health)
        enemy.health -= damage
        print(f"⚔️ {self.name} attacks {enemy.name} for {damage} damage!")
        print(display_health_bar(enemy))

    def is_alive(self):
        return self.health > 0


class Wizard(Character):
    def cast_spell(self, enemy):
        spell_damage = self.attack + 5
        damage = max(spell_damage - enemy.defense, 0)
        damage = min(damage, enemy.health)
        enemy.health -= damage
        print(f"✨ {self.name} casts a spell on {enemy.name} for {damage} damage!")
        print(display_health_bar(enemy))


class Knight(Character):
    def shield(self):
        self.defense += 5
        print(f"🛡️ {self.name} raises a shield! Defense temporarily increased to {self.defense}.\n")


# Create characters
wizard = Wizard("Oz", 110, 10, 6)
knight = Knight("Metanoid", 80, 20, 3)

# Game loop
while wizard.is_alive() and knight.is_alive():
    print("\n" + "="*30)
    print(display_health_bar(wizard))
    print(display_health_bar(knight))
    print("="*30)
    
    print("\nYour turn! Choose an action:")
    print("1. ⚔️ Attack")
    print("2. ✨ Cast Spell")

    try:
        spl_attack = int(input("Enter your choice (1 or 2): "))
    except ValueError:
        print("❌ Invalid input. Please enter 1 or 2.\n")
        continue

    if spl_attack == 1:
        wizard.attack_enemy(knight)
    elif spl_attack == 2:
        wizard.cast_spell(knight)
    else:
        print("❌ Invalid choice. Please select 1 or 2.\n")
        continue

    if not knight.is_alive():
        break

    print("\n🤖 Knight's turn!")
    action = random.choice(['attack', 'shield'])
    if action == 'attack':
        knight.attack_enemy(wizard)
    else:
        knight.shield()

# Game result
print("\n🏁 Game Over!")
if wizard.is_alive():
    print("🎉 You have Won!")
else:
    print("💀 You have Lost!")

# Final stats
print("\n📊 Final Stats:")
wizard.print_info()
knight.print_info()
