# Text adv game :D
import cmd
import textwrap
import sys
import os
import time
import random
import termcolor
import curses
import random
from random import seed
from random import randint
from termcolor import colored, cprint

screen_width = 100
seed(1)
#### Player setup (health, etc.) ####
global starter
starter = False

class player:
    def __init__(self):
        self.name = ''
        self.nickname = ''
        self.hp = 10
        self.cp = 0
        self.gen = ''
        self.loc = 'corridor'
        self.gameovr = False
        self.easy = False
        self.medium = False
        self.hard = False




myPlayer = player()
questions = 1
perfect = False
outof = 3
points = 0
line = ("")



""" Title screen selection code """

def title_screen_selections():
    potato = ['start', 'howto', 'quit']
    global takeable_things
    global inv
    global optionlast
    global options_start
    options_start = ['start', 'howto', 'quit']
    option = input(""">""")
    if option.lower() == ("start"):
        start_game()  # placeholder until written
    elif option.lower() == ("howto"):
        help_menu()
    elif option.lower() == ('bhoom'):
        hello = ("""
Creator hack accepted.\n""")
        for character in hello:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        myPlayer.name = 'Bhoom'
        myPlayer.gen = 'male'
        time.sleep(3)
        Japan_done = True
        russia_done = True
        ending()
    elif option.lower() == ("quit"):
        quitter = input("""




                        Are you sure? (y/n)

        """)
        if quitter == ("y"):
            print("""





                            Well, seeya!

        """)
        time.sleep(3)
        sys.exit()



    elif option.lower() not in potato:
        os.system('clear')
        print("""


                    Now that's a word I've never heard of...
                        I didn't understand that.
            Could you please type in something that I actually understand?
                                Thank you.


                  Choose between 'start', 'howto', or 'quit'.



        """)

        restate = input(""">""")
        if restate.lower() == ("start"):
            start_game()  # placeholder until written
        elif restate.lower() == ("howto"):
            howto()
        elif restate.lower() == ("quit"):
            quitter = input("""




                            Are you sure? (y/n)

            """)
            if quitter == ("y"):
                print("""





                                Well, seeya!

            """)
            time.sleep(3)
            sys.exit()

    times_wrong = 2
    optionlast = input(""">""")
    os.system('clear')
    while restate not in potato:
        times_wrong += 1
        restate2 = input("> ")
        if times_wrong < 4:
            print("""

                            No, I still didn't understand that.
                            Maybe we should try something else.

                                What? You want to try again?
                                    Very well then...

                        Choose between 'start', 'howto', or 'quit'.


            """)

            if restate2.lower() == ("start"):
                start_game()  # placeholder until written
            elif restate2.lower() == ("howto"):
                howto()
            elif restate2.lower() == ("quit"):
                quitter = input("""




                                    Are you sure? (y/n)

            """)
                if quitter == ("y"):
                    print("""





                                        Well, seeya!

            """)
                    time.sleep(3)
                    sys.exit()

        if times_wrong > 4:

            os.system('clear')
            cprint("""


                        That was not a valid option! I've gone out of my way to try and
                        convince you to type in the correct answers by faking that I don't
                        understand what you said. But I actually do! THEY'RE JUST NOT ONE
                        OF THE VALID OPTIONS!

                        Why did you say that? That was not what you are supposed to say.
                        Try saying either 'start', 'howto', or 'quit', and maybe I won't
                        respond to you this way!




                """, "red", attrs=['bold'])
            option = input(""">""")
            if option.lower() == ("start"):
                print("""

                        Finally, some sense! I'll direct you to the game right away.
                        Bye bye, and try not to anger me with invalid options again!



                    """)
                time.sleep(6)
                os.system('clear')
                start_game()
            elif option.lower() == ("howto"):
                print("""

                        Finally, some sense! I'll direct you to the tutorial right away.
                        Bye bye, and try not to anger me with invalid options again!



                    """)
                time.sleep(6)
                os.system('clear')
                howto()
            elif option.lower() == ("quit"):
                os.system('clear')
                quitter = input("""




                                Seriously? After all this time bothering
                                me, you're just gonna leave without
                                saying sorry?     (y/n)

                """)
                if quitter == ("y"):
                    print("""





                                ......

                                Well...

                                Just... The next time you play this game,
                                please don't make me feel bad again.

                                I'm gonna cry soon... Goodbye now...

                                [sobs]

                """)
                    time.sleep(7)
                    sys.exit()

        elif times_wrong > 6:
            os.system('clear')
            cprint("""


                    Seriously, you one very stubborn person.
                    Now please.
                    Do. Not. Enter. Invalid. Commands!

                    You can choose from 'start', 'howto', and 'quit'





            """, "red", attrs=['bold', 'underline', 'blink'])
            option = input(""">""")
            if option.lower() == ("start"):
                os.system('clear')
                print("""

                    Finally, some sense! I'll direct you to the game right away.
                    Bye bye, and try not to anger me with invalid options again!



                """)
                time.sleep(6)
                start_game()
            elif option.lower() == ("howto"):
                os.system('clear')
                print("""

                    Finally, some sense! I'll direct you to the tutorial right away.
                    Bye bye, and try not to anger me with invalid options again!



                """)
                time.sleep(6)
                howto()
            elif option.lower() == ("quit"):
                quitter = input("""




                            Seriously? After all this time bothering
                            me, you're just gonna leave without
                            saying sorry?     (y/n)

            """)
                if quitter == ("y"):
                    print("""





                            ......

                            Well...

                            Just... The next time you play this game,
                            please don't make me feel bad again.

                            I'm gonna cry soon... Goodbye now...

                            [sobs]

            """)
                    time.sleep(7)
                    sys.exit()



# Menu Screen

def title_screen():
    os.system('clear')
    print("""

                            ||||||||||||||||||||||||||||||
                            |............................|
                            |.       Fix the Past       .|
                            |. *a text-adventure game.* .|
                            |.                          .|
                            |.        - start -         .|
                            |.        - howto -         .|
                            |.        - quit -          .|
                            |............................|
                            ||||||||||||||||||||||||||||||

                              Copyright 2019 rocketbhoom



    """)
    title_screen_selections()

def help_menu():
    os.system('clear')
    input_1 = input("""

                        |||||||||||||||||||||||||||||||||||||
                        |...................................|
                        |.        - Instructions -         .|
                        |.    This is a text-based game.   .|
                        |.   You can navigate using the    .|
                        |.  options on screen. Type them   .|
                        |.   in to the console to choose   .|
                        |.     that particular option.     .|
                        |.                                 .|
                        |.             [next]              .|
                        |...................................|
                        |||||||||||||||||||||||||||||||||||||

                             Copyright 2019 rocketbhoom



    """)

    if input_1.lower() == ("next"):
        os.system('clear')
        input_2 = input("""

                        |||||||||||||||||||||||||||||||||||||
                        |.          - Tutorial -           .|
                        |.    You're doing it! Good job.   .|
                        |.   Now try choosing something.   .|
                        |. Type in the option you want to  .|
                        |.            choose!              .|
                        |.                                 .|
                        |. {1 cookie}         {2 cookies}  .|
                        |.    [1c]               [2c]      .|
                        |...................................|
                        |||||||||||||||||||||||||||||||||||||

                             Copyright 2019 rocketbhoom

                        Note: type in the option key in the
                        [square] brackets. The ones in the
                          {curly} brackets are the full
                                    sentence. """)
        if input_2 == '2c':
            os.system('clear')
            input_4 = input("""

                        |||||||||||||||||||||||||||||||||||||
                        |...................................|
                        |.          - Tutorial -           .|
                        |.    Ha-ha, I knew you would do   .|
                        |.   that. That's awesome though,  .|
                        |.  you now know how to play text  .|
                        |.        adventure games!         .|
                        |.                                 .|
                        |.     {Return to menu screen}     .|
                        |.            [return]             .|
                        |...................................|
                        |||||||||||||||||||||||||||||||||||||

                             Copyright 2019 rocketbhoom


                    """)
            if input_4 == ("""return"""):
                title_screen()
        if input_2 == '1c':
            os.system('clear')
            input_3 = input("""

                        |||||||||||||||||||||||||||||||||||||
                        |...................................|
                        |.          - Tutorial -           .|
                        |.   Seriously? Most people take   .|
                        |.   two. That's awesome though,   .|
                        |.  you now know how to play text  .|
                        |.        adventure games!         .|
                        |.                                 .|
                        |.     {Return to menu screen}     .|
                        |.            [return]             .|
                        |...................................|
                        |||||||||||||||||||||||||||||||||||||

                             Copyright 2019 rocketbhoom


                    """)
            if input_3 == ("return"):
                os.system('clear')
                title_screen()




# Intro



def start_game():
    global takeable_things
    global inv
    global gender_2
    global availible_options
    global starter
    starter = False
    os.system("clear")
    question1 = """

Name your character.\n"""
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)

    player_name = input(""">""")
    myPlayer.name = player_name
    time.sleep(2)
    os.system('clear')
    name = ("""
%s?
""" % (myPlayer.name))
    for character in name:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    strange = ("""
A strange name.
A strange name indeed.
""")
    for character in strange:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(4)
    os.system('clear')
    gender = ("""


What is your character's gender?

(male/female/unknown)


""")

    for character in gender:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    gender_in = input("> ")
    if gender_in.lower() == ("male"):
        myPlayer.gen = 'boy'
        myPlayer
        os.system('clear')
        confirm_gen = ("""
Hey there, %s! Just to confirm, your gender is '%s', correct?

(y/n)

""" % (myPlayer.name, gender_in))
        for character in confirm_gen:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.08)
        confirm_gender = input(">")
        if confirm_gender.lower() == ("n"):
            os.system('clear')
            oopsie = ("""
Huh? Computers are usually never wrong.
It should be a human error. \n
""")
            for character in oopsie:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            oopsie2 = ("""
Or are you intentionally pranking me?
IF YOU ARE...\n
Well, anyways, you may have to re-enter your gender.
        """)
            for character in oopsie2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(5)
            gender_2 = ("""


What is your character's gender?

(male/female/unknown)\n
""")



            for character in gender_2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            gender_2_in = input("> ")
            if gender_2_in.lower() == ("male"):
                os.system('clear')
                myPlayer.gen = 'boy'
                game()
            if gender_2_in.lower() == ("female"):
                os.system("clear")
                myPlayer.gen = 'girl'
                game()
            if gender_2_in.lower() == ("unknown"):
                os.system("clear")
                myPlayer.gen = 'child'
                game()


        elif confirm_gender.lower() == ("y"):
            game()
    if gender_in.lower() == ("female"):
        myPlayer.gen = 'girl'
        os.system('clear')
        confirm_gen = ("""
Hey there, %s! Just to confirm, your gender is '%s', correct?

(y/n) \n """ % (myPlayer.name, gender_in))

        for character in confirm_gen:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.08)
        confirm_gen_in_2 = ("> ")
        if confirm_gen_in_2.lower() == ("n"):
            os.system('clear')
            oopsie = ("""
Huh? Computers are usually never wrong.
It should be a human error.
""")
            for character in oopsie:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            oopsie2 = ("""
Or are you intentionally pranking me?
IF YOU ARE...
Well, anyways, you may have to re-enter your gender.
        """)
            for character in oopsie2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(5)
            gender_2 = ("""


What is your character's gender?

(male/female/unknown)\n""")



            for character in gender_2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            gender_2_in = ("> ")
            if gender_2_in.lower() == ("male"):
                os.system('clear')
                myPlayer.gen = 'boy'
                game()
            if gender_2_in.lower() == ("female"):
                os.system("clear")
                myPlayer.gen = 'girl'
                game
            if gender_2_in.lower() == ("unknown"):
                os.system("clear")
                myPlayer.gen = 'child'
                game()

        elif confirm_gen_in2.lower() == ("y"):
            game()
    if gender_in.lower() == ("unknown"):
        myPlayer.gen = 'child'
        os.system('clear')
        confirm_gen = ("""
Hey there, %s! Just to confirm, you chose '%s', correct?

(y/n)

""" % (myPlayer.name, gender))
        for character in confirm_gen:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.08)
        confirm_gen_in = input(">")
        if confirm_gen_in.lower() == ("n"):
            os.system('clear')
            oopsie = ("""
Huh? Computers are usually never wrong.
It should be a human error.
""")
            for character in oopsie:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            oopsie2 = ("""
Or are you intentionally pranking me?
IF YOU ARE.../n
Well, anyways, you may have to re-enter your gender.
        """)
            for character in oopsie2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(5)
            gender_2 = ("""


What is your character's gender?

(male/female/unknown)
\n""")
            gender_2_in = input("> ")



            for character in gender_2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            if gender_2_in.lower() == ("male"):
                os.system('clear')
                myPlayer.gen = 'boy'
                game()
            if gender_2_in.lower() == ("female"):
                os.system("clear")
                myPlayer.gen = 'girl'
                game
            if gender_2.lower() == ("unknown"):
                os.system("clear")
                myPlayer.gen = 'child'
                game()


        if confirm_gen_in2.lower() == ("y"):
            game()







