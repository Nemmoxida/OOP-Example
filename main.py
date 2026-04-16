from data import *
import time
import sys
import random

enemy = boss()
player = character()


# char stat ref
# class character(boss):
#     def __init__(self):
#         super().__init__()
#         self.name = "hero"
#         self.hp = 50
#         self.level = 1
#         self.atk = 10
#         self.int = 10
#         self.defense = 5

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
    normalized = chance / 50
    p = normalized ** k
    
    return 1 if random.random() <= p else 0





def player_turn(player_obj, enemy_obj):
    print(f"\n{player_obj.name}'s turn!")
    print(f"HP: {player_obj.hp}")
    print("1. Attack")
    print("2. Use Item")
    choice = input("\n")
    
    if choice == "1":
        # Attack with INT-based accuracy
        if rngRoll(player_obj.int):
            damage = player_obj.atk
            enemy_obj.hp -= damage
            print(f"You hit! Dealt {damage} damage to {enemy_obj.name}!")
            print(f"{enemy_obj.name} HP: {enemy_obj.hp}")
        else:
            dodge(enemy_obj)
    elif choice == "2":
        # Item, will print all the avalable item 
        pass

    else:
        print("Invalid choice")


def boss_turn(enemy_obj, player_obj):
    print(f"\n{enemy_obj.name}'s turn!")
    action = random.randint(0, 1)  # 0 = use item, 1 = attack
    
    if action == 1:  # Attack
        if rngRoll(10):
            damage = enemy_obj.atk
            player_obj.hp -= damage
            print(f"{enemy_obj.name} hit you! Took {damage} damage!")
            print(f"Your HP: {player_obj.hp}")
        else:
            print(f"{enemy_obj.name}'s attack missed!")
    else:  # Use item (recovery)
        enemy_obj.hp += 20
        print(f"{enemy_obj.name} used an item to recover 20 HP!")
        print(f"{enemy_obj.name} HP: {enemy_obj.hp}")


def apply_training_stat(player_obj, training_choice):
    if training_choice == "1":
        player_obj.atk += 10
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

# dialogWrite("Once upon a time there's a brave hero who wants to protect humankind")
# player.name = input("\nEnter your name : ")
# dialogWrite("\nDad, can i become a hero so that i can protect you, mom, and the entire people?")
# dialogWrite("\nofcourse son. when you grow up to become an adult, you will be the bravest, strongest, and the best hero of all time.")

# dialogWrite("\n\n20 years later...")
# dialogWrite(f"\n{player.name}: Man this dungeon is big, i feel like even if i explore this place for 1000 years it still not close to finish.")
# dialogWrite(f"\n{player.name}: huh... was that just in my head or i see a monster.")
# dialogWrite(f"\n{player.name}: hmmm. must've been the wind.")
# dialogWrite(f"\n{player.name}: well i guess it's time to rest and continue the exploration tomorrow.")
# dialogWrite(f"\n\nOne day later...")


turn = 0
day = 1

while player.hp >= 1:
    dialogWrite(f"\nDay {day}", 0.5)

    while turn < 11:
        print("\nChoose Activity")
        print(f"Energy: {player.energy}")
        print(f"Turn: {turn}/10")
        print("1. Train")
        print("2. Explore")
        print("3. Check Inventory")
        print("4. Check Stat")
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

            if inputTrain not in ["1", "2", "3", "4"]:
                print("Invalid training option.")
                continue

            if not rngRoll(player.energy - 50):
                print("Training failed.")
                turn += 1
                break

            apply_training_stat(player, inputTrain)
            turn += 1
            

        elif inputTurn == "2" or inputTurn.lower() == "explore":
            print("\nYou explored the area.")
            player.energy -= 10
            turn += 1

        else:
            print("Invalid activity option.")

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

