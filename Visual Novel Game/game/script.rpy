# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Main = Character("Melissa")

define Voice = Character("...")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show test character at right with moveinright
    
    # These display lines of dialogue.

    Main "Greetings Mortal"

    Main "....You are new aren't you?"

    # Menu Creates Selection
    menu Test_Dialog:
        #Character Dialog
        "This is the realm of shadows, do you care to know more?"
        # Response choice 1
        "no":
            # Dialog from reponse
            Main "well thats unfortunate"

            Main "..."

        # Response choice 2       
        "yes":
            # Dialog from reponse
            Main "the Realm of Shadows is a place where light dares not tread, a domain caught between the living world and the spectral plane. It's a landscape woven from darkness and whispers, where shadows seem to breathe and the boundaries between substance and shade blur."
    show test character with dissolve
    Main "Close your eyes.."
    with Pause(3)
    
label Second_Scene:
    scene black
    Main "Listen closely"

    Main "that is your heart beating"

    Voice "You Died"

        

    # This ends the game.

    return


    # This ends the game.

    return