#########################
#    The actual game!   #
#########################





def game():
    global takeable_things
    global inv
    global starter
    os.system('clear')
    if starter == False:
        printer = ("""

%s, you are about to go on a journey.
It will not be an easy one, but I believe in you.
You can do it""" % (myPlayer.name))
        for character in printer:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.09)
        printy2 = ("""...

        """)
        for character in printy2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.5)
        time.sleep(2)
        os.system('clear')
        starter = True
        game()



    elif starter == True:
        os.system("clear")
        what = ("""
...


What was that?



        """)
        for character in what:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.09)
        time.sleep(5)
        os.system("clear")
        description = ("""

You sit up in your bed.

    """)
        for character in description:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        os.system("clear")
        no_2 =  ("""
You are %s, a %s living in the year 2072. You are in your bedroom. It is 1:34 AM.
Everything seems normal. Except for the fact that you just had a weird dream.
Somebody spoke to you about a journey. And that particular person (or thing)
believes in you.


Dismissing the thought, you go back to sleep, and decide that it isn't worth thinking
about.



                        {Continue}  [c]
""" % (myPlayer.name, myPlayer.gen))
        for character in no_2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)


        no_input = input("""

        """)
        if no_input == ('c'):
            os.system('clear')
            main_loop()







##### MAP #####
"""
1st floor


-----------------_______|-----------|------------|
|                |   p  |           | dining     |-------|
|                |   o  | doorstep  | room       kitchen |
|  Front yard    |   r  |           |
|                |   c  |-------|                        |
|           -----|   h  |       |    --------------------|
|           |    --------       |    - s t a i r s -     |
|           |     Garage        |                        |
|           |                   |------------------------|
--------------------------------|



2nd floor

|                   -N-


|------------------------------------------|
| bath | Granpa's | Grandma's | Player's   |
| room | bedroom  | bedroom   | bedroom    |
|------|----      |           |            |
| LAB ROOM |      |-----------|------------|-----|
|          |------|             corridor         |
|          |         |--------|-------------     |
|                    |bathroom|      stairs      |
|--------------------|--------|------------------|



|                   -S-

"""


a1 = False
a2 = False
a3 = False
a4 = False
a5 = False
b1 = False
b2 = False
b3 = False
b4 = False
b5 = False
c1 = False
c2 = False
c3 = False
c4 = False
c5 = False
d1 = False
d2 = False
d3 = False
d4 = False
d5 = False
mrjohn_yes = False
map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111             11111111    4444444444444  11111111 0
                0  1                           1                   1        0
       C        0  1                           1                   1        0
                0  1        44444444444        1                   1        0
                0---------------------------------------------------------- 0
                0                                                       4   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")

energy = 5
stringy2 = ""
pm25_points = 0
pm25_time = 0
pm25_outof = 7
name = ''
DESCRIPTION = 'look'
visited = False
Japan_done = False
saudi_done = False
Russia_done = False
ger_done = False
USA_done = False
japan_done = False
russia_done = False
india_done = False
source1 = False
source2 = False
source3 = False
UP = 'up'
DOWN = 'down'
FRWRD = 'forward'
BCKWRD = 'back'
LEFT = 'left'
RIGHT = 'right'
OUT = 'out'
inv_gone = False
inv_gone2 = False
inv = []
takeable_things = []
examinable_things = []



visited = {'bedroom': False, 'bathroom': False, 'corridor': False,
            'stairs': False, 'kitchen': False, 'diningroom': False,
            'lab': False, 'bedroom2': False, 'bedroom3': False,
            '1stfloor': False, 'stairs1': False,
            'doorstep': False}


solved = {'china': False, 'usa': False, 'india': False, 'russia': False, 'japan': False, 'China': False, 'USA': False, 'saudiindia': False,
          'Russia': False, 'Japan': False}




"""
2nd floor:

bedroom, bedroom2 (grandmother's bedroom,
grandmother is dead, room empty), bedroom3
(grandfather's bedroom), bathroom, livingroom,
corridor2, lab

1st floor:

kitchen, diningroom (next to porch)

Outside:

porch, frontyard

"""

map_game = {
    'china': {
        name: ("China"),
    },
}

mappy = {
    'bedroom': {
        name: ("%s's bedroom" % (myPlayer.name)),
        DESCRIPTION: """

This is your bedroom. A rather large room, it sits on the northeast side of the house.
There is a book on the floor. It's titled 'Time Travel Science'.
There is a picture of your parents on the windowsill.
There is an ancient Game Boy Advance that your dad always kept. The label on the cartridge
reads 'Sonic The Hedgehog'.
There is a chest of drawers. Inside contains your clothes, on top there is a Nintendo Glass,
your see-through hologram video game console.
Your backpack lays in the corner of the room.
To your front is the corridor.



        """,
        FRWRD: "corridor",
        BCKWRD: "",
        LEFT: "",
        RIGHT: "",
        UP: "",
        DOWN: "",


    },
    'doorstep': {
        name: ("Doorstep"),
        DESCRIPTION: """
This is the doorstep. Quite dusty.
You don't dare open the door, for fear of dust.
Nothing to see here.
Go backwards to the path to the stairs.""",
        FRWRD: "",
        BCKWRD: "1stfloor",
        LEFT: "",
        RIGHT: "",
        UP: "",
        DOWN: "",


    },
    'corridor': {
        name: ("The 2nd floor corridor"),
        DESCRIPTION: """

This is the second floor corridor.
Not much to tell here.
To your right is the walkway to the Lab, going past both your grandparents's
rooms. To your left is a walkway to the stairs, lined with windows.
Behind you is your bedroom.


        """,
        FRWRD: "",
        BCKWRD: "bedroom",
        LEFT: "stairs",
        RIGHT: "lab",
        UP: "",
        DOWN: "",



    },
    'lab': {
        name: ("Granddad's laboratory"),
        DESCRIPTION: """

This is Granddad's lab.
There are papers on the workdesk.
There seems to be something glowing on the shelf. Looks like a small handheld game console.
There is a bottle with a strange-looking liquid labeled 'Prototype 2'. There's another sticker on it
saying 'Warning : contains acid'.
There are notes with your Granddad's handwriting taped all over the desk.
The computer is on. The screen glows faintly.
There is a special navigation function here. By typing 'walk', then typing 'out',
you will exit the lab and move to the corridor.

Navigation : [left] will lead to bathroom.
             [right] will lead to Granddad's Bedroom.



        """,
        FRWRD: "",
        BCKWRD: "",
        LEFT: "bathroom",
        RIGHT: "bedroom3",
        UP: "",
        DOWN: "",
        OUT: "corridor",





    },
    'bathroom': {
        name: ("The Lab's bathroom"),
        DESCRIPTION: """
Why are you in the bathroom?
There doesn't seem to anything to do here, unless you count flushing the
toilet as interesting.

Let's go. Navigation directions : Backward (to lab), and right (Granddad's Bedroom).
""",
        FRWRD: "",
        BCKWRD: "lab",
        LEFT: "",
        RIGHT: "bedroom3",
        UP: "",
        DOWN: "",





    },
    'stairs': {
        name: ("Stairs"),
        DESCRIPTION: """
These are the stairs leading down.
To go down, type [walk], then [down].
To walk back to the corridor type [walk], then [right].
""",
        FRWRD: "",
        BCKWRD: "stairs",
        LEFT: "",
        RIGHT: "corridor",
        UP: "",
        DOWN: "1stfloor",





    },
    '1stfloor': {
        name: ("1st Floor"),
        DESCRIPTION: """
This is the first floor.
To your right is the path to the kitchen and the dining room.
To your left is the doorstep.
Behind you are the stairs.""",
        FRWRD: "",
        BCKWRD: "stairs1",
        LEFT: "doorstep",
        RIGHT: "diningroom",
        UP: "",
        DOWN: "",





    },
    'stairs1': {
        name: ("Stairs"),
        DESCRIPTION: """
These are the stairs leading up.
To go up, type [walk], then [up].
To walk back type [walk], then [backwards].
""",
        FRWRD: "",
        BCKWRD: "1stfloor",
        LEFT: "",
        RIGHT: "",
        UP: "corridor",
        DOWN: "",





    },
    'diningroom': {
        name: ("Dining room"),
        DESCRIPTION: """
This is the dining room. All the plates on the table are upside down,
to protect from dust. A heating stove sits on the table.

There are chairs sitting around the table. All are covered with big pieces of cloth,
only the legs are visible.
There is a path to the right leading to the kitchen.
Walk backwards to go back.""",
        FRWRD: "",
        BCKWRD: "1stfloor",
        LEFT: "",
        RIGHT: "kitchen",
        UP: "",
        DOWN: "",





    },
    'kitchen': {
        name: ("Kitchen"),
        DESCRIPTION: """
This is the kitchen. A wash basin sits over to the left. There are shelves
stacked with instant noodles. A drawer labled 'Cutlery' sits near the
wash basin.

Behind you is the path to the dining room.
""",
        FRWRD: "",
        BCKWRD: "diningroom",
        LEFT: "",
        RIGHT: "",
        UP: "",
        DOWN: "",





    },

    'bedroom2': {
        name: ("Grandma's Bedroom"),
        DESCRIPTION: """
This was your Grandma's bedroom. The room is empty and cold.
You decide to leave, as seeing her room, you can't bear to think
about the fact that she's dead.

Leave by typing [walk], then [backward]
Move to Granddad's bedroom by walking right.""",
        FRWRD: "",
        BCKWRD: "corridor",
        LEFT: "",
        RIGHT: "bedroom3",
        UP: "",
        DOWN: "",





    },
}




##### MAP #####
"""
-----------------_______|-----------|------------|
|                |   p  |           | dining     |-------|
|                |   o  | doorstep  | room       kitchen |-------|
|  Front yard    |   r  |           |                    bathroom|
|                |   c  |-------|                        |-------|
|           -----|   h  |       |    --------------------|
|           |    --------       |    - s t a i r s -     |
|           |     Garage        |                        |
|           |                   |------------------------|
--------------------------------|

"""


def print_loc():
    if myPlayer.loc == ('bedroom3'):
        bedroom3()
    else:
        print('\n' + ('#' * (4 + len(myPlayer.loc))))
        print('# ' + myPlayer.loc.upper() + ' #')
        print('# ' + mappy[myPlayer.loc] [DESCRIPTION] + ' #')
        print('\n' + ('#' * (4 + len(myPlayer.loc))))

