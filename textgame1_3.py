#!/usr/bin/env python3
#----------------------------------------------------------
#  This text adventure game will let people gleefully plan
#  the apocolypse because they are fed up with all of h
#  humanity. This is a fantasy I am sure no one has had
#  ever, so it should be a unique experience and not
#  be a form of wish fulfillment in a fanciful setting.
#
# Lara Landis
# 7/24/2022
# Personal Python Project
#---------------------------------------------------------


import sys
import math
import os
import random
import pickle


# We're going to need to set up some global parse items

# This is where we define the various commands the game allows.
#  Get allows you to pick up something, place allows you to
# put something on something, close closes a door or lid, open does the
# reverse. Search allows you to look for something. Attack may or
# may not be implement, as with equip.

verbs = ['get', 'place', 'open', 'close', 'put', 'search', 'attack', 'move',
         'equip', 'read', 'look', 'save', 'load']
prepositions =['in', 'on', 'under', 'above', 'to', 'beneath']
directions = ['east', 'north', 'south', 'east', 'northeast', 'northwest', 'southwest', 'southeast',
            'e', 'n', 's', 'w', 'E', 'N', 'S', 'W', 'NE', "SE", 'SE', 'Sw',
            'ne', 'nw', 'se', 'sw']
objects = ['journal, knife, gun, sword', 'toilet', 'rat', 'dog', 'jacket', 'leather']


room = 1
#----------------------------------------------------------------------------
#
# We're going to start by defining 3 different classes.  Weapon, vehicle,
# player.
#
# Weapon will have methods that determine attack damage.
# Armor will just have characteristics that resist damage.
# Player will define characteristics unique to the player.
#
#----------------------------------------------------------------------------


class Weapon:

    def __init__ (self, type = None, damage = 0, elemental_type = None, elemental_percentage = 0):
        self.type = type
        self.damage = damage
        self.elemental_type = elemental_type
        self.elemental_percentage = elemental_percentage


    def swing (self):
        # We're going to de
        elemental_damage = int(self.damage * (1+self.elemental_percentage))
        if self.elemental_type == 'fire':

            return random.randint(0, elemental_damage)


        if self.elemental_type == 'water':
            return random.randint(0, elemental_damage)


        if self.elemental_type == 'air':
            return random.randint(0, elemental_damage)


        if self.elemental_type == 'earth':
            return random.randint(0, elemental_damage)

        if self.elemental_type == None:
            return random.randint(0, self.damage)


#---------------------------------------------------------------------------------

class Armor:

     def __init__ (self, type = None, value = 0, resistance = 0):
         self.type = None
         self.value = 0
         self.resistance = 0


class player:

     def __init__(self):
         self.hitpoints = 10
         self.speed = 1
         self.defense = 3
         self.equip = None
         self.worn = None
         self.damage = 3
         self.ratbeaten = False
         self.puzzle_solved = False
         self.dog_beaten = False
         self.rabid_beaten = False
         self.room = 1



player_One = player()
player_Armor =  Armor()
player_Weapon =  Weapon()


def display_news ():
    print ('')
    print ('Genetic Engineer blamed for crop failure.')
    print ('')
    print ('Frank Azaria, local gentic engineer, faces accusations')
    print ('that he caused the local plant failures, and manyu residents')
    print ('demand that he face criminal charges.')
    print ('')
    print ('Azaria, who did not work on the local crops that failed, told')
    print ('the Alisdale Journal that due to public perception no genetically')
    print ('modified crops were used in the area, and climate science models')
    print ('predicted such crop failures unless a way could be found to end')
    print ('the multi-year drought.')
    print ('')
    print ('Climate change skeptics believed that natural cycles caused the ')
    print ('prolong drought that grips the region.  Scientific models predicted')
    print ('human activity would cause the situation to get worse if corporations')
    print ('did not act to correct the damage they had caused...')
    print ('')
    print ('The article continues, but your eyes begin to glaze over. The ')
    print ('towns few remaining residents switched over to the genetically')
    print ('plants months ago, when they could find them.')
    return


#--------------------------------------------------------------------------
#
# This is a function that might be called often enough to have its down
# separate function.
#
#--------------------------------------------------------------------------
def end_screen ():
    print ('You shuffle off your mortal coil.  Weeks later, the')
    print ('the city is overrun by crazed invidiauls attacking the')
    print ('few remaining people not affected by the virus.')
    print ('')
    print ('Game Over.')
    exit()

#--------------------------------------------------------------------------
#
# This is the first puzzle in the game and it is arelatively simple
# statistics problem. I could have chose something more difficult, but it
# seemed better not to.
#
#---------------------------------------------------------------------------
def solve_puzzle ():

    global player_one
    choice = 0

    print ('As you move to open the chest, oen chest automatically opens')
    print (' to show that it is empty. After it opens, you hear the ')
    print ('disembodied voice of your father. One of these three chests')
    print ('contains something useful to you. Before I opened one, you had')
    print (' a 33 percent chance of picking the right one.  Now, you know')
    print (' that you have two boxes left. Would switching the initial box')
    print ('improve the odds. My daughter should already know the answer.')
    print ('')
    print ('The voice finally says, \'What is your answer?\' Should you switch boxes? (Y/N)')

    while (choice != 'Y') or (choice != 'N'):
        choice = input()
        choice = choice.upper()
        if (choice == 'N'):
            print ('A shot rings out through the chamber. You feel the bullet')
            print ('enter your chest.')
            print ('')
            end_screen ()
        elif (choice == 'Y'):
            print ('')
            print ('All but one of the chests disappears, and the remaining one')
            print ('opens. YOu find a sword that seems to have a button attached.')
            print ('When you press the button flames shoot out of the sword.')
            print ('')
            print ('You equip the flaming shiskebab sword.')
            print ('')
            player_One.equip = 'sword'
            player_One.puzzle_solved = True
            break

    return
#------------------------------------------------------------------------------
#
# The ever popular, ever-exciting, and ever cliched-battle with the rat.
#
#------------------------------------------------------------------------------
def rat_battle (god_mode):
    rat_hp = 10
    rat_damage = random.randint(0,2)+1
    rat_armor = 1

    global knife
    global sword
    global player_One
    global player_Armor
    global player_Weapon

    # Note, much of this code is repetitive and should be broken
    # up into smaller functions to reduce the number of lines.

    # Also, why am I not creating a module where all the game's monsters
    # and rooms are defined as objects?

    player_damage = 0
    if god_mode == True:
        print ('The rat dies in the presence of an obvious god.')
        player_One.ratbeaten = True
        return
    else:
        while (rat_hp > 0) or (player_One.hitpoints > 0):
            input('Press Enter to continue.')

            print (f'Rat HP: {rat_hp}, Your HP: {player_One.hitpoints} ')
            hit_chance = random.randint(0,100)
            initiative = random.randint(0,2)
            if (initiative == 0):
                print ('You win initiative.')

                if hit_chance <= 75:

                    if player_One.equip == None:
                        player_damage = random.randint(0,4)+1
                        rat_hp -= player_damage
                    else:
                        player_damage = knife.swing()
                        print (f'You swing your {player_One.equip} at the rat for {player_damage}')
                        rat_hp -= player_damage
                        hit_chance = random.randint(0,60)
                        if (hit_chance <= 60):
                            rat_damage = random.randint(0,2)+1 - player_Armor.value
                            print (f'The rat hits you for {rat_damage} points')
                            player_One.hitpoints -= rat_damage
                        else:
                            print ('The rat misses you.')
                else:
                            print ('You miss the rat')

            # The Rat goes first
            else:
                    hit_chance = random.randint(0,100)

                    if (hit_chance <= 60):
                        print ('The rat wins initiative')
                        rat_damage = random.randint(0,2)+1 - player_Armor.value
                        print (f'The rat hits you for {rat_damage} points')
                        player_One.hitpoints -= rat_damage
                    else:
                        print ('The rat misses you.')

                    hit_chance = random.randint(0,100)
                    if (hit_chance <= 75):
                        if player_One.equip == None:
                            player_damage = random.randint(0,player_One.damage) + 1
                        else:
                            player_damage = random.randint(0,4)+1

                        print (f'You hit the rat with your {player_One.equip} for {player_damage}')
                        rat_hp -= player_damage
                    else:
                        print ('You miss the rat.')

            if (rat_hp <= 0):
                break
            if (player_One.hitpoints <= 0):
                break


        if player_One.hitpoints <= 0:
            end_screen()
        elif rat_hp  <= 0:
            print ('The rat no longer bars your way.')
            player_One.ratbeaten = True
            player_One.htipoints = 10
            return
#------------------------------------------------------------------------------
#
# To elp compartmnetalize this further, we're just going to get an armor values
#
#------------------------------------------------------------------------------
def determine_Amor_Value (fplayer_One):
    global player_Armor

    if player_One.worn == 'None':
        player_Armor.value = 1
    if fplayer_One.worn == 'cloth':
        player_Armor.value = 2
    if fplayer_One.worn == 'leather':
        player_Armor.value = 3
    if fplayer_One.worn == 'steel':
        player_Armor.value = 4
    if fplayer_One.worn == 'Kevlar':
        player_Armor.value = 5

