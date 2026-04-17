# item
class itemDefault:
    def __init__(self):
        self.name = "item"
        self.effect = "attack"
        self.effectValue = 10
        self.description = "item description"

    def useItem(self):
        print(f"{self.name} has been used, {self.effect} has gone up by {self.effectValue}")
        

class vita(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Vita"
        self.effect = "recovery"
        self.effectValue = 50
        self.description = "Recover Hp by 50"

    def useItem(self, player):
        print(f"{player} has been blessed by Vita, recover 50 Hp")

# 1. Infinity Edge
class infinityEdge(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Infinity Edge"
        self.effect = "attack"
        self.effectValue = 10
        self.description = "Boost critical strike damage massively"
    def useItem(self, player):
        print(f"{player} used {self.name}, damage increased by {self.effectValue}%")

# 2. Zhonya's Hourglass
class zhonyasHourglass(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Zhonya's Hourglass"
        self.effect = "defense"
        self.effectValue = 10
        self.description = "Enter stasis and become invulnerable briefly"
    def useItem(self, player):
        print(f"{player} used {self.name}, entered stasis for {self.effectValue} seconds")

# 3. Banshee's Veil
class bansheesVeil(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Banshee's Veil"
        self.effect = "defense"
        self.effectValue = 15
        self.description = "reduce next incoming enemy attack"
    def useItem(self, player):
        print(f"{player} used {self.name}, Incoming attack recude by {self.effectValue}")

# 4. Rabadon's Deathcap
class rabadonsDeathcap(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Rabadon's Deathcap"
        self.effect = "attack"
        self.effectValue = 35
        self.description = "Amplify damage by 35"
    def useItem(self, player):
        print(f"{player} used {self.name}, total power amplified by {self.effectValue}")

# 5. Warmog's Armor
class warmogsArmor(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Warmog's Armor"
        self.effect = "Recovery"
        self.effectValue = 100
        self.description = "Rapidly regenerate health in combat"
    def useItem(self, player):
        print(f"{player} used {self.name}, regenerating {self.effectValue} Hp")


# 1. Malefic Gun
class maleficGun(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Malefic Gun"
        self.effect = "attack"
        self.effectValue = 10
        self.description = "Increase attack penetration"

    def useItem(self, player):
        print(f"{player} used {self.name}, attack penetration + {self.effectValue}")


# 2. Sea Halberd
class seaHalberd(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Sea Halberd"
        self.effect = "attack"
        self.effectValue = 50
        self.description = "increase attack"

    def useItem(self, player):
        print(f"{player} used {self.name}, increase attack by {self.effectValue}%")


# 3. Hunter Strike
class hunterStrike(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Hunter Strike"
        self.effect = "attack"
        self.effectValue = 15
        self.description = "Increase Crit temporarily"

    def useItem(self, player):
        print(f"{player} used {self.name}, attack increase by {self.effectValue} Temporary")


# 4. Blade of Despair
class bladeOfDespair(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Blade of Despair"
        self.effect = "attack"
        self.effectValue = 100
        self.description = "Massive attack boost"

    def useItem(self, player):
        print(f"{player} used {self.name}, attack increased by {self.effectValue}")


# 5. Endless Battle
class endlessBattle(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Endless Battle"
        self.effect = "attack"
        self.effectValue = 45
        self.description = "Gain attack"

    def useItem(self, player):
        print(f"{player} used {self.name}, gained attack {self.effectValue}")

# equipment
class equipmentDefault:
    def __init__(self):
        self.name = "equipment name"
        self.effect = "defense"
        self.effectValue = 10

    def description(self, character):
        print(f"{self.name} give the {character} {self.effect}")

class rageAnklet(equipmentDefault):
    def __init__(self):
        super().__init__()
        self.name = "rage Angklet"
        self.effect = "attack"
        self.effectValue = 10
    
    def description(self, character):
        print(f"Make {self.name} stronger by giving {character} {self.effect}")

class nimbleHammer(equipmentDefault):
    def __init__(self):
        super().__init__()
        self.name = "Nimble Hammer"
        self.effect = "attack"
        self.effectValue = 15

    def description(self, character):
        print(f"Increase wearer attack by {self.effectValue}")

class watchfulEyes(equipmentDefault):
    def __init__(self):
        super().__init__()
        self.name = "Watchful Eyes"
        self.effect = "defense"
        self.effectValue = "20"
    
    def description(self, character):
        print(f"Gain protection from the gods, increase defense by {self.effectValue}")

class sparklingSoda(equipmentDefault):
    def __init__(self):
        self.name = "Sparkling Soda"
        self.effect = "attack"
        self.effectValue = 30

    def description(self, character):
        print(f"{character} just drank a Soda, attack increase by {self.effectValue}")

class emblemOfTheGreatest(equipmentDefault):
    def __init__(self):
        
        self.name = "Emblem of The Greatest"
        self.effect = "Level up"
        self.effectValue = 1

    def description(self, character):
        print(f"The greatest honor of all, permanently increase level by {self.effectValue}")

# character
class boss:
    def __init__(self):
        self.name = "the dark lord"
        self.hp = 100
        self.level = 10
        self.defense = 10
        self.attack = 15

    def attack(self, value):
        print(f"{self.name} attack for {value}")

    def item(self, item):
        print(f"{self.name} using {item.name} to boost {item.effect} ")

    def dodge(self):
        print(f"{self.name} dodge the attack!")

class character(boss):
    def __init__(self):
        super().__init__()
        self.name = "hero"
        self.hp = 50
        self.level = 1
        self.atk = 10
        self.defense = 5

    def attack(self, value):
        print(f"{self.name} bravely attacks for {value}")

    def item(self):
        print(f"{self.name} buff him self with an item")

    def dodge(self):
        print(f"the {self.name} was getting attack, but luckly he dodged it")



# import all class to main 
__all__ = [
    # Item classes
    "itemDefault",
    "vita",
    "infinityEdge",
    "zhonyasHourglass",
    "bansheesVeil",
    "rabadonsDeathcap",
    "warmogsArmor",
    "maleficGun",
    "seaHalberd",
    "hunterStrike",
    "bladeOfDespair",
    "endlessBattle",
    # Equipment classes
    "equipmentDefault",
    "rageAnklet",
    "nimbleHammer",
    "watchfulEyes",
    "sparklingSoda",
    "emblemOfTheGreatest",
    # Character classes
    "boss",
    "character"
]