def prompt():
    global takeable_things
    global inv_gone
    global inv_gone2
    global inv
    os.system('clear')
    while myPlayer.loc != 'bedroom3':
        print_loc()
        print("""

To do something, use verbs such as 'examine' or 'inspect'
You can also use 'take.'
Or for movement, 'walk', then specify which direction.

Choose an option by typing it in and pressing enter.
Normal commands : 'menu', 'inv'(inventory), 'exit'


""")
        action = input("> ")
        acceptable_actions = ['examine', 'walk', 'go to', 'talk', 'take', 'inv', 'menu', 'exit', 'inspect', 'look']
        walk_commands = ['walk', 'go to']
        look_commands = ['examine', 'inspect', 'look']
        while action.lower() not in acceptable_actions:
            os.system('clear')
            print("""
Huh? That doesn't seem to be in the options list. Try typing
something that exists in there.



""")
            action = input(">")
        if action.lower() == 'exit':
            os.system('clear')
            exitplay = ("""
Are you sure? You will lose all progress on the game so far,
and your character's name will be erased from the system.

(y/n)

""")
            for character in exitplay:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            exitplay_input = input("""
> """)
            if exitplay_input == ("n"):
                prompt()
            elif exitplay_input == ("y"):
                goodbye = ("""
Goodbye, old friend. I hope to see you again.
""")
                for character in goodbye:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.1)
                time.sleep(4)
                sys.exit()

        elif action.lower() in walk_commands:
            player_move(action.lower())
        elif action.lower() in look_commands:
            player_examine(action.lower())
        elif action.lower() == 'take':
            take_things()
        elif action.lower() == 'menu':
            options_screen()
    if myPlayer.loc == 'bedroom3':
        bedroom3()





def take_things():
    global papers_taken_yes
    global inv
    warned = False
    global takeable_things
    if len(inv) < 10:
        take = ("""
What would you like to take?
Options : %s
""" % (takeable_things))
        for character in take:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        if myPlayer.loc == 'bedroom':
            bedroom_take = input("> ")
            if bedroom_take.lower() == 'book':
                book_taken = ("""
You have taken the book.\n""")
                for character in book_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'book' not in inv:
                    inv.append('book')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'picture':
                picture_taken = ("""
You have taken the picture.\n""")
                for character in picture_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'picture' not in inv:
                    inv.append('picture')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'gameboy':
                gameboy_taken = ("""
You have taken the Game Boy.\n""")
                for character in gameboy_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'gameboy' not in inv:
                    inv.append('gameboy')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'clothes':
                clothes_taken = ("""
You have taken the your clothes.\n""")
                for character in clothes_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'clothes' not in inv:
                    inv.append('clothes')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'nintendoglass':
                nintendoglass_taken = ("""
You have taken your Nintendo Glass.\n""")
                for character in book_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'nintendoglass' not in inv:
                    inv.append('nintendoglass')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'backpack':
                backpack_taken = ("""
You have taken your backpack.\n""")
                for character in backpack_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'backpack' not in inv:
                    inv.append('backpack')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
        elif myPlayer.loc == 'lab':
            lab_take = input("""> """)
            if lab_take.lower() == ('papers'):
                papers_taken = ("""
You fold the papers and put them in your pocket. I wonder, will
your Granddad get mad at you for taking his papers?\n""")
                papers_taken_yes = True
                for character in backpack_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'papers' not in inv:
                    inv.append('papers')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'acid':
                acid_taken = ("""
You carefully take the acid. Let's hope it doesn't come in contact with air,
and activate.\n""")
                for character in acid_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'acid' not in inv:
                    inv.append('acid')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
        elif myPlayer.loc == ('kitchen'):
            kitchen_input = input("> ")
            if kitchen_input.lower() == 'instantnoodles':
                noodles_taken = ("""
You pocket a bag of instant noodles. For later.\n""")
                for character in noodles_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'noodles' not in inv:
                    inv.append('noodles')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
        elif myPlayer.loc == ('diningroom'):
            diningroom_in = input("""> """)
            if diningroom_in.lower() == ("plates"):
                plates_taken = ("""
You lift up the plate. Doesn't seem to fit in your pocket.\n""")
                for character in plates_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(3)
                main_loop()



    elif len(inv) > 8:
        if warned == False:
            nearly = ("""
You may only store 10 items in your inventory. You currently have %d
items in your inventory.""" % (len(inv)))
            for character in nearly:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            warned = True
        elif warned == True:
            take_things()




def player_move(myAction):
    global takeable_things
    global inv_gone
    global inv_gone2
    global inv
    ask = """


Use [forward], [backward], [left], [right], [up], or [down] to navigate.\n
\n """
    for character in ask:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    ask_in = ("> ")
    dest = input(ask_in)
    if dest in ['forward']:
        destination = mappy[myPlayer.loc][FRWRD]
        movement_handler(destination)
    elif dest in ['backward']:
        destination = mappy[myPlayer.loc][BCKWRD]
        movement_handler(destination)
    elif dest in ['left']:
        destination = mappy[myPlayer.loc][LEFT]
        movement_handler(destination)
    elif dest in ['right']:
        destination = mappy[myPlayer.loc][RIGHT]
        movement_handler(destination)
    elif dest in ['up']:
        destination = mappy[myPlayer.loc][UP]
        movement_handler(destination)
    elif dest in ['down']:
        destination = mappy[myPlayer.loc][DOWN]
        movement_handler(destination)

def movement_handler(destination):
    global takeable_things
    global examinable_things
    global inv
    global inv_gone
    global inv_gone2
    if destination == '':
        invalid_direction = ("""
There doesn't seem to be a pathway leading to that direction.
And you don't seem to be a Kung Fu master, so you can't
punch through the walls.""")
        for character in invalid_direction:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        prompt()
    else:
        location_player = ("""
\nYou have moved to """ + destination + ".\n")
        for character in location_player:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(2)
        myPlayer.loc = destination
        if myPlayer.loc == 'lab':
            takeable_things = ['papers', 'notes', 'acid']
            examinable_things = ['shelf', 'computer', 'acid', 'papers', 'notes']
        elif myPlayer.loc == 'bedroom':
            takeable_things = ['book', 'picture', 'gameboy', 'clothes', 'nintendoglass', 'backpack']
            examinable_things = ['book', 'picture', 'gameboy', 'nintendoglass']
        elif myPlayer.loc == 'bathroom':
            examinable_things = ['nothing']
        elif myPlayer.loc == 'kitchen':
            examinable_things = ['shelves', 'washbasin']
            takeable_things = ['instantnoodles']
        elif myPlayer.loc == 'diningroom':
            examinable_things = ['chair']
            takeable_things = ['plates']
        elif myPlayer.loc == 'corridor' or 'stairs' or 'bedroom2' or 'bedroom3' or '1stfloor' or 'stairs1' or 'doorstep':
            del examinable_things[:]
            del takeable_things[:]









    main_loop()
def player_examine(action):
    global takeable_things
    global examinable_things
    global inv_gone
    global inv_gone2
    global inv
    question = ("""
What would you like to examine?
These are the options : %s \n""" % (examinable_things))
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    if myPlayer.loc == 'lab':
        in_lab = input("> ")
        if in_lab == ("shelf"):
            shelf_examine = ("""
You can't seem to reach the handle to open the shelf.
The handheld-game-console looking object remains a mystery.\n""")
            for character in shelf_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_lab == ("computer"):
            computer_examine = ("""
The computer screen shows a calculator app with some numbers.
Beside the calculator app is a programming application that
you seem to know. Upon closer inspection, it seems to be
your favorite code editor, Sublime Text. It shows a
Python file with just over one hundred thousand lines.

There also seems to be a text editor window open with some
notes that you can't make any sense out of.
\n
""")
            for character in computer_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_lab == ("acid"):
            acid_examine = ("""
The liquid inside the bottle seems to glow. You wonder how corrosive this would be.

You discover that the label on the bottle can unfold. You read :

"Activates when in contact with air."

That's just about it that you can find on the bottle.\n """)
            for character in acid_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()

        elif in_lab == ("papers"):
            papers_examine = ("""
The papers have calculations and weird symbols on them. Some have
some pictures drawn on them. You're not that smart, but judging by
the line on a sheet of paper that has years written on it with arrows
pointing backwards and forwards, it has something to do with time.
\n""")
            for character in papers_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_lab == ("notes"):
            notes_examine = ("""
The notes have 'more power' and 'add return function' on them.
There are some more, but you can't quite read them as they've been crossed out.\n""")
            for character in notes_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        while in_lab not in examinable_things:
            invalid = ("""
You can't seem to spot any such thing. I wonder, how exactly did you come up
with that word? It seems supernatural. Hmm....""")
            for character in invalid:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            time.sleep(3)
            prompt()
    if myPlayer.loc == 'bedroom':
        in_pbed = input("> ")
        if in_pbed == ("book"):
            book_examine = ("""
This book used to be your Granddad's. He had finished it 10 times,
and now occationally reads it, but otherwise, it's yours.
""")
            for character in book_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_pbed == ("picture"):
            picture_examine = ("""
This is a picture of your parents at the park. The sky is brown with dust, but otherwise,
this picture is beautiful.

You check the date written on the back. 2061.
""")
            for character in picture_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_pbed == ("gameboy"):
            gameboy_examine = ("""
This is an antique your father kept. It was given to him by his father, who got it
second-hand. The screen is scratched slightly.

The cartridge inside says 'Sonic The Hedgehog'. Sonic was a character your Granddad
always liked.
""")
            for character in gameboy_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_pbed == ("nintendoglass"):
            nintendoglass_examine = ("""
This was your Christmas present 2 years ago. The Nintendo Glass was only a tab of glass
and a game controller. When the button on the little tab was pressed, a holographic screen would appear,
the size of a 2019 home flat-screen TV.

The CPU of the glass tab would automatically update and get new games every day.

""")
            for character in nintendoglass_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        while in_pbed not in examinable_things:
            os.system('clear')
            invalid2 = ("""
You can't seem to spot any such thing. I wonder, how exactly did you come up
with that word? It seems supernatural. Hmm....""")
            for character in invalid2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            time.sleep(3)
            prompt()
    elif myPlayer.loc == 'bathroom':
        in_bathroom = input('> ')
        if in_bathroom == ("nothing"):
            hint = ("""
You have found a hint!
The hint is : What you are looking for lies in Granddad's Bedroom.

Good luck!\n""")
            for character in hint:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        while in_bathroom not in examinable_things:
            os.system('clear')
            invalid2 = ("""
You can't seem to spot any such thing. I wonder, how exactly did you come up
with that word? It seems supernatural. Hmm....""")
            for character in invalid2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            time.sleep(3)
            prompt()
    elif myPlayer.loc == 'kitchen':
        in_kitchen = input("""> """)
        if in_kitchen == 'shelves':
            shelves_examine = ("""
You only see stacks of instant noodles on top of each other. The shelf
itself looks quite old, but only because of the dust covering it.

The noodles seem to expire next year.\n""")
            for character in shelves_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_kitchen == 'washbasin':
            washbasin_examine = ("""
This is the wash basin.
It looks clean on the inside.
On the outside it's dusty.

The faucet dates back to 2015. It has an old-fashioned handle instead
of turning on the moment you approach it like most faucets do.

There is a dish holder near the wash basin. It's covered with a piece of cloth.
""")
            for character in washbasin_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        while in_kitchen not in examinable_things:
            os.system('clear')
            invalid2 = ("""
You can't seem to spot any such thing. I wonder, how exactly did you come up
with that word? It seems supernatural. Hmm....""")
            for character in invalid2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            time.sleep(3)
            prompt()
    elif myPlayer.loc == 'diningroom':
        in_diningroom == input("> ")
        if in_diningroom == 'chair':
            chair_examine == ("""
The chair dates back to 2030.
It's a wooden chair. One of your Granddad's.

There's nothing interesting about the chair you can find.
""")
            for character in chair_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()









def inventory_check():
    global takeable_things
    global inv_gone
    global inv_gone2
    global inv
    os.system('clear')
    print(inv)
    inv_return = input("""
This is your inventory. Type in 'r' to return to menu screen.\n""")
    if inv_return == ("r"):
        main_loop()

