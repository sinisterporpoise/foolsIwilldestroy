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
objects = ['journal, knife, gun, sword', 'toilet', 'rat']


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
        if self.elemental_type == 'fire':
            return random.randint(0,self.damage * (1 + self.elemental_percentage)) +1


        if self.elemental_type == 'water':
            return random.randint(0, self.damage * (1+ self.elemental_percentage)) + 1


        if self.elemental_type == 'air':
            return random.randint(0,selff.damage * (1+ self.lemantal_percentage)) +1


        if self.elemental_type == 'earth':
            return random.randint(0, self.damage * (1+ self.elemental_percentage)) +1

        if self.elemental_type == None:
            return random.randint(0, self.damage) + 1


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
         self.room = 1



player_One = player()
player_Armor =  Armor()
player_Weapon =  Weapon()



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
    print ('improve the god_modes. My daughter should already know the answer.')
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
            player_One.equip == 'sword'
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
            input()

            print (f'Rat HP: {rat_hp}, Your HP: {player_One.hitpoints} ')
            hit_chance = random.randint(0,100)
            initiative = random.randint(0,2)
            if (initiative == 0):
                print ('You win initiative.')

                if hit_chance <= 75:

                    if player_One.equip == None:
                        player_damage = random.randint(0,2)+1
                        rat_hp -= player_damage
                    else:
                        player_damage = knife.swing()
                        print (f'You swing your {player_One.equip} at the rat for {player_damage}')
                        rat_hp -= player_damage
                        hit_chance = random.randint(0,60)
                        if (hit_chance <= 60):
                            rat_damage = random.randint(0,2)+ - player_Armor.value
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
                            random.randint(0,player_One.damage) + 1
                        else:
                            player_damage = knife.swing()

                        print (f'You hit the rat with your {player_One.equip} for {player_damage}')
                        rat_hp -= player_damage
                    else:
                        print ('You miss the rat.')

            if player_One.hitpoints <= 0:
                end_screen()
            elif rat_hp  <= 0:
                print ('The rat no longer bars your way.')
                player_One.ratbeaten = True
                return

    return

