# The script of the game goes in this file.

# symbol "#" is being used as decoration and to make code easier to read
# symbol "#" is also used before any line of code to create a comment

##########################################################################
#############         CHARACTERS LIST               ##########################
##########################################################################
#-------------------------------------------------------------------------
define Voice = Character(" ")
#-------------------------------------------------------------------------
# Characters will be defined here
# Current character named "Voice" is acting as narrator for now
# describing scenes, player thoughts, and actions
##########################################################################
#############        IN-GAME OBJECTS/ITEMS          ##########################
##########################################################################
#-------------------------------------------------------------------------
define Key = False
define Silver_Key = False
define Knife = False
define Weapon = False
define Music_Room_Gems = False
#-------------------------------------------------------------------------
# Items here are enabled once player has found an Item
# Items enable player to move through the game
# some items will change dialogue or add new dialogue
##########################################################################
##############        TEST BOOLEANS               #############################
##########################################################################
#-------------------------------------------------------------------------
define Room1_p1_complete = False
define Room1_extra_complete = False
define Study_Room_p2_01 = False
define A_01_Complete = False
define B_01_Complete = False
define C_01_Complete = False
define D_01_Complete = False
#-------------------------------------------------------------------------
# Test Booleans are here are meant to check if a character has acquired an Item,
# or has already completed a dialogue or room.
# this will help the game be more dynamic
#-----------------------------------------------------------------------------
# IMPORTANT! not all booleans are being used right now and some may be deleted
# as we continue testing game.
#-----------------------------------------------------------------------------
################################################################################
####################################################################################
################################################################################



# The game starts here.
#-------------------------------------------------------------------------
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
#-------------------------------------------------------------------------
#############################################################################################\
###                  |                                          |                   ###########\
###                 |||                                        |||                   ############\
####                |||                CHAPTER I               |||                   #############\       
###                 |||                                        |||                   #############/
####                |||                                        |||                   ############/
##                   |                                          |                   ###########/
#############################################################################################/
label Chapter1_01:
    Voice "You find yourself in a dimly lit room."
    Voice "The air is heavy with an. eerie stillness. The walls are adorned with faded wallparper, peeling away to receal glimpses of the past."
    Voice "What would you like to do?"
# label added as a checkpoint
label Room1_p1:
# added a boolean to hide text "What would you like to do next" on first pass through

    if Room1_p1_complete ==  True:
        Voice "What would you like to do next"
# after this line of code, the changing Room1_p1_complete to 'True', will allow hidden text to be shown.
# dollar sign before code enables python code, only python code can munipulate variables in renpy (that I know of so far)
    $ Room1_p1_complete = True
    menu:
        "Examine the furniture for any hidden objects":
            Voice "You carefully inspect the furniture..."
            Voice "running your hands along the dusty surfaces. As you rummage through drawers and list up cushions, you discover a rusted key hidden beneath a stack of old newspapers."
            Voice "It glimmers faintly in the dim light, hinting at its potential usefulness."
            Voice "You pocket the key, its weight a resassuring presence."
            $ Key = True

            jump Room1_p1
        
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
                        jump Room1_p1
            else:
                jump Room1_p1
        "Investigate the peeling wallpaper for clues":
            Voice "You turn your attention to the peeling wallpaper, its faded patterns hinitng at forgotten stories."
            Voice "As you carefully peel back a section, revealing a hidden layer beneath, you notice faintly etched symbols and cryptic writings."
            Voice "The words seem to writhe and twist, as if alive, fueling your growing unease."
            Voice "They appear to be fragments of a diary, revealing the inner thoughts of somoene who walked these halls long ago."
            Voice "The wods blur and dance before your eyes, but a phrase stands out..."
            Voice "\"Beware of the masked ones\""
            