def main_loop():
    global takeable_things
    global inv
    while myPlayer.gameovr is False:
        prompt()
def menu():
    welcome_message = ("""
Welcome to the menu screen.\n""")
    for character in welcome_message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    menu = ("""
################################
#          [ Menu ]            #
#                              #
#                              #
#      [r] Return to game.     #
#    [inv] Check inventory.    #
#    [exit] Quit the game.     #
#   [option] Check options.    #
#                              #
################################\n""")
    for character in menu:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.0002)
    menu_input = input("> ")
    if menu_input.lower() == ('r'):
        os.system('clear')
        prompt()
    elif menu_input.lower() == ('inv'):
        inventory_check()
    elif menu_input.lower() == ('option'):
        options_screen()
    elif menu_input.lower() == ('about'):
        about()
    elif menu_input.lower() == ('exit'):
        exitsure = ("""
Are you sure, buddy? All your progress will be lost, and your character's
name will be erased from the system. (y/n)\n""")
        for character in exitsure:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        exit_in = input("> ")
        if exit_in == ('y'):
            goodbye_menu = ("""
Well, goodbye. Hope to see you again.

Till next time!\n""")
            for character in goodbye_menu:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            sys.exit()




def options_screen():
    os.system('clear')
    menu_screen = ("""
         #################################
         #           [ MENU ]            #
         #                               #
         #      [r] Return to game.      #
         #    [inv] Check inventory.     #
         #  [about] About the creator.   #
         #    [exit] Quit the game.      #
         #                               #
         #                               #
         #################################\n""")
    for character in menu_screen:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.002)
    input_menu = input("""> """)
    if input_menu.lower() == ('r'):
        time.sleep(1)
        prompt()
    elif input_menu.lower() == ('inv'):
        inventory_check()
    elif input_menu.lower() == ('about'):
        about()
    elif input_menu.lower() == ('exit'):
        exitsure = ("""
Are you sure, buddy? All your progress will be lost, and your character's
name will be erased from the system. (y/n)\n""")
        for character in exitsure:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        exit_in = input("> ")
        if exit_in == ('y'):
            goodbye_menu = ("""
Well, goodbye. Hope to see you again.

Till next time!\n""")
            for character in goodbye_menu:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            sys.exit()
        elif exit_in == ('n'):
            yay = ("""
Yay! I'll lead you back to the menu right away!\n""")
            for character in yay:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            options_screen()

def about():
    about_text = ("""
Bhoom Tansirimas (aka rocketbhoom) is an 12-year-old boy who loves coding.
He only writes Python. In his spare time, he likes to read, and listen to music.


Note : All info written here is from the time of coding (Feb 2020).
       To download the latest version of this game, or to get
       more up-to-date information, go to :

       https://github.com/rocketbhoom/fixthepast




Type in [r] to return to the menu selection screen. \n""")
    for character in about_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    about_in = input("> ")
    if about_in == ('r'):
        options_screen()
def bedroom3():
    global papers_taken_yes
    bedroom3_info = ("""
This is your Granddad's bedroom.
Your Granddad is currently in there.


There are pictures of famous scientists on the wall.
There is a notebook on the bedside table.




"Well, hello, %s!" your Granddad says. "What brings you here?"


[a] : "Nothing, just wanted to check on you."
[b] : "I wanted to ask you something."\n\n""" % (myPlayer.name))
    for character in bedroom3_info:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    bedroom3_in1 = input("> ")
    if bedroom3_in1 == ("a"):
        nice = ("""
"That's nice of you, %s! Well, anyways, I better get out of bed already."
Your Granddad starts to get up.

"What say we go over to the Lab and have a little chat?"

You nod in agreement.

""" % (myPlayer.name))
        for character in nice:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        moved = ("""
You have moved to lab.""")
        for character in moved:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        lab_chatting()
    elif bedroom3_in1 == 'b':
        ask = ("""
"Hmm? Well, you say you want to ask me a question? Ask away!"



[a] - "What are you working on?"
[b] - "Why do you have books on time travel?"
\n""")
        for character in ask:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        print("we got til here")
        ask_input_1 = ("> ")
        if ask_input_1.lower() == 'a':
            path2()
            print("did we get here?")

        elif ask_input_1.lower() == 'b':
            path1()



def lab_chatting():
    time_machine = colored("""handheld time machine""", "red", attrs=['bold'])
    working_on = ("""
"Do you know what I'm working on?"



[y] - Yes
[n] - No\n\n\n""")
    for character in working_on:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    working_in = input("> ")
    if working_in.lower() == ("n"):
        no = ("""
Your Granddad chuckles.

Granddad opens the shelf and takes out an object. It looks like the game-
console-looking thing.


"This is a %s." """ % (time_machine))
        for character in no:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        time.sleep(3)
        next()

    elif working_in.lower() == ("y"):
        yes = ("""
"Wow, really? And I thought I was being secret about it."

Your Granddad chuckles.

Granddad opens the shelf and takes out an object. It looks like the game-
console-looking thing.


"This is a %s." """ % (time_machine))
        for character in yes:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        time.sleep(3)
        next()








def next():
    serious = ("""
"Yes, I'm serious!"

Your Granddad laughs.

"I've been trying this out many times. I don't anymore, though, I'm too old
to travel back through space-time again. And ever since that epidemic occured,
I don't dare exit the house to find new parts."


You have no idea what he's talking about. What epidemic?


                            [c]
                        {continue}

\n""")
    for character in serious:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    serious_in = input("> ")
    if serious_in.lower() == 'c':
        serious2 = ("""
"Ah, of course! You don't know anything about the epidemic yet.
It occured a few months after your birth. Your parents immediately
went out and filed a complaint to the plastic and meat industry."


"Why meat, Granddad? There's nothing wrong with meat, is there?"
\n

                          [c]
                      {continue}\n\n""")
        for character in serious2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        serious2_in = input("> ")
        if serious2_in == 'c':
            meat = ("""
Your Granddad looks at you.


"Meat production is extremely climate-harming." Granddad says.
"for each hamburger you eat, it requires 660 gallons of water, did you know that?
Plus, cows produce a lot of waste and methane, multiply that by 200 cows in each farm.
We're not even supposed to be eating meat. Our intestines are meant for eating plants.
Farming a lot of cows also produces sicknesses, so antibiotics are used. But that increases
the chance of creating a superbug, an antibiotic-resistant virus that could plague the world.
So, naturally, your mom and dad, who were vegans, like me, went against the meat industry.\n
Meat production also creates a greenhouse gas 296x more dangerous that Co2, Nitrous Oxide.

                         [c]
                      {continue}
\n\n\n""")
            for character in meat:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            meat_in = input("> ")
            if meat_in == 'c':
                died = ("""
Granddad sighs.

“They both died from the disease itself, after a few months. You were hardly 1 year old at that time.”
"The environment has gotten so much worse because nobody listened at that time. And now it's so bad
that even I can't have created a gadget to help the world."\n\n
""")
                for character in died:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                time.sleep(3)
                os.system('clear')
                stringy = ("")
                if myPlayer.gen == 'boy':
                    stringy = ("m'boy")
                elif myPlayer.gen == 'girl':
                    stringy = (myPlayer.name)
                brainwave = ("""
"Why don't we go back and prevent the disease from being created by using the time machine, Granddad?"

Your Granddad looks at you.

"I would love to do that, %s, but I'm too old to travel through time anymore. If I do, there is a
risk that my molecular structure would get mixed up before I got there."



"Then why don't I do it?"


"It's too dangerous, %s. I wouldn't want to lose you too."


""" % (myPlayer.name, myPlayer.name))
                for character in brainwave:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.07)
                time.sleep(4)
                choice_text = ("""
Make the choice.




[a] - "I can do it."
[b] - Agree, and abandon the idea.
\n""")
                for character in choice_text:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                choice_input = input("> ")
                if choice_input == 'a':
                    sure_message = ("""
"Are you sure, %s? This is very dangerous. Think carefully."


You start to have doubts.



Confirm your choice.


[y] - "Yes"
[n] - "No" \n\n""" % (myPlayer.name))
                    for character in sure_message:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    sure_input = input("> ")
                    if sure_input == 'y':
                        go = ("""
Your Granddad looks at you and sighs.

"I guess." Granddad slowly says.\n """)
                        for character in go:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(3)
                        go2 = ("""
"I don't want you to be in danger, but..."

Granddad looks stressed.
\n""")
                        for character in go2:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.08)
                        time.sleep(4)
                        go3 = ("""
"The time machine is to be handled carefully, it's very delicate."
"It can only be powered by 2 quartz crystals, and can only be
kick-started with equipment of today, so you should mind the power.
If you run out of power, you would be stuck in the past."


Your Granddad reels that off and then looks at you.



"If anything happened to you, your mother would never forgive me."

Granddad chuckles. """)
                        for character in go3:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.07)
                        time.sleep(4)
                        go4 = ("""
"Press the yellow button to travel. Spin the dial to adjust the year. Those are the
basics."


Granddad puts his arm on your shoulder.

"Good luck, %s."\n\n\n""" % (myPlayer.name))
                        for character in go4:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.06)
                        time.sleep(5)
                        go5 = ("""
You set the dial for 2019.





"Come back, okay?" Granddad says.



Type in 't' to travel. """)
                        for character in go5:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.07)
                        input_time = input("> ")
                        if input_time.lower() == 't':
                            initiated = colored("""
\n\nTime travel initiated.""", "red", attrs=['bold'])
                            for character in initiated:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.05)
                            time.sleep(2)
                            cprint("""
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||""", "red", attrs=['reverse', 'bold', 'blink'])
                            time.sleep(5)
                            os.system('clear')
                            game_true()
                elif choice_input == 'b':
                    phew = ("""
"Phew," your Granddad sighs. "It's a good thing you didn't want to risk your life
on a dangerous mission like that one."

You walk out of the room, feeling a little curious about that time travel device.""")
                    myPlayer.loc = 'lab'
                    time.sleep(5)
                    prompt()







    while serious_in.lower not in ['c']:
        hmm = ("""
Hmm, that didn't seem to be an option.\n""")
        for character in hmm:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(2)
        next()
def path1():
    bookstimetravel = ("""
"It has to do with the thing that I'm working on. Would you like to see it?"

Your Granddad says.


You nod your head.\n""")
    for character in bookstimetravel:
        sys.stdout.write(character)
        sys.stdout.write()
        time.sleep(0.05)
    time.sleep(3)
    lab_chatting()
def path2():
    lab_goto = ("""
"We can talk about this in the lab. What I'm working on is also in the
lab." \n
You nod in agreement.""")
    for character in lab_goto:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(3)
    lab_chatting()



def game_true():
    welcome_2019 = ("""
Welcome to 2019.
You are in a room.

Wait, a room? This seems to be a holo-room. There are no doors. On the screen there is a list of 10 countries.

You find a memo attached to the time-machine, saying "You will emerge in a room, but this is just a function I implimented
so that you can travel all over the world. More details are availible in the time machine. Press the green button."






                                                Press green button.

                                                       [g]
                                                                     \n""")
    for character in welcome_2019:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    input_game = input("> ")
    if input_game == ("g"):
        g_details = ("""
You press the green button.

The screen says : "loading space-time portal email system."





It's finished loading. There is a message saying:




Hey there, %s! This is the space-time portal email system. Welcome to 2019!


There is a message from Granddad.



"Dear %s,


You must be quite confused. This is a holo-room I created to make my time-traveling
easier. You see the countries on the screen? These are the countries creating the most environmental damage.
You must use your knowledge of electronics to create a machine that will help solve the problem of these countries.


This holo-room was designed so I could travel anywhere, but since you're using it, I used remote settings to
change it from all countries to countries affecting the climate the most.



Try to stop the meat and dairy industry as well, otherwise, the disease might still be there.


Good luck." \n\n\n\n\n\n\n\n\n\n\n\n\n\n
You look at the screen.""" % (myPlayer.name, myPlayer.name))
        for character in g_details:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)
        time.sleep(3)
        prompt_game()



