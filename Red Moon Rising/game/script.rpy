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

    narrator "You, White Knight, have been investigating the disappearance of The Architects, the city's greatest
    team of heroes. In doing so, you discovered a conspiracy leading all the way up to the highest levels of
    government in the city."

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
        "...Fair point. But how did you get so many city officials involved?":
            jump fairPoint
        "That's not the point. What have you done with the Architects?":
            jump notThePoint
    label fairPoint:
        $ fairPointFlag = True
        $ notThePointFlag = False

        sm "Simple. I offered them something they already wanted."

        wk "What do you mean?"

        sm "All the city officials involved in the Red Masks were already corrupt. I just offered them the
        chance to line their pockets some more."

        wk "How could you possibly know that all of them were already corrupt?"

        sm "Because I'm psychic."

        narrator "She smiles, tapping her temple."

        sm "I read their minds and saw the things they'd already done. Then I offered them more, and the greedy
        things snatched up the opportunity."

        menu:
            "What, your organization is just to help corrupt officials get richer?":
                sm "What an accusation. No, I'll tell you what it's for."
                jump theWhy
            "If you're really psychic, what am I thinking right now?":
                jump proveIt

        

    label notThePoint:
        $ notThePointFlag = True
        $ fairPointFlag = False

        sm "Don't worry. They're quite safe. They're asleep in the holding cells here."

        wk "How did you capture them, anyway? They're the most powerful heroes in the city."

        sm "For a team of capable heroes, they don't have very good psychic defenses. I used an amplifier on
        my psychic powers to induce sleep so they couldn't get in my way."

        menu:
            "You monster, I'll put a stop to you!":
                $ youMonsterFlag = True
                
                narrator "As you lunge toward her, she leaps from her throne and blocks your first blow."

                jump startTheFight
            
            "Get in the way of what?":
                
                sm "I'm glad you asked."
                
                jump theWhy
    
    label proveIt:
        $ proveItFlag = True
        
        sm "You were just considering whether to ask me if the Red Masks are just around to help corrupt
        officials get richer."
        
        menu:
            "Okay, you're psychic. So... is it?":
                
                sm "What an accusation. No, I'll tell you what it's for."
                
                jump theWhy
            
            "So you invade people's minds. That's all the proof I need that you're evil.":
                
                narrator "As you lunge toward her, she leaps from her throne and blocks your first blow."
                
                jump startTheFight

    label theWhy:
        $ theWhyFlag = True
        
        narrator "Scarlet Mask stands up from her chair, casually walking over to the huge computer behind the
        throne. Now that she's drawn your attention to it, you can see it's processing some kind of data. A
        loading bar takes up most of the main monitor."

        sm "I'm technically a criminal mastermind, but it was all for a reason. These corrupt officials have
        destroyed so many lives. They put their own interests above the needs of those they're meant to serve."

        sm "So I thought, as someone who can actually tell when someone's lying, I could put my powers to good
        use. Being psychic is all well and good, but it doesn't hold up in the court of law. I needed evidence."

        sm "I approached these officials as the messenger of a mysterious criminal mastermind, Scarlet Mask. I
        told them there was an opportunity for them to profit, and without fail every single one joined me. The
        more they did the better, because I was watching all of them and recording every illegal activity."

        narrator "She gestures to the other monitors, showing all kinds of shady dealings. A judge taking a
        bribe here, the mayor spending government funds on himself there, all of them flashing across the
        screens fast enough to make anyone dizzy."

        sm "And now? Now I can send all this evidence out to every news organization and every upstanding official
        left in the city. Finally, I can make these people face consequences for their actions."

        narrator "She turns to you again, smiling as the loading bar behind her creeps along."

        sm "The Architects tried to stop me before this was ready. But as soon as it's out there, I'll release them.
        You though, you understand what it's like to be looked down on by adults."

        narrator "Before you can protest at her invading your mind, she puts a hand up to stop you."

        sm "I don't have to read your mind to know that. I've been where you are: trying to do the right thing,
        only to have the people you look up to dismiss you. After all, why aren't you a part of the Architects?
        You're just as accomplished as any of them."

        sm "If you let me go, I can promise you the Red Masks will go away as well. After all, I collected
        enough evidence that they should all go to jail for a long, long time."

        menu:
            "Why should I believe you?":
                jump believeYou
            "Even if I do, how are you going to avoid getting caught by the Architects?":
                jump howNoArchitects

    label believeYou:
        sm "You can take a look at the evidence yourself if you like."

        narrator "She steps to the side, gesturing for you to come up to the computer. You approach, seeing the
        evidence flash across the screens."

        menu:
            "{i}Destroy the evidence{/i}":
                
                $ destroyEvidenceFlag = True
                
                narrator "With this opportunity, you quickly type on the computer before Scarlet Mask can stop
                you, deleting the evidence before it has a chance to finish uploading. You bring your fist down,
                your super strength destroying the computer for good measure."

                sm "You really shouldn't have done that."

                narrator "She lunges at you and you barely have time to block her first attack."

                jump startTheFight
            
            "Seems like you've got this pretty well handled. What do you need me to do?":

                narrator "She smiles, clearly relieved."

                sm "Once this has finished uploading, I'll wake up the Architects. While I'm making my escape, I'll
                need you to distract them."

                wk "I'll do my best"

                narrator "She holds out her hand to you."

                sm "Thank you. I'm glad my trust in you wasn't misplaced."

                narrator "You take her hand, shaking it."

                wk "You're doing the right thing. It's the least I can do to help you."

                narrator "As you speak, the loading bar finishes its journey across the screen. Scarlet Mask goes to
                the side of the room where there's some sort of elevator waiting to take her up to the surface."

                narrator "As she climbs inside, she gives you one final wave, disappearing right as the Architects
                burst into the room."

                jump helpEpilogue
        
    label howNoArchitects:
        sm "reasons"

    label helpEpilogue:
        narrator "Thanks to you, Scarlet Mask is never found. The other members of the Red Masks are almost all
        apprehended, and those who scatter to the wind will never be able to come back to the city."

        narrator "The corrupt officials of the city are prosecuted for their crimes thanks to the overwhelming evidence
        collected on them. The Architects, while unhappy that Scarlet Mask made her escape, do their due diligence in
        overseeing justice carried out."

        narrator "Some see Scarlet Mask as a criminal mastermind through and through, still calling for the Architects
        to find her and bring her to justice. There are some, though, who see her as a hero for what she's done. You
        count yourself among them."

        narrator "{size=+10}{b}The End{/b}{/size}"

        return

    label startTheFight:
        narrator "fight sequence"
        

    # This ends the game.

    return
