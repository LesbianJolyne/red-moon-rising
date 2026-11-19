# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define uk = Character("???", who_color = "#a83232")
define sm = Character("Scarlet Mask", who_color = "#a83232")
define narrator = Character(what_italic=True)
define wk = Character("White Knight", who_color = "#FFFFFF")

transform rightside:
    xalign 0.75
    yalign 1.0

transform leftside:
    xalign 0.25
    yalign 1.0

transform centerside:
    xalign 0.5
    yalign 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at rightside

    # These display lines of dialogue.

    narrator "It's been nearly a month since this all began."

    narrator "You've been investigating the disappearance of The Architects, the city's greatest team of heroes.
    In doing so, you discovered a conspiracy leading all the way up to the highest levels of government in the
    city."

    narrator "Government officials have been involved with a group known as the Red Masks, a criminal organization
    who seem to have their fingers in every kind of illegal activity in the city. As a lone teen hero, you were
    in over your head trying to deal with all of this."

    narrator "You've finally tracked down the leader of the organization, known only as Scarlet Mask, to this
    underground facility deep in the heart of the city."

    narrator "After fighting your way through dozens of mooks, you finally come to what looks to be an audience
    chamber. Well, throne room would be more accurate, as on the dais in front of the huge array of computers
    there's a throne. Lounging on it is a girl your age."

    narrator "She's dressed much like the henchmen you've seen so far- red leather jacket, black tech pants,
    and red animal mask, although hers looks slightly different. Instead of being a full animal, it's instead
    shaped like the jaw bones of some predatory beast."

    narrator "As you enter she claps slowly."

    uk "Congratulations, hero. You've finally made it."

    wk "Who are you?"
   
    uk "Me? Why, isn't it obvious? I'm Scarlet Mask."

    wk "You? But... you're just a teenager."

    sm "And? So are you."

    menu:
        "...Fair point.":
            jump fairPoint
        "That's not the point. What have you done with the Architects?":
            jump architectsLocation
    label fairPoint:
        $ fairPointFlag = True

        jump choice1Done

    label architectsLocation:
        $ architectsLocationFlag = True

        jump choice1Done
    
    label choice1Done:
        sm "Some dialogue"
        

    # This ends the game.

    return