def prompt_game():
    check()
    if myPlayer.easy == False:
        print("""
{Time Machine Virtual Room}


{Welcome, %s! This is the Virtual Room. Your chosen countries are below.}




Countries (by most polluting first):

1. ����� - Locked
2. ��� - Locked
3. India - Locked
4. Russia - Locked
5. Japan - Locked



Countries are sorted with pollution by C02 emissions.


Type in the number of the country you would like to go to.
""" % (myPlayer.name))
        input_prompt_game = input("> ").lower().strip()
        if input_prompt_game == "5":
            os.system('clear')
            time.sleep(1)
            touch = ("""
You touch the little tab marked 'Japan'.



Suddenly, the room whirres.""")
            for character in touch:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.07)
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            Japan()
        elif input_prompt_game == "4":
            os.system('clear')
            touch9 = ("""

You touch 'Russia'.

The room whirres into action.""")
            for character in touch9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.07)
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            russia()
        elif input_prompt_game == "3":
            touch8 = ("""

You touch 'India'.

The room blurres, then flashes.""")
            for character in touch8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.07)
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            india()
    elif myPlayer.easy == True and myPlayer.medium == False:
        print("""
{Time Machine Virtual Room}


{Welcome, %s! This is the Virtual Room. Your chosen countries are below.}




Countries (by most polluting first):

1. China
2. USA
3. India
4. Russia
5. Japan



Countries are sorted with pollution by C02 emissions.


Type in the number of the country you would like to go to.

""" % (myPlayer.name))
        input_prompt_game = input("> ").lower().strip()
        if input_prompt_game == "2":
            os.system('clear')
            touch7 = ("""
You touch 'USA'.

The holo-room blinks and fizzles out.""")
            for character in touch9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.07)
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            USA()
        elif input_prompt_game == "1":
            touch8 = ("""

You touch 'China'.

There's a whirr, and then a click.""")
            for character in touch8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.07)
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            China()
    elif myPlayer.easy and myPlayer.medium == True:
        results_end()



def check():
    global Japan_done
    global Russia_done
    global saudi_done
    global USA_done
    global ger_done
    global japan_done
    global russia_done
    global india_done
    if Japan_done and Russia_done and india_done == True:
        myPlayer.easy = True
        prompt_game()
    if myPlayer.easy and USA_done and ger_done == True:
        if message == False:
            meanwhile_future1 = ("""
    Meanwhile, in the future...""")
            for character in meanwhile_future1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            meanwhile_future2 = ("""
    Granddad turns on his green office chair, worried.


    He turns around to his cabinet, where he keeps a newspaper collection with sunday comics.
    On the news, something has changed.


    The headline is now 'Dr. John Osman invents energy generator.'


    Granddad smiles.""")
            for character in meanwhile_future2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            message = True
        else:
            myPlayer.medium = True
            prompt_game()

def USA():
    os.system('clear')
    USA_text = ("""
The time machine has transported you to the USA.

Would you like to [explore] the area, or [build] the machine?

""")
    for character in USA_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    USA_input = input("""> """).lower().strip()
    if USA_input == 'explore':
        explore_USA()
    elif USA_input == 'build':
        build_USA()

def build_USA():
    while energy > 0:
        build_USA_text = ("""
To build a machine you must find the sources of pollution.""")
        for character in build_USA_text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.08)
        build_USA_text_2 = ("""
You must navigate %s to the sources of pollution.\n""" % (myPlayer.name))
        for character in build_USA_text_2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.08)
        time.sleep(3)
        continue_USA = input("Enter to continue")
        USA_game()
def USA_game():
    global USA_done
    global source1
    global source2
    global source3
    os.system('clear')
    if source1 and source2 and source3 == False:
        print("""
You are standing in a clearing.

Using soil pollution level measuring, a trail of contamination leads to the right.

Which direction would you like to go?

i.e. right, left, straight. OR r, l, s.\n\n""")
        direction = input("> ").lower().strip()
        if direction == 'right':
            os.system('clear')
            print("""
You follow the trail of pollution to a intersection in the woods. The trail is getting stronger.

It seems to be leading forward, but there is also slight residue leading to the right in drops.

Which way would you like to go?""")
            direction_2 = input("> ").lower().strip()
            if direction_2 == 'forward':
                os.system('clear')
                print("""
You walk along.

There is a pipe here. It seems to run from a factory nearby. It's leaking and dripping into the ground.
You seal it up, then drop a letter to the factory.

Congratulations! You have found 1 source of pollution!""")
                source1 = True
                time.sleep(6)
                USA_game()
            else:
                energy -= 1
                print("""
You walk along, but this doesn't seem to be the right way. The trails completely disappear after a awhile
and you must backtrack out.

You lost one energy point. You have %d remaining.""" % (energy))
                time.sleep(5)
                USA_game()
        else:
            energy -= 1
            print("""
You walk along, but this doesn't seem to be the right way. The trails completely disappear after a awhile
and you must backtrack out.


You lost one energy point. You have %d remaining.""" % (energy))
            time.sleep(5)
            USA_game()

    elif source1 and source2 == True and source3 == False:
        print("""
The time machine has teleported you into a river. Luckily it has also built a shield bubble around you.

There is a section in the water that is not as clear. Well, time to find its pollution source.


It's leading to the left (south). Which way would you like to go? (r, l, f)


                    N
                    |
            <-- W---|---E
                    |
                    S




""")
        in_source3 = input("""> """).lower().strip()
        if in_source3 == 'l':
            print("""
You follow the pollution by running in your bubble shield, but the pollution is spreading.
It's harder to tell which way it's coming from now. You think it's coming from the left (East).
But there's also a possibility that it's coming from the right (West)
Which way would you like to go? (r, l, f)


                    N
                    |
                W---|---E
                    |
                    S
                   \\/


""")
            in_source3 = input("""> """).lower().strip()
            if in_source3 == 'l':
                print("""
It seems to be right. The pollution is getting stronger. I think you're close.
Now it is so widespread, all directions are covered with pollution.
The areas marked with '@' are areas with pollution.


|-----------------------------------------------------------------------------|
|                                    N                                        |
|                                                                             |
|                                   @@@@@         @@@@@@@                     |
|                                                     @@@@@   @@@@@@          |
|W     @@@@@@@@@@@@@@@@@@                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@E|
|      @@@@@@@@@@@@            @@@@@      @@@@@@@@     @@@@@@@@@@             |
|                                                                             |
|                                      @@                                     |
|                                    S                                        |
|-----------------------------------------------------------------------------|

Where do you think the pollution is coming from?

(n/w/s/e)

""")
                in_source3 = input("""> """)
                if in_source == 'e':
                    print("""
Congratulations! You have found the source of water pollution. It's coming from the outlet pipe of a factory.
From the bubble shield, you invent a water purifier that doesn't require any filters and can be used forever.
You implant it on the outlet pipe, and the water that rushes out is not polluted anymore. You then drop
another letter, to the factory once you've gotten out, and your job is done!



You have completed this country.\n""")
                    USA_continue = input("""Enter to continue""")
                    USA_done = True
                    prompt_game()

    elif source1 == True and source2 and source3 == False:
        print("""
You walk out of the woods, and go out, only to find yourself in another clearing. It's a different one.
Don't worry about getting out, the time machine can do that. Just find the sources of pollution and see.



There is no visible trail of soil pollution. However, the air pollution is quite high. There is smog
coming from a certain direction. You check your compass. North.


You are facing west. Which way do you go? [r]ight, [l]eft, or [f]orward?


                    N
                    |
            <-- W---|---E
                    |
                    S

""")
        in_source2 = input("> ").strip().lower()
        if in_source2 == 'r':
            print("""
Correct! You follow the smog rising from a chimney. You are now facing north, but you seem to have gone too far.
The smog is now rising from the east. Which way do you go?

                    ^
                    |

                    N
                    |
                W---|---E
                    |
                    S
""")
            in_source22 = input("> ").strip().lower()
            if in_source22 == 'r':
                print("""
You found the source of pollution! It's coming from a factory chimney. You use the time machine to teleport
yourself up there and put a filter over the chimney. Should last for a year. After you get down, you leave a letter
at their mailbox and a parcel with the energy generator from India.

Good job! You found the 2nd source of pollution!""")
                time.sleep(6)
                source2 = True
                USA_game()
            else:
                energy -= 1
                print("""
You walk along, but this doesn't seem to be the right way. The smoke completely disappear after a awhile
and you must backtrack out.


You lost one energy point. You have %d remaining.""" % (energy))
                time.sleep(5)
                USA_game()
        else:
            energy -= 1
            print("""
You walk along, but this doesn't seem to be the right way. The smoke completely disappear after a awhile
and you must backtrack out.


You lost one energy point. You have %d remaining.""" % (energy))
            time.sleep(5)
            USA_game()




def China():
    China_text = ("""
You are in China. A soft breeze blows.


Would you like to [explore] the area or [help] the country?

""")
    for character in China_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    in_ger = input("> ")
    if in_ger == 'explore':
        ger_explore = ("""
You seem to be in Haerwusu, a town that has the biggest coal mine in China.

Would you like to explore the [water] or go [back]?\n\n\n""")
        for character in ger_explore:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        input_ger_explore = input("> ")
        if input_ger_explore == 'water':
            ger_explore_water = ("""
There is a puddle nearby. Looks like it just rained.

Wow, this water is acidic! It must be acid rain from coal plants.""")
            for character in ger_explore_water:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(4)
            China()
        elif input_ger_explore == 'back':
            China()
    elif in_ger == 'help':
        help_ger()

def help_ger():
    global energy
    os.system('clear')
    build_China = ("""
To help the country, you must find an alternative to coal power. Follow the trail of coal left from the
trucks to the mine, then see if you can invent something.

You have limited energy, so if you do something wrong, it'll cost you a lot.\n\n\n""")
    continue_ger = input("Enter to continue")
    cprint("Start.", "green")
    energy = 10
    ger_game()


level = 1
def ger_game():
    global energy
    os.system('clear')
    while energy > 0:
        if level == 1:
            print("""
You don't seem to know where to go, but the time machine does. It just needs you to
answer a question, because the sattelites connected to the machine near China don't
exist yet.



{Where are we?}
{Please enter a city or town name}

""")
            input_machine = input("""> """).lower().strip()
            if input_machine == 'haerwusu' or 'haewursu' or 'haewusu':
                print("""
Correct! The machine clicks and leads you for a little bit, but then fails to use the modern GPS.
Well, you're on your own now. There are bits of black rock on the street. Hmm... Haerwusu has a mine,
but what type is it? [c]oal mine, or [d]iamond mine?\n\n""")
                input_machine = input("> ").lower().strip()
                if input_machine == 'c':
                    print("""
You're correct again! You follow the trails until they disappear completely. Now what? You didn't bring
your Chinese translator. But you have the time machine...

It's still on the fritz. It cannot locate you. But it can translate. It just needs a language.

Enter a language into the time machine.\n\n""")
                    input_machine = input("""> """).lower().strip()
                    if input_machine == 'chinese':
                        print("""
You translate the sign.

'Coal Mine : 20 kilometers.'

That's quite far. You could use the time machine to teleport, but it cannot locate you. You could end
up in America if you tried it.

It might need a continent to check as well. Enter the continent China is located in.
\n""")
                        input_machine = input("""> """).lower().strip()
                        if input_machine == 'asia':
                            print("""
Now it works. It teleports you to the coal plant. Hooray!\n\n""")
                            input_continue = input("enter to continue")
                            level = 2
                            ger_game()
                        else:
                            print("""
Hmm... That didn't seem right. As you enter it, the machine doesn't agree and teleports you back where you
started. Too bad.""")
                            time.sleep(5)
                            energy -= 1
                            ger_game()
                    else:
                        print("""
Um, that's probably not Chinese. The time machine was not able to translate, and glitched, causing it to teleport
you back to where you started. Too bad.""")
                        energy -= 1
                        ger_game()
            else:
                os.system('clear')
                print("""
Hmm, that doesn't seem to be right. Are we even in China?""")
                time.sleep(4)
                energy -= 1
                ger_game()
        if level == 2:
            if energy > 5:
                os.system('clear')
                print("""
You have reached the coal mine!

Your energy : %d

You were able to think up a small portable wind power generator and left it at the front door of
the coal mine, with a note to the workers to send this to the power plant instead of coal. You 
wrote another note inside the machine saying to use this instead of burning coal. Good job! You've
completed this country.""" % (energy))
                ger_done = True
                time.sleep(3)
                prompt_game()
            elif energy < 5:
                os.system('clear')
                print("""
You have reached the coal mine!

Your energy : %d

You weren't able to think up an idea for a machine to produce power, because you were so tired.
Too bad, you failed.""" % (energy))
                time.sleep(7)
                prompt_game()
