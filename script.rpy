﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# stp cursing - fiona

# Generic
define idk = Character("???")
define p1 = Character("You")

# Ghosts
define abby = Character("Abby")
image A_P = "Abby_place.png"
define magnus = Character("Magnus")
image M_P = "Magnus_place.png"
define hugh = Character("Hugh")
image H_P = "Hugh_place.png"
define malerie = Character("Malerie")

# Side Characters
define ll = Character("Landlord")
define jared = Character("Jared")
define sean = Character("Sean")
define mrs = Character("Ms. Wadell")

# Backgrounds
image office = "office.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene office
    play music "detective.wav" loop

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
        idk "My name is Jared, my wife and I just moved into a new home."
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
            jared "There was only one previous owner, a woman named Abby, she lived with a roommate before it was sold to us."
            $ abby_name = True
            p1 "Anything else?"
    label after_jared_call_questions:
        jared "Do you think you could come take a look?"
    menu jared_call_final_question:
        "Say..."
        "Of course, I'll need the night alone to look around.":
            jared "Perfect, we're already at a Hotel. When can you come?"
            p1 "I'll be right over."
            jared "Thank you, thank you! Call me if you need anything, /he Repeats his Phone Number for you/"
        "I don't think so.":
            "I really need this job..."
            jump jared_call_final_question
    label after_jared_call_final_question:
        "Time to paranormal the investigate"
    "You get into your Sedan, loaded up with some of the essentials, and drive to the address..."

    stop music fadeout 1.0
    play music "house.wav" loop

    scene bg room # Entryway

    "Time to take a look around, a Cold-spot is an easy sign to look for in a heated building..."
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
    show A_P
    "A woman wearing a bloodstained wedding dress floats through the door."
    idk "COME BACK TO BREAK MY HEART?!"
    menu abby_hunt:
        "What do you do?"
        "Hide":
            menu abby_hide:
                "Where do you hide?"
                "Hall Closet":
                    hide A_P
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
                            show A_P
                            jump after_abby_hunt
                "Master Bedroom":
                    hide A_P
                    "You quickly rush to the master bedroom, closing the door and hiding behind the bed."
                    # play sound "abby_hum.mp3"
                    "You hear someone humming outside, a sound that seems to be getting closer."
                    "The door creaks open as the humming stops."
                    "The room is silent..."
                    # play sound "abby_screech.mp3"
                    "The ghost appears in front of you and goes to attack."
                    jump abby_hide
                "Guest Bedroom":
                    hide A_P
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
            # some money variable idk
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
            "The ghost slowly calms down with a twisted look of realization, and pathetically collapses on the ground."
            # play sound "abby_cry.mp3"
    label after_abby_hunt:
        # Wowza (wowza)
        "You look at the strange ghost woman crying on the ground."
    "You notice the temperature is no longer freezing, colder than the surrounding rooms- but bearable."
    menu abby_hello:
        "What do you say?"
        "Hello?":
            "She looks up at you, her face no longer angry and distorted, but entirely distraught."
            if abby_name:
                idk "h-h-hello?"
                p1 "Hi. What's your name?"
                abby "..."
                abby "Well as you said earlier, my name is Abby."
            else:
                abby "Abby. My name is Abby."
        "Are you OK?":
            if abby_name:
                "Abby nods without looking up."
                p1 "Did I hurt you?"
                "There's no response."
                "Slowly Abby stands up and looks at you, her face no longer angry and distorted, but confused, maybe annoyed, you can't really tell you don't talk to many girls.."
                abby "Hi..."
                p1 "Who are you?"
                abby "Well as you said earlier, my name is Abby."
            else:
                p1 "Did I hurt you?"
                "There's no response."
                "Slowly the girl stands up and looks at you, her face no longer angry and distorted, but confused, maybe annoyed, you can't really tell; you don't talk to many girls.."
                p1 "who are you?"
                abby "I'm Abby."
        "Get up.":
            if abby_name:
                "Abby does not respond."
                p1 "C'mon, Abby, please stop crying and get up."
                "Abby Looks up at you hopelessly while sobbing, eventually resolving enough to hold back her ghastly tears and stand"
                "Her face is no longer angry and distorted, but she still looks unhappy..."
                abby "What do you want?" 
                p1 "What is your name?"
                abby "Well as you said earlier, my name is Abby."
            else:
                "The girl does not respond."
                p1 "C'mon, stop crying and get up."
                "The girl slowly gets up and looks at you."
                "The girl burrows her face into her arms even more initially, but is finally resolved enough to face you, and slowly gets up, looking at you."
                "Her face is no longer angry and distorted, but she still looks unhappy.."
                idk "What do you want?"
                p1 "What is your name?"
                abby "My name is Abby."
    label after_abby_hello:
        p1 "Well Abby, I'm not sure if you've noticed"
    p1 "But your haunting of this place is causing a lot of issues."
    abby "..."
    abby "I'm sorry."
    abby "As you've noticed, I'm dead."
    p1 "/you nod moronically like this is new information/"
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
            "She might be able to help me."
            jump abby_really
    label after_abby_really:
        "Now then, where to start..."
    "I don't have too much time."
    "I can probably only look at 4 rooms."
    $ sub_rooms = 4
    $ found_sledge = False
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
                    "The knife block you noticed was empty earlier, now has a single *look up knife type* knife occupying one of the slots." # whatever micheal myers has
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
    hide A_P
    "Something about traveling"

    stop music fadeout 1.0
    # office
    scene office

    play music "detective.wav" loop
    # "CONFIRMING THAT NOTHING IS BROKEN AND THE GAME CAN END"

    "Well that was certainly interesting." # goofy ahh
    "I'll have to think about how to handle the situation."
    "I can let Abby stay there, but I don't think I'll get paid." # romance options later (just kidding) (not really) (:3)
    "I can exorcise her, which would kill her but I'd get paid." # no loyalty
    "I do have the materials to free her, but only enough to do it once. (I might need it for future jobs.)" # this makes no sense
    "Let me sleep on it..."
    # fade or something???

    scene office

    "What a beautiful morning" # it's raining
    "Time to think about what happened yester-"
    # play sound "phone_ring.mp3"
    "*ring ring*"
    "What now?"
    idk "Hello? Hello?" # fnaf-ahh dialogue 
    p1 "Hello, Paranormal Investigator's office."
    idk "Glad I got the right number, I require your services immediately!"
    p1 "How can I help you sir?"
    idk "Well how do you think?! I need a ghost gone."
    p1 "Ah, right." # internal monologue thinking that this guy is an ass
    sean "My name is Sean, I represent the state property bureau." # no idea what the real life equivilent is, IRS?
    sean "We're trying to bulldoze a property but our workers won't get near it. They claim its' \"haunted\""
    p1 "I see."
    menu sean_call_questions:
        "Ask..."
        "What sort of activity have they experienced?":
            sean "Do I look like I care?" # intentional
            sean "*audible sigh* Look all they said is that there was some sort of screaming?"
            sean "And apparently there's strange symbols being drawn on the walls."
            p1 "Have you verified these claims yourself?"
            sean "Well, um, no I didn't give them any validity."
            sean "However if having some ecto gumshoe check it out will speed this up then I'm all for it." # add deragatory term for Paranormal Investigator here
        "Do you have any records from the previous owner?":
            sean "The previous owner was a private corporation, don't remember the name."
            sean "They ran an insane asy- sorry, \"Mental Hospital\"."
            sean "Probably just did it for the government payouts but I'm not one to judge." # there's another word I'm thinking of here but can't recall it
            sean "Place got shut down in the mid 1900s due to health violations."
            sean "There were so few regulations I'm sure that wasn't unfounded."             
    label after_sean_call_questions:
        sean "Anyways, enough of this chit-chat. Can you come out here?"
    p1 "Of course, I'll head out right now."
    "more traveling dialogue"

    stop music fadeout 1.0
    play music "hospital.wav" loop

    scene bg room
    "You arrive at the old \"mental hospital\"."
    "There's a sign out front that's overgrown with vines, it's text having faded over the years."
    "Damn this place looks spooky..." # average phasmo player doing apoc challenge on sunnyside
    menu mental_first_look:
        "Go to..."
        "Reception":
            "There's an old wooden desk decaying in the middle of the room."
            "Vines and moss cover the walls adn the broken wooden floordboards."
            "Something makes me think no one's kept this place up." # wow what a zinger
        "Solitary Confinement":
            "It's a white padded room, but the padding is all ripped and stained."
            "Eerily quiet here..."
        "Staff Room":
            "A very cramped room. There's a small round table and a single chair in the corner."
            "There's a cupboard full of various medical supplies, miracle it hasn't been looted by now."
        "Examination Room":
            "A sqaure room with tile walls. There's a single examination chair in the center."
            "There's a pool of dried blood at the feet of the chair, and the chair itself has quite a few...scratch marks?"
            "As you turn to leave you notice the same scratch marks on the walls and door."
    label after_mental_first_look: # this next part feels way too long but idk
        "After investigating osme of the main rooms you begin inspecting some of the patient \"rooms\"."
    "You're unsure if it's merely the age and state of the buildings but the rooms look more like prison cells...barebone cells at that."
    "You come across a room whose door has numerous white scratches and markings."
    "The little window on it is blacked out as well."
    "After a moment of hesitation (this place is *really* creepy after all), you open the door and step inside."
    "You're immediately met with a blast of cold air."
    "You begin to step inside when the room is engulfed in fire."
    "An inhuman scream comes out of nowhere as the fire rages closer to you."
    show M_P
    "Then, out of the flames the ghostly form of a young man rises."
    idk "YOU TOO SHALL BURN FOR WHAT YOU DID"
    menu magnus_hunt:
        "What do you do?"
        "Hide":
            menu magnus_hide:
                "Where do you hide?"
                "Staff Room":
                    hide M_P
                    "You rush back to the staff room and crouch under the little table."
                    idk "YOU...WILL...BURN"
                    "..."
                    idk "COME...BACK...*cough*...HERE"
                    "You hear violent coughing outside."
                    idk "I...*cough*...WON'T...*cough*...LET-*cough*"
                    "*thud*"
                    idk "*groan*"
                    show M_P
                    "You slowly open the door and see the ghostly man curled up on the ground in a coughing fit."
                "Examination Room":
                    hide M_P
                    "You turn the corner and go into the examination room."
                    "There's not much to hide behind besides the chair, better than nothing."
                    idk "THE FIRE...WILL...CONSUME YOU"
                    show M_P
                    "The door flies open and the ghostly man is standing there, fire all around his body."
                    idk "YOU...WON'T...DO IT...AGAIN"
                    "He charges at you but you're able to roll out of the way and run out the door."
                    hide M_P
                    jump magnus_hide
                "Solitary Confinement":
                    hide M_P
                    "You run back to the solitary confinement room."
                    "Shutting the door behind you, you realize that there's nothing to hide behind in here..."
                    idk "WHY...WON'T...YOU...BURN"
                    "The footsteps are getting closer."
                    idk "I...CAN'T...DIE...THIS...WAY"
                    "The ghost pounds on the door."
                    idk "DON'T...*cough* LEAVE ME...*cough*"
                    "He continues pounding on the door."
                    idk "*cough cough* THE FIRE...IT HURTS..."
                    "The pounding on the door stops."
                    show M_P
                    "You cautiously open it and find the ghostly man leaning against a wall, coughing uncontrollably."
        "Attack (uses money)":
            "You whip out your incense and quickly light it."
            "The smoke coming from it causes the ghost to stumble back."
            idk "WHAT ARE...*cough* YOU DOING?!"
            "The ghost doubles over coughing."
            idk "THE FIRE, THE SMOKE, NEVER AGAIN"
            "He screams and collapses."
        # invoke name? Idk how that'd come up
    label after_magnus_hunt:
        p1 "Hey there."
    idk "*cough* What do you want?"
    p1 "For starters, what's your name?"
    idk "Why should I tell you?"
    p1 "Because I'm here to get rid of the ghost haunting this place, I assume that's you?"
    "He gives you murderous look."
    p1 "Now we can do this the easy way, or we can do this the hard way." # pretty much bluffing
    magnus "Fine, my name is Magnus. Can you go away now?"
    p1 "Nice to meet you Magnus, and no, I won't."
    "..."
    p1 "Magnus, do you remember how you died?"
    magnus "What? No, I don't."
    magnus "All I remember is...burning. Flames eating away at my flesh."
    p1 "Were you here when you died, or somewhere else?"
    magnus "How the hell would I know?!"
    p1 "...alright. I'm gonna look around; you're welcome to come with me."
    "He rolls his eyes."
    # add something about only having time to look at 3 rooms
    $ patient_book = False
    $ mental_rooms = 3.
    $ found_papers = False
    menu mental_ghost_look:
        "Go to..."
        "Reception" if mental_rooms > 0:
            $ mental_rooms -= 1
            "You walk back to the front reception room."
            magnus "Why are you over here? There's nothing interesting."
            p1 "You'd be surprised."
            "He scoffs."
            menu mental_recep_look:
                "Investigate..."
                "Receptionist's Desk":
                    $ patient_book = True
                    "You examine the old, wooden desk. It's somehow still standing despite it's age."
                    "You open one of the drawers with a screech; there's a binder inside."
                    p1 "What's this..."
                    "Opening the binder you find it's a list of patients admitted to the hospital."
                    "Magnus peers over your shoulder."
                    magnus "What's that?"
                    p1 "I thought you weren't interested?"
                    magnus "Shut up."
                    p1 "It's a list of patients."
                    magnus "Am I in there?"
                    "You flip through it looking for his name."
                    p1 "Indeed you are, Magnus H."
                    magnus "Does it say what I was sent here for?"
                    p1 "\"Aggressive tendencies, prone to outbursts of anger.\""
                    magnus "...that's it?"
                    p1 "Says here that you injured several family members."
                    magnus "...I...didn't remember that."
                    "He regains his composure."
                    magnus "I'm sure they deserved it anyways."
                    jump mental_recep_look
                "Stack of Papers":
                    "You sift through the stack of yellowed paper on the floor."
                    "It seems to be a mix of medical notes and strange black symbols."
                    p1 "Any of these look familiar?"
                    magnus "Not paticulary."
                    "One sheet catches your eye."
                    p1 "Here we go, Magnus H., October 30th, 1904."
                    p1 "\"Brought the patient in for the daily injection, preparing him for the...ritual...\""
                    magnus "Ritual?"
                    p1 "\"Patient resisted but staff calmed him down with the usual method.\""
                    p1 "\"Injection was not recieved well, patient screamed, convulsed, etc.\""
                    p1 "\"All is ready for tomorrow.\""
                    magnus "...and?!"
                    p1 "The rest is covered by the black symbols."
                    magnus "..."
                    jump mental_recep_look
                "I'm done in this room.":
                    jump mental_ghost_look
        "Examination Room" if mental_rooms > 0:
            $ mental_rooms -= 1
            "You walk into the Examination Room."
            magnus "Even as a ghost, I've always hated this room..."
            menu mental_exam_look:
                "Investigate..."
                "Examination Chair":
                    "You look at the chair with scratches on it."
                    p1 "Do you know how it got like this?"
                    if found_papers:
                        magnus "Me or someone else must've been trying to escape."
                        magnus "I wonder if that burning feeling I have relates to this."
                    else:
                        magnus "Not really."
                        magnus "I must've been in here at some point, since I always feel uncomfortable in here."
                        p1 "I'm sure the blood on the floor doesn't help."
                    jump mental_exam_look
                "Instruments Table":
                    "There's a little cart/table with medical instruments on it."
                    "Under it there's a notebook."
                    "You open it up and flip through it."
                    p1 "Looks like a diary of some sort."
                    magnus "Ha, what loser here kept a diary?"
                    p1 "A doctor, from the looks of it."
                    p1 "\"The ritual is almost ready. We've been injecting Magnus daily for the past month.\""
                    p1 "\"As much as it goes against my oath as a doctor, my devotion to the Dark Father is more important.\""
                    magnus "Dark father? These guys were more psycho than I was."
                    jump mental_exam_look
                "I'm done in this room.":
                    jump mental_ghost_look
        "Solitary Confinement" if mental_rooms > 0:
            $ mental_rooms -= 1
            "You walk into the Solitary Confinement room."
            "It's eerily silent."
            magnus "Those voices...I wonder whose they are..."
            "You don't hear anything."
            menu mental_confine_look:
                "Investigate..."
                "Walls":
                    "As you approach the walls, strange symbols appear, as if being etched in by a knife."
                    p1 "Odd..."
                    p1 "Recognize any of those?"
                    magnus "Nah."
                    "How helpful..."
                    "The symbols all appear to have a similar design; an X with a circle in the middle."
                    jump mental_confine_look
                "Floor":
                    "The floor, that was white, albeit with rips, earlier seems to turn deep red where Magnus steps."
                    p1 "Hey, you notice that?"
                    magnus "Huh?"
                    p1 "The floor, when you step on the floor in here you leave blotches of red behind."
                    magnus "Oh...cool?"
                    p1 "It means you have a connection to this room, I'd assume, but I don't know what that connection would be."
                    magnus "Some investigator you are."
                    jump mental_confine_look
                "I'm done in this room.":
                    jump mental_ghost_look
        "Staff Room" if mental_rooms > 0:
            $ mental_rooms -= 1
            "You walk into the Staff Room."
            p1 "Remember this room?"
            magnus "Pft, never even came in here, at least, I don't remember it."
            menu mental_staff_look:
                "Investigate..."
                "Medical Cabinet":
                    "You open the wooden cabinet to reveal all sorts of medicine."
                    "Most of the labels appear to be scratched off, probably not very safe."
                    p1 "I wonder what these are for."
                    magnus "You're the investigator."
                    p1 "An investigator, not a doctor." # lol
                    "You notice a slip of paper behind the pill bottles and syringes."
                    p1 "\"NERVE STIMULANT\". That doesn't sound very pleasant."
                    p1 "\"RITUAL\"..."
                    # could probably add more here
                    magnus "What kind of drug is that?"
                    p1 "I don't know, better keep looking."
                    jump mental_staff_look
                "Patient List":
                    "You notice a list of patients on a piece of paper lying on the table."
                    "It's a table showing each patient's reaction to different drugs."
                    p1 "\"ALEXANDER - NERVE STIMULANT - DECEASED\""
                    p1 "\"EMILY - OPTIC SEVERANCE - DECEASED\""
                    p1 "\"MAGNUS - RITUAL - THE FATHER IS PLEASED\"" # fc5 vibes
                    magnus "What the hell did they do to me..."
                    jump mental_staff_look
                "I'm done in this room.":
                    jump mental_ghost_look
        "Room 39" if mental_rooms > 0:
            $ mental_rooms -= 1
            if patient_book:
                "You walk into the room that was noted as being Magnus'."
            else:
                "This is the room where Magnus appeared."
            magnus "Hey, this is, er, was my room."
            p1 "Brilliant detective, you're going to put me out of a job."
            "Magnus gives you a harsh look."
            menu mental_39_look:
                "Investigate..."
                "Bed":
                    "You look at the barebones bed."
                    "It's a thin matress on a cheap metal frame."
                    magnus "Top notch accomodations."
                    "You notice a metal U-shaped object attached to the wall next to the bed." # like somewhere where you'd attach a chain
                    "Across the room is a length of bloodied chain."
                    p1 "I'm guessing these two go together."
                    magnus "..."
                    p1 "Guess they didn't want you escaping. Still, seems like overkill."
                "Scorch marks":
                    "You notice scorch marks all over the walls."
                    p1 "How could these have gotten here?"
                    if patient_book:
                        magnus "Could it have...nah that's stupid."
                        p1 "What?"
                        magnus "The ritual, the chain, the drugs they gave me."
                        magnus "And, the burning feeling I have, like I'm constantly on fire."
                        magnus "You think those are tied together?"
                        p1 "Wouldn't surprise me, but hard to say for sure."
                        magnus "Right..."
                    jump mental_39_look
                "I'm done in this room.":
                    jump mental_ghost_look
        "I'm out of time" if mental_rooms == 0:
            p1 "Looks like I'm out of time."
    label after_mental_ghost_look:
        magnus "Finally."
    p1 "I'll be back at the end of the week."
    magnus "What for? Gonna try and help me remember more of the awful things that happened to me?"
    p1 "Something like that." # smirking
    magnus "Well....see you."
    hide M_P
    "Magnus walks away."
    "Traveling text :3"

    stop music fadeout 1.0
    play music "detective" loop

    scene office
    "Yet another thing to worry about."
    "Time to get some sleep..."

    scene office
    "Hopefully I have some time to think about the cases tod-"
    # play sound "ring.mp3"
    "*ring ring*"
    "One day I'll get a break..."
    p1 "Hello?"
    idk "HEY!"
    "Ow...that was loud."
    p1 "Y-yes?" # wincing
    idk "CAN YOU HEAR ME?"
    p1 "YES I can hear you."
    "It's an eldery lady."
    idk "GOOD!"
    idk "ARE YOU A GHOST HUNTER?"
    p1 "Um, you could say that."
    p1 "I'm more into the investi-"
    idk "PERFECT! THE YELLOW PAGES NUMBER WAS CORRECT THEN."
    p1 "..."
    idk "I HAVE A GHOST PROBLEM SON, AND I NEED IT FIXED ASAP."
    p1 "Could I get your name?"
    mrs "JANE WADELL, BUT YOU CAN CALL ME MS. WADELL."
    menu mrs_call_questions:
        "Ask..."
        "Do you have examples of the activity?":
            mrs "EXAMPLES? HMM."
            mrs "WELL I RUN THIS CAMPSITE YOU SEE."
            "You turn the volume down, it's starting to really hurt your ear." # whenever bendy joins a call
            mrs "The campers are complaining about all sorts of random crap."
            mrs "Something about blue fire? And axes floating around?"
            mrs "Wouldn't have cared until something REAL strange happened last night."
            mrs "I was sitting in my trailer, on property, when all of the sudden the windows were blacked out!"
            mrs "Then there was this awful screaming, like a man was being chopped to bits."
            mrs "I knew there was something up, so that's why I need you to come take a look."
        "Has anyone owned your property previously?":
            mrs "WELL IT'S A CAMPSITE YOU SEE."
            "You turn the volume down, it's starting to really hurt your ear."
            mrs "My dad bought it back in the 70s, not sure who owned it previously."
            mrs "As far I can tell it was just woods."
            mrs "There was supposedly a cabin from the 1800s there at some point, but I don't remember ever seeing it."
    label after_mrs_call_questions:
        mrs "Is that all you need?"
    p1 "Should be. Is it OK if I come over now?"
    mrs "Of course, the sooner this is dealt with the better."
    "traveling here"

    stop music fadeout 1.0
    play music "campfire.wav" fadein 2.0
    scene bg room

    "You arrive at the campsite in the evening after a long travel time." # dont like the phrasing here
    "Not as many places to check out as the previous locations, hopefully this will be easier." # is this weird?
    menu camp_first_look:
        "Go to..."
        "Campfire":
            "There's a spot for a campfire with logs for sitting around it."
            "It's a nice little setup, perfect for making smores."
        "Ranger Station":
            "A ranger station sits a little distance away from the campfire."
            "Presumably there'd be a park ranger here, but none seems to be on duty."
            "You wonder if the ghosts drove them away."
        "Trailer":
            "This is the trailer Ms. Wadell was talking about."
            "The windows don't appear to be blacked out, must've been from the ghost."
        "Cemetary":
            "You notice a little cemetary away from everything else."
            "A giant weeping willow tree stands above a few tombstones."
    label after_camp_first_look:
        "You start walking back to your car to get ghost detection equipment."
    "As you pass the campfire circle, a fire suddenly roars to life."
    "You stare at it for a second, confused as to what started it."
    show H_P
    "The fire then turns blue, and a man manifests in it."
    idk "WHO ARE YE WHO DARES TO ENTER MY DOMAIN."
    idk "I HAVE DONE NOTHING WRONG, BEGONE!"
    "You hesitate, this ghost does not seem as aggresive as the others."
    "An axe flies by your head."
    idk "I WILL NOT FALL VICTIM TO YOUR FALSE CLAIMS AGAIN!"
    menu hugh_hunt: # naming probably inconsistent but idc
        "What do you do?"
        "Hide":
            menu hugh_hide:
                "Where do you hide?" # add vars so you cant repeat
                "Ranger Station":
                    hide H_P
                    "You run over to the Ranger Station and go inside."
                    "There's not much in here, so you hide under the bed."
                    "You hear heavy footsteps outside."
                    "The door flies open."
                    idk "WHERE IST THOU WHO SEEKS MY DOWNFALL?"
                    show H_P
                    "The bed you're hiding under is flung away, the man standing over you with his axe."
                    idk "YOU HAD THE CHANCE TO TAKE YOUR RETRIBUTION ELSEWHERE, NO YOU DIE!"
                    "He swings his axe but misses, and hits the wall instead."
                    "You take this opprotunity to run back outside."
                    jump hugh_hide
                "Trailer":
                    hide H_P
                    "You run into Ms. Wadell's trailer and duck behind a table."
                    "Heavy footsteps are heard outside."
                    idk "COME BACK AND FACE YOUR CRIMES!"
                    "The footsteps stop, and a loud crack noise is heard, followed by the man screaming."
                    menu hugh_step:
                        "What do you do?"
                        "Step outside.":
                            show H_P
                            jump after_hugh_hunt
        "Attack (uses money)":
            "You light your trusty incense and wave it around."
            "The smoke drifts torward the man and he recoils."
            idk "HOW DARE YOU CONTINUE TO PERSECUTE ME!"
            "The man continues walking forward, but stops short."
            "A loud crack noise is heard and he screams."
            jump after_hugh_hunt
    label after_hugh_hunt:
        "The man is holding his head and shaking it back and forth."
    idk "Why...I never...I wouldn't..."
    "He drops his hands and hangs his head in shame."
    idk "Aye, I am beat."
    menu hugh_question:
        "Ask..."
        "What happened?":
            idk "I...don't know."
            idk "All I remember is sudden darkness, a sharp pain in my head, and then I woke up like this."
            "He gestures to the axe in his head."
            hugh "My name is Hugh, by the way."
            p1 "Nice to meet you."
            hugh "And you."
        "Who are you?":
            hugh "My name is Hugh, I was a lumberjack in these woods for many-a-year."
            p1 "Pleasure to meet you Hugh."
            hugh "And you."
    label after_hugh_question:
        hugh "May I inquire as to why you're here?"
    p1 "I was hired to investigate the hauntings here."
    hugh "Aye, that'd be me."
    p1 "What I find is that hauntings are usually tied to the ghost's death."
    p1 "Do you remember how you died?"
    hugh "Sadly not, besides it having to do with the axe in my head."
    p1 "Right."
    p1 "In that case, let's take a look around."
    hugh "Sounds good to me."
    $ camp_rooms = 2
    menu camp_ghost_look:
        "Go to..."
        "Campfire":
            $ camp_rooms -= 1
            "You walk over to the campfire."
            hugh "Sorry about earlier, don't know what came over me."
            p1 "No worries, it's part of the job."
            menu camp_camp_look:
                "Investigate..."
                "Campfire":
                    "You look at the logs that have been arranged for the optimal campfire."
                    "There's no scorch marks on them, despite the blue fire earlier."
                    p1 "What's your relation to fire?"
                    hugh "Eh?"
                    p1 "Do you remember dying by fire? Or starting any notable ones?"
                    hugh "No, I don't think so. Fire was merely a way to warm oneself."
                    jump camp_camp_look
                "Logs":
                    "There's 4 logs in a circle around the campfire."
                    "They all look very old."
                    "Next to one appears to be a very old lamp."
                    p1 "What's this?"
                    hugh "That's my trusty lamp!"
                    p1 "You remember it?"
                    hugh "How could I not? It guided me through many a dark night."
                    p1 "I see..."
                    "You notice a crack in the glass."
                    p1 "Do you know how this got broken?"
                    "Hugh examines it."
                    hugh "Must've been thrown or something, I can't imagine how it'd get that way with normal usage."
                    jump camp_camp_look
                "I'm done in this area.":
                    jump camp_ghost_look
        "Ranger Station":
            $ camp_rooms -= 1
            "You walk into the ranger station."
            # add var text from hunt
            p1 "This place familiar?"
            hugh "Doesn't seem to be."
            menu camp_ranger_look:
                "Investigate..."
                "Desk":
                    "You go over to the desk."
                    "There's a bunch of papers here, most appear to be forms and memos."
                    hugh "What is all of this?"
                    p1 "Just ranger stuff it seems."
                    "You check the drawers, and in one of them is a mini bouquet of flowers."
                    "It's three yellow flowers tied together with some sort of cord." # find actual flower name
                    hugh "I remember those."
                    hugh "They were for my little girl; she died of the fever when she was a child."
                    hugh "..."
                    hugh "I meant to put these on her grave out there, but I never got the chance."
                    jump camp_ranger_look
                "Pinboard":
                    "You walk up to the pinboard."
                    "It's filled with various notices and info."
                    "One in paticular catches your eye, it's a very old newspaper clipping."
                    p1 "\"Revisiting the site of the 1872 Lumberjack Murder\"."
                    "Most of it is cut out or faded, but you can make out small parts of it." # dont like the phrasing
                    p1 "\"Mob of people...suspected serial killer...child missing.\""
                    hugh "Is that about me? Is that how I died?"
                    p1 "It seems very likely."
                    "Hugh looks on sadly."
                    jump camp_ranger_look
                "I'm done in this room.":
                    jump camp_ghost_look
        "Trailer":
            $ camp_rooms -= 1
            "You walk into the trailer."
            hugh "Hey, I was just here earlier."
            p1 "Ah, you were haunting Ms. Wadell right?"
            hugh "Some old lady, yes. Something about her name seemed...familiar."
            p1 "Let's see if we can find anything then."
            menu camp_trailer_look:
                "Investigate..."
                "Table":
                    "You look at the table." # this sounds stupid
                    "It's covered with random papers and documents, most relating to the campsite property."
                    p1 "Looks like Ms. Wadell is struggling to pay for the property's upkeep."
                    "There's a yellowed envelope in the pile, addressed to \"WADELL\". It has a stamp from the 70s on it."
                    hugh "Well, aren't you going to open it?"
                    p1 "Um, I think that's illegal..."
                    hugh "I'll do it then, they can't prosecute a ghost anyways."
                    "Hugh opens the envelope and pulls out a very old letter, appearing to have been typed on a typewriter."
                    hugh "\"Dear Mr. Wadell, I pray my letter reaches you in time. You do not understand what curse lies on that property.\""
                    hugh "\"I cannot elaborate too much, as I'm afraid I do not know the whole story, but I do know this much:\""
                    hugh "\"Your family name will reawaken a great injustice that was done many years ago.\""
                    hugh "\"If you wish for your family's safety, DO NOT PURCHASE THAT PLOT OF LAND.\""
                    p1 "So the name \"Wadell\" apparently has something to do with it."
                    p1 "Unfortunate that they bought it anyway..."
                    jump camp_trailer_look
                "Photo on the wall":
                    "There's an old family photo on the wall."
                    "Pictured is what you assume is the Wadell family when the bought the property in the 70s."
                    "Behind them is a log cabin and a campfire."
                    p1 "Assuming that's the same campfire, the cabin should be right around here."
                    hugh "They must've demolished it...that was my house you know."
                    jump camp_trailer_look
                "I'm done in this room.":
                    jump camp_ghost_look
        "Cemetary":
            $ camp_rooms -= 1
            "You walk over to the cemetary."
            hugh "What a solemn place."
            hugh "I wonder if anyone ever visits it, or takes note of the tombstones."
            menu camp_cemetary_look:
                "Investigate..."
                "Tombstones":
                    "There's a few tombstones scattered around the old willow tree."
                    "Most have their names etched off, except a small one that reads \"EMILY\"."
                    hugh "That was my...wee daughter."
                    hugh "Her mother passed from the fever during the winter, so it was just me and her for a while."
                    hugh "One time in the summer, we were out in the woods cutting down some trees when she collapsed."
                    hugh "I tried to get a doctor to come look at her, but they thought I was cursed."
                    hugh "I...I couldn't do anything..."
                    p1 "..."
                    # add var text if they saw the flowers earlier
                    jump camp_cemetary_look
                "Willow Tree":
                    "You walk around the weeping willow tree, looking for any markings."
                    "The only one you can find is a crude \"W\" on the back."
                    p1 "W for Wadell maybe?"
                    hugh "Perhaps. But why is that the only one?"
                    p1 "I'm afraid I don't know."
                    # feel like there should be more here
                    jump camp_cemetary_look
                "I'm done in this area.":
                    jump camp_gho
        "I'm out of time.":
            p1 "Well it looks like I'm out of time Hugh."
    label after_camp_ghost_look:
        hugh "Aye, it is getting quite late."
    hugh "I appreciate you coming out here, trying to help and all."
    p1 "No problem, I'll be back at the end of the week. Hopefully with a solution."
    hugh "Thank you kindly."
    hide H_P

    "Traveling"
    
    scene office
    "I feel bad for Hugh."
    "I don't know exactly what happened, but the name Wadell definitely meant something."
    "Time to rest, gotta start thinking about how to handle all these things."

    scene office
    "TOP O' THE MORNING TO YA"

    # This ends the game.

    return
