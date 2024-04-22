# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
##########################################################################
#############         CHARACTERS LIST          ###############################
##########################################################################
define Main = Character("Melissa")
define Voice = Character(" ")

##########################################################################
#############        IN-GAME OBJECTS/ITEMS          ##########################
##########################################################################
define Key = False
define Knife = False
define Weapon = False
##########################################################################
##########################################################################
#################### TEST BOOLEANS #############################
define chapter1_01_p1_complete = False
define chapter1_01_ex_complete = False
define A_01_Complete = False
define B_01_Complete = False
define C_01_Complete = False
define D_01_Complete = False
################################################################



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show test character at right with moveinright
    
    # These display lines of dialogue.
###########################################################################
#####                     Chapter 1 Part 01                           #####
label Chapter1_01:
    Voice "You find yourself in a dimly lit room."
    Voice "The air is heavy with an. eerie stillness. The walls are adorned with faded wallparper, peeling away to receal glimpses of the past."
    Voice "What would you like to do?"
# label added as a checkpoint
label Chapter1_01_p1:
# added a boolean to hide text "What would you like to do next" on first pass through

    if chapter1_01_p1_complete ==  True:
        Voice "What would you like to do next"
# after this line of code, the changing chapter1_01_p1_complete to 'True', will allow hidden text to be shown.
# dollar sign before code enables python code, only python code can munipulate variables in renpy (that I know of so far)
    $ chapter1_01_p1_complete = True
    menu:
        #A_01
        "Examine the furniture for any hidden objects":
            Voice "You carefully inspect the furniture..."
            Voice "running your hands along the dusty surfaces. As you rummage through drawers and list up cushions, you discover a rusted key hidden beneath a stack of old newspapers."
            Voice "It glimmers faintly in the dim light, hinting at its potential usefulness."
            Voice "You pocket the key, its weight a resassuring presence."
            $ Key = True

            jump Chapter1_01_p1
        
        "Approach the window and peer outside":
            Voice "You cautiously make your way towards the window, drawn to the silver of moonlight that spills into the room."
            Voice "As you reach the window, you notice the glass is cracked, resembling a spider's web."
            Voice "You peer outside, expecting to see a tranquil night, but instead, you're greeted by a twisted, distorted version of reality."
            Voice "The moon hangs in a sickly green sky, casting an unnatrual glow upon the barren trees that sway ominously."
            Voice "Shadows dance and shift in the distance, playing tricks on your mind."
            
            if Key == True:
                Voice "There is a key hole on window"
                menu:
                    "Try Key?":
                        Voice "key does not fit here"
                        jump Chapter1_01_p1
            else:
                jump Chapter1_01_p1
        #B_03
        "Investigate the peeling wallpaper for clues":
            Voice "You turn your attention to the peeling wallpaper, its faded patterns hinitng at forgotten stories."
            Voice "As you carefully peel back a section, revealing a hidden layer beneath, you notice faintly etched symbols and cryptic writings."
            Voice "The words seem to writhe and twist, as if alive, fueling your growing unease."
            Voice "They appear to be fragments of a diary, revealing the inner thoughts of somoene who walked these halls long ago."
            Voice "The wods blur and dance before your eyes, but a phrase stands out..."
            Voice "\"Beware of the masked ones\""
            
label Chapter1_01_p1_2:
            menu:
                "Approach the window and peer outside (further investigate)":
                    Voice "You cautiously make your way towards the window, drawn to the silver of moonlight that spills into the room."
                    Voice "As you reach the window, you notice the glass is cracked, resembling a spider's web."
                    Voice "You peer outside, expecting to see a tranquil night, but instead, you're greeted by a twisted, distorted version of reality."
                    Voice "The moon hangs in a sickly green sky, casting an unnatrual glow upon the barren trees that sway ominously."
                    Voice "Shadows dance and shift in the distance, playing tricks on your mind."
                    jump Chapter1_01_p1_2

                "Return to the furniture and search again":
                    Voice "You retrace your steps back. The furniture stands silently. You scour every nook and cranny, determined to uncover any hidden treasures."
                    Voice "Your persistence pays off as you where you discover a small key"
                    Voice "a serrated knife is tucked away in a hidden compartment of an old wooden cabinet."
                    Voice "Its balde glistens in the faint light, promosing protection and potential uses in the trails to come. You pocket the knife, feeling a mixture of anxiety and reassureance."
                    $ Key = True
                    $ Knife = True
                    Voice "What will you do know?"
                    menu:
                        "leave the room and explore the hallway":
                            jump chapter1_02
                        "Continue investigating":
                            jump chapter1_01_ex
label chapter1_01_ex:
    menu:
        "Examine the furniture for any hidden objects":
            Voice "Furniture looks dusty, does not seem to hold anything else of use"
            jump chapter1_01_ex

        "Approach the window and peer outside":
            Voice "so beautiful...the moon"
            if Key == True:
                Voice "Wait.."
                Voice "There is a key hole on Window panel"
                menu:
                    "Try Key?":
                        Voice "You forced the key...now its stuck"
                        menu:
                            "twist key":
                                Voice "*GRUNT*..KEY IS FREE"
                                Voice "You retreived key, though it is now a dented key."
                                Voice "You place dented key back into your pocket"
                    "Continue Investigating":
                        jump chapter1_01_ex

            jump chapter1_01_ex

        "Investigate the peeling wallpaper for clues":
            Voice "\"Beware the Masked Ones\""
            Voice "I wonder what that means..."
            if Knife == True:
                Voice "Hmmmm I wonder"
                menu:
                    "Carve something on the wall with knife?":
                        Voice "A perfect smiley face!"
                        jump chapter1_01_ex
                    "Continue Investigating":
                        jump chapter1_01_ex
            jump chapter1_01_ex

        "leave the room and explore the hallway":
                            jump chapter1_02
label chapter1_02:
    scene black
    Voice "End of Preview"
        

    # This ends the game.

    return