def explore_USA():
    os.system('clear')
    USA_explore = ("""
What would you like to examine first? The [air]?
Or would you like to go [back]?

""")
    for character in USA_explore:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    in_explore_USA = input("> ").lower().strip()
    if in_explore_USA == 'air':
        air_USA = ("""
Well, I'll be. The air pollution here is very high. You've read before that most of the
air pollution here is caused by burning fossil fuels.""")
        for character in air_USA:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        explore_USA()
    elif in_explore_USA == 'back':
        USA()
def india():
    os.system('clear')
    india_text = ("""
You are in India.

Some sand blows by. It's quite dusty.

Would you like to [explore] the area, or [build] the machine?\n\n\n\n\n""")
    for character in india_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    india_input = input("> ").lower().strip()
    if india_input == 'explore':
        explore_india()
    elif india_input == 'build':
        build_india()
def build_india():
    os.system('clear')
    build_india_text = ("""
To build a machine you must know how to connect the circuits properly.\n\n""")
    for character in build_india_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    time.sleep(3)
    inputty = input(colored("Enter to continue", "red"))
    os.system('clear')
    print("""
HOW TO PLAY:

Type in 'move', wait for the prompt, then type in the coordinates of the wire you would
like to move. (please note: do not make any spaces in your coordinate commands, the program may
fail.)

Just enter the coordinates, the time machine will correct the wires.
If the program tells you that you touched a wrong wire, it means you're not meant to move that one or
it just doesn't exist.

Zero (0) represents the map area.
One (1) represents a movable piece.
Four (4) represents an immovable piece. Never attempt to move these, you'll just end up electrocuting
yourself.



Please adjust the wires layer-by-layer, as not to break the game.

                                       +
Move the wires to connect the 'plus' + + +
                                       +

To the 'minus' -----



                        000
                      0     0
                       0   0
                        000
                        | |
Through the 'lightbulb' \\/


""")
    time.sleep(5)
    inputty = input(colored("Enter to start", "red"))
    os.system('clear')

    circuit_builder()



def circuit_builder():
    global map_electric
    global a1
    global a2
    global a3
    global a4
    global a5
    global b1
    global b2
    global b3
    global b4
    global b5
    global c1
    global c2
    global c3
    global c4
    global c5
    global d1
    global d2
    global d3
    global d4
    global d5
    os.system('clear')
    print(map_electric)
    print("""
What would you like to do? (move/reset)\n\n""")
    input_india_main = input("""> """)
    if input_india_main == 'reset':
        a1 = False
        a2 = False
        a3 = False
        a4 = False
        a5 = False
        b1 = False
        b2 = False
        b3 = False
        b4 = False
        b5 = False
        c1 = False
        c2 = False
        c3 = False
        c4 = False
        c5 = False
        d1 = False
        d2 = False
        d3 = False
        d4 = False
        d5 = False
        map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111                                            +      0
       A        0  1                    4444444444444444444444444  + + +    0
                0  1        1111111111114                            +      0
                0  11111111                                                 0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
        circuit_builder()

    elif input_india_main == 'move':
        print("""
Which coordinate would you like to move?
Answer in coordinates (i.e. c3, d2)
""")
        coordinate_in_india = input("> ")
        if coordinate_in_india == 'a1':
            print("Circuit coordinate : A-1 corrected.")
            a1 = True
            time.sleep(3)
            if a2 == False:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111111   1                                     +      0
       A        0  1       1   1        4444444444444444444444444  + + +    0
                0  1       1   1        4                            +      0
                0  1           1                                            0
                0--1------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                circuit_builder()

            elif a2 == True:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111111                                         +      0
       A        0  1       1            4444444444444444444444444  + + +    0
                0  1       11111111111114                            +      0
                0  1                                                        0
                0--1------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                circuit_builder()

        elif coordinate_in_india == 'a2':
            print("Circuit coordinate : A-2 corrected.")
            a2 = True
            time.sleep(3)
            if a1 == False:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111                                            +      0
       A        0  1                    4444444444444444444444444  + + +    0
                0  1        1111111111114                            +      0
                0  11111111                                                 0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                circuit_builder()

            elif a1 == True:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111111                                         +      0
       A        0  1       1            4444444444444444444444444  + + +    0
                0  1       11111111111114                            +      0
                0  1                                                        0
                0--1------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                circuit_builder()


        elif coordinate_in_india == 'a3':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()

        elif coordinate_in_india == 'a4':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'a5':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()


        elif coordinate_in_india == 'b2':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'b3':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'b4':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'b5':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'c1':
            print("""Circuit coordinate : C-1 corrected. """)
            c1 = True
            time.sleep(3)
            if a1 == True:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111111   1                                     +      0
       A        0  1       1   1        4444444444444444444444444  + + +    0
                0  1       1   1        4                            +      0
                0  1           1                                            0
                0--1------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0--1------------------------------------------------------- 0
                0  1                                                        0
                0  1                                                        0
       C        0  1                                                        0
                0  11111111144444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            if a1 and a2 == True:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111111                                         +      0
       A        0  1       1            4444444444444444444444444  + + +    0
                0  1       11111111111114                            +      0
                0  1                                                        0
                0--1------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0--1------------------------------------------------------- 0
                0  1                                                        0
                0  1                                                        0
       C        0  1                                                        0
                0  11111111144444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                circuit_builder()

        elif coordinate_in_india == 'c2':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'c3':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'c4':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'c5':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'd1':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'd2':
            print(c1)
            print("Circuit coordinate : D-2 corrected")
            time.sleep(3)
            if a1 == True and a2 and c1 == False:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111111   1                                     +      0
       A        0  1       1   1        4444444444444444444444444  + + +    0
                0  1       1   1        4                            +      0
                0  1           1                                            0
                0--1------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  4444444441111111111                                  4   0
                0  4                 1                                  4   0
                0  4                 1                                  4   0
                0  4                 444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                circuit_builder()
            if a2 == True and c1 and a1 == False:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111                                            +      0
       A        0  1                    4444444444444444444444444  + + +    0
                0  1        1111111111114                            +      0
                0  11111111                                                 0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  4444444441111111111                                  4   0
                0  4                 1                                  4   0
                0  4                 1                                  4   0
                0  4                 444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                circuit_builder()
            if a1 and a2 == True and c1 == False:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111111                                         +      0
       A        0  1       1            4444444444444444444444444  + + +    0
                0  1       11111111111114                            +      0
                0  1                                                        0
                0--1------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0                              44444444444444444444444444   0
                0  4444444441111111111                                  4   0
                0  4                 1                                  4   0
                0  4                 1                                  4   0
                0  4                 444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                circuit_builder()
            if c1 == True and a1 and a2 == False:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0--1------------------------------------------------------- 0
                0  1                                                        0
                0  1                                                        0
       C        0  1                                                        0
                0  11111111144444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  4444444441111111111                                  4   0
                0  4                 1                                  4   0
                0  4                 1                                  4   0
                0  4                 444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                circuit_builder()
            if c1 and a1 and a2 == True:
                map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111111                                         +      0
       A        0  1       1            4444444444444444444444444  + + +    0
                0  1       11111111111114                            +      0
                0  1                                                        0
                0--1------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0--4------------------------------------------------------- 0
                0  1                                                        0
                0  1                                                        0
       C        0  1                                                        0
                0  11111111144444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0                              44444444444444444444444444   0
                0  4444444441111111111                                  4   0
                0  4                 1                                  4   0
                0  4                 1                                  4   0
                0  4                 444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
                india_results()







        elif coordinate_in_india == 'd3':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'd4':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()
        elif coordinate_in_india == 'd5':
            print("""\nOops! You seem to have touched a wrong wire. You get electrocuted, but it isn't fatal.
During the shock though, you seem to have batted away the other wires. You're gonna have to start over again.""")
            time.sleep(6)
            map_electric = ("""



                    1          2           3            4           5

                0000000000000000000000000000000000000000000000000000000000000
                0  111111      1                                     +      0
       A        0  1           1        4444444444444444444444444  + + +    0
                0  1           1        4                            +      0
                0  11111111    1                                            0
                0---------------------------------------------------------- 0
                0  4                                                        0
                0  4                                                        0
       B        0  4                                                        0
                0  4                                                        0
                0---------------------------------------------------------- 0
                0  11111111                                                 0
                0  1                                                        0
       C        0  1                                                        0
                0  1        44444444444444444444                            0
                0------------------------------4--------------------------- 0
                0                              44444444444444444444444444   0
                0  444444444 111111111                                  4   0
                0  4         1                                          4   0
                0  4         1                                          4   0
                0  4         1       444            000                 4   0
       D        0  4                   4           0   0                4   0
                0  4                   4            000                 4   0
                0  4                   4444444444444| |444444444444444444   0
                0  4                                \\/                      0
                0  -----                                                    0
                0                                                           0
                0000000000000000000000000000000000000000000000000000000000000




""")
            circuit_builder()







def india_results():
    global mrjohn_yes
    results_india = ("""
You have completed the circuit! The light bulb glows, and that means your new power source alternative
works. Now, to find someone to present it to.""")
    for character in results_india:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(3)
    if mrjohn_yes == False:
        results_india2 == ("""
Hmm... Maybe explore the city, then see if you can find anyone...

Once you think you've found the right person, simply type [present] into the India main menu.
(This will not show as an option, but it will work.)\n\n\n""")
        for character in results_india2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(4)
        india()
    elif mrjohn_yes == True:
        india_results2()

def india_results2():
    if mrjohn_yes == True:
        results_india2 = ("""
Hmm... What about Mr. John?

That seems like a good idea. Let's call him.

You check the time machine. As usual, it doesn't disappoint you. A phone icon pops up with a loading bar.

Enter to continue.""")
        for character in results_india2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        continue_india = input("")
        results_india4 = ("""
'Please enter the number you would like to call.' says the time machine.


[look] at Mr. John's business card, or [enter] a number.\n""")
        print(results_india4)
        input_phone = input(">")
        if input_phone == 'look':
            business_card = ("""
|------------------------------------------------|
|                                                |
|               John Osman, PhD.                 |
|                                                |
|      Mechanical engineering professor at       |
|           King Abdulaziz University.           |
|                                                |
|                012-124-5268                    |
|------------------------------------------------|


               [enter] to exit""")
            input_business = input("")
            os.system('clear')
            print(results_india4)
            input_phone = input(">")
            if input_phone == 'enter':
                phone = ("""
Enter the phone number you wish to call (without dashes)""")
                for character in phone:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                phone_in = input("> ")
                if phone_in == '0121245268':
                    mrjohn = ("""
"Hello, this is John Osman speaking. Who is this?"

"Hello, Mr. John! It's me, %s!"

"Ah, hello, %s! What are you calling for?"


"I was wondering if you can do me a favor, Mr. John."



"Of course. What would it be?"

"Could you tell the other teachers about the energy generator prototype that I made?"






"You made an energy generator?"


"Yes, Mr. John."

"Does it use up any resources?"

"No, sir."




"But... There's no such thing as a non-resource energy generator. You invented it?"

"Yes, sir."

"Okay... Where can I pick it up? I may need the real thing."

"Can I mail it to you? Express mailing, maybe?"

"Sure."


Mr. John has ended the call.""" % (myPlayer.name, myPlayer.name))
                    for character in mrjohn:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.07)
                    time.sleep(3)
                    os.system('clear')
                    wait_india = ("""
You send the generator and wait for the response from Mr. John.

He calls you at 4 PM.


"%s, this energy generator is nothing like I've ever seen. I've showed it to the other professors
and they all agree that this is like a miracle of engineering. You really must attend our college when you grow up."

"Sorry, Mr. John, but I don't live here. I live in America."

"... Well, that's too bad. But maybe when you grow up, then. By the way, may I take your project and present it to
the government?"

"Of course, sir."

"Well, good luck on your path, %s. I hope that we can meet again."



Mr. John has ended the call.


You have completed this country.""")
                    for character in wait_india:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.07)
                    time.sleep(5)
                    saudi_done = True
                    prompt_game()