#------------------------------------------------------------------------------
#
# The player got here by using the search here or search area command, whichever
# one I hard code into the game. This will give them a chance of finding a
# useful random item to help them finish the game.
#
#------------------------------------------------------------------------------
def search_area ():
    global player_One
    loot_chance = random.randint(0,10)


    if (loot_chance <= 8):
        print ('You rummage around the area and find nothing.')
        return

    if (loot_chance >= 9):
        if (player_One.worn != 'steel') and (player_One.equip != 'gun'):
            found = random.randint(0,1)
            print (f'Found: {found}')
            if (found == 0) and (player_One.equip != "gun") or (found == 1) and (player_One.worn != 'steel'):
                if found == 0:
                    print ('You find a Glock 9mm.')
                    print ('You equip the gun.')
                    player_One.equip = 'gun'
                    return

                if found == 1:
                    print ('You find a steel chestplate.')
                    print ('You equip the steel chestplate)')
                    player_One.worn = 'steel'
                    return

#------------------------------------------------------------------------------
#
# This is the final sreen of the game. I'm still not sure I want  to keep
# it purely text based.
#
#-----------------------------------------------------------------------------
def game_beaten ():

    pass

#------------------------------------------------------------------------------
#
# This is a simple function that will handle all the battles in this game_
# after the initial encounter with the rat. We're going to use the concept
# of objects to make this far easier.
#
#-------------------------------------------------------------------------------
def handle_battle (monster_type, sg_godmode):

    class Monster:
        def __init__ (self, damage = 3, hitpoints = 10, armor = 2, resistance = None):
            self.damage = damage
            self.hitpoints = hitpoints
            self.armor = armor
            self.resistance = resistance

    #Monster Objects
    dog = Monster(3, 10, 2, 'water')
    rabid = Monster(6, 12, 3, 'earth')
    rat = Monster (2,10,1, None)
    father = Monster(10,16,4, 'fire')

    #Weapon Objects
    knife = Weapon('slashing', 5, None, 0)
    sword = Weapon('slashing', 8, 'fire', .25)
    gun   = Weapon ('piercing', 12, 'water', .25)

    global player_One

    player_One.hitpoints = 10
    damage = 0
    monster_damage = 0
    player_damage = 0

    # Determine monste rdamage and Armor

    if monster_type == 'dog':
        monster_hitpoints = dog.hitpoints
        monster_Armor  = dog.armor


    elif monster_type == 'rabid':
        monster_hitpoints = rabid.hitpoints
        monster_Armor = rabid.armor


    elif monster_type == 'rat':
        monster_hitpoints = rat.hitpoints
        monster_Armor = rat.armor


    elif monster_type == 'father':
        monster_hitpoints = father.hitpoints
        monster_Armor = rat.armor

    player_armor = 0
    player_armor = determine_Amor_Value (player_One)
    if (sg_godmode == True):
        print (f'The {monster_type} dies in the presence of an obvious god.')
        if (monster_type == 'dog'):
            player_One.dog_beaten = True
        if (monster_type == 'rabid'):
            player_One.rabid_beaten = True
        return


    while (player_One.hitpoints > 0) or (monster_hitpoints > 0):
        initiative = random.randint(0,1) + 1
        player_hit_chance = random.randint(0,100)
        monster_hit_chance = random.randint(0,100)

        print (f'Monster hitpoints: {monster_hitpoints}, Player hitpoints: {player_One.hitpoints}')
        input ()
        if (initiative == 1):
            print ('You win initiative.')

            if (player_hit_chance <= 85):
                if player_One.equip == None:
                    player_damage = random.randint(0,2)+1 - monster_Armor
                if player_One.equip == 'knife':
                    player_damage = knife.swing() - monster_Armor
                if player_One.equip == 'sword':
                    player_damage = sword.swing() - monster_Armor
                if player_One.equip == 'gun':
                    player_damage = gun.swing() - monster_Armor

                if (player_damage > 0):
                    print (f'You hit the {monster_type} for {player_damage} with your {player_One.equip}')
                    monster_hitpoints -= player_damage
                else:
                    print (f'Your {player_One.equip} glances off the {monster_type}')
            else:
                print (f'You miss the {monster_type}')

            if (monster_hit_chance <= 65):
                if monster_type == 'dog':
                    monster_damage = random.randint(0, dog.damage) + 1 - player_Armor.value

                if (monster_damage > 0):
                    print (f'The {monster_type} hits you for {monster_damage}')
                    player_One.hitpoints -= monster_damage
                else:
                    print (f'The {monster_type}\'s attack glances off your {player_One.worn} armor.')
            else:
                print (f'The {monster_type} misses you.')

        elif (initiative == 2):
            print (f'The {monster_type} wins initiative')

            if (monster_hit_chance <= 65):
                if monster_type == 'dog':
                    monster_damage = random.randint(0, dog.damage) + 1 - player_Armor.value

                if (monster_damage > 0):
                    print (f'The {monster_type} hits you for {monster_damage}')
                    player_One.hitpoints -= monster_damage
                else:
                    print (f'The {monster_type}\'s attack glances off your {player_One.worn} armor.')
            else:
                print (f'The {monster_type} misses you.')


            if (player_hit_chance <= 85):
                if player_One.equip == None:
                    player_damage = random.randint(0,2)+1 - monster_Armor
                if player_One.equip == 'knife':
                    player_damage = knife.swing() - monster_Armor
                if player_One.equip == 'sword':
                    player_damage = sword.swing() - monster_Armor
                if player_One.equip == 'gun':
                    player_damage = gun.swing() - monster_Armor
                if (player_damage > 0):
                    print (f'You hit the {monster_type} for {player_damage} with your {player_One.equip}')
                    monster_hitpoints -= player_damage
                else:
                    print (f'Your {player_One.equip} glances off the {monster_type}')
            else:
                print (f'You miss the {monster_type:}')

        if player_One.hitpoints < 1:
            break
        if monster_hitpoints < 1:
            break

        if (monster_type == 'father') and (monster_hitpoint < 1):
            end_screen()
        if (player_One.hitpoints < 1):
            end_screen()

    if (monster_hitpoints < 1) and (monster_type == 'dog'):
        player_One.dog_beaten = True
    if (monster_hitpoints <1) and (monster_type == 'rabid'):
        player_One.rabid_beaten == True

#------------------------------------------------------------------------------
#
# This is where we will save the game's current state and this will allow the
# player to pick up where they left off.
#
#-----------------------------------------------------------------------------
def save():
    global player_One
    global player_Armor
    global player_Weapon
    global verbs


    print ('')
    print ('Enter the filename: ', end = ' ')
    f = input()

    if os.path.exists(f):
        print('File exists. Do you wish to overwrite (Y/N): ', end = '')
        overwrite = input()
        print (overwrite.upper())
        if overwrite.upper() != 'Y':
            return


    try:
        with open(f, "wb") as save_file:
            pickle.dump(player_One, save_file)
            pickle.dump(player_Armor, save_file)
            pickle.dump(player_Armor, save_file)


    except Exception as e:
        print (e)
        print('Gavme could not be saved.')


    return

#------------------------------------------------------------------------------
#
# This function will load the game from a previous save state, and move the
# player to the room where they last saved. it will also check load the
# values of the player's armor and weapon.
#
#-----------------------------------------------------------------------------
def load():

    global player_One
    global player_Armor
    global player_Weapon
    global room

    print ('What saved game file would you like to load?', end = '')
    f = input ()

    if os.path.exists(f):
        try:
            with open(f, 'rb') as load_file:
               player_One = pickle.load(load_file)
               player_Armor = pickle.load(load_file)
               player_Weapon = pickle.load(load_file)

        except Exception as e:
                print (e)


    else:
        print ('File does not exist.')

    room = player_One.room
    return
