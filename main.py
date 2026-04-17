from data import *
import time
import sys
import random

# Assign class boss and player to make an objct
enemy = boss()
player = character()


# function to handle dialog
def dialogWrite(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char == "." and "?":
            time.sleep(0.5)
        else:
            time.sleep(delay)


# chance value is between 0 to 50
def rngRoll(chance, k=2):
    # exponantial curve
    normalized = chance / 50
    p = normalized ** k
    
    return 1 if random.random() <= p else 0

# handle item damage temporary
temporaryDamage = 0

# handle equipment calc (f it's working that is)
def equipmentDamageCacl(equip):
    damageTotal = 0
    for equipment in equip:
        if equipment.effect == "attack":
            damageTotal += equipment.effectValue
    return damageTotal

# handle player turn
def player_turn(player_obj, enemy_obj):
    print(f"\n{player_obj.name}'s turn!")
    print(f"HP: {player_obj.hp}")
    print("1. Attack")
    print("2. Use Item")
    choice = input("\n")
    
    if choice == "1":
        # Attack RNG
        if rngRoll(random.randint(30,50)):
            global temporaryDamage
            equipmentDamage = equipmentDamageCacl(equipmentInventory)
            damage = player_obj.atk + equipmentDamage + temporaryDamage
            enemy_obj.hp -= damage
            print(f"You hit! Dealt {damage} damage to {enemy_obj.name}!")
            print(f"{enemy_obj.name} HP: {enemy_obj.hp}")
            temporaryDamage = 0
        else:
            dodge(enemy_obj)
    elif choice == "2":
        # Ask for item type
        print("Choose item type:")
        print("1. Attack")
        print("2. Defense")
        print("3. Recovery")
        type_choice = input("\n")
        if type_choice == "1":
            type_str = "attack"
        elif type_choice == "2":
            type_str = "defense"
        elif type_choice == "3":
            type_str = "recovery"
        else:
            print("Invalid item type.")
            return

        # Show only items of that type
        filtered_items = [item for item in itemInventory if str(item.effect).lower() == type_str] # will chose based on the type_str
        if not filtered_items:
            print(f"No items of type {type_str} available.")
            return
        print("Available items:")
        # print item list and use enumerate
        for idx, item in enumerate(filtered_items, 1):
            print(f"{idx}. {item.name} - {item.description}")
        # input item choise
        item_choice = input("Choose item by number: ")

        # handle player choise
        try:
            item_idx = int(item_choice) - 1
            chosen_item = filtered_items[item_idx]
        except (ValueError, IndexError):
            print("Invalid item selection.")
            return
        # Apply item effect

        # ccheck if an item has atr attack or recovery
        if hasattr(chosen_item, "effect") and str(chosen_item.effect).lower() == "attack":
            temporaryDamage
            temporaryDamage += chosen_item.effectValue
            chosen_item.useItem()
        chosen_item.useItem(player.name)
        if hasattr(chosen_item, "effect") and str(chosen_item.effect).lower() == "recovery":
            player.hp += chosen_item.effectValue
            chosen_item.useItem(player.name)

        if hasattr(chosen_item, "effect") and str(chosen_item.effect).lower() == "defense":
            player.defense += chosen_item.effectValue
            chosen_item.useItem(player.name)

    else:
        print("Invalid choice")

# handle boss turn
def boss_turn(enemy_obj, player_obj):
    print(f"\n{enemy_obj.name}'s turn!")
    damage = round(15 *(enemy_obj.level / 20) + (10/player_obj.defense + 10))
    player_obj.hp -= damage
    print(f"{enemy_obj.name} hit you! Took {damage} damage!")
    print(f"Your HP: {player_obj.hp}")



# apply training stat if succeed
def apply_training_stat(player_obj, training_choice):
    if training_choice == "1":
        player_obj.atk += 10
        print(player_obj.atk)
        print("Attack training success! Attack +10")
    elif training_choice == "2":
        player_obj.defense += 10
        print("Defense training success! Defense +10")
    elif training_choice == "3":
        player_obj.int += 5
        player_obj.atk += 5
        print("Agility training success! Intelligence +5, Attack +5")
    elif training_choice == "4":
        player_obj.level += 10
        print("Luck training success! Level +10")



# polymorph Concept. duck typing
def attack(char, value):
    char.attack(value)
def item(char, item):
    char.item(item)
def dodge(char):
    char.dodge()


dialogWrite("Once upon a time there's a brave hero who wants to protect humankind")
player.name = input("\nEnter your name : ")
dialogWrite("\nDad, can i become a hero so that i can protect you, mom, and the entire people?")
dialogWrite("\nofcourse son. when you grow up to become an adult, you will be the bravest, strongest, and the best hero of all time.")

dialogWrite("\n\n20 years later...")
dialogWrite(f"\n{player.name}: Man this dungeon is big, i feel like even if i explore this place for 1000 years it still not close to finish.")
dialogWrite(f"\n{player.name}: huh... was that just in my head or i see a monster.")
dialogWrite(f"\n{player.name}: hmmm. must've been the wind.")
dialogWrite(f"\n{player.name}: well i guess it's time to rest and continue the exploration tomorrow.")
dialogWrite(f"\n\nOne day later...")



# Item objects
vita_item = vita()
infinity_edge = infinityEdge()
zhonyas_hourglass = zhonyasHourglass()
banshees_veil = bansheesVeil()
rabadons_deathcap = rabadonsDeathcap()
warmogs_armor = warmogsArmor()
malefic_gun = maleficGun()
sea_halberd = seaHalberd()
hunter_strike = hunterStrike()
blade_of_despair = bladeOfDespair()
endless_battle = endlessBattle()

# Equipment objects
rage_anklet = rageAnklet()
nimble_hammer = nimbleHammer()
watchful_eyes = watchfulEyes()
sparkling_soda = sparklingSoda()
emblem_of_the_greatest = emblemOfTheGreatest()

item_objects = [
    vita_item,
    infinity_edge,
    zhonyas_hourglass,
    banshees_veil,
    rabadons_deathcap,
    warmogs_armor,
    malefic_gun,
    sea_halberd,
    hunter_strike,
    blade_of_despair,
    endless_battle
]

equipment_objects = [
    rage_anklet,
    nimble_hammer,
    watchful_eyes,
    sparkling_soda,
    emblem_of_the_greatest
]

turn = 10
day = 1
itemInventory = []
equipmentInventory = []



# main loop
while player.hp >= 1:
    dialogWrite(f"\nDay {day}", 0.1)

    while turn < 11:
        # player input
        print("\nChoose Activity")
        print(f"Turn: {turn}/10")
        print("1. Train")
        print("2. Explore")
        print("3. Check Inventory")
        inputTurn = input("\n")

        if inputTurn == "1" or inputTurn.lower() == "train":
            print("\nChoose what to train")
            print("1. Attack")
            print("2. Defense")
            print("3. Agility")
            print("4. Luck")
            print("5. Go back")
            inputTrain = input("\n")

            if inputTrain == "5":
                continue

            # validate player input
            if inputTrain not in ["1", "2", "3", "4"]:
                print("Invalid training option.")
                continue

            # train RNG
            if not rngRoll(random.randint(30,50)):
                print("Training failed.")
                turn += 1
                continue

            apply_training_stat(player, inputTrain)
            turn += 1
            

        # handle explore
        elif inputTurn == "2" or inputTurn.lower() == "explore":
            dialogWrite("\nExploring...", 0.5)
            all_arrays = [item_objects, equipment_objects]
            randomObject = random.randint(0,1)
            # check if player get item or equipment
            if randomObject == 0:
                itemInventory.append(random.choice(item_objects))
            else:
                equipmentInventory.append(random.choice(equipment_objects))
            
            dialogWrite("\nyou just got something")
            turn += 1
        
        # handle check inventory
        elif inputTurn == "3" or inputTurn.lower() == "Check Inventory":
            print("item list:")
            for item in itemInventory:
                print(f"{item.name}")

            print("\nequipment list:")

            for equipment in equipmentInventory:
                print(f"{equipment.name}: ", end="")
                equipment.description(player.name)
        


        else:
            print("Invalid activity option.")


    # battle system
    dialogWrite(f"\nYou found and enemy, you must defeat it\n")

    while enemy.hp > 0 and player.hp > 0:
        player_turn(player, enemy)
        
        if enemy.hp <= 0:
            print(f"\n{enemy.name} has been defeated!")
            break
        
        boss_turn(enemy, player)
        
        if player.hp <= 0:
            print(f"\nYou have been defeated by {enemy.name}!")
            break

    # Reset boss for next day if player won
    if enemy.hp <= 0:
        enemy.hp *= 1.5
        turn = 0
    else:
        # Player died, game over
        break

    day += 1