def explore_india():
    global mrjohn_yes
    explore_india1 = ("""
Some sand blows right onto the screen of your handheld time machine.

You wipe it off.

From your surroundings, you seem to be around the outskirts of New Delhi,
India's capital. No problem traveling to the city to get supplies, then.

Would you like to examine the [soil] nearby, go to the [city], or go [back]?""")
    for character in explore_india1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    input_exploreindia1 = input("> ").lower().strip()
    if input_exploreindia1 == 'soil':
        soil_india = ("""
As soon as you bring the time machine near the soil hoping for it to be able to scan it from there,
an apparatus extends out from the machine. It goes into the soil.

From the readings it seems that this soil is contaminated with waste. Hmm...""")
        for character in soil_india:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)
        time.sleep(5)
        explore_india()
    elif input_exploreindia1 == 'city':
        city_india = ("""
You walk to a nearby farm, where you catch a taxi and go to the city. The driver seems confused when you
hand him your holo-coins, but accepts them.

Now, time to ask some locals.

Enter to continue.\n\n\n""")
        for character in city_india:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        continue_india = input("")
        if myPlayer.gen == "boy":
            nickname = ", young man"
        elif myPlayer.gen == 'girl':
            nickname = ", little girl"
        elif myPlayer.gen == 'child':
            nickname = ''
        city_india2 = ("""

There is a nice-looking man nearby. You strike up a conversation. Hopefully he can speak English.

"Well, hello there%s! What brings you here?" He replies in a friendly manner.


[a] - "Oh, nothing. Just traveling, sir. I wanted to meet some of the locals here."
[b] - "I'm looking for some locals to answer some of my questions, sir."

""" % (nickname))
        for character in city_india2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        input_city_india = input("> ").lower().strip()
        if input_city_india == 'a':
            city_india_a = ("""
"That's nice. Well, my name is Mr. John. What's yours?"

"%s, sir. Say, will you answer some questions for me, Mr. John?"

"Of course!"


Enter to continue. \n\n\n\n""" % (myPlayer.name))
            for character in city_india_a:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            city_india_cont = input("")
            city_india_a2 = ("""
"Well, Mr. John, I've heard that this country has met some deadly environmental hazards and
damages the environment a lot as well, by having many vehicles that burn fuel. Is that true?"

Mr. John darkens.

"Well, not to insult my country in any way, but it is true. Traveling the most with cars is
... Well, inefficient." Mr. John says. "But there's no alternative right now. We don't have 
alternative energy" he says. "It also damages the environment. I wish we had an alternative,
but there is nothing else right now."

""")
            for character in city_india_a2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            city_india_end = ("""
A bus arrives.


"Well, that's my bus! It was nice chatting to you, %s."

He hands you a card.

"This is my business card. Whenever you need me, just call, okay?"


He hurries off.

""" % (myPlayer.name))
            for character in city_india_end:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            explore_india()
        elif input_city_india == 'b':
            city_india_b = ("""
"Well, I'm a local, so ask away! My name is Mr. John. What's yours?"

"%s, sir."

"Nice to meet you, %s! Now, what do you want to ask me?"


Enter to continue. \n\n\n\n""" % (myPlayer.name, myPlayer.name))
            for character in city_india_b:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            city_india_cont = input("")
            city_india_b2 = ("""
"Well, Mr. John, I've heard that this country has met some deadly environmental hazards and
damages the environment a lot as well, by having many vehicles that burn fuel. Is that true?"

Mr. John darkens.

"Well, not to insult my country in any way, but it is true. Traveling the most with cars is
... Well, inefficient." Mr. John says. "But there's no alternative right now. We don't have 
alternative energy" he says. "It also damages the environment. I wish we had an alternative,
but there is nothing else right now."


""")
            for character in city_india_b2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            city_india_endb = ("""
A bus arrives.


"Well, that's my bus! It was nice chatting to you, %s."

He hands you a card.

"This is my business card. Whenever you need me, just call, okay?"


He hurries off.

""" % (myPlayer.name))
            for character in city_india_endb:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            mrjohn_yes = True
            explore_india()


    elif input_exploreindia1 == 'back':
        india()


def russia():
    os.system('clear')
    Russia_text = ("""
You are in Russia.


Would you like to [explore] the area, or [build] the machine to help the country?\n
""")
    for character in Russia_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    Russia_input = input("""> """).lower().strip()
    if Russia_input == 'explore':
        explore_Russia()
    elif Russia_input == 'build':
        build_Russia()

def explore_Russia():
    os.system('clear')
    explore_Russia1 = ("""
You seem to be in Moskow.

The air is filled with sound.

It is approximately 10 am.


Would you like to examine the [water] go [back]? \n\n\n\n""")
    for character in explore_Russia1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    input_exploreRussia1 = input("> ")
    if input_exploreRussia1 == 'air':
        air_examine_Russia = ("""
This water is not safe. It's caused by obsolete water treatment plants.

Enter to go back.\n\n\n""")
        input_air = input("")
        russia()
    elif input_exploreRussia1 == 'back':
        russia()
def build_Russia():
    pm25 = ("""
To build a machine you must have data of the environment.""")
    for character in pm25:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(2)
    pm25in1 = input(colored("\nEnter to continue", "red", attrs=['bold']))
    os.system('clear')
    pm252 = ("""
You must click when you see water pollution to collect a sample.""")
    for character in pm252:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    pm25in2 = input(colored("\nEnter to start", "red", attrs=['bold']))
    os.system('clear')
    cprint("Game starts in 5", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 4", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 3", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 2", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 1", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 0", "red", attrs=['bold'])
    time.sleep(1)
    cprint("Start", "red", attrs=['bold'])
    time.sleep(3)
    curses.wrapper(Russia_clicker_game)



def Russia_clicker_game(stdscr):
    global pm25_points, pm25_time, pm25_outof
    stdscr.clear()
    curses.curs_set(0)
    curses.mousemask(1)
    while pm25_time < 7:
        value = randint(0, 1)
        if value == 0:
            stdscr.addstr(0, 0, """
        ______________________________________________________
        |                                                    |
        |               Laser particle sensor                |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |              [No particles detected]               |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |____________________________________________________|

""")
            time.sleep(3)
            curses.wrapper(Russia_clicker_game)
        elif value == 1:
            stdscr.addstr(0, 0, """
        ______________________________________________________
        |                                                    |
        |               Laser particle sensor                |
        |                                                    |
        |                                                    |
        |                   _______                          |
        |                  /       \\                       <-|
        |                 |Pollution|                        |
        |                  \\_______/                       <-|
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                Pollution Alert!                    |
        |                                                    |
        |____________________________________________________|

""")
            key = stdscr.getch()
            if key == curses.KEY_MOUSE:
                _, x, y, _, _ = curses.getmouse()
                if y in range(9, 18) and x in range(4, 54):
                    pm25_points += 1
                    pm25_time += 0.5
                    stdscr.clear()
                    stdscr.addstr(0,0, "Sample collected: Time %d" % (pm25_time))
                    curses.wrapper(Russia_clicker_game)
            else:
                pm25_time += 0.5
                pm25_outof -= 1
    Russia_results()
def Russia_results():
    global pm25_points, pm25_time, pm25_outof
    curses.endwin()
    os.system('clear')
    print("""Complete.""")
    time.sleep(3)
    os.system('clear')
    print("Going to results page in 5")
    time.sleep(1)
    os.system('clear')
    print("Going to results page in 4")
    time.sleep(1)
    os.system('clear')
    print("Going to results page in 3")
    time.sleep(1)
    os.system('clear')
    print("Going to results page in 2")
    time.sleep(1)
    os.system('clear')
    print("Going to results page in 1")
    time.sleep(1)
    os.system('clear')
    print("Going to results page in 0")
    time.sleep(1)
    os.system('clear')
    if pm25_points < 4:
        stringy2 = ("Cool!")
    elif pm25_points < 2:
        stringy2 = ("Bad. Very bad.")
    elif pm25_points == 7:
        stringy2 = ("Perfect!")
    print("""
RESULTS:


You got %d out of 7 samples detected.

%s

Would you like to 'continue' or 'retry'?

""" % (pm25_outof, stringy2))
    cont_retry_Russia = input("> ")
    if cont_retry_Russia == 'continue':
        if pm25_points > 5:
            Russia_done = True
            what_do = ("""
You create a cheap and resource-effective HEPA (high-efficiency particulate arrestance) filter
for companies in Russia to replicate, and put in treatment plants.""")
            for character in what_do:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.07)
            prompt_game()
        elif pm25_points < 3:
            Russia_done = False
            sure = ("""
Are you sure? You haven't done well enough in this country, this will not count as progress.

(y/n)\n\n""")
            for character in sure:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.07)
            sure_input = input("> ")
            if sure_input.lower().strip() == 'y':
                prompt_game()
            elif sure_input.lower().strip() == 'n':
                os.system('clear')
                print("You will be directed to the Virtual Room in a moment...")
                time.sleep(3)
                prompt_game()
    if cont_retry_Russia == 'retry':
        print("You will be directed to Russia in a moment...")
        time.sleep(3)
        build_Russia()












def Japan():
    Japan_text = ("""
You are in Japan.


A soft breeze hits your face.



Would you like to [explore] the area, or [build] the machine to help the country?\n
""")
    for character in Japan_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    Japan_input = input("""> """).lower().strip()
    if Japan_input == 'explore':
        explore_Japan()
    elif Japan_input == 'build':
        build_Japan()

def explore_Japan():
    explore_Japan1 = ("""
You walk around. You seem to be in Tokyo.


A Japanese man walks by.


Should you test the [air] first?\n\n\nOr, type in [back] to return to the options screen.
""")
    for character in explore_Japan1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    input_exploreJapan1 = input("> ")
    if input_exploreJapan1 == 'back':
        Japan()
    elif input_exploreJapan1 == 'air':
        measure = ("""
There is a function to measure air in the time machine. Quite thoughtful, Granddad.

Type in 'measure' to measure.\n\n""")
        for character in measure:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        measure_input_Japan = input("> ").lower().strip()
        if measure_input_Japan == 'measure':
            measured = ("""
You press 'measure'.


The air pollution levels are quite high.

It comes from waste inceneration, I think.


            [back]\n\n\n\n""")
            for character in measured:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            input_back = input("> ").lower().strip()
            if input_back == 'back':
                explore_Japan()
