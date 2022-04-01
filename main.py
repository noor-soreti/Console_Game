# Import function
import random

from function import *

# Lab 6: Call Test Functions
print("    ------------------------------------------------------------------")
test_use_loot()
print("    ------------------------------------------------------------------")

# Lab 6 (1) Test Collect Loot
print("    ------------------------------------------------------------------")
test_collect_loot()
print("    ------------------------------------------------------------------")

# Lab 6: (2) Test Hero Attack
print("    ------------------------------------------------------------------")
test_hero_attack()
print("    ------------------------------------------------------------------")

# Lab 6: (2) Test Monster Attack
print("    ------------------------------------------------------------------")
test_monster_attack()
print("    ------------------------------------------------------------------")

# Lab 6: (2) Test Final Score
print("    ------------------------------------------------------------------")
test_final_score()
print("    ------------------------------------------------------------------")


# Game Flow
num_stars = 0
num_lives = 10
m_num_lives = 12
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define Loot
loot_options = ["Health Potion", "Mysterious Potion", "Secret Note", "Leather Boots", "Flimsy Boots"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define Monster's Features
# Lab 5: Answer 1.a
monster_features = {
    "Spikes": 1,
    "Big_Tail": 3,
    "Sharp_Teeth": 5
}

# Define loop
i = 0
valid_input = False

# Lab 6 - Save game
save_file = open("save.txt", "r+")
if save_file.readline():
    print("Loading your saved game...")
    combat_strength = int(save_file.readline())
    print("combat_strength: " + str(combat_strength))
    health_points = int(save_file.readline())
    print(save_file.readline())
# Lab 6: Loop for player's combat strength + health points
else:
    print("    ----------------------------Game Setup----------------------------")
    while not valid_input and i in range(5):
        print("     |", end="   ")
        combat_strength = input("Enter your combat Strength (1-6): ")
        if not combat_strength.isnumeric():
            print("     |   One or more invalid inputs. Please enter an integer")
            i += 1
        elif int(combat_strength) not in small_dice_options:
            print("     |   You input was out of range. Please enter an integer between 1 and 6...")
            i = i + 1
        else:
            valid_input = True
    if valid_input:
        combat_strength = int(combat_strength)
        # Roll for Player health points
        print("     |", end="   ")
        input("Roll the dice for your health points (Press Enter)")
        health_points = random.choice(big_dice_options)
        print("     |   You rolled: " + str(health_points) + " health points")

        # Weapon for Player
        print("     |", end="   ")
        input("Time to choose a weapon, young adventurer. Roll the dice (Press Enter)")
        weapon_roll = random.choice(small_dice_options)
        combat_strength = min(6, (combat_strength + weapon_roll))
        print("     |   You've rolled a " + str(weapon_roll) + ".... That means you get a " + weapons[
            weapon_roll - 1] + " as a weapon")

        if weapon_roll <= 2:
            print("     |   --- You've rolled a weak weapon, lad")
        elif 2 < weapon_roll <= 4:
            print("     |   --- Your weapon is decent, lad")
        else:
            print("     |   --- Nice weapon, lad")

        if weapon_roll != 1:
            input("     |   --- Thank Mithras you didn't roll the Fist")

save_file.close()

# Monster health roll
print("     |", end="   ")
input("Roll for Monster health points (PRESS ENTER)")
m_health_points = random.choice(big_dice_options)
print("     |   You rolled: " + str(m_health_points) + " for monster's health points")

# Monster strength roll
print("     |", end="   ")
input("Now for the Monster's combat strength (PRESS ENTER)")
m_combat_strength = random.choice(big_dice_options)
print("     |   You rolled a " + str(m_combat_strength))

# Lab 4: Roll for the Monster's Power
print("     |", end="   ")
input("Time to roll for the monster's weapon (PRESS ENTER)")
power_roll = random.choice(list(monster_powers.keys()))

# Lab 5: Answer 1.a/b
print("     |", end="   ")
input("Time to get the Monster's features (PRESS ENTER)")
feature_roll = random.choice(list(monster_features.keys()))

# Lab 4: Increase the Monster's Strength by its Power
m_combat_strength = min(6, m_combat_strength + monster_powers[power_roll])
print("     |   The monster's combat strength is now " + str(
    m_combat_strength) + " using the " + power_roll + " magic power")

m_health_points = min(20, m_health_points + monster_features[feature_roll])
print("     |", end="   ")
input("The monster's health points is now " + str(m_health_points))

# Call Collect Loot Function
print("         ╔═.✵.═════════════════════════════════════════════════════════════════════════════════╗")
print("            As you're walking down an enchanted path, you see a young maiden drop her bag.\n"
      "            You retrieve it for her but when you look around, she is nowhere to be seen!")
print("      ", end="      ")
input("Oh well. You inspect the item and realize.... (PRESS ENTER) ")

print("      ", end="      ")
input("It's a loot bag! Lucky you, young adventurer. You look inside to find 2 items: (PRESS ENTER) ")
print("      ", end="      ")
input("Roll for the first item (Press Enter)")
loot_options, belt = collect_loot(loot_options, belt)
print("      ", end="      ")
input("Roll for the second item (Press Enter)")
loot_options, belt = collect_loot(loot_options, belt)

# Organize Belt
belt.sort()
print("            Your belt: ", belt)
print("      ", end="      ")
input("Interesting items... I wonder what use the young maiden had for these? (PRESS ENTER)")
print("         ╚══════════════════════════════════════════════════════════════════════════════════.✵.═╝")

# Use Loot
print("     |    You continue down the enchanted path and spot something in the distance.... It's a "
      "MONSTER!\n     |    Quickly, choose a loot item from your belt")
health_points, belt = use_loot(health_points, belt)

# Roll Analysis
print("     |", end="   ")
input("Analyze the roll (Press Enter)")
print("     |   --- You are matched in strength: ", (combat_strength == m_combat_strength))

print("     |   --- You have a strong player: ", (combat_strength + health_points >= 8))

if health_points >= 5:
    print("     |   --- Your health is okay")
else:
    print("     |   --- Your health is low at: " + str(health_points) + " and you have no healing potions")

# Lab 5: Recursive Function
print("    ------------------------------------------------------------------")
print("     |", end="   ")
num_dream_levels = input("How many dream levels do you want to go down?")
# VALIDATION
while not num_dream_levels.isnumeric():
    print("     |", end="   ")
    num_dream_levels = input("Please enter a numeric value")
num_dream_levels = int(num_dream_levels)

print("""
    ┊┊┊┊         
    ┊┊┊✧    𝕐𝕠𝕦 𝕒𝕣𝕖 𝕟𝕠𝕨 𝕖𝕟𝕥𝕖𝕣𝕚𝕟𝕘 𝕕𝕣𝕖𝕒𝕞𝕨𝕠𝕣𝕝𝕕......
    ┊┊✦ 
    ┊✧                      
    ✦ .                         ...𝕕𝕠𝕟'𝕥 𝕘𝕖𝕥 𝕝𝕠𝕊𝕥  𝕪𝕠 𝕦 𝕟 𝕘
     .                                                   ᵃ𝕕 ₑₙ ₜ  ʳᵘᵣ  ₑ ᵣ
    ·                                                   
                                                               
    """)

if num_dream_levels != 0:
    health_points -= 5
    crazy_level = inception_dream(num_dream_levels)
    combat_strength += int(crazy_level)
    print("     |   Your combat strength is now " + str(combat_strength))
    print("     |   Your health is now " + str(health_points))
print("    ------------------------------------------------------------------")

# Fight Sequence
print("     |", end="   ")
input("Time to fight! Roll the dice to see who goes first (PRESS ENTER)")

attack_roll = random.choice(small_dice_options)

if not (attack_roll % 2 == 0):
    # Hero Attacks First
    m_health_points = hero_attacks(combat_strength, m_health_points)
    if m_health_points == 0:
        num_stars = 3
    else:
        print("    |", end="    ")
        input("The monster strikes (Press enter)!!!")
        # Monster Attacks Back
        health_points = monster_attack(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
        else:
            num_stars = 2
            # Lab 5 - Answer 2b: If you have more items on your belt, use them
            if belt:
                belt, health_points = use_loot(belt, health_points)

else:
    print("------------------------------------------------------------------")
    print("    |", end="    ")
    # Monster Attacks First
    input("The Monster strikes (Press enter)")
    health_points = monster_attack(m_combat_strength, health_points)
    if health_points == 0:
        num_stars = 1
    else:
        print("    |", end="    ")
        input("The hero strikes!! (Press enter)")
        # Hero Attacks Back
        m_health_points = hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
        else:
            num_stars = 2

        # Lab 5 - Answer 2b: If you have more items on your belt, use them
        if belt:
            belt, health_points = use_loot(belt, health_points)

final_score(health_points, num_stars)

if num_stars == 3:
    print("Saving Game....")
    # First clear old saved game
    open("save.txt", "w").close()
    save_file = open("save.txt", "w")
    save_file.write("Most Recent Save\n")
    save_file.write(str(combat_strength + "\n"))
    save_file.write(str(health_points) + "\n")
    # Lab 6: (5)
    save_file.write("Hero has killed a monster")
    # Close file
    save_file.close()






