#-----------------------------------------------------------------------------s
# This function will display the father's journal, which will explain the
# basic premise of the game. It will also give some basic commands, if I
# remember to put them in.
#-----------------------------------------------------------------------------
def display_journal ():
    print ('------------------------------------------------------------------')
    print (' Diary of Josiah Franklin, Genetic Engineer')
    print ('------------------------------------------------------------------')
    print ('')
    print ('We spent years perfecting those crops to be resistant to ')
    print ('drought and disease. We increased the food  yield and tried ')
    print ('to make sure they tasted good. You would think with the looming')
    print ('enviornmental crisis, people would at least show some respect')
    print ('for hardworking engineers and scientists.')
    print ('')
    print ('It has been several months since they called us all in ')
    print ('to testify before the council to address some concerns')
    print ('they had about genetically modified organisms.')
    print ('')
    delay_key = input('Press enter to continue')
    print ('And I still can''t believe that they were worried that')
    print ('these organisms might affect the spirtiual health of anyone')
    print ('who consumed them, because they were not natural and therefore')
    print ('not made by God or something like that. I wasn\'t paying attention.')
    print ('')
    dleay_key = input('Press enter to contine')
    print ('I  had enough. I wasn\'t going to stand around waiting for the')
    print ('inquisition. The world is on the brink of destruction because')
    print ('of the abuses of corporations and politicians, and instead of ')
    print ('working together to fix the problem, they want to scapegoat')
    print ('the scientists and engineers')
    print ('')
    delay_key = input('Press enter to continue')
    print ('I''m not going to sit around waiting for their inquisition')
    print ('so I can be burned at the stake like some Mideival heretic')
    print ('If they want to make me a villain, I\'m  going to make sure')
    print ('that I am.')
    print ('')
    delay_key = input('Press enter to continue')
    print ('I am nearly finished perfecting a new version of the rabies')
    print ('virus with a much faster spawning time. If the clueless ')
    print ('politicians want to live in a post-apocalyptic landscape')
    print ('ruled by ignorance and fear. I will give it to them.')
    print ('')
    print ('------------------------------------------------------------------')

    return


#-----------------------------------------------------------------------------
#
# For this function, we are displaying the player's personal journal, where
# she explains how she feels about her father and how she knows that she must
# stop him in some way.  I really need to put some kind of puzzle in this
# game, but I can't figure out what it should be yet.
#
#-----------------------------------------------------------------------------
def display_personal_journal ():


    j = 0
    print ('------------------------------------------------------------------')
    print (' My Perosnal Journal -- Top Secret Clearance Required             ')
    print ('------------------------------------------------------------------')
    print ('')
    print (' FML. My dad like takes himself way too seriously.  Somoene said ')
    print ('you mad, bro to him yesterday, and he let out some kind of evil laugh')
    print ('and said that\'s what they\'ll call me.')
    print ('')
    j = input ("Press any key to continue...")
    print ('So the other day at school, I was forced to read this totally boring')
    print ('website for biology. I think it was about how to like change plants')
    print ('around or something, and the word jeans might have been involved.')
    print ('I don\'t remember exactly. It was something that sounded like jeans')
    print ('anyway. I don\'t think the site said jack about clothing.')
    print ('')
    j = input('Press enter to continue...')
    print ('But right there, like in the middle of the page, was my dad\'s name')
    print ('The website said he like saved lives by making sure farmers')
    print ('made more crops or something.')
    print ('')
    j = input ('Press enter to continue')
    print ("Then all other peeps in the class started dissing me 'cuz my dad\'s")
    print ('an egghead, and a I nearly died of embarrassment.  But some of them')
    print ('said my dad would like destroy the world or something and they')
    print ('said they\'d meet me outside near the flagpole after school or something.')
    print ('Like I donn\'t remember what they said, \'cuz I didn\'t go where')
    print ('they wanted me to.')
    print ('')
    j = input('Press enter to continue')
    print ('Anwyay, I go home and I see my dad fiddling around with something in his')
    print ('lab, which he put in the shed for some reason. Even weirder, it\'s like')
    print ('in our front yard, but he tells me not to come in or I might die.')
    print ('He often says stuff like this, but I went in anyway, and he got really')
    print ('angry before injecting me with something, pushing me out, and storming')
    print ('out.')
    print('--------------------------------------------------------------------')
    print ('')
    j = input('Press Enter to return to game')

    print ('As you put the journal back down, you realize that this entry was')
    print ('written several days ago and you have not seen your father since.')


    return
