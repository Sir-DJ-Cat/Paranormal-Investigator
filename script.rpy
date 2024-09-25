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
    $ sub_rooms = 4
    menu sub_ghost_look:
        "Go to..."
        "Guest Bedroom" if sub_rooms > 0:
            $ sub_rooms -= 1
            "You walk into the Guest Bedroom."
            abby "I wasn't in here that much..."
            p1 "Do you remember who stayed in here?"
            abby "Hmmm..."
            "She takes a look around, looking for some object to jog her memory."
            "Abby stops and stares at the circular red carpet beneath the bed."
            abby "I remember that..."
            p1 "What is it?"
            abby "This was my friend's room. We shared the house."
            abby "I told her the carpet was too small and didn't match the paint."
            p1 "..."
            abby "That's probably not very helpful..."
            p1 "Maybe we could find your friend? She might know more about your death."
            abby "Maybe...I don't remember her ever coming back after I died."
            jump sub_ghost_look
        "Master Bedroom" if sub_rooms > 0:
            $ sub_rooms -= 1
            "You walk into the Master Bedroom."
            abby "I know this room, it's mine!"
            "..."
            abby "Or was..."
            "You notice the writing on the wall that Jared had mentioned earlier."
            p1 "Let's take a look around."
            menu sub_master_look:
                "Investigate..."
                "Dresser":
                    "This dresser is made of antique wood."
                    "Inside the back of the top drawer there appears to be a clothing tag."
                    abby "Hey, that's mine."
                    p1 "What?"
                    abby "The tag for my wedding dress."
                    p1 "Oh..."
                    "The tag has a company name you've never heard of on it."
                    jump sub_master_look
                "Nightstand":
                    "The nightstand seems quite old."
                    abby "I didn't have a safe, so this is where I'd keep my valuables."
                    "The drawers, however, are empty."
                    abby "Man, I really thought there'd be something in there..."
                    "..."
                    abby "Wait! Pull it out!"
                    p1 "???"
                    abby "The dresser, pull it out from the wall."
                    "Your weak body somehow manages to pull the dresser away from the wall."
                    abby "Look on the back."
                    "There's a small, rectangle indent on the back."
                    "You push it in and it falls out, revealing a hidden compartment."
                    abby "Aha! I told you."
                    "You reach in there and pull out a small diamond wedding ring."
                    abby "..."
                    p1 "Is that yours?"
                    abby "It *was*."
                    abby "Guess I never got to wear it." # this is so lame but I can't write
                    "THIS IS TEXT REMINDING LUKE TO ADD VAR TEXT IF THEY FIND THE LOCKET FIRST"
                    jump sub_master_look
                # maybe one more place to check out here?
                "I'm done in this room.":
                    jump sub_ghost_look
            # that ends the master bedroom
        "Nursery" if sub_rooms > 0:
            $ sub_rooms -= 1
            "You walk into the Nursery."
            abby "Aw, how cute."
            p1 "You realize you were haunting this earlier, right?"
            abby "Yeahh, but that wasn't *really* me."
            abby "..."
            abby "Was it?"
            p1 "Let's look around."
            menu sub_nursery_look:
                "Investigate..."
                "Crib":
                    "It's a small, light blue crib. Appears to be new."
                    abby "Aw, look at this little crib."
                    p1 "Recognize it?"
                    abby "No, but I like it."
                    p1 "..."
                    abby "I always wanted to have kids."
                    abby "Too bad I was...you know."
                    jump sub_nursery_look
                "Bookshelf":
                    "It's a light blue bookshelf, smaller than a normal one would be."
                    abby "This looks nice. I wonder what books will be in there."
                    p1 "Doesn't seem too relevant."
                    abby "I guess not..."
                    "As you turn away, a glint from underneath it catches your eye."
                    "You crouch down and see a small chain sticking out from underneath the bookshelf."
                    "The chain is pulled out and is revealed to be attached to a locket."
                    abby "Hey, that's my locket. I thought I lost it."
                    p1 "Lost it?"
                    abby "The day of my wedding I lost my locket...I don't remember much after that."
                    "You open it up and see a picture of a man and Abby next to each other. It looks like a professional photo."
                    # play sound "abby_screech.mp3"
                    "You turn around to see Abby transformed back into the monster you saw earlier."
                    abby "YOU DARE SHOW YOUR FACE HERE?"
                    abby "DID YOU NOT GET YOUR HAPPILY EVER AFTER?"
                    p1 "Abby calm down! I'm not who you think I am!" # this feels like a cop out but im tired
                    "Abby shifts back to normal and looks down, ashamed."
                    abby "I'm sorry, I don't know what came over me."
                    p1 "I think it was this picture."
                    abby "The one of me and my...fiance..."
                    p1 "Do you think he was the one who killed you?"
                    abby "I-I-I don't know."
                    abby "Why would he?"
                    p1 "..."
                    abby "I guess we'll...keep looking."
                    jump sub_nursery_look
                "I'm done in this room.":
                    jump sub_ghost_look
        "Kitchen" if sub_rooms > 0:
            $ sub_rooms -= 1
            "You walk into the Kitchen."
            abby "I used to love cooking, one of my many hobbies."
            p1 "You think you'd have left anything behind?"
            abby "Probably not...unless it's a utensil I probably ate it."
            $ knife_checked = False
            menu sub_kitchen_look:
                "Investigate..."
                "Knife block":
                    $ knife_checked = True
                    "The knife block you noticed was empty earlier, now has a single butcher knife occupying one of the slots."
                    p1 "Does that knife look familiar?"
                    abby "Not paticulary."
                    "You take the knife out and find the end dripping with blood."
                    p1 "How about now?"
                    "Abby looks down at the large bloodstain around her heart."
                    abby "It would make sense..."
                    "She trails off"
                    jump sub_kitchen_look
                "Cabinet":
                    "There's a row of cabinets above the countertop, each with a glass front."
                    "You notice that one, however, is missing that front."
                    p1 "How peculiar..."
                    "You peer inside and notice droplets of dried blood on the wood base."
                    if knife_checked:
                        p1 "Not much to go on, but seems to fit with the knife..."
                    else:
                        "I wonder what caused this..."
                    jump sub_kitchen_look
                "I'm done in this room.":
                    jump sub_ghost_look
        "Living Room" if sub_rooms > 0:
            $ sub_rooms -= 1
            "You walk into the Living Room."
            abby "I forgot what a cozy room this is."
            abby "I'm sure I left something in here."
            p1 "Let's look then."
            menu sub_living_look:
                "Investigate..."
                "Bookshelf":
                    abby "Too bad my books aren't here anymore."
                    "You examine at the old white bookshelf."
                    "The shelves are empty and covered in dust."
                    # idk what you'd find here
                    jump sub_living_look
                "Storage Chest":
                    "There's a strange brown chest hidden in the corner behind the couch."
                    p1 "What's this for?"
                    abby "I'm not sure, must've been a family heirloom or something."
                    "You tug on the chest's lid, but it won't open."
                    abby "Let me try."
                    "Abby puts her hand on the lid and it explodes open."
                    "Black mist swirls out of it as voices whisper and scream."
                    idk "LIES...BLOOD OF THE INNOCENT...LEFT FOR ANOTHER"
                    "As soon as it started, everything stops."
                    p1 "That seems...unusual."
                    "You cautiously peer inside the chest, and find a bouquet of black roses."
                    p1 "Were these roses always black?"
                    abby "I...do remember getting those."
                    abby "I don't know who gave them to me, but I hated them."
                    p1 "It seems they're trying to tell us something...but what..."
                    jump sub_living_look
                "I'm done in this room.":
                    jump sub_ghost_look
        "Dining Room" if sub_rooms > 0:
            $ sub_rooms -= 1
            "You walk into the Dining Room."
            "You're a bit uneasy after what happened the first time you came in this room."
            abby "Sorry did I put you on edge?"
            p1 "A little."
            menu sub_dining_look:
                "Investigate..."
                "Sliding Glass Door":
                    "You cautiously approach the sliding glass door."
                    "The cracks and blood from earlier are still there."
                    p1 "Do you remember anything of what happened here?"
                    abby "...the door was broken by someone."
                    abby "It was early in the morning."
                    abby "I came running out and they were standing in the shards."
                    abby "..."
                    abby "That's all I can remember, sorry."
                    p1 "No that's helpful."
                    if found_sledge:
                        p1 "I bet they used the sledgehammer we found in the garage."
                    else:
                        "We can try and find what they used to break it."
                    jump sub_dining_look
                "Table":
                    "You examine the wooden table, it's set for two."
                    abby "I had it set like this the day I died."
                    p1 "Are you sure?"
                    abby "Yes...I was planning to come back here after the wedding."
                    abby "I guess I never got a chance to leave though."
                    jump sub_dining_look
                "I'm done in this room.":
                    jump sub_ghost_look
        "Garage" if sub_rooms > 0:
            $ sub_rooms -= 1
            $ found_sledge = False
            "You walk into the Garage."
            abby "I never liked this place, always too cold."
            p1 "As garages tend to be."
            p1 "Let's take a look around"
            menu sub_garage_look:
                "Investigate..."
                "Toolbench":
                    "The red metal toolbench seems largely untouched."
                    abby "I'm not sure anyone's ever used this."
                    abby "...wait. No someone did use this."
                    p1 "Who?"
                    abby "I...I don't remember."
                    p1 "Hmm, let's keep looking."
                    jump sub_garage_look
                "Paint Cans":
                    $ found_sledge = True
                    "There's a bunch of empty paint cans sitting in the corner."
                    abby "I remember planning to paint the house."
                    abby "I don't think I ever got around to it though..."
                    "They seem to be arranged in a pyramid, as if concealing something."
                    "You take the top can off and put it to the side."
                    abby "What's that?"
                    "It appears to be a broken sledgehammer."
                    p1 "Were you planning to do some demolition as well?"
                    abby "No...I don't even remember buying that. Or having it in here at all."
                    p1 "By the way the cans were stacked, it seems someone was intentionally trying to hide it."
                    abby "But why..."
                    p1 "I'm not sure, let's keep looking."
                    jump sub_garage_look
                # another place maybe? or is 2 for each enough?
                "I'm done in this room":
                    jump sub_ghost_look
            # done with the garage
        "I'm out of time" if sub_rooms == 0:
            p1 "Looks like I'm out of time."
    label after_sub_ghost_look:
        abby "Oh...alright."
    abby "..."
    abby "Thanks for trying to help."
    abby "Really! I haven't had anyone to talk to since I, you know."
    p1 "No problem."
    abby "So what are you going to do now?"
    p1 "I'm going to think it over and come back at the end of the week with my decision."
    abby "Ok. See you then."
    "Abby smiles solemnly as you walk out the door."
    
    "Something about traveling"

    # office
    scene bg room

    "CONFIRMING THAT NOTHING IS BROKEN AND THE GAME CAN END"

    # This ends the game.

    return