label Room1_p1_2:
            menu:
                "Approach the window and peer outside (further investigate)":
                    Voice "You cautiously make your way towards the window, drawn to the silver of moonlight that spills into the room."
                    Voice "As you reach the window, you notice the glass is cracked, resembling a spider's web."
                    Voice "You peer outside, expecting to see a tranquil night, but instead, you're greeted by a twisted, distorted version of reality."
                    Voice "The moon hangs in a sickly green sky, casting an unnatrual glow upon the barren trees that sway ominously."
                    Voice "Shadows dance and shift in the distance, playing tricks on your mind."
                    jump Room1_p1_2

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
                            jump Hallway_p1
                        "Continue investigating":
                            jump Room1_extra
label Room1_extra:
    menu:
        "Examine the furniture for any hidden objects":
            Voice "Furniture looks dusty, does not seem to hold anything else of use"
            jump Room1_extra

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
                        jump Room1_extra

            jump Room1_extra

        "Investigate the peeling wallpaper for clues":
            Voice "\"Beware the Masked Ones\""
            Voice "I wonder what that means..."
            if Knife == True:
                Voice "Hmmmm I wonder"
                menu:
                    "Carve something on the wall with knife?":
                        Voice "A perfect smiley face!"
                        jump Room1_extra
                    "Continue Investigating":
                        jump Room1_extra
            jump Room1_extra

        "leave the room and explore the hallway":
                            jump Hallway_p1
label Hallway_p1:
    Voice "You step away from the peeling wallpaper, the words lingering in your mind like a haunting melody."
    Voice "As you exit the room, the hallways streches before you, its darkness seemingly alive wiht unseen whispers."
    Voice "The flickering lightbulb above struggles to illuminate the path ahead, casting eerie shadows that seem to dance and shift with each step."
    Voice "The air grows colder, sending shivers down your spine, as if the very walls are watching every move."
    Voice "What would you like to do next?"

label Hallway_p1_01:
    menu:
        "Proceed cautiously down the hallway, deeper into the unknown":
            Voice "You leave the room behind, the weight of the knife in your pocket is a comforting reminder."
            Voice "as you proceed cautioulsy, you notice a flickering light in the distance, casting eerie shadows along the corridor. it beckons you forward."
            Voice "What will you do next?"
            menu:
                "Examine your surroundings":
                    Voice "there is a flickering light"
                    menu:
                        "Venture deeper into the hallway?":
                            Voice "you steel yourself against the encroaching darkness and follow the mesmerizing flickering light that dances ahead."
                            Voice "each step forward feels heavy, as if you are descending further into the labyrinth of your own unraveling mind."
                            Voice "As you press on, the intesity of the light grow, illuminating a door at the end of the corridor."
                            Voice "It stands ajar, inviting you to to unvover the secretes that lie beyond. The air grows colder, your heart pounding with a mixture of anticipation and dread."
                            Voice "What will you do next?"
                            menu:
                                "Gather your courage, and push open the door, bracing yourself for whatever awaits":
                                    Voice "Summoning your resolve, you braced yourself for the unknown that lies beyond the door."
                                    Voice "As you step inside, the door creaks ominously, its sound reverberting through the silence."
                                    Voice "The air feels heavy and suffocaiting, as if a malevolent presence lingers just out of sight. Your senses heighten, and every fiber of your being urges with caution."
                                    Voice "What will you do next?"
                                    menu:
                                        "Feel your way along the walls, searching for a light swithc or source of illumination.":
                                            jump Study_Room_p1

                                        "carefully explore the room usin ghands and other senses.":
                                            Voice "You stumble around unable to see much in the dimly lit light. You trip over books and think to yourself that you need to find another source of light."
                                            Voice "Feel your way along the walls, searching for a light swithc or source of illumination."
                                            menu:
                                                "Hesistate and examine the door for any signs of danger":
                                                    jump Study_Room_p1

                        "Retrace your steps":
                            jump Hallway_p1_01
        "Look around":
            Voice "You notice a door"
            menu:
                "Examine door?":
                    jump Study_Room_p1