#-----------------------------------------------------------------------------
#
# This function will simply print out a visiaul display of each rooom.
#
#------------------------------------------------------------------------------
def display_room (gd_room, gd_inGame, sg_godmode):

    global player_One
    # Your father's lab
    player_One.room = gd_room
    print (gd_room)
    if gd_room == 1:
        print ('1. This is your father\'s genetics engineering lab. In the ')
        print ('corner of the room there is a living pet dinosaur that he')
        print ('made you. You also find an open diary on his desk.')
        print ('')
        print ('You see your father''s journal on the table.')
        print ('')
        print ('There is an exit to the south')
        return
    # A hallway

    if gd_room == 2:
        print ('2. This is a hallway in your father\'s single story')
        print ('dewlling. A dim light shows an exit to to the living')
        print ('room, and exit to your father\'s bedroom to the north,')
        print ('another exit to your room to the south, and the living')
        print ('room to the east')
        print ('')
        return

    # The living room

    if gd_room == 3:
        print ('3. This is a fairly standard living room. There is a chair')
        print ('along the southern wall, a television mounted on the northern')
        print ('wall, and a sofa beneath a window on the western wall, and a')
        print ('bathroom to the east')

        # Does the player have armor equipped? If not, show this line.
        if player_One.worn == None:
            print ('')
            print ('You see a suit of  cloth from your father\'s days')
            print ('in the Society for Creative Anarchism.')
        else:
            pass

        print ('')
        print ('There are exits to the west, east and to the North.')
        return


    # The player's bedroom
    if gd_room == 4:
        print ('4. This is your bedroom. The wall is decorated with a few')
        print ('posters of you favorite band. There is a desk with a computer')
        print ('on the wall opposite your bed. There are a few clothes on the floor')
        print ('and the room is in a state of disarray that only the most diligent')
        print ('teenagers can achieve by neglecting to clean their room on a regular')
        print ('basis.')
        print ('')


        if player_One.equip == None:
            print ('Your journal is open on your bed, and you think you left your pocket knife in')
            print ('a pile of clothes')
        else:
            print ('Yoour journal is open on your bed:')

        print ('There is an exit to the north .')
        return

    if gd_room == 5:    #The Bathroom
        print('This is the bathroom. There is a medicine cabinet, a sink, a toilet, and an')
        print('old style  tub that is great for taking a bubble bath in, despite your father\'s')
        print ('repeated insistences that you do not. It looks like there is something behind')
        print ('the toilet.')
        print ('')
        print ('The is an exit to the west')
        return

    if gd_room == 6:   # Dining Room
        print ('This ias the dining room. The table is cluttered with dishes, and it looks like')
        print ('there are the remains of some hastily eaten meal here. Although the kitchen sink')
        print ('is empty. You do not have time to tidy up the remains of your father\'s dinner.')
        print ('')
        print ('There are exits to the North and South')
        return

    # The Kitchen in the Father's Home
    if gd_room == 7:
        print ('This is the kitchen. There are dishes in te sink, empty jars left on the counter')
        print ('and a few papers scattered on the counters that have little to do with food     ')
        print ('preparation. The pages contain many scribbles and crossed out diagrams written  ')
        print ('and drawn by your father.')
        print ('')
        print ('There is a closed door to the north and an exit to the south.')
        if player_One.ratbeaten == False:
            print ('You see a large rat blocking the exit.  It will need to be removed. It does not')
            print ('look friendly. It looks like its gene code has been altered in some way.')
        else:
            print ('There is nothing blocking your way to the north and an exit to the south.')

        return

    # Backyard -- Center
    if gd_room == 8:
        print ('This is your backyard. You spent many hours playing here. The wind howls off in')
        print ('the distance. The once green grass has become dry  through the prolonged drought.')
        print ('A disused mower sits on the porch along with a long-abandonned barbecue grill.')
        print ('')
        print ('There are exits to the east and west and a shed to the north. There is a closed kitchen door to the south')
        return

    # Backyard -- east
    if gd_room == 9:
        print ('This is the eastern edge of the backyard. As with the rest of the backyard, there is dry')
        print ('grass ans cracked, brown soil covering the yard. You take a moment to reflect on the')
        print ('situation as you pause in the wind. If  your father hadn\'t engineered crops that could')
        print ('withstand the drought, thousands of people in the region would be suffering from starvation.')
        print ('')
        print ('There is an exit to the west')
        return

    # Backyard -- west
    if gd_room == 10:
        print ('This is the western edge of your backyard. The grass is brown and the dirt is cracked')
        print ('and dusty. You can see an alley heading off to the sthreet. Your father\'s car is')
        print ('missing from its usual spot in the driveway.')
        print ('')
        print ('There are obvious exits to the east and north.')
        return

    #Backyard -- Shed
    if gd_room == 11:
        print ('This is the standard gardening shed. The older tools are rusty and once saw')
        print ('heavy use. The few newer tools that exist maintain a shiny direct from the')
        print ('hardware store look.')


        if player_One.puzzle_solved == False:
            print ('')
            print ('You see three chests here.')


        print ('')
        print ('There is an exit to the south.')
        return


    if gd_room == 12:
        print ('This is an alleayway meandering through the the town. The')
        print ('shoulder of the road gives way to dry, cracked soil. There is')
        print ('little of interest here')
        print ('')
        print ('There are exits to the north and south.')
        return

    if gd_room == 13:
        print ('The alley gives way to a strett here. The city council did')
        print ('its best to keep the major thoroughfares green, and you see')
        print ('a strain of grass your father developed early clinging on to')
        print ('life, but it looks lke the continued drought and rising')
        print ('temperatures have been too much for it.')
        print ('')
        print ('There are obvious exits to the west and to the south.')
        return

    if gd_room == 14:
        print ('The alley gives way to a strett here. The city council did')
        print ('its best to keep the major thoroughfares green, and you see')
        print ('a strain of grass your father developed early clinging on to')
        print ('life, but it looks lke the continued drought and rising')
        print ('temperatures have been too much for it.' )
        print ('')
        if player_One.dog_beaten == False:
            print ('A snarling dog leaps towards you and attacks.')
            print ('')
            monster_type = 'dog'
            print('')
            handle_battle(monster_type, sg_godmode)
        print ('The are obvious exists to the east, west and to the south.')
        return


    if gd_room == 15:
        print ('This is a neighbor\'s tiny house. The one room dwelling has')
        print ('everything a person needs to live. The various appliances')
        print ('might have been helpful to the corpse you see before you')
        print ('at one point. You guess, from your father\'s lessons in')
        print ('anatomy, she has been dead for at least a week.')
        print ('')
        print ('After going outside to throw up, you return to the area.')
        print ('')
        print ('The is an obvious exit to the North.')
        return


    if gd_room == 16:
        print ('This is the main street in the city. A few green plants')
        print ('created by your father hang on despite the dray, parached')
        print ('earth. The rest of the plants are dead and decaying.')
        print ('The road contains a few sets of human footprints that seem')
        print ('to be made by someone with no clear intention of where they')
        print ('intended to go.')
        print ('')
        print ('You see exits to the North, South, West, and East.')
        return


    if gd_room == 17:
        print ('This is an abonadonned motorcycle workshop. At least you')
        print ('think it is abandonned.  Various tools and motorcycle parts')
        print ('are strewn across the floor as if someone had ransacked the')
        print ('place looking for something in a hurry.')
        print ('')
        if (player_One.worn == None) or (player_One.worn == 'cloth'):
            print ('There is a biker jacket on the floor here.')
            print ('')

        print ('There is an obvious exit to the south')
        return


    if gd_room == 18:
        print ('This is an abandoned convenience store. It has been ')
        print ('closed for as long as your family has lived in this town.')
        print ('The original owners took whatever useful goods it once held')
        print ('long ago.')
        print ('')
        print ('There is an obxious exit to the north.')
        return


    if gd_room == 19:
        print ('The alley gives way to a strett here. The city council did')
        print ('its best to keep the major thoroughfares green, and you see')
        print ('a strain of grass your father developed early clinging on to')
        print ('life, but it looks lke the continued drought and rising')
        print ('temperatures have been too much for it.' )
        print ('')
        print ('There are obvious exits to the south, west and east.')
        return


    if gd_room == 20:
        print ('This is the hobby shop where you spent many hours looking')
        print ('for supplies for your own projects. Your father also spent')
        print ('many hours here trying to make sure you had STEM toys so you')
        print ('could develop whatever skills you had. Although you had no')
        print ('interest in becoming a genetic engineer, yoiu did discover a')
        print ('a passion for programming and computer science that the store')
        print ('could not adequately server.  You see recent foam periodically')
        print ('dotting the floor and a set of footprints that head in a')
        print ('northeasterly direction.')
        print ('')
        print ('There is an obvious exit to the north.')
        return


    if gd_room == 21:
        print ('The alley gives way to a strett here. The city council did')
        print ('its best to keep the major thoroughfares green, and you see')
        print ('a strain of grass your father developed early clinging on to')
        print ('life, but it looks lke the continued drought and rising')
        print ('temperatures have been too much for it. It looks like the')
        print ('proprietor has left some newspaper clippings on the counter.')
        print ('')
        print ('There are obvious exits to the northwest, southwest, east and south.')
        return


    if gd_room == 22:
        print ('This dwelling is now abandonned. Whoever lives here put decided')
        print ('to frame something that looks like a letter on one of the walls.')
        print ('As you begin to read it, you realize that this is a plan to form')
        print ('a group of citizens to collect your father and put him on trial')
        print ('for his crimes. It seems that the members of this group')
        print ('decided on  your father\'s sentence long before they ever got')
        print ('to hold their trial.')
        print ('')
        print ('There is an obvious exit to the north.')
        return


    if gd_room == 23:
        print ('This is a side street that leads to a dead end. The trail you')
        print ('saw at the convience store continues to amble from the wast.')
        print ('You hear some growling sounds coming from the Northwest.')
        print ('')
        print ('You see obvious exits heading to the west and southeast.')
        return


    if gd_room == 24:
        print ('This is your father\'s work lab.It is surprisingly empty')
        print ('and looks like it has been recently cleaned and vacated.')
        print ('You go over to his desk and look through his drawers to see')
        print ('if he left some notes. Even those are gone. Unlike many of')
        print ('the other buildings in town, this one looks like its been')
        print ('used recently.')
        print ('')
        print ('You see a trapdoor here.')
        print ('There is an obvious exit leading to the northeeast.')
        return


    # Hehe, we finally spring the rabid human on the player.
    # Good thing they've been vaccinated/
    if gd_room == 25:
        print ("This is -- or rather was a -- a dead end street. It is")
        print ('slowly being reclaimed by the scrublands, desert, or whatever')
        print ('the climate of this area has become.')
        print ('')
        if player_One.rabid_beaten == False:
            print ('There is a lone figure standing here.  You glance at the')
            print ('footprints quickly and realize that the person is foaming')
            print ('at the mouth. You realize your father was sucessful in')
            print ('altering the virus. You also realize that you are about')
            print ('to be attacked as you ready your sword.')
            handle_battle ('rabid', sg_godmode)

        print ('The is an obvious exit to the southeast.')
        return

    if (gd_room >= 26) and (gd_room % 3 == 0):
         print ('This is a once sterile hallway leading through the underground')
         print ('labs where your father worked. The flourescent lights remain on')
         print ('but they still flicker overhead.')
         print ('')
         if (gd_room == 48):
             print ('There are obvious exits to the north, south, and east')
             return
         if (gd_room == 27):
             print ('There are obvious exits to the north, south, and wast')
             return
         if (gd_room > 27) or (gd_room < 48):
            if (gd_room < 27) or (gd_room < 48):
                print ('There are obvious exits to the north, south, east, west')
                return

    if (gd_room >= 26) and (gd_room <= 48) and (gd_room % 3 == 2):
        print ('This appears to be a lab that someone kept meticulously')
        print ('clean at one point. It has since fallen into disuse')
        print ('and the shelves have gotten dusty.')
        print ('')
        if (gd_room == 26):
            print ('There is a trapdoor above you.')
            print ('')
        print ('There is an obvious exit to the south.')
        return

    if (gd_room >= 26) and (gd_room < 49) and (gd_room % 3 == 1):
        print ('These labs are similar to the ones to the north, but they')
        print ('show signs of recent use.  Someone has made an attempt to')
        print ('maintain and repair the equipment even when supplies are short')
        print ('There is a whiteboard with what appear to be indecipherable')
        print ('chemical problems on the board.')
        print ('')
        print ('There is an obvious exit to the North.')
        return

    if (gd_room == 49):
            print ('This room seems to have seen recent use. There is a suit')
            print ('of kevlar body armor lying on one of the tables.  You can')
            print ('hear something that sounds like your father mumbling to')
            print ('himself off to the west.')
            print ('')
            print ('There are obvious exists to the north and west.')
            return



    if gd_room == 50:
        print ('')
        print ('The doors swing open briefly and shut behind you. ')
        print ('')
        print ('Your father stands before you. He looks ill, and you')
        print ('think you see some foam at the mouth, but you cannot be')
        print ('sure.')
        print ('')
        print ('He shoots something at you, and you feel a dart pierce')
        print ('your skin.')
        print ('')
        input()
        print ('I am sorry, daughter. The vaccine needs more than one dose.')
        print ("This is the 3rd one, you will need at least ten more and")
        print ("I have prepared it for you.")
        print ("")
        print ("It is too late for ...")
        input()
        print ('Your father snarls and attacks')
        handle_battle('father', sg_godmode)


    return

#----------------------------------------------------------------------------------
#
# Ths function will check to see if the user's commands work with the game's own
# syntax which I know is a context-ftree grammar. The nice thing about context-
# free grammars it that thewhat is the m&m shell made of?what is the m&m shell made of?y are easy to implement.
#
#----------------------------------------------------------------------------------
def check_syntax (fcommand_list):
    # Let the game know it's using global variablesif (len(fcommand_list) >1) and (fcommand_list[command] == 'equip') and not(fcommand_list[command+1] in objects)

    global verbs
    global directions
    global prepositions
    global objects

    command = 0
    try:

        if (len(fommand_list) > 2) and not (fcommand_list[command+1] in prepositions) and not(fcommand_list[command+2] in objects):
            print (f'The word commands must take the form of verbs: ')
            return False
        if (len(fcommand_list) > 2) and not ((fcommand_list[command+1] in objects) or (fcommand_list[command+1] in prepositions)):
            print (f'Command syntax is verbs: {versbs} or directions {directions} or verb object: {objects} or verb, preposition: {prepositions}, object')
            return False
        if (len(fcommand_list) == 1) and not (fcommand_list[command] in verbs) or not (fcommand_list[command] in directions):
            print (f'Commands must start with a verb:  {verbs} or with a direction: {directions}')
            return False

    except:
        return True