def build_Japan():
    intro_10 = ("""
To build a machine, you must have knowledge of climate change.\n""")
    for character in intro_10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    ques_10 = ("""
You must answer 3 questions about climate change to build a machine.

(Hint. Stuck? [explore] will help you get more info.)\n""")
    for character in ques_10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(3)
    ques_start = input(colored("""Enter to continue """, "red", attrs=['bold']))
    os.system('clear')
    start = colored("""
Start.\n\n\n\n""", "red",  attrs=['bold'])
    for character in start:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(4)
    ques_10_1()













def ques_10_1():
    global perfect
    global questions
    global outof
    global points
    if questions == 1:
        ques_1_10 = ("""
QUESTION 1:


What causes most air pollution in Japan?


[a] - Transportation.
[b] - Waste burning.
[c] - Factory exhaust.
[d] - All of above.

""")
        for character in ques_1_10:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        ques_1_in_10 = input("> ")
        if ques_1_in_10 == 'a':
            if points == 0:
                outof -= 1
                questions = 2
                ques_10_1()
            else:
                questions = 2
                ques_10_1()
        elif ques_1_in_10 == 'b':
            if points == 0:
                points += 1
                questions = 2
                ques_10_1()
            else:
                questions = 2
                ques_10_1()
        elif ques_1_in_10 == 'c':
            if points == 0:
                points -= 1
                questions = 2
                ques_10_1()
            else:
                questions = 2
                ques_10_1()
        elif ques_1_in_10 == 'd':
            if points == 0:
                points -= 1
                questions = 2
                ques_10_1()
            else:
                questions = 2
                ques_10_1()

    elif questions == 2:
        ques_2_10 = ("""
QUESTION 2:

What does the term 'Climate Change' mean?

[a] - The warming of the planet
[b] - The sea's acidification
[c] - More people in a room
[d] - Neighbors moving in
[e] - A and B, etc.
[f] - None of above.\n\n\n""")
        for character in ques_2_10:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        ques_2_in_10 = input("> ")
        if ques_2_in_10 == 'a':
            if points == 1:
                outof -= 1
                points -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
        elif ques_2_in_10 == 'b':
            if points == 3:
                points -= 1
                outof -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
        elif ques_2_in_10 == 'c':
            if points == 1:
                points -= 1
                outof -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
        elif ques_2_in_10 == 'd':
            if points == 1:
                points -= 1
                outof -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
        elif ques_2_in_10 == 'e':
            points += 1
            questions = 3
            ques_10_1()
        elif ques_2_in_10 == 'f':
            if points == 1:
                outof -= 1
                points -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
    elif questions == 3:
        ques_3_10 = ("""
QUESTION 3:


What causes the pollution of water?

[a] - Acid rain
[b] - Dirt
[c] - Rocks
[d] - None of above\n\n\n\n\n\n\n\n""")
        for character in ques_3_10:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        ques_1_in_10 = input("> ")
        if ques_1_in_10 == 'a':
            points += 1
            questions = 4
            ques_10_1()
        elif ques_2_in_10 == 'b':
            if points > 0:
                points -= 1
                questions = 4
                ques_10_1()
            else:
                questions = 4
                ques_10_1()
        elif ques_2_in_10 == 'c':
            if points > 0:
                points -= 1
                questions = 4
                ques_10_1()
            else:
                questions = 4
                ques_10_1()
        elif ques_2_in_10 == 'd':
            if points > 0:
                points -= 1
                questions = 4
                ques_10_1()
            else:
                questions = 4
                ques_10_1()
    elif questions == 4:
        os.system('clear')
        if points == 3:
            perfect = True
            line = ("Congratulations! You won.")
        elif points == 2:
            perfect = False
            line = ("Good job.")
        elif points == 1:
            perfect = False
            line = ("You could have done better.")
        score_print = ("""

You have completed the questions.



This is your score : %d

You got %d out of 3 questions correct.

%s


Would you like to [retry] or [continue]?



FUN FACT: "It's only one straw" said by one million people (= 1 million straws.)
          Do you want to be one of them, or not

""" % (points, outof, line))
        for character in score_print:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        input_score_print = input("> ")
        if input_score_print == 'retry':
            os.system('clear')
            perfect = False
            outof = 5
            points = 0
            questions = 1
            print("Restarting quiz in 5 seconds")
            time.sleep(4)
        elif input_score_print == 'continue':
            if points == 3:
                printer = ("""
You built a solar power generator magnifier design and a prototype for the
government to reproduce, and sent it to them anonymously. It seems they've
realized what they're doing to the environment.


Good job. 9 more to go.\n\n\n""")
                for character in printer:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(3)
                os.system('clear')
                Japan_done = True
                print("[Returning to Virtual Room...]")
                time.sleep(3)
                prompt_game()
            elif points == 2:
                printer = ("""
You built a generator powered by C02 to attach to cars, and sold the designs to the government.

Good job. 9 more to go.\n\n\n""")
                for character in printer:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(3)
                os.system('clear')
                Japan_done = True
                print("[Returning to Virtual Room...]")
                time.sleep(3)
                prompt_game()
            elif points == 1:
                printer = ("""
You struggled, but could not think of something to help the environment, as you don't have
enough data. Sorry, Granddad.

You failed to complete this country. Try again.\n\n\n""")
                for character in printer:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(3)
                os.system('clear')
                Japan_done = False
                perfect = False
                outof = 5
                points = 0
                questions = 1
                print("[Returning to Virtual Room...]")
                time.sleep(3)
                prompt_game()
def results_end():
    global lv
    os.system('clear')
    gj = ("""
Good job, you have completed all countries.""")
    for character in gj:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(5)
    os.system('clear')
    however = ("""
However, you still need to take down the meat and dairy industry.""")
    for character in however:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(5)
    os.system('clear')
    ques_text = ("""
Answer 3 questions to prove your knowledge and take them down.""")
    for character in ques_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(5)
    os.system('clear')
    cprint("""
START.""", "red", attrs=['bold', 'reverse', 'underline', 'blink'])
    time.sleep(3)
    lv = 1
    results_endgame()

def results_endgame():
    global lv
    if lv == 1:
        ques_one = ("""
QUESTION I:

How much water is required to produce a hamburger?

[a] - 546 gallons
[b] - 10 gallons
[c] - 660 gallons
[d] - 340 gallons

""")
        for character in ques_one:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        inques = input("> ").lower().strip()
        if inques == 'c':
            os.system('clear')
            correct = ("""
Correct! A hamburger costs you very little money, but a lot of water! Animal agriculture
is harming the climate a lot - from the food producing - at the start of the line - to the
hamburger in your hands. Cows also produce a lot of methane and waste, waste from a farm of
2500 cows is equal to the waste of a city with 411,000 people!\n\nEnter to continue.""")
            for character in correct:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            continue_end = input("")
            lv = 2
            results_endgame()
        else:
            print("""
That didn't seem to be right. Here's a thought. Granddad mentioned it in the beginning.
And it starts with a even number.""")
            time.sleep(3)
            results_endgame()
    elif lv == 2:
        ques_two = ("""
QUESTION II:

What can create a superbug (antibiotic resistant mutant virus) in factory farming?

[a] - Many doses of antibiotics with animals, kept close with each other
[b] - There's no such possibility - you're mad!
[c] - It just creates itself, it has nothing to do with farming
[d] - I don't know.\n\n""")
        inques = input("> ").lower().strip()
        if inques == 'a':
            os.system('clear')
            correct = ("""
You're correct! Animals in factory farming take the majority of antibiotics produced, and 
take many doses. Because the animals are kept close to each other, the possibility of 
animals being infected is high, and so they are given large doses of antibiotics each day.
This increases the possibility of creating an mutant virus that is resistant to antibiotics,
and that would be fatal to humans.\n\n""")
            for character in correct:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            lv = 3
            results_endgame()
        else:
            os.system('clear')
            print("""
Oops! It seems that's wrong. Well, try again!
Here's some info. What do you think would happen when animals are kept very close together?""")
            time.sleep(3)
            results_endgame()
    elif lv == 3:
        ques_3 = colored("""
QUESTION III:

What is Nitrous Oxide?

[a] - An imaginary superfuel for race cars
[b] - A greenhouse gas 296x more destructive than CO2
[c] - Fuel for toy cars
[d] - Fart gas


""", "red", attrs=['bold'])
        inques = input("> ").lower().strip()
        if inques == 'b':
            os.system('clear')
            alcorrect = colored("""
You are correct! You have pass£ƒ the ƒ©å∂ åç˙´†ˆø˜ß! 
ß©˙∂ƒ≈√∂ßƒΩ©ß´∂ƒΩß∂ƒ©ß©ß©ƒßƒ©ßƒß∂©ß∂©ß∂©˙†˚˚¨ø…ª¨∞§¶£∞§™Ωç≈˜ç√µ√
""", "red", attrs=['bold', 'reverse'])
            correct = ("""
You are correct! You have pass£ƒ the ƒ©å∂ åç˙´†ˆø˜ß! 
ß©˙∂ƒ≈√∂ßƒΩ©ß´∂ƒΩß∂ƒ©ß©ß©ƒßƒ©ßƒß∂©ß∂©ß∂©˙†˚˚¨ø…ª¨∞§¶£∞§™Ωç≈˜ç√µ√
""")
            print(correct)
            time.sleep(5)
            os.system('clear')
            print(alcorrect)
            time.sleep(5)
            os.system('clear')
            cprint("""
EXTR4 QUES710N


HOW POLLUTING IS MEAT PRODUCTION?!

[a] - NOT DANGEROUS
[b] - PERFECTLY SAFE
[c] - åµåΩˆ˜©¬¥ å∑´ßøµ´
[d] - QUITE POLLUTING

ÍÓ©Œ£∞Ó∑ı®´ÁÔ¨ÎÓ˜Ï©Ô§ˆ®¨ÏÁ†

""")
            inques = input(""">>> """).lower().strip()
            if inques == 'd':
                print("""
Correct! The time machine glitched out for a moment there, it's back to normal now.


Congratulations! You have completed the game! Type [return] to return to the future.

""")
                input_done = input("> ").lower().strip()
                if input_done == 'return':
                    ending()
                else:
                    os.system('clear')
                    print("""
You didn't type 'return', but I'll take that as a 'return'. Seeya!""")
                    time.sleep(5)
                    ending()
        else:
            print("""
That's not correct! Try again.""")
            time.sleep(4)
            results_endgame()
def ending():
    os.system('clear')
    ending = ("""
You zap back to the future, and go back to the location that you were before you traveled, but it's not
the same. You're supposed to be in the lab, but instead, you're in some sort of... hangar?

There are a few planes here. A small table sits at the far end, with a solder, some papers, and a computer. 
Everything seems so... different. You wonder what happened.

""")
    for character in ending:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    input_cont_end = input("Enter to continue")
    ending2 = ("""
There is a door right behind you. You near it, and it hisses open. Now this is familiar.
You seem to be looking at the corridor. The stair is gone, replaced by a shiny hydraulic lift.
And coming up it is... Granddad?


""")
    for character in ending2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    input_cont_end = input("Enter to continue")
    ending3 = ("""
Granddad has a new cane, looks younger, and with him, come.. Mom and Dad?


Granddad's jaw dropped. "%s?"

You smile back. """ % (myPlayer.name))
    for character in ending3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(3)
    ending4 = ("""
Granddad comes over and gives you a big hug. Mom and Dad do the same next.

"I thought you'd never come back" said Granddad "But you did."
""")
    for character in ending4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    time.sleep(7)
    ending5 = ("""
The three of them go out and enjoy their new world.

The trees are green everywhere. Everyone is outside taking a walk.

Not a sign of anyone wearing a mask.



"Who's ready for some Shitake mushrooms?" Mom says.

%s groans. "Not again, Mom!"

The three of them laugh.




The End.

""" % (myPlayer.name))
    for character in ending5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(5)
    os.system('clear')
    print("""
Thanks for playing! This game will reset in a few seconds (sorry, but I don't know how to do save files :P)

I hope you enjoyed!

""")
    time.sleep(10)
    sys.exit(0)

















































title_screen()