label Study_Room_p1:
    Voice "You extend your trembling hands, reaching out to feel the walls for any sign of a light switch or some source of illumination."
    Voice "Your fingertips brush against the rough texture of the wallpaper, searchin gor a flicker of hope in the darkness."
    Voice "As you inch forward, yor hand grazes over something cold and metallic -- a switch!"
    Voice "as you flick the switch, the light struggles to light back to life, casting unsettling shadows."
    Voice "The room appears to be a study, its shelves lined iwth decaying books and forgotten artifacts."
    Voice "A desk stands in the center, covered in dusty papers and dried ink."

    Voice "What will you do now?"
    menu: 
        "Investigate the desk and examine the peres and objects on it.":
            Voice "You cautiously approach the desk, the flickering lifht casting eerie shadows on its surface. A layer of dust coats the paper and objects, suggesting that this room has been undistrubed for a long time."
            Voice "With a mix of curiousity and unease, you begin to examine the items scattered accross the desk."
            Voice "among the papers, you find a torn diary page, its faded ink barely legible. It speaks of a growing paranoia, mentions of twisted visions, and an unshakable belief that everone around the writer was a monster."
            Voice "It resonates uncomfortably with your own experiences."
            Voice "In addition to the diary page, you come across an old key, tarnished with age."
            Voice "Its purpose remains a mystery, but its weight in your hand fills you with a sense of potential usefulness."
            menu: 
                "examine the shelves and search for any userful items or clues.":
                    jump Study_Room_p1_02
        "examine the shelves and search for any userful items or clues.":
            jump Study_Room_p1_02
        "retrace your steps back":
            jump Hallway_p1_01
label Study_Room_p1_02:
    Voice "You turn your attention to the shelves, filled with a variety of objects and books that have weathered the passage of time. As you scan the items, you eyes catch a glimmer of something promising amidst the fogotten relic."
    Voice "Reaching out, you pick up a small vial filled with shimmering liquid. It radiates an ethereal glow, its contents mysterious and unknown. The vial seems to hold a poptent substance that could potentially aid you in your journey or unlock hidden paths."
    Voice "In addition to the vial, you spot a weathered tome that stands out from the rest. its leather cover is adorned in cryptic symbols, hiting at forbidden knowlege. Perhaps within its pages lie the answers you seek or the key to utangling the web of madness that surrounds you."
    menu:
        "Open the acient tome and delve into its secrets":
            Voice "you carefully open the weathered tome, its pages creaking with age as they reveal the hidden knowledge within. The contents of the book are a mixture of handwritten notes, diagrams, and cryptic passsages, as if the author's mind was as chaotic as your own."
            Voice "as you dleve deeper into the pages, you come across a section that speaks of ancient rituals and the potential to pierce the veil betweeeen realities. it describes a ritual involving mirrors, darkness, and whipered incantations -- a path to uncover the truth or descend further into madness."
            Voice "reading further, you notice a diagram depicting a peculiar mirror with intricate symbols etched around its fram. The mirror appears to be central piece in the ritual, its purpose shrouded in mystery."

            Voice "what will you do next?"
            menu: 
                "Study the diagram closely and try to decipher its meaning.":
                    jump Study_Room_p1_03

                "Continue readying the tome for any additional insights or clues.":
                    jump Study_Room_p2_02