#----------------------------------------------------------------------------------
# This command just parses general_commands that are not tied to any room, suchf
# as save, load, quit, or exit.
#----------------------------------------------------------------------------------
def parse_general(fcommand_list):


    z = 0
    try:
        if len(fcommand_list) > 1:
            return


        if (fcommand_list[0] == 'quit') or (fcommand_list[0] == 'exit'):
            try:
                print ('I hope you remembered to save.')
                exit ()


            except IOError:
                print ('This is an I/O Error that you likely should not be getting.')
                exit()


            finally:
                exit ()


        if (fcommand_list[0] == 'load'):
            load()
            return


        if (fcommand_list[0] == 'save'):
            save()
            return

        return

    except:
        return

    return

#----------------------------------------------------------------------------------
#
# This is the study in your father's house. There is an exit to the  south and a
# journal on  his desk.
#
#----------------------------------------------------------------------------------
def parse_room1 (fcommand_list):

    global room
    global player_one
    z = 0
    room = 1
    player_One.room = room




    # the player forgot to tell the game what to read
    if (fcommand_list[z] == 'read') and (fcommand_list[z+1] == 'journal'):
        display_journal();

    if (fcommand_list[z] == 'read' ) and (fcommand_list[z+1] != 'journal'):
        print ('Read what?')


    if (fcommand_list[z] == 's') or (fcommand_list[z] == 'S') or (fcommand_list[z]== 'south') :
            room =  2



    return
#-----------------------------------------------------------------------------
#
# Room 2 is a hallway in you father's house. It has exits to the west,
# an exit to the north to  your father's lab, and aanohter exit to the south
# to  your bedroom. The bedrrom is room 4, the hallway is to room 3.
#
#-------------------------------------------------------------------------------
def parse_room2 (fcommand_list):
    global room
    global player_One
    player_One.room = room
    z = 0


    try:

        # So, what happens if the player forgets to add the wright word?
        if  (cfommand_list[z] == 'equip') and (fcommand_list[z+1] != 'sword' or \
            fcommand_list[z+1] != 'knife' or \
            fcommand_list[z+1]  != 'gun'):
            print ('Equip what?')


        # the player forgot to tell the game what to read
        if (fcommand_list[z] == 'read') and (fcommand_list[z+1] == 'journal'):
            display_journal();
        if  (fcommand_list[z] == 'read' ) and (fcommand_list[z+1] != 'journal'):
            print ('Read what?')

        if (fcommand_list[z] == 's') or (fcommand_list[z] == 'S') \
                or (fcommand_list[z]== 'south'):
                room =  1
        if (fcommand_list[z] == 'e') or (fcommand_list[z] == 'E') or (fcommand_list[z] == 'east'):
                room = 3
        if  (fcommand_list[z] == 's') or (command_list[z] == 'S') or (fcommand_list[z] == 'south') :
                room = 4


        # Now call the code/functions for when the player gets them
        # parse commands correctfa
        if (fcommand_list[z] == 'equip') and (fcommand_list[z+1] == 'sword') or (fcommand_list[z+1] == 'knife') or (fcommand_list[z+1] == 'gun'):
            print ('')


        if (fcommand_list[z] == 'equip'):
                print ('Equip what?')



        if (fcommand_list[z] == 'n') or (fcommand_list[z] == 'N') or (fcommand_list[z] == 'north') :
                room = 1
        if (fcommand_list[z]) == 'e' or (fcommand_list[z] == 'E') or (fcommand_list[z] == 'east'):
                room = 3
        if  (fcommand_list[z] == 's') or (fcommand_list[z] == 'S') or (fcommand_list[z]== 'south'):
                room = 4

    except:
        # For now, we are assuming there is only one item.
        # We will add code to ensure this is the case later.
        try:

            if (fcommand_list[z] == 'equip'):
                print ('Equip what?')

            if (fcommand_list[z] == 'n') or (fcommand_list[z] == 'N') or (fcommand_list[z] == 'north') :
                room = 1
            if (fcommand_list[z] == 'e') or (fcommand_list[z] == 'E') or (fcommand_list == 'east'):
                room = 3
            if  (fcommand_list[z] == 's') or (fcommand_list[z] == 'S') or (fcommand_list == 'south'):
                room = 4

        except:
            print ('You can\'t do that here.')


    return


#-----------------------------------------------------------------------------
#  This is where we parse the commands for room 3.  Room 3 will have  some
# simple armor in it, but not much else.
# Exits to this room are east and north.   East goes to a hallway
# north goes to a kitchen.
#-----------------------------------------------------------------------------
def parse_room3 (fcommand_list):

    global player_One
    global room
    global player_Armor
    player_One.room = room
    command = 0


    if (len(fcommand_list) == 3):
        if (fcommand_list[command] == 'equip') and (fcommand_list[command+1] == 'cloth') or (fcommand_list[command+1] == 'armor'):
            print ('You put the cloth suit on.')
            player_One.worn == 'cloth'
            player_Armor.value += 1
    if (len(fcommand_list) == 2):
        if (fcommand_list[command] == 'equip') and (fcommand_list[command+1] == 'cloth'):
            print ('You put the cloth suit on.')
            player_One.worn = 'cloth'
    if (len(fcommand_list) == 1):
        if (fcommand_list[command] == 'w') or (fcommand_list[command] == 'W') or (fcommand_list[command] == 'west'):
            room = 2
        if (fcommand_list[command] == 'n') or (fcommand_list[command] == 'N') or (fcommand_list[command] == 'north'):
            room = 6
        if (fcommand_list[command] == 's') or (fcommand_list[command] == 'S') or (fcommand_list[command] == 'south'):
            print ('You cannot go that direction.')
        if (len(fcommand_list) == 1) and (fcommand_list[command] == 'e') or (fcommand_list[command] == 'E') or (fcommand_list[command] == 'east'):
            room = 5
    if (len(fcommand_list) > 1) and (fcommand_list[command] == 'read'):
        print ('There is nothing here to read.')
    if (len(fcommand_list) == 3) and (fcommand_list[command] == 'look') and (fcommand[command+1] in prepositions) and (fcommand_list[command+2] in objects):
        print ('There is nothing here of interest')


    return


#-----------------------------------------------------------------------------
# Room 4 is the bedroom. It will contain a knife and the player's personal
# journa l.  The intent is to explain a little more of the plot here.
#-----------------------------------------------------------------------------
def parse_room4 (fcommand_list):
    global room
    global player_One
    player_One.room = room
    command = 0

    # We will check to see if she has a weapon equipped first
    if player_One.equip == None:

            if (len(fcommand_list) == 2) and (fcommand_list[command] == "equip") and (fcommand_list[command+1] == "knife"):
                print ('You wield your trusty pocket knife.')
                player_One.equip = 'knife'
            if (len(fcommand_list) == 2) and (fcommand_list[command] == 'read') and (fcommand_list[command+1] == 'journal'):
                display_personal_journal ()
            if (len(fcommand_list) ==  2) and (fcommand_list[command] == 'read') and (fcommand_list[command+1] != 'journal'):
                print ('You can\'t read that.')
            if (len(fcommand_list) == 1) and (fcommand_list[command] ==  'N') or (fcommand_list[command] == 'n') or (fcommand_list[command] == 'north'):
                room = 2
            else:
                pass
    elif player_One.equip != None:
            if (len(fcommand_list) == 2) and (fcommand_list[command] == 'read') and (fcommand_list[command+1] == 'journal'):
                display_personal_journal ()
            if (len(fcommand_list) ==  2) and (fcommand_list[command] == 'read') and (fcommand_list[command+1] != 'journal'):
                print ('You can\'t read that.')
            if (len(fcommand_list) == 1) and (fcommand_list[command] ==  'N') or (fcommand_list[command] == 'n') or (fcommand_list[command] == 'north'):
                room = 2
    else:
                print ('You can\'t do that here.')


    return