#------------------------------------------------------------------------------
#
# This is a simple function that will handle all the battles in this game_
# after the initial encounter with the rat. We're going to use the concept
# of objects to make this far easier.
#
#-------------------------------------------------------------------------------
def handle_battle (monster_type):

    class Monster:
        def __init__ (self, damage = 3, hitpoints = 10, armor = 2, resistance = None):
            damage = damage
            hitpoints = hitpoints
            armor = armor
            resistance = resistance

        def atack(self):
            return (random.randint(0, self.damage))

    damage = 0
    monster_damage = 0

    dog = Monster(3, 10, 2, 'water')
    knife = Weapon('slashing', 3, None, 0)
    sword = Weapon('slashing', 6, None, 'fire')
    global player_One

    if monster_type == 'dog':
        monster_hitpoints = dog.hitpoints

    while (player_One.hitpoints >= 1) or (monster.hitpoints >= 1):
        initiative  = random.randint(0,2)
        print (f'Monster Hitpoints: {monster_hitpoints}, Player Hitpoints: {player_One.hitpoints}')

        if (initiative == 0):
            print ('You win the initiative')
            if player_One.equip == 'knife':
                player_damage = knife.swing()
            elif player_One.equipe == 'sword':
                player_damage = sword.swing()

            monster_damage = determine_damage (monster_type)
            monster_hitpoints -= player_damage
            player_hitpoints -= monster_damage
        else:
            print ('The rat wins initiative')






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
def display_room (gd_room, gd_inGame):

    global player_One
    # Your father's lab
    player_One.room = gd_room

    if gd_room == 1:
        print ('1. This is your father\'s genetics engineering lab. In the ')
        print ('corner of the room there is a living pet dinosaur that he')
        print ('made you. You also find an open diary on his desk.')
        print ('')
        print ('You see your father''s journal on the table.')
        print ('')
        print ('There is an exit to the south')

    # A hallway

    if gd_room == 2:
        print ('2. This is a hallway in your father\'s single story')
        print ('dewlling. A dim light shows an exit to to the living')
        print ('room, and exit to your father\'s bedroom to the north,')
        print ('another exit to your room to the south, and the living')
        print ('room to the east')
        print ('')

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


            print ('')
            print ('There are exits to the west, east and to the North.')


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


    if gd_room == 5:    #The Bathroom
        print('This is the bathroom. There is a medicine cabinet, a sink, a toilet, and an')
        print('old style  tub that is great for taking a bubble bath in, despite your father\'s')
        print ('repeated insistences that you do not. It looks like there is something behind')
        print ('the toilet.')
        print ('')
        print ('The is an exit to the west')

    if gd_room == 6:   # Dining Room
        print ('This ias the dining room. The table is cluttered with dishes, and it looks like')
        print ('there are the remains of some hastily eaten meal here. Although the kitchen sink')
        print ('is empty. You do not have time to tidy up the remains of your father\'s dinner.')
        print ('')
        print ('There are exits to the North and South')

    # The Kitchen in the Father's Home
    if gd_room == 7:
        print ('This is the kitchen. There are dishes in te sink, empty jars left on the counter')
        print ('and a few papers scattered on the counters that have little to do with food     ')
        print ('preparation. The pages contain many scribbles and crossed out diagrams written  ')
        print ('and drawn by your father.')
        print ('')
        print ('There is a closed door to the north and an exit to the south.')
        if player_One.ratbeaten == False:
            print ('You see a large rate blocking the exit.  It will need to be removed. It does not')
            print ('look friendly. It looks like its gene code has been altered in some way.')
        else:
            print ('There is nothing blocking your way to the north and an exit to the south.')

    # Backyard -- Center
    if gd_room == 8:
        print ('This is your backyard. You spent many hours playing here. The wind howls off in')
        print ('the distance. The once green grass has become dry  through the prolonged drought.')
        print ('A disused mower sits on the porch along with a long-abandonned barbecue grill.')
        print ('')
        print ('There are exits to the east and west and a shed to the north. There is a closed kitchin door to the south')


    # Backyard -- east
    if gd_room == 9:
        print ('This is the eastern edge of the backyard. As with the rest of the backyard, there is dry')
        print ('grass ans cracked, brown soil covering the yard. You take a moment to reflect on the')
        print ('situation as you pause in the wind. If  your father hadn\'t engineered crops that could')
        print ('withstand the drought, thousands of people in the region would be suffering from starvation.')
        print ('')
        print ('There is an exit to the west')

    # Backyard -- west
    if gd_room == 10:
        print ('This is the western edge of your backyard. The grass is brown and the dirt is cracked')
        print ('and dusty. You can see an alley heading off to the sthreet. Your father\'s car is')
        print ('missing from its usual spot in the driveway.')
        print ('')
        print ('There are obvious exits to the east and north.')

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

    if gd_room == 12:
        print ('This is an alleayway meandering through the the town. The')
        print ('shoulder of the road gives way to dry, cracked soil. There is')
        print ('little of interest here')
        print ('')
        print ('There are exits to the north and south.')
    if gd_room == 13:
        print ('The alley gives way to a strett here. The city council did')
        print ('its best to keep the major thoroughfares green, and you see')
        print ('a strain of grass your father developed early clinging on to')
        print ('life, but it looks lke the continued drought and rising')
        print ('temperatures have been too much for it.')
        print ('')
        print ('There are obvious exits to the west and to the south.')

    if gd_room == 14:
        print ('The alley gives way to a strett here. The city council did')
        print ('its best to keep the major thoroughfares green, and you see')
        print ('a strain of grass your father developed early clinging on to')
        print ('life, but it looks lke the continued drought and rising')
        print ('temperatures have been too much for it.' )
        print ('')
        if player_One.dob_beaten == False:
            print ('A snarling dog leaps towards you and attacks.')
            print ('')
            monster_type = 'dog'
            handle_battle(monster_type)
            print('')
        print ('The are obvious exists to the east and to the south.')
    if gd_room == 15:
        pass
    if gd_room == 16:
        pass
    if gd_room == 17:
        pass
    if gd_room == 18:
        pass
    if gd_room == 19:
        pass
    if gd_room == 20:
        pass
    if gd_room == 21:
        pass
    if gd_room == 22:
        pass
    if gd_room == 23:
        pass
    if gd_room == 24:
        pass
    if gd_room == 25:
        pass

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
# This command just parses general_commands that are not tied to any room, such
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
    player_One.room = room
    command = 0


    if (len(fcommand_list) == 2) and ((fcommand_list[command] == 'equip') and (fcommand_list[command+1] == 'cloth') or (fcommand_list[command+1] == 'armor')):
        print ('You put the cloth suit on.')
        player_Armor.type = 'cloth'
    if (len(fcommand_list) == 1) and (fcommand_list[command] == 'w') or (fcommand_list[command] == 'W') or (fcommand_list[command] == 'west'):
        room = 2
    if (len(fcommand_list) == 1) and (fcommand_list[command] == 'n') or (fcommand_list[command] == 'N') or (fcommand_list[command] == 'north'):
        room = 6
    if (len(fcommand_list) == 1) and (fcommand_list[command] == 's') or (fcommand_list[command] == 'S') or (fcommand_list[command] == 'south'):
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
            room = 4
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
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'e') or (fcommand_list[0] == 'e'):
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
            room = 13
        if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'e') or (fcommand_list[0] == 'e'):
            room = 16
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
            room = 16

    else:
        print ('You can\'t do that here.')

    pass

