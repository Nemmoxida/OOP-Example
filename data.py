# item
class itemDefault:
    def __init__(self):
        name = "item"
        effect = "attack"
        effectValue = 10
        description = "item description"

    def useItem(self):
        print(f"${self.name} has been used, ${self.effect} has gone up by ${self.effectValue}")
        


# equipment
class equipmentDefault:
    def __init__(self):
        name = "uquipment name"
        effect = "defense"
        effectValue = 10
        description = "equipment description"

    def use(self, character):
        print(f"{self.name} give the ${character} {self.effect}!")

# character
class boss:
    def __init__(self):
        name = "the dark lord"
        hp = 100
        level = 10

    def attack(self, value):
        print(f"${self.name} attack for ${value}")

    def item(self, item):
        print(f"${self.name} using ${item.name} to boost ${item.effect} ")

    def dodge(self):
        print(f"${self.name} dodge the attack!")

class character(boss):
    def __init__(self):
        super().__init__()
        self.name = "hero"
        self.hp = 50
        self.level = 1

    def attack(self, value):
        print(f"{self.name} bravely attacks for {value}")

    def item(self):
        print(f"${self.name} buff him self with an item")

    def dodge(self):
        print(f"the ${self.name} was getting attack, but luckly he dodged it")



# import all class to main 
__all__ = [
    "itemDefault",
    "equipmentDefault",
    "boss",
    "character"
]