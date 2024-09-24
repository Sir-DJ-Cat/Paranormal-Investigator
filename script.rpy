# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Generic
define idk = Character("???")
define p1 = Character("You")

# Ghosts
define abby = Character("Abby")
define magnus = Character("Magnus")
define hugh = Character("Hugh")
define malerie = Character("Malerie")

# Side Characters
define ll = Character("Landlord")
define jared = Character("Jared")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    play music "detective_office.wav"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    "Another day without any jobs..."
    "I don't know how much longer I can keep this up."
    # play sound "phonering.mp3"
    "*ring ring*"
    "I wonder who that could be."
    p1 "Hello?"
    idk "You're late."
    menu:
        "Say..."
        "I don't know what you're talking about":
            idk "Oh yes you do!"
            ll "You're late on your rent payments again!"
        "Who are you?":
            ll "It's your landlord."
            ll "And you're late on your rent payments...AGAIN!"
    label after_menu:
        p1 "Oh...sorry about that."
    ll "You have until Friday to pay up."
    ll "Otherwise I'm kicking you out for good!"
    # play sound "phoneclick.mp3"
    "*click*"
    "That only gives me 5 days to find a job..."
    "As if one job would pay for everything."
    # play sound "phonering.mp3"
    "*ring ring*"
    "What now..."
    p1 "Hello?"
    idk "Um...hi?"
    p1 "Yes?"
    idk "Is this the Paranormal Investigator's office?"
    menu jared_call:
        "Say..."
        "Why yes it is!":
            idk "Oh great! I need your help."
        "Sorry, wrong number.":
            "Why would I pass up a job?"
            jump jared_call
    label after_jared_call:
        idk "My name is Jared, and my wife and I just moved into a new home."
        jared "And there's been a lot of...strange activity."
    menu jared_call_questions:
        "Ask..."
        "What sort of activity?":
            jared "Well, at first it was just furniture being moved around."
            jared "But later we noticed strange writing on the wall."
            p1 "Writing?"
            jared "Y-yeah. Things like \"HE LOVES ME NOT\" and \"BLED AT THE ALTAR\""
            p1 "Interesting..."
            $ abby_name = False
        "Do you have any records from the previous owners?":
            jared "Yeah, actually."
            jared "There was only one previous owner, a woman named Abby."
            $ abby_name = True
            p1 "Anything else?"
    label after_jared_call_questions:
        jared "Do you think you could come take a look?"
    menu jared_call_final_question:
        "Say..."
        "I sure can.":
            jared "Great! When can you come?"
            p1 "I'll come right away."
            jared "Perfect, see you soon!"
        "I don't think so.":
            "I really need this job..."
            jump jared_call_final_question
    label after_jared_call_final_question:
        "Time to paranormal the investigate"
    "Something about traveling here"

    scene bg room # Entryway

    "Time to take a look around"
    menu sub_first_look:
        "Go to..."
        "Guest Bedroom":
            "It's a small little room, not furnished much besides the bed."
            "Doesn't appear to be anything of note in here."
            jump sub_first_look
        "Master Bedroom":
            "This is where most of the hauntings were said to have taken place."
            "I don't see any writing on the walls, I wonder if they painted over it."
            jump sub_first_look
        "Nursery":
            "Looks like they're preparing for a baby."
            "There's a lot of stuff on the floor, I guess they haven't finished furnishing."
            jump sub_first_look
        "Kitchen":
            "Not many dishes left out."
            "And all the knives are missing from the block..."
            jump sub_first_look
        "Living Room":
            "It's a cozy little room."
            "The magazines on the table appear to be undisturbed."
            jump sub_first_look
        "Dining Room":
            "This room appears to be norma-"
            # play sound "abby_screech.mp3"
            # ending the menu here to start the ghost hunt
        "Garage":
            "It's so cold in here."
            "I think it's the lack of insulation rather than a ghost though."
            jump sub_first_look

    label after_sub_first_look:
        "What was that?!"
    "Suddenly the room becomes very cold."
    "The sliding glass door in front of you starts cracking as if it's being hit."
    # play sound "abby_screech.mp3"
    "Blood splatters across the glass door as a woman screams."
    "A woman wearing a bloodstained wedding dress floats through the door."
    idk "COME BACK TO BREAK MY HEART?!"
    menu abby_hunt:
        "What do you do?"
        "Hide":
            menu abby_hide:
                "Where do you hide?"
                "Hall Closet":
                    "You quickly run around the corner into the hall closet."
                    "You can hear the ghost looking around outside"
                    idk "WHERE ARE YOU?!"
                    "..."
                    idk "HAVE YOU LEFT ME AGAIN?!"
                    "..."
                    "..."
                    # play sound "abby_cry.mp3"
                    "There's a soft crying coming from outside."
                    menu abby_closet:
                        "What do you do?"
                        "Step out":
                            jump after_abby_hunt
                "Master Bedroom":
                    "You quickly rush to the master bedroom, closing the door and hiding behind the bed."
                    # play sound "abby_hum.mp3"
                    "You hear someone humming outside, a sound that seems to be getting closer."
                    "The door creaks open as the humming stops."
                    "The room is silent..."
                    # play sound "abby_screech.mp3"
                    "The ghost appears in front of you and goes to attack."
                    jump abby_hide
                "Guest Bedroom":
                    "You turn the corner and run to the guest bedroom by the entryway."
                    "You hide in the corner behind the small bed."
                    idk "WHERE DID YOU GO?!"
                    "..."
                    idk "HAVE YOU LEFT ME AGAIN?!"
                    "..."
                    "..."
                    # play sound "abby_cry.mp3"
                    "There's a soft crying coming from outside."
                    jump abby_closet
        "Attack (uses money)":
            "You whip out your incense and lighter."
            p1 "Better stay back!"
            "You light the incense and it's smell quickly fills the room."
            # play sound "abby_screech.mp3"
            "The ghost shrieks and immediately retreats."
            idk "WHY?! WHY ARE YOU HURTING ME AGAIN?!"
            # play sound "abby_cry.mp3"
            "The ghost falls to the ground, weeping."
            jump after_abby_hunt
        "Invoke Name" if abby_name:
            "You remember the name that was mentioned by Jared earlier."
            p1 "I invoke your true name:"
            p1 "ABBY"
            "The ghost suddenly withdraws and collapses on the ground."
            # play sound "abby_cry.mp3"
    label after_abby_hunt:
        # Wowza
        "You look at the strange ghost woman crying on the ground."
    "You notice the temperature is no longer freezing."
    menu abby_hello:
        "What do you say?"
        "Hello?":
            "She looks up at you, her face no longer angry and distorted."
            idk "h-h-hello?"
            p1 "Hi. What's your name?"
            idk "..."
            if abby_name:
                idk "Well as you said earlier, my name is Abby."
            else:
                abby "Abby. My name is Abby."
        "Are you OK?":
            "The girl nods without looking up."
            p1 "Did I hurt you?"
            "There's no response."
            "Slowly the girl stands up and looks at you, her face no longer angry and distorted."
            idk "Hi..."
            p1 "Who are you?"
            if abby_name:
                idk "Well as you said earlier, my name is Abby."
            else:
                abby "I'm Abby."
        "Get up.":
            "The girl does not respond."
            p1 "C'mon, stop crying and get up."
            "The girl slowly gets up and looks at you."
            "Her face is no longer angry and distorted, but she still looks unhappy.."
            idk "What do you want?"
            p1 "What is your name?"
            if abby_name:
                idk "Well as you said earlier, my name is Abby."
            else:
                abby "My name is Abby."
    label after_abby_hello:
        p1 "Well Abby, I'm not sure if you've noticed"
    p1 "But your haunting of this place is causing a lot of issues."
    abby "..."
    abby "I'm sorry."
    abby "As you've noticed, I'm dead."
    abby "I don't know how it happened exactly but..."
    abby "Sometimes I lose control, and become some sort of monster."
    p1 "I noticed."
    "There's a moment of silence."
    p1 "Well if you don't mind, I can try to help you out."
    abby "Really? You'd do that for me?"
    abby "...even after I freaked out on you?"
    menu abby_really:
        "What do you say?"
        "Of course.":
            abby "Wow, thanks!"
            "..."
            abby "So, um, what all are you going to do?"
            p1 "I'm going to have a look around and see if I can find any clues."
            abby "Clues?"
            p1 "As to how you died."
            abby "Oh..."
            p1 "And of course, if you remember anything that would be very helpful."
            abby "Right, I'll do my best."
        "On second thought...":
            p1 "Let me do my job."
            abby "Oh...ok."
            abby "Just, um, let me know if you need me..."
    label after_abby_really:
        "Now then, where to start..."
        "I don't have too much time."
        "I can probably only look at 4 rooms."
    menu sub_ghost_look:
        "Go to..."
        "Guest Bedroom":
            "Place."
        "Master Bedroom":
            "Place."
        "Nursery":
            "Place."
        "Kitchen":
            "Place."
        "Living Room":
            "Place."
        "Dining Room":
            "Place."
        "Garage":
            "Place."

    # This ends the game.

    return