#-----------------------------------------------------------------------------
# This is the barthoom.   It will not contain anything useful to the player
# And there will only be one exit. It is only their because houses nee
# bathrooms.
#----------------------------------------------------------------------------
def parse_room5 (fcommand_list):

    global room
    global player_one

    player_One.room = room



    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'under') and (fcommand_list[2] == 'toilet'):
            print ('If you really want to search behind the toilet I won\'t stop you, but I personally wouldn\'t.')
            print ('After carefully avoding some of the nastier things that dropped behind the the commode,')
            print ('you find a hastily scrawled note in your father\'s handwriting.')
            print ('')
            print ('It reads: ')
            print ('Daughter and I inocculated and should be safe even if we were bit. It took a series of shots')
            print ('and I hated convincing her that she injured herself in her sleep, but it was necessary to ')
            print ('keep my plans secret')
            room = 5
        else:
            print ('I didn\'t understand that.')
    elif (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'toilet'):
            print ('Ewww.')
        else:
            print ('You can\'t do that here.')
    else:  # This means it's either 4 or more words or one
        if (len(fcommand_list) >= 4):
            print ('The longest acceptable command is three words')
        else:
            if (len(fcommand_list) == 1) or (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
                room = 3
            else:
                print ('You can\'t do that here.')



#----------------------------------------------------------------------------
# This is the dining room area. It looks rather disheveled and there is
# little of interest here. There are exists to the north and south. North
# goes to the kitchen. South goes to the living room.
#----------------------------------------------------------------------------
def parse_room6 (fcommand_list):
    global player_One
    global player_Armor
    global player_Weapon

    global room

    player_One.room = room

    if (len(fcommand_list) >=1):
        if (fcommand_list[0] == 'N') or (fcommand_list[0] == 'n') or (fcommand_list[0] == 'north'):
            room = 7
            return
        if (fcommand_list[0] == 'S') or (fcommand_list[0] == 's') or (fcommand_list[0] == 'south'):
            room = 3
        else:
            print ('You can\'t do that here')
    return


#----------------------------------------------------------------------------
#
# This is the kitchen. This is where the player will encounter the first
# obstacle in their path and the first combat routine. There will also be
# an autosave point here.
#
#----------------------------------------------------------------------------
def parse_room7 (fcommand_list, godmode):
    global ratbeaten
    global player_One
    global player_Armor
    global player_Weapon
    global room

    player_One.room = room
    if (len(fcommand_list) >= 4):
        print ('Commands can be no more than three words.')
    elif (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 2):

        if (fcommand_list[0] == 'open') and (fcommand_list[1] == 'door'):
            if player_One.ratbeaten == False:
                print ('There is a rat blocking the door.')
            if player_One.ratbeaten == True:
                print ('You open the door.')
                room = 8


        if (fcommand_list[0] == 'attack') and (fcommand_list[1] == 'rat') and (player_One.ratbeaten == False):
            rat_battle (godmode)


    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 6
            return

    else:
        print ('You can\'t do that here')
    return


#----------------------------------------------------------------------------
#
# This is the mian chacater's backyard. It is green and dry due to an ongoing
# drought. There are a few flavor items here, but the important exits area
# the shed, and extended backyards to the east and west.
#
#----------------------------------------------------------------------------
def parse_room8 (fcommand_list):

    global player_One
    global room

    player_One.room = room
    player_One.hitpoints = 10


    if (len(fcommand_list) >= 4):
        print ('Commands can be no more than 3 words.')
    elif (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'open') and (fcommand_list[1] == 'door'):
            room = 7
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 9
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 10
        if (fcommand_list[0] == 'n') or fcommand_list[0] == 'N' or (fcommand_list[0] == 'north'):
            # Shed
            room = 11
    else:
        print ('You can\'t do that here.')

    return

#---------------------------------------------------------------------------
# This is where we will parse room 9. I do not know what will be in it.
#---------------------------------------------------------------------------
def parse_room9 (fcommand_list):

    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) >= 4):
        print ('Commands can be no more than 3 words.')
    elif (len(fcommand_list) == 3):
        print ('You can\'t do that here')
    elif (len(fcommand_list) == 2):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'w') or (fcommand_list[0] == 'west'):
            room = 8
    else:
        print ('You can\'t do that here.')

    return


#----------------------------------------------------------------------------
#
# This is where we will parse room 10. I do not know what will be in it.
#
#----------------------------------------------------------------------------
def parse_room10 (fcommand_list):
    global player_One
    global room

    player_One.room = room

    if (len(fcommand_list) >= 4):
        print('Commands can be no more than 3 words.')
        return
    elif (len(fcommand_list) == 3):
        print ('You can\'t do that here')
    elif (len(fcommand_list) == 2):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'e') or (fcommand_list[0] == 'e'):
            room = 8
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 12

    return
#---------------------------------------------------------------------------
#
# This is the shed with the simple logic puzzlie I have found.
#
#------------------------------------------------------------------------------
def parse_room11 (fcommand_list):

    global player_One
    global room

    player_One.room = room
    if (len(fcommand_list) >= 4):
        print ('Commands can be no more than 3 words.')
        return
    elif (len(fcommand_list) == 3):
        if player_One.puzzle_solved == False:
            if (fcommand_list[0] == 'open') and  (fcommand_list[1] == 'the') and (fcommand_list[2] == 'chest'):
                solve_puzzle()
        else:
            print ('You can\'t do that here.')
    elif (len(fcommand_list) == 2):
            if player_One.puzzle_solved == False:
                if (fcommand_list[0] == 'open') and (fcommand_list[1] == 'chest'):
                    solve_puzzle()
            else:
                print ('You can\'t do that here.')
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 8
    else:
        print ('You can\'t do that here.')


    return

#---------------------------------------------------------------------------
#
# This is an uninteresting alleyway with exits leading north and south.
#
#----------------------------------------------------------------------------
def parse_room12 (fcommand_list):

    global room
    global player_One

    player_One.room = room

    if (len(fcommand_list) >= 4):
        print ('Commands can be no more than 3 words.')
        return
    elif (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 2):
                print ('You can\'t do that here.')
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 10
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 13
    else:
        print ('You can\'t do that here.')

    return
#---------------------------------------------------------------------------
#
# This is a street way. There will be a rabid animal encounter here.
#
#-----------------------------------------------------------------------------
def parse_room13 (fcommand_list):

    global player_One
    global room
    player_One.room = room

    if (len(fcommand_list) >= 4):
        print ('Commands can be no more than 3 words.')
        return
    elif (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 2):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 12
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'w') or (fcommand_list[0] == 'w'):
            room = 14
    else:
        print ('You can\'t do that here.')

#----------------------------------------------------------------------------
#
#  Room 14
#
#-----------------------------------------------------------------------------
def parse_room14 (fcommand_list):

    global player_One
    global room
    player_One.room = room

    if (len(fcommand_list) >= 4):
        print ('Commands can be no more than 3 words.')
        return
    elif (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 2):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'w'):
            room = 16
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'e') or (fcommand_list[0] == 'e'):
            room = 13
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 15
    else:
        print ('You can\'t do that here.')


#----------------------------------------------------------------------------
#
# This is one of the manin chacacter's neibhbor's ouses. (Room 15.) there
# is an exit to the north leading to the street.   The player will find
# a dead body inside that has clearly been the victim of the plague.
#
#----------------------------------------------------------------------------
def parse_room15 (fcommand_list):
    global player_One
    global room
    player_One.room = room

    if (len(fcommand_list) >= 4):
        print ('Commands can be no more than 3 words.')
        return
    elif (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 2):
        print ('You can\'t do that here.')
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 14

    else:
        print ('You can\'t do that here.')

    pass

#------------------------------------------------------------------------------
#
#  This is part of the main street through the town.
#
#-----------------------------------------------------------------------------
def parse_room16 (fcommand_list):
        global player_One
        global room
        player_One.room = room

        if (len(fcommand_list) >= 4):
            print ('Commands can be no more than 3 words.')
            return
        elif (len(fcommand_list) == 3):
            print ('You can\'t do that here.')
        elif (len(fcommand_list) == 2):
            print ('You can\'t do that here.')
        elif (len(fcommand_list) == 1):
            if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
                room =  18
            if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
                room = 19
            if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
                room = 14
            if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
                room = 17
        else:
            print ('You can\'t do that here.')



#----------------------------------------------------------------------------
#
#  This is the abandonned motorcycle shop. There is a an exit to the southern
# and a leather jacket the player can find here.
#
#----------------------------------------------------------------------------
def parse_room17 (fcommand_list):

    global room
    global player_One
    global player_Armor

    player_One.room = room


    if (len(fcommand_list) >= 4):
        print ('Commands can be no longer than three words.')
    if (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'equip') and (fcommand_list[1] == 'armor') or (fcommand_list[1] == 'jacket'):
            print ('You equip the leather jacket.')
            player_One.worn = 'leather'
            player_Armor.value = 3
        else:
            print ('You can\'t do that here.')
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list == 'south'):
            room = 16

#---------------------------------------------------------------------------
#
# Room 18. This is an abondonned convenience store. The player will find few
# clues here about what happened.
#
#----------------------------------------------------------------------------
def parse_room18 (fcommand_list):

        global player_One
        global room
        player_One.room = room

        if (len(fcommand_list) >= 4):
            print ('Commands can be no more than 3 words.')
            return
        elif (len(fcommand_list) == 3):
            print ('You can\'t do that here.')
        elif (len(fcommand_list) == 2):
            print ('You can\'t do that here.')
        elif (len(fcommand_list) == 1):
            if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
                room = 16