label Study_Room_p1_03:
    Voice "you continue studying the diagrams closely. your eyes scanning the faded words for further insights and clues. as you progress through its pages, you stuble upon a passage that mentions a hidden chamber within the house -- a place where the truth is said to be concealed."
    Voice "According to the passage, accessing this hidden chamber requires a specific sequence of steps involving the key you discovered earlier. It describes a series of symbols that need to be traced with the key on a certain wall, unlockin gthe way to the chamber."
    Voice "The tome also warns of the dangers that await within the hidden chamber, cautioning that the truth may be more unsettling that you can imagine."
    Voice "What will you do next?"
    menu:
        "Memorize the sequence of symbols and prepare to unlock the hidden chamber":
            Voice "You focus your attention on the passage describing the sequence of symbols needed to unlock the hdden chamber. Carefully comitting the symbos to memory, you envision tracing them with the key you've found running it along the designated wall."
            Voice "The symbols are etched into tyour mind."
            Voice "With the sequence memorized, you prepare yourself for the next step."
            Voice "What will you do now?"
            menu:
                "return to the hallway and proceed to the designated wall to trace the symbols.":
                    jump Study_Room_p2_02
                "seek out additional information or clues before unlocking the hidden chamber.":
                    Voice "You decided to seek out additional information or clues before unlocking the hidden chamber, hoping ot gather more insights that might aid you in your quest. You search the remaining pages of the ancient tome, scouring for any hints or warnings that might be of importance."
                    Voice "As you read on, you come across a passage that speaks of a haunting melody--a tune that can either unlock deepest recesses of the mind of plunge it further into madness. It suggest that finding and playing the melody might reveal hidden truths or provide rpotection against the enroaching darkness."
                    Voice "the passage also hints at anold music room within the house, where the melody may be discovered or perhaps compsed anew."
                    Voice "what next?"
                    menu:
                        "return to the hallway and proceed to the designated wall to trace the symbols.":
                            jump Study_Room_p2_02
                        "reflect on the signficance of the haunting melody and its potential effects":
                            Voice "After reflecting you decide to look for the music room within the house"
                            # enabling this boolean "Music_Room_quest" will grant character additional dialogue options
                            # and secrets.
                            $ Music_Room_quest = True
                            jump Music_Room

                        "search for the music room within the house":
                            # enabling this boolean "Music_Room_quest" will grant character additional dialogue options
                            # and secrets.
                            $ Music_Room_quest = True
                            jump Music_Room

        "Continue reading the tome for more information and warnings.":
            Voice "You delve deeper inot the ancient tome, seeking more information and potential warnings that may guide you through twisted path ahead. The pages, worn and fragile, hold a wealth of unsettling knowledge."
            Voice "Amidst the passges, you come accross a chilling account of a previous inhabitant's descent into madness. It speaks of the growing paranoia, the haunting whispers that echoed through the halls, and the relentless perception of ordinary people as grotesque monsters."
            Voice "The author's rambling reveals a deep-rooted fear and the beleif that the house itself possesses a malevolent presence, driving those who dare enter to the brink of insanity."
            menu:
                "Memorize the sequence of symbols and prepare to unlock the hidden chamber":
                    jump Study_Room_p2_01
                    
label Study_Room_p2_01:
            Voice "You focus your attention on the passage describing the sequence of symbols needed to unlock the hdden chamber. Carefully comitting the symbos to memory, you envision tracing them with the key you've found running it along the designated wall."
            Voice "The symbols are etched into tyour mind."
            Voice "With the sequence memorized, you prepare yourself for the next step."
            Voice "What will you do now?"
            menu:
                "return to the hallway and proceed to the designated wall to trace the symbols.":
                    jump Study_Room_p2_02
                "seek out additional information or clues before unlocking the hidden chamber.":
                    Voice "You decided to seek out additional information or clues before unlocking the hidden chamber, hoping ot gather more insights that might aid you in your quest. You search the remaining pages of the ancient tome, scouring for any hints or warnings that might be of importance."
                    Voice "As you read on, you come across a passage that speaks of a haunting melody--a tune that can either unlock deepest recesses of the mind of plunge it further into madness. It suggest that finding and playing the melody might reveal hidden truths or provide rpotection against the enroaching darkness."
                    Voice "the passage also hints at anold music room within the house, where the melody may be discovered or perhaps compsed anew."
                        
                    menu:
                        "return to the hallway and proceed to the designated wall to trace the symbols.":
                            jump Study_Room_p2_02

                        "reflect on the signficance of the haunting melody and its potential effects":
                            Voice "....."
                            Voice "the melody...makes my body feel weightless and free"
                            Voice "but why does my head feel..."
                            Voice "different"
                            # Idea: enabling this boolean "Music_Room_quest" will grant character additional dialogue options
                            # and secrets.
                            $ Music_Room_quest = True
                            menu:
                                "search for the music room within the house?":
                                    jump Music_Room
                        "search for the music room within the house":
                            $ Music_Room_quest = True
                            jump Music_Room
