Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================ RESTART: C:\Users\sinis\Desktop\textgame1_3.py ================
1
1. This is your father's genetics engineering lab. In the 
corner of the room there is a living pet dinosaur that he
made you. You also find an open diary on his desk.

You see your fathers journal on the table.

There is an exit to the south
There is an obvious exit to the north

>s
Debugging ['s']
2
2. This is a hallway in your father's single story
dewlling. A dim light shows an exit to to the living
room, and exit to your father's bedroom to the north,
another exit to your room to the south, and the living
room to the east

There are obvious exits to the north, south, and east
There is an obvious exit to the north

>s
Debugging ['s']
4
4. This is your bedroom. The wall is decorated with a few
posters of you favorite band. There is a desk with a computer
on the wall opposite your bed. There are a few clothes on the floor
and the room is in a state of disarray that only the most diligent
teenagers can achieve by neglecting to clean their room on a regular
basis.

Your journal is open on your bed, and you think you left your pocket knife in
a pile of clothes
There is an exit to the north .
There is an obvious exit to the north

>equip knife
Debugging ['equip', 'knife']
You wield your trusty pocket knife.
4
4. This is your bedroom. The wall is decorated with a few
posters of you favorite band. There is a desk with a computer
on the wall opposite your bed. There are a few clothes on the floor
and the room is in a state of disarray that only the most diligent
teenagers can achieve by neglecting to clean their room on a regular
basis.

Yoour journal is open on your bed:
There is an exit to the north .
There is an obvious exit to the north

>n
Debugging ['n']
Traceback (most recent call last):
  File "C:\Users\sinis\Desktop\textgame1_3.py", line 2680, in <module>
    main()
  File "C:\Users\sinis\Desktop\textgame1_3.py", line 2671, in main
    parse_args(args)
  File "C:\Users\sinis\Desktop\textgame1_3.py", line 2660, in parse_args
    game_start(godmode)
  File "C:\Users\sinis\Desktop\textgame1_3.py", line 2599, in game_start
    monster_type == 'dog'
NameError: name 'monster_type' is not defined
