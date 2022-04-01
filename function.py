# Import the random library to use for the dice later
import random


def use_loot(health_points, belt):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Mysterious Potion"]
    item_num = 0

    # Lab 6: Validate Arguments

    if len(belt) <= 0 or len(belt) > 5:
        print("Loot bag is empty")
    elif health_points <= 0 or health_points > 20:
        print("Must be alive")
    else:
        for item in belt:
            print("     |   Enter " + str(item_num + 1) + " for " + belt[item_num], end=" ")
            item_num += 1
        print()
        print("     |", end="   ")
        choose_item = input("Choose wisely young adventurer, you don't want to die in on first fight!")
        while not choose_item.isnumeric():
            print("     |", end="   ")
            choose_item = input("Madness! This is not time to play around!! Choose a valid item... NOW!")
        loot_item = belt.pop(int(choose_item) - 1)

        loot_item = belt.pop(0)

        if loot_item in good_loot_options:
            health_points = min(20, (health_points + 2))
            print("     |    You used " + loot_item + ". Your health is now: " + str(health_points))
        elif loot_item in bad_loot_options:
            health_points = max(0, health_points - 2)
            print("     |    You used " + loot_item + ". Your health is now: " + str(health_points))
        else:
            print("     |    You used " + loot_item + ". Your health remains the same")
        return health_points, belt


def collect_loot(loot_options, belt):
    # Lab 6: (1) -- Validate
    if hasattr(belt, '__len__') is False or len(belt) > 5:
        print("Belt is full")
    elif hasattr(loot_options, '__len__') is False or len(loot_options) == 0:
        print("Hmmm... Must have been a trick of the eyes.... This bag is empty!")
    else:
        loot_roll = random.choice(range(1, len(loot_options) + 1))
        loot = loot_options.pop(loot_roll - 1)
        belt.append(loot)
        print("            Loot Item: " + loot)
        return loot_options, belt


def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                  @@   @@ 
                                  @    @  
                                  @   @   
                 @@@@@@          @@  @   
              @@       @@        @ @@     
             @%         @     @@@ @       
              @        @@     @@@@@     
                 @@@@@        @@       
                 @    @@@@                
            @@@ @@                        
         @@     @                         
     @@*       @                          
     @        @@                          
             @@                                                    
           @   @@@@@@@                    
          @            @                  
        @              @                  
    """
    # print("     |    Your sword (" + str(combat_strength) + ") ---> Monster (" + str(m_combat_strength) + ")")
    # Lab 6: (2) Validate
    if m_health_points == 0:
        print("As the monster approaches you, he comes to a sudden halt, screams in agony and drops to the ground. "
              "\nYou approach the body and (since you have a background in medicine), take his pulse."
              "\nYou pronounce him dead. \nThe cause: heart failure....\nMoving on....")
    elif combat_strength == 0:
        print("As you approach the monster, you come to a sudden halt, scream in agony, drop to the ground and black "
              "\nout. After a few moments, you come to. You open your eyes, look around and realize you are "
              "\nbeing swaddled in a blanket. You try to escape from its tight grip but moments later someone"
              "\ncomes towards you and lifts you up in their arms. You try to say something.... anything"
              "\nbut the only words that seem to come out of your mouth are.... mama\n\nThat was weird....")
    else:
        input("Your time to strike (Press Enter)")
        print(ascii_image)
        print("    |", end="    ")
        if combat_strength >= m_health_points:
            m_health_points = 0
            print("    |", end="    ")
            input("Nice one! You've killed the monster (Press Enter)")
        else:
            m_health_points -= combat_strength
            # print("     |    You've reduced the monster's health to: " + str(m_combat_strength))
        return m_health_points


def monster_attack(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    if m_combat_strength == 0:
        print("This monster looks weak.... We will leave him be until he gains his strength back")
    elif health_points == 0:
        print("You seem pretty weak, your adventurer... Are you on the verge of death?")
    else:
        print(ascii_image2)

        print("     |    Monster's Claw (" + str(m_combat_strength) + ") ---> Hero (You) (" + str(health_points) + ")")
        if m_combat_strength >= health_points:
            health_points = 0
            print("     |    You have been killed")
        else:
            health_points -= m_combat_strength
            print("     |    Your health is reduced to: " + str(health_points))
        return health_points


# Lab 5: Recursion
def inception_dream(num_dream_levels):
    # Base Case
    num_dream_levels = int(num_dream_levels)
    if num_dream_levels == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    # Recursive Case
    else:
        # inception_dream(5)
        # 1 + inception_dream(4)
        # 1 + 1 + inception_dream(3)
        # 1 + 1 + 1 + inception_dream(2)
        # 1 + 1 + 1 + 1 + 2
        return 1 + inception_dream(num_dream_levels - 1)


def final_score(health_points, num_stars):

    if health_points == 0:
        print("We thank the Mighty Mithras for looking over the young adventurer, whose name was never "
              "\nknown, while he lived. May his adventurous spirit live on forever. \n")
    elif num_stars == 0:
        print("0 stars....")
    else:
        print("     |", end="   ")
        hero_name = input("Enter your Hero's name (in two words)").upper().split()
        short_name = hero_name[0][slice(2)] + "." + hero_name[1][1]
        stars = "*" * num_stars
        print("     |   The Mighty Mithras has looked upon you favourably!"
              "\n     |   You, young adventurer, also known as " +
              short_name + " have earned <" + stars + "> stars!\n     |   Praise be to the Mighty Mithras")


# Lab 6: Test Function
def test_use_loot():
    input("Press enter to test USE_LOOT")
    # Arguments: belt, health_points
    print("Test 1:")
    # Test belt
    use_loot(15, [])
    print("Test 1:")
    # Test health points
    use_loot(-2, ["Leather Boots"])


# Lab 6: (1) Test Collect Loot
def test_collect_loot():
    input("Press enter to test COLLECT_LOOT")
    # Test Case 1:
    print("Test 1: ")
    collect_loot(2, [])
    # Test Case 2:
    print("Test 2: ")
    collect_loot([], 3)


# Lab 6: (2) Test Hero Attack
def test_hero_attack():
    input("Press enter to test HERO_ATTACK")
    # Test Case 1:
    print("Test 1:")
    hero_attacks(5, 0)
    # Test Case 2:
    print("Test 2:")
    hero_attacks(0, 4)


# Lab 6: (3) Test Monster Attack
def test_monster_attack():
    input("Press enter to test MONSTER_ATTACK")
    # Test Case 1:
    print("Test 1:")
    monster_attack(5, 0)
    # Test Case 2:
    print("Test 2:")
    monster_attack(0, 4)


# Lab 6: (4) Test Final Score
def test_final_score():
    input("Press enter to test FINAL_SCORE")
    # Test Case 1:
    print("Test 1:")
    final_score(2, 0)
    # Test Case 2:
    print("Test 2:")
    final_score(0, 2)
