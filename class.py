class character:
    def __init__(self, name, health, attack, defense ):
        self.name=name
        self.health = health
        self.attack = attack
        self.defense = defense 

    def print_info(self):
        print(f" '{self.name}' stats \n -------------- \n health = {self.health} \n attack power = {self.attack} \n defense = {self.defense} \n" )

Wizard = character("Oz", 80, 15, 10)
Knight = character("Metanoid", 100, 10, 5)

Wizard.print_info()
Knight.print_info()