#----------------------------------------------------------------------------
#
#  This is the abandonned motorcycle shop. There is a an exit to the southern
# and a leather jacket the player can find here.
#
#----------------------------------------------------------------------------
def parse_room19 (fcommand_list):

    global player_One
    global room
    player_One.room = room

    if (len(fcommand_list) >= 4):
        print ('Commands can be no longer than three words.')
    if (len(fcommand_list) == 3):
        print ('You ca(n\'t do that here.')
    if (len(fcommand_list) == 2):
        print ('You can\'t do that here.')
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 20
            return
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 16
            return
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 21
            return


#----------------------------------------------------------------------------
#
#  This is the abandonned motorcycle shop. There is a an exit to the southern
# and a leather jacket the player can find here.
#
#----------------------------------------------------------------------------
def parse_room20 (fcommand_list):

    global player_One
    global room
    player_One.room = room

    if (len(fcommand_list) >= 4):
        print ('Command can be no longer than three words.')
    if (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'read') and (fcommand_list[1] == 'clippings'):
            display_news()
        else:
            print ("You can\'t do that here.")
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 19





#---------------------------------------------------------------------------
#
# Room 21: Allway way through the street
#
#---------------------------------------------------------------------------
def parse_room21 (fcommand_list):

    global player_One
    global room
    player_One.room = room

    if (len(fcommand_list) >= 4):
        print ('Command can be no longer than three words.')
    if (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 19
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 22
        if (fcommand_list[0] == 'nw') or (fcommand_list[0] == 'NW') or (fcommand_list[0] == 'northwest'):
            room = 23
        if (fcommand_list[0] == 'sw') or (fcommand_list[0] == 'SW') or (fcommand_list[0] == 'southwest'):
            room = 24



#---------------------------------------------------------------------------
#
#  This is an abaondnned house that willl advence the background for the game_
# a little bit futher.  The player will found out what the citizens planned
# to do to her father and why he might have been driven to such extremes.
#
#---------------------------------------------------------------------------
def parse_room22 (fcommand_list):
    global player_One
    global room
    player_One.room = room

    if (len(fcommand_list) >= 4):
        print ('Command can be no longer than three words.')
    if (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'read') and (fcommand_list[1] == 'clippings'):
            display_news()
        else:
            print ("You can\'t do that here.")
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 21
            return

#---------------------------------------------------------------------------
#
# Room 23
#
#---------------------------------------------------------------------------
def parse_room23 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) >= 4):
        print ('Command can be no longer than three words.')
    if (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    if (len(fcommand_list) == 2):
        print ("You can\'t do that here.")
    elif (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'se') or (fcommand_list[0] == 'SE') or (fcommand_list[0] == 'southest'):
            room = 21
            return
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 25
            return


#---------------------------------------------------------------------------
#
# Room 24.This is the lab of the player's father. There is a trap trapdoor
# leading to his underground base of operations. it has been overrun
# by victims of the virus he has engineered.
#
#---------------------------------------------------------------------------
def parse_room24 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) >= 4):
        print ('Command can be no longer than three words.')
    if (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'open') and (fcommand_list[1] == 'door') or (fcommand_list[1] == 'trapdoor'):
            print ('You open the trap door and climb down. You make sure')
            print ('to close and lock the trap door behind you as you asend.')
            room = 26
            return

        else:
            print ("You can\'t do that here.")


    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'ne') or (fcommand_list[0] == 'NE') or (fcommand_list[0] == 'northeast'):
            room = 21
            return

#---------------------------------------------------------------------------
#
# Room 25
#
#----------------------------------------------------------------------------
def parse_room25 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) >= 4):
        print ('Commands can be no longer than three words.')
    if (len(fcommand_list) == 3) or (len(fcommand_list) == 2):
        print ('You can\'t do that here')
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'se') or (fcommand_list[0] == 'SE') or (fcommand_list[0] == 'southeast'):
            room = 21

#----------------------------------------------------------------------------
#
# Room 26
#
#-----------------------------------------------------------------------------
def parse_room26 (fcommand_list):
    global room
    global player_One
    player_One.room = room


    if (len(fcommand_list) > 3):
        print ("Commands can be no longer than 3 words.")
    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
        if (fcommand_list[0] == 'close') and (fcommand_list[1] == 'door') or (fcommand_list[1] == 'trapdor'):
            print ('The door will not budge')
        if (fcommand_list[0] ==  'open') and (fcommand_list[1] == 'door') or (fcommand_list[1] == 'trapdoor'):
            print ('The door will not budge')
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'south') or (fcommand_list[0] == 's') or (fcomand_list[0] == 'S'):
            room = 27

#----------------------------------------------------------------------------
#
# Room 27
#
#-----------------------------------------------------------------------------
def parse_room27 (fcommand_list):
    global room
    global player_One
    player_One.room = room


    if (len(fcommand_list) > 3):
        print ("Commands can be no longer than 3 words.")
    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list == 'north'):
            room = 26
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 30
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 28


#----------------------------------------------------------------------------
#
# Room 28
#
#-----------------------------------------------------------------------------
def parse_room28 (fcommand_list):
    global room
    global player_One
    player_One.room = room

    if (len(fcommand_list) > 3):
        print ("Commands can be no longer than 3 words.")
    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 27

#----------------------------------------------------------------------------
#
# Room 29
#
#-----------------------------------------------------------------------------
def parse_room29 (fcommand_list):
    global player_One
    global room
    player_One.room = room

    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 30


#----------------------------------------------------------------------------
#
# Room 30
#
#-----------------------------------------------------------------------------
def parse_room30 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) > 3):
        print ("Commands can be no longer than 3 words.")
    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 29
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 27
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 33
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 31


#----------------------------------------------------------------------------
#
# Room 31
#
#-----------------------------------------------------------------------------
def parse_room31 (fcommand_list):
    global room
    global player_One
    player_One.room = room

    if (len(fcommand_list) > 3):
        print ("Commands can be no longer than 3 words.")
    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 30



#----------------------------------------------------------------------------
#
# Room 32
#
#-----------------------------------------------------------------------------
def parse_room32 (fcommand_list):
    global player_One
    global room
    player_One.room = room

    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 33


#----------------------------------------------------------------------------
#
# Room 33
#
#-----------------------------------------------------------------------------
def parse_room33 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 32
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 30
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 36
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 34


#----------------------------------------------------------------------------
#
# Room 34
#
#-----------------------------------------------------------------------------
def parse_room34 (fcommand_list):
    global room
    global player_One
    player_One.room = room


    if (len(fcommand_list) > 3):
        print ("Commands can be no longer than 3 words.")
    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list == 'north'):
            room = 33



#----------------------------------------------------------------------------
#
# Room 35
#
#-----------------------------------------------------------------------------
def parse_room35 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list == 'south'):
            room = 36


#----------------------------------------------------------------------------
#
# Room 36
#
#-----------------------------------------------------------------------------
def parse_room36 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 35
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 33
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 39
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 37


#----------------------------------------------------------------------------
#
# Room 37
#
#-----------------------------------------------------------------------------
def parse_room37 (fcommand_list):
    global room
    global player_One
    player_One.room = room


    if (len(fcommand_list) > 3):
        print ("Commands can be no longer than 3 words.")
    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list == 'north'):
            room = 36



#----------------------------------------------------------------------------
#
# Room 38
#
#-----------------------------------------------------------------------------
def parse_room38 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list == 'south'):
            room = 39

#----------------------------------------------------------------------------
#
# Room 39
#
#-----------------------------------------------------------------------------
def parse_room39 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 38
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 36
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 42
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 40


#----------------------------------------------------------------------------
#
# Room 40
#
#-----------------------------------------------------------------------------
def parse_room40 (fcommand_list):
    global room
    global player_One

    if (len(fcommand_list) > 3):
        print ("Commands can be no longer than 3 words.")
    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list == 'north'):
            room = 39

#----------------------------------------------------------------------------
#
# Room 41
#
#-----------------------------------------------------------------------------
def parse_room41 (fcommand_list):
    global player_One
    global room

    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list == 'south'):
            room = 42


#----------------------------------------------------------------------------
#
# Room 42
#
#-----------------------------------------------------------------------------
def parse_room42 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 41
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 39
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 45
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 43


#----------------------------------------------------------------------------
#
# Room 43
#
#-----------------------------------------------------------------------------
def parse_room43 (fcommand_list):
            global room
            global player_One

            if (len(fcommand_list) > 3):
                print ("Commands can be no longer than 3 words.")
            if (len(fcommand_list) == 3):
                if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
                    search_area()
            if (len(fcommand_list) == 2):
                if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
                    search_area()
            if (len(fcommand_list) == 1):
                if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list == 'north'):
                    room = 42

#----------------------------------------------------------------------------
#
# Room 44
#
#-----------------------------------------------------------------------------
def parse_room44 (fcommand_list):
    global player_One
    global room

    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list == 'south'):
            room = 45


#----------------------------------------------------------------------------
#
# Room 45
#
#-----------------------------------------------------------------------------
def parse_room45 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 44
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 42
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'W') or (fcommand_list[0] == 'west'):
            room = 48
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 46


