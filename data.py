# item
class itemDefault:
    def __init__(self):
        name = "item"
        effect = "attack"
        effectValue = 10
        description = "item description"
        


# equipment
class equipmentDefault:
    def __init__(self):
        name = "uquipment name"
        effect = "defense"
        effectValue = 10
        description = "equipment description"

# character

class boss:
    def __init__(self):
        name = "the dark lord"
        hp = 100
        level = 100

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
        print(f"${self.name} the ${self.name} was getting attack, but luckly he dodged it")