label Study_Room_p2_02:
    scene bg room
    Voice "With the symbols firmly etched in your mind and the rusted key in hand, you make your way back to the hallway. The air feels heavy as you appreach the desgnated wall, its surface awaiting the touch of the key."
    Voice "Alighning yourself with the wall, you trace the symbols with the key, following the precise sequence described in the ancient tome. As the key glides along the wall, a faint click resonates through the corridor, signaling that something has been unlocked."
    Voice "A hidden doorway matertializes before you, blending seamlessly into the wallpaper. The path tot he hidden chamber stands revealed."
    menu:
        "Step through the hidden doorway, vneturing into the unknown":
            jump chapter1_end

label Music_Room:
    Voice "With the knowledge of the hainting melody and its potential significance, you set out to find the music room within the house. Leaving the study behind, you reenter the hallway, the dim light casting elongated shoadows along the worn carpet."
    Voice "As you explore, you notice a faint sound, carried on the air like a distant echo. It grows louder as you follow its trail, leading you to a door that stands slightly ajar. Pushing it open you step into a room bathed in muted moonlight streaming through tattered curtains."
    Voice "The music room reveals itself, its atmosphere heavy with a sense of melancholy. A grand piano sits at the center, its keys covered in a thin layer of dust. sheets of music are scattered about, their notes seemingly frozen in time."
    menu:
        "Examine the scattered sheets of music for any clues or hidden compositions.":
            Voice "You carefully examine the scattered sheets of music, hoping to find clues or hidden compositions that might further unravel the mysteries of the house. As you sift through the delicate pages, you notice one sheet that stands out from the rest."
            Voice "The sheet appears to be composition titled \"melody of shadows\" its notes are written in an intricate and hainting arrengament, evoking a sense of unease and melancholy. The composition seems to mirror the unsettling atmosphere of the hosue, resonating with the turmoil within your own mind."
            Voice "Upon sloer inspection, you notice a faint marking on the sheet, as if someone had made annotations or corrections. These Markings highlight certain sections of the composition, suggesting alternative interpretations or varieations."
            menu:
                "attempt to play the orignal composition as written on the sheet":
                    pass
                "experiment with the annotated sections, trying out the variations suggested by the marking":
                    pass
        "attempt to play the orignal composition as written on the sheet":
            Voice "You take a eat at the grand piano, your fingers poised above the dusty keys. With a mixture of anticipation and apprehension, you behgin to play the original composition as written on the sheet. As your hands move across the keybaord, the room is filled with a haunting melody that reverberates through the air."
            Voice "The music resonates with the essance of the house, its melancholic notes weaving through the shadows. As youcontinue to play, you feel a shift in the atmosphere, as if the house itself is responding to the ethereal sound."
            Voice "Suddently, a hidden compartment beneath the pinao opens, revealing a small wooden box. It beckons to you."
            jump Music_Room_p2