#----------------------------------------------------------------------------
#
# Room 46
#
#-----------------------------------------------------------------------------
def parse_room46 (fcommand_list):
    global room
    global player_One

    if (len(fcommand_list) > 3):
        print ("Commands can be no longer than 3 words.")
    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list == 'north'):
            room = 45


#----------------------------------------------------------------------------
#
# Room 47
#
#-----------------------------------------------------------------------------
def parse_room47 (fcommand_list):
    global player_One
    global room

    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list == 'south'):
            room = 48


#----------------------------------------------------------------------------
#
# Room 48
#
#-----------------------------------------------------------------------------
def parse_room48 (fcommand_list):
    global player_One
    global room
    player_One.room = room


    if (len(fcommand_list) == 3):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'the') and (fcommand_list[2] == 'area'):
            search_area()
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            search_area()
    if (len(fcommand_list) == 1):
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
            room = 47
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
            room = 45
        if (fcommand_list[0] == 's') or (fcommand_list[0] == 'S') or (fcommand_list[0] == 'south'):
            room = 49


#----------------------------------------------------------------------------
#
# Room 49
#
#-----------------------------------------------------------------------------
def parse_room49 (fcommand_list):
    global player_One
    global room
    global player_Armor
    player_One.room = room


    if (len(fcommand_list) == 3):
        print ('You can\'t do that here.')
    if (len(fcommand_list) == 2):
        if (fcommand_list[0] == 'equip') and (fcommand_list[1] == 'armor'):
            player_One.equip = 'Kevlar'
            player_Armor.value = 14
        if (fcommand_list[0] == 'equip') and (fcommand_list[1] == 'kevlar'):
            palyer_One.equip = "Kevlar"
        if (fcommand_list[0] == 'search') and (fcommand_list[1] == 'area'):
            print ("This area has been cleared of any random debris.")
    if (len(fcommand_list) == 1):
        # You can exit east,  and west here.
        if (fcommand_list[0] == 'w') or (fcommand_list[0] == 'w') or (fcommand_list[0] == 'w'):
            answer = ""
            print ('')
            print('------------------------------------------------------------------')
            print ('The door to the west will close and lock behind you and')
            print ('you will be unable to come back. Do you wish  to proceed (Y/N)?')
            print ('-----------------------------------------------------------------')
            answer = input()
            answer = answer.upper()
            if (answer == 'Y'):
                room = 50
        if (fcommand_list[0] == 'n') or (fcommand_list[0] == ' n') or (fcommand_list[0] == 'north'):
            room = 48


#----------------------------------------------------------------------------
#
# Room 50. The Final Room where the player encounters his father/
#
#-----------------------------------------------------------------------------
def parse_room50 (fcommand_list):
    global player_One
    global room
    palyer_One.room = room



#----------------------------------------------------------------------------
#  In rooms 26 through 48, the player has a chance to encounter a random
# creature.
#-----------------------------------------------------------------------------
def random_encounter(sg_godmode):


    monster_types = ['rat', 'dog', 'rabid']
    monster_type = random.choice(monster_types)
    print ('')
    print (f'A {monster_type} appears before you and attacks.')
    print ('')
    handle_battle(monster_type, sg_godmode)
    return


#----------------------------------------------------------------------------
#
# In this function, we contian the gme control loop that will load the first
# room and start the game. This will also contian the code that will handle
# the grammar of the various commands and then head on to whatever room
# the player wishes to go to.
#
#-----------------------------------------------------------------------------
def game_start (sg_godmode):

    # Okay, we're going to set this to True to start, eand
    # when the player enters the exit or quit commands,
    # it will e set to false.


    inGame = True
    global room
    global player_One
    global player_Armor
    global player_Weapon

    while inGame:
        player_One.room = room
        display_room (room, inGame, sg_godmode)

        print ("")
        print (">", end='')
        command = input ()


        try:
            command_list = command.split(' ')


        except:
            print('I hope you remembered to save.')
            exit()


        print ('Debugging', command_list)


        if (command_list[0] == 'quit') or (command_list[0] == 'exit'):
            print ('I hope you remembered to save')
            exit ()


        if (check_syntax (command_list) == True):
            parse_general(command_list)

            # We need to add some random encounters into the later bathrooms
            if (room > 25 and room < 49):
                encounter_chance = random.randint(0,100)
                if encounter_chance < 11:
                    random_encounter(sg_godmode)


            if room == 1:
                parse_room1 (command_list)
            elif room == 2:
                parse_room2 (command_list)
            elif room == 3:
                parse_room3 (command_list)
            elif room == 4:
                parse_room4 (command_list)
            elif room == 5:
                parse_room5 (command_list)
            elif room == 6:
                parse_room6 (command_list)
            elif room == 7:
                parse_room7 (command_list, sg_godmode)
            elif room == 8:
                parse_room8 (command_list)
            elif room == 9:
                parse_room9 (command_list)
            elif room == 10:
                parse_room10 (command_list)
            elif room == 11:
                parse_room11 (command_list)
            elif room == 12:
                parse_room12 (command_list)
            elif room == 13:
                parse_room13 (command_list)
            elif room == 14:
                parse_room14 (command_list)
            elif room == 15:
                parse_room15 (command_list)
            elif room == 16:
                parse_room16 (command_list)
            elif room == 17:
                parse_room17 (command_list)
            elif room == 18:
                parse_room18 (command_list)
            elif room == 19:
                parse_room19 (command_list)
            elif room == 20:
                parse_room20 (command_list)
            elif room == 21:
                parse_room21 (command_list)
            elif room == 22:
                parse_room22 (command_list)
            elif room == 23:
                parse_room23 (command_list)
            elif room == 24:
                parse_room24 (command_list)
            elif room == 25:
                parse_room25 (command_list)
            elif room == 26:
                parse_room26 (command_list)
            elif room == 27:
                parse_room27 (command_list)
            elif room == 28:
                parse_room28 (command_list)
            elif room == 29:
                parse_room29 (command_list)
            elif room == 30:
                parse_room30 (command_list)
            elif room == 31:
                parse_room31 (command_list)
            elif room == 32:
                parse_room32 (command_list)
            elif room == 33:
                parse_room33 (command_list)
            elif room == 34:
                parse_room34 (command_list)
            elif room == 35:
                parse_room35 (command_list)
            elif room == 36:
                parse_room36 (command_list)
            elif room == 37:
                parse_room37 (command_list)
            elif room == 38:
                parse_room38 (command_list)
            elif room == 39:
                parse_room39 (command_list)
            elif room == 40:
                parse_room40 (command_list)
            elif room == 41:
                parse_room41 (command_list)
            elif room == 42:
                parse_room42 (command_list)
            elif room == 43:
                parse_room43 (command_list)
            elif room == 44:
                parse_room44 (command_list)
            elif room == 45:
                parse_room45(command_list)
            elif room == 46:
                parse_room46 (command_list)
            elif room == 47:
                parse_room47 (command_list)
            elif room == 48:
                parse_room48 (command_list)
            elif room == 49:
                parse_room49 (command_list)
            elif room == 50:
                parse_room50 (command_list)
        else:
            print ('Syntax error')


        command_list = []
        command = ""

    return


#----------------------------------------------------------------------------
#
# Now that we've got the command line arguments, it's time to decide what
# if anything to do with them. This includes functions that allow users # TODO:
# enter a 'god mode' if they so wish.
#
#-----------------------------------------------------------------------------

def parse_args (fargs):
    godmode = False
    for item in fargs:


        if item == '-v' or item == '--version':
            print ("Version 1.3")
            exit()
        elif item == '-h' or item == '--help':
            print ('Fools! I will Destroy you All Help')
            print('------------------------------------')
            print ()
            print ('-v or --version: Version number')
            print ('h or --help: Prints this screen.')
            print ()
            print ('There may be some additional items')
            print ('not included here that will affect')
            print ('game play.')
            print('')
            print('This version includes some bug fixes')
            print('and better code organization.)')
            exit()


        # If the player has used this switch, they will not
        # take any damage, although they may be subject to
        # other hazards that occur as part of the game play,
        # such as traps with a falling compoenent.
        # If the argument is not present, the flag is setting
        # to fals eand play proceeds nromally.


        if item == '-g' or item ==  '--godmode':
            # Make the player immune to damage
            godmode = True
            # Okay, no args to parse so, go!
        else:
            godmode = False



    game_start(godmode)


    return
#===========================================================================
#
# THIS IS THE MAIN FUNCTION. THIS IS THE MAIN FUNCTION. MAIN FUNCTION
#
#================parody============================================================
def main ():
    args = sys.argv[1:]             # Get all command line arguments
    parse_args(args)


knife = Weapon('slashing', 3, None, 0)
sword = Weapon('slashing', 6, None, 'fire')
if __name__ == "__main__":
    player_One = player()
    player_Armor =  Armor()
    player_Weapon =  Weapon('blunt', 2, None, 0)
    main()