#------------------------------------------------------------------------------
#
# Room 16
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
                room =  15
            if (fcommand_list[0] == 'w') or (fcommnad_list[0] == 'W') or (fcommand_list[0] == 'west'):
                room = 19
            if (fcommand_list[0] == 'e') or (fcommand_list[0] == 'E') or (fcommand_list[0] == 'east'):
                room = 15
            if (fcommand_list[0] == 'n') or (fcommand_list[0] == 'N') or (fcommand_list[0] == 'north'):
                room = 18
        else:
            print ('You can\'t do that here.')



#----------------------------------------------------------------------------
#
# Room 17
#
#----------------------------------------------------------------------------
def parse_room17 (fcommand_list):

    pass

#---------------------------------------------------------------------------
#
# Room 18
#
#----------------------------------------------------------------------------
def parse_room18 (fcommand_list):

    pass

#---------------------------------------------------------------------------
#
# Room 19
#
#----------------------------------------------------------------------------
def parse_room19 (fcommand_list):

    pass

#---------------------------------------------------------------------------
#
# Room 20
#
#---------------------------------------------------------------------------
def parse_room20 (fcommand_list):

    pass

#---------------------------------------------------------------------------
#
# Room 21
#
#---------------------------------------------------------------------------
def parse_room21 (fcommand_list):

    pass

#---------------------------------------------------------------------------
#
# Room 22
#
#---------------------------------------------------------------------------
def parse_room22 (fcommand_list):

    pass

#---------------------------------------------------------------------------
#
# Room 23
#
#---------------------------------------------------------------------------
def parse_room23 (fcommand_list):

    pass

#---------------------------------------------------------------------------
#
# Room 24
#
#---------------------------------------------------------------------------
def parse_room24 (fcommand_list):

    pass


#---------------------------------------------------------------------------
#
# Room 25
#
#----------------------------------------------------------------------------
def parse_room25 (command_list):

    pass

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
        display_room (room, inGame)

        print ("")
        print (">", end='')
        command = input ()


        try:
            command_list = command.split(' ')


        except:
            print('I hope you remembered to save.')
            exit()


        print ('Debugging', command_list)
        pritn (f'Room: {room}')


        if (command_list[0] == 'quit') or (command_list[0] == 'exit'):
            print ('I hope you remembered to save')
            exit ()


        if (check_syntax (command_list) == True):
            parse_general(command_list)


            if room == 1:
                parse_room1 (command_list)
            elif room == 2:
                player_One.room = 2
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
                paarse_room17 (command_list)
            elif room == 18:
                parse_room18 (command_list)
            elif room == 19:
                parse_room19 (command_list)
            elif room == 20:
                parse_room20 (command_list)
            elif room == 21:
                parse_room22 (command_list)
            elif room == 22:
                parse_room22 (command_list)
            elif room == 23:
                parse_room23 (command_list)
            elif room == 24:
                parse_room24 (command_list)
            elif room == 25:
                parse_room25 (command_list)

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