label Music_Room_p2:
    Voice "Intrigued by the small wooden box that has been revealed, you approach it with anticiaption. the box is intricately carved, its surface worn with age. You gently lift the lid, reavling its contents."
    Voice "Inside the box, you find a delicate silver key, glimmering faintly in the moonlight that seeps through the room's curtains. its itricate design suggests taht it unlocks something of significance, though what exactly remains a mystery."
    Voice "Alongside the key, you discover a folded note, yellowed with time. opening it, you read a cryptic message written in elegant script: \"Unlock the secrets that lie within the mirrors and the truth shall be revealed\""
    Voice "The note hints at the connection betweent the key and hte mirrors within the house, alluding to a hidden truth waiting to be unveiled."
    menu:
        "take the silver key and note with you, preparing to explore the mirrors.":
            Voice "You carefully pocket the silver key and fold the note, tucking them away for safekeeping. Prepared to delve deeper into the secrets that lie within, you take a moment to gather your thoughts and steady your resolve."
            Voice "The whipsers of your own sanity echo in your mind, urging you forward, even as fear gnaws at the edges of your consciousness."
            Voice "With the silver key and the enigmatic note in your possession, you stand ready to confront the truths that the mirrors hold."
            # Enabling this Boolean means player now possess a "Silver Key" in game Item.
            # Player will now be able to unlock something that requires this Silver Key
            $ Silver_Key = True
            menu:
                "return to the hallway and proceed to the designated wall to trace the symbols.":
                    jump Study_Room_p2_02
                "explore the remaining areas of the house for any additional clues":
                    Voice "witht he silver key and cryptic note in your possesion, you decided to explore the remining areas of the house in search of additional clues. Leaving the music room behind, you retrace your steps through the hallway, your senses on high alert."
                    Voice "As you venture deeper into the house, you come accross a dusty corridor adorned with several ornate mirrors. each mirror reflects distroted images of the surroundings, casting an eerie atmosphere upon the space. the whispers of your own doubts grow louder, but you press on, determained to uncover truth."
                    Voice "You inspect each mirror carefully, searching for any hidden compartments or peculiarities. After a thorough examination, you notice a small niche concealed behind one of the mirrors. Excitement surges through ou as you realize there might be something of importance hidden within."
                    # This "IF" statement checks if player has a silver key
                    if Silver_Key == True:
                        menu:
                            "use the silver key to unlock the niche behind the mirror":
                                Voice "You take out the silver key from your pocket, its delicate design glinting in the dim light of the corridor. With a steady hand, you insert the key into the keyhole. It fits perfectly."
                                Voice "With a twist of the key, a mechanism clicks, and the mirror shifts slightly, reavelinga. hidden compartment. Inside, you find a velvet pouch, its conetents unknown."
                                Voice "Curiousity piqued, you carefully open the pouch to discover a collection of shimmering gemstones. Each stone holds a different hue. sparking with an otherwoldy brilliance. They seem to hold a power of their own, their significance and purpose yet to be unveiled."
                                menu:
                                    "collect the gemstones and carry them with you for future use.":
                                        jump Music_Room_p3
                    # if the "IF" statement is not true, (character does not possess silver key)
                    # Then player will proceed to this dialogue instead of opening niche
                    else:
                        Voice "you do not have key to unlock this"
                        Voice "maybe retrace your steps?"
                        menu: 
                            "return to music room":
                                jump Music_Room
                            "return to the study":
                                jump Study_Room_p2_01
                            "return to the first room":
                                jump Room1_extra
label Music_Room_p3:
    Voice "You carefully collect theshimmering gemstones from the velvet pouch, their vibrant hues mesmerizing in the palm of your hand. Each gemstone holds an ethereal quality, their radiance casting a subtle glow in the dim light of the corridor."
    Voice "You secure the gemstones in a sfae place, knowing that their unique properties might prove valuable in the challanges yet to come. their potential uses and effects remain a mystery, but their presensce instills a sense of hope and empowerment within you."
    Voice "With the gemstones in your possession, you feel an additional weight responsibility. It is up to you to uncover their true purpose and utilize them wisely."
    menu:
        "Reflect on the significance of the gemstones and plan your next move.":
            Voice "The gems, like a burning fire in my hands"
            Voice "The haunted melody now with me...always"
            $ Music_Room_Gems = True
            Voice "you get a sudden chill, as if the house itself rejecting your very presence"
            Voice "your feet start moving, the doors close and you come to a stop."
            scene black with dissolve
            Voice "Everything goes black as you remember your last intentions"
            
            
            
            jump Study_Room_p2_02




label chapter1_end:
    # Scene is the background
    # this code will turn background to black
    # "dissolve" is an effect that makes background change a little slower but still fast.
    scene black with dissolve
    "you have completed chapter I"
#############################################################################################\
###                  |                                          |                   ###########\
###                 |||                                        |||                   ############\
####                |||          CHAPTER I Complete           |||                    #############\       
###                 |||                                        |||                   #############/
####                |||                                        |||                   ############/
##                   |                                          |                   ###########/
#############################################################################################/  





    # This ends the game.
    return
