# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("[name]", what_color="#000")
define L = Character("LEGION", window_background="gui/textbox_cinematic.png", namebox_background="gui/namebox_cinematic.png", what_color="#fff")
define q = Character("???")
define m = Character("Marcy", what_color="#000")
define p = Character("Sir Cromwell")

# The game starts here.

label start:
    stop music fadeout 1.0
    scene black
    with Dissolve(0.5)
    pause 0.5
    "DISCLAIMER:"
    "This game is a horror game, and contains multiple descriptions of graphic violence and death."
    "Player discretion is advised."
    "Also."
    "This game is very unfinished."
    show legion normal
    with Dissolve(0.5)
    pause 0.2
    L "You are useless."
    L "Time and time again, you fail to know your place."
    L "So, we must remind you in the only way you'll understand."
    L "Henceforth, you are banished to the Realm of the Living."
    L "You will be given 1 week to gauge your utility to the Lord."
    L "Send as many souls to HELL as you can manage."
    L "We will evaluate you afterwards."
    L "If you satisfy us, you will regain your home in Pandaemonium."
    show legion glow
    L "Do you understand?"

menu:
    "Yes, sirs.":
        jump choice1_null
    
    "...":
        jump choice1_null

label choice1_null:
    $ menu_flag = True
    show legion normal
    L "Do not bother answering, worm."
    L "You have no say in the matter."
    L "Our words were clear; either you act as the demon you are..."
    L "Or you die."
    show legion glow
    L "Now, begone from here!"
    L "Your time starts now."
    hide legion
    jump rise

label rise:
    "Those were the words that sealed your fate."
    "That reafirmed your nature as a demon."
    "Cast out of hell and forced to accept it."
    "You have your mission."
    "Now it is time to ascend."

label chapter1_start:
    scene dirt
    show dark peril
    with Dissolve(0.5)
    "You feel dirt rushing all around you as you are propelled upward."
    "Every bone in your body is searing with pain."
    "Just as you think this torment will never end, you finally break ground, and pop up to the surface."
    scene forestnight
    show dark peril
    with Dissolve(0.5)
    "You groan, and try to prop yourself up, but..."
    "Your arm snaps under the pressure of your weight, causing you to collapse back to the dirt."
    "You scream out in agony."
    "Nobody hears you."
    "You cry for help."
    "Nobody hears you."
    "You whimper."
    "Nobody hears you."
    "..."
    "Then, as you think your fate is truly sealed..."
    "A set of footsteps begin approaching."
    scene black
    with Dissolve(0.8)
    "But you can't even muster the strength to celebrate as you fall unconscious."
    scene black
    show marcy down
    with Dissolve(0.5)
    "You come to in a bedroom."
    "Warm lighting flooding in from the window surrounds you as your eyes flicker open."
    "As you look around the room, you notice someone sitting at the edge of the bed you are on."
    "It appears to be a human woman, wearing a beige blouse and reading some sort of book."
    show marcy look
    "You let out a soft groan, feeling the throbbing ache of your injuries from last night. She notices."
    "Then, the girl begins talking to you."
    show marcy smile
    q "Oh! Wonderful! You are awake!"
    show marcy relieved
    q "I was worried you would never open those eyes of yours."
    "It seems this human was the one to save your life."
    "Their curious eyes stare into yours, inquiring."
    q "Can you speak? What is your name?"
    python:
        name = renpy.input("State your name.")

        name = name.strip() or "Az"
    
    y "M.... my name is [name]."
    q "[name], hm? That's quite a nice name."
    show marcy smile
    m "My name is Marcy. It is quite nice to meet you!"
    y "... Likewise, I suppose."
    show marcy worried
    m "You were quite battered up when I found you in the woods. What were you doing there?"
    menu:
        "Lie.":
            jump chapter1_2
    
        "Lie.":
            jump chapter1_2

    label chapter1_2:
        "You attempt to think of a realistic reason as to why you would be in the woods covered in dirt and bloody."
        y "I, uh..."
        y "Animals."
        y "Dogs. Rabid dogs."
        y "Very very bad dogs."
        show marcy look
        m "..."
        show marcy worried
        define marcy_trust = 1
        m "Oh, you poor thing! I knew Mr. Marcer's dogs were no good."
        show marcy relieved
        m "Worry not, friend. I am here to help."
        y "Much obliged."
        m "If you have any questions, don't feel afraid to ask."
        "This lady 'Marcy' seems very nice."
    label ask_marcy:
        menu:
            "What do you wish to ask her?"

            "Where am I?":
                jump choice_whereyouare
            "How badly wounded was I?":
                jump choice_howhurt
            "Who are you?":
                jump choice_whomarcyis
            "I have nothing else to ask.":
                jump chapter1_3
    
    label choice_whereyouare:
        show marcy look
        m "You really don't know where you are, hm?"
        show marcy worried
        m "Those dogs must have really done you in."
        show marcy lookoutside
        m "Well, you're currently in Westheim. This is an older village on the outskirts of Massachusets."
        m "As for where you are specifically, you're in my cabin."
        show marcy relieved
        m "Well, technically not *my* cabin. It's my brother's, but he's usually out serving in the military."
        show marcy smile
        m "So, I take care of it for him during the weeks he's gone."
        jump ask_marcy
    label choice_howhurt:
        show marcy worried
        m "Ugh, it makes me wince just thinking about it..."
        m "Your right arm was completely shattered, and you seemed to be bleeding from ever orifice possible."
        m "Also, severely malnourished."
        show marcy lookoutside
        m "So, I dragged you back here and spent the night patching you up, hoping you'd live."
        show marcy worried
        m "I wasn't sure if you would."
        show marcy relieved
        m "Thankfully, you seem to have healed the major injuries, and the bleeding has ceased."
        show marcy look
        m "Although, I must say... you did heal rather quickly."
        m "Most people that injured naturally take weeks to look like how you do now."
        jump ask_marcy
    label choice_whomarcyis:
        show marcy smile
        m "Well, I work as a nurse at the nearby hospital."
        m "Have been for a couple years now."
        show marcy relieved
        m "It ain't pretty work, but it does bring me comfort knowing that the stuff I do saves lives."
        show marcy smile
        m "I guess it's a good thing I encountered you of all people!"
        jump ask_marcy
    label chapter1_3:
        y "Regardless, thank you for saving me, Ms. Marcy."
        y "I am forever in your debt."
        show marcy relieved
        m "Hahahah... you're quite the character."
        show marcy smile
        m "You don't owe me anything at all, hun. I take care of people for a couple bucks a day."
        y "That concept is strange to me."
        show marcy look
        m "What concept?"
        y "Helping people."
        y "Where I come from, that is not common practice."
        y "If anything, it is highly frowned upon."
        show marcy worried
        m "...Helping people is taboo where you're from? Why?"
        y "Well, at my home, it is an 'Every Man for Himself' kind of mentality."
        y "Either be wicked or weak."
        y "I... was too weak, so I was forced to leave."
        y "And I cannot return there unless I once again prove myself."
        m "Ah, I.... I see."
        show marcy relieved
        m "That is quite unfortunate, [name]. I promise I'll be as nice to you as any other person would."
        scene black
        hide marcy
        with Dissolve(0.5)
        "So, here you are."
        "Trapped in the Living World, forced to kill and regain your favor in the eyes of your masters"
        "...Or you could die, proving how weak you truly are."
        "What a strange, sad fate."
    label day1_intro:
        scene black
        show logo:
            xalign 0.5 
            yalign 0.2
        with Dissolve(1.0)
        pause 0.5
    label day1_tutorial:
        "Welcome to UNA SEPTIMANA!"
        "The way this game works is simple."
        "You have 7 DAYS to kill as many people as you can without being killed yourself."
        "Or befriend as many people as you can and possibly die in a week."
        "You need blood of some variety in order to have energy to do certain things."
        "There are 14 hours in a day, which you can spend talking to characters to gain their trust..."
        "Or sleeping to also gain energy, although this fastforwards you to a later point in the day."
        "This is the tutorial, so click on any of the following options to get clarification."
    label tutorial:
        menu:
            "Interacting":
                jump how2interact
            "Sleeping":
                jump how2sleep
            "Killing":
                jump how2kill
            "Okay, I think I got it.":
                jump tutorial_ending
    label how2interact:
        "Depending on the time of day, a character will be able to be interacted with."
        "This is very important for gaining their trust, whether it be for the sake of being friends with them, or making it easier to kill them."
        "This is tracked through the TRUST GAUGE (pretend that I've made it already.)"
        "The Trust Gauge is a scale from -5 to +5. It determines, as you might guess, how much a character trusts you."
        "For example, say you're talking to Marcy."
        m "Hello!"
        "If you choose to interact with her, you'll get three options; A positive, neutral, or negative option."
        "By default, her Gauge is set to +1."
        menu:
            m "Do you think I'm annoying?"

            "Yes, you are.":
                $ marcy_trust -= 1
                m "Oh. I see."
            "I don't know you enough to say.":
                m "That is fair, I suppose."
            "No, you are not.":
                $ marcy_trust += 1
                m "That is reassuring. I never want to annoy anybody..."
        "If this code works properly, then depending on what you said, Marcy has [marcy_trust] value on the Trust Gauge."
        "Based on this, it will be harder to kill her later in the day, as the sun sets."
        "Being too neutral will do, as the name implies, nothing."
        jump tutorial
    label how2sleep:
        "Sleeping is a vital mechanic of the game."
        "Sleeping is a semi-reliable way to gain energy without harming anyone or anything."
        "However, there is a downside to this."
        "Sleeping during the day fast forwards the game by a random amount of time, ranging from 3 hours to a whopping 8."
        "Depending on when you sleep, the day could just straight up end, and you'll be forced to act."
        jump tutorial
    label how2kill:
        "Killing! Every demon loves that."
        "Except, depending on who you are, you."
        "There are 3 results from trying to kill some one: Success, Failure, and Critical Failure."
        "When you try and kill someone, there is a random number generated that will determine the success of your murder attempt."
        "Success is always the least likely to take place."
        "Since, y'know, your character is bad at killing."
        "There is an exception to this, of course."
        "If your trust gauge with that character is at a 4 or a 5, your chance of killing them will be almost guarenteed."
        "In addition, you'll get more Blood, and increase your Max Energy."
        "The catch?"
        "Your morality will decrease."
        "What's morality?"
        "It just determines your capacity to kill."
        "The less morality you have, the sooner and sooner you'll be able to kill people..."
        "But also the more and more reckless you'll get with killing."
        "It makes the game harder the more you kill people."
        "Just like real life!"
        "Inversely, the more morality you have, the easier it is to befriend people, and the harder it is to kill them."
        "Simple sugar."
        jump tutorial
    label tutorial_ending:
        "Well, that's pretty much all you need to know for now!"
        "Good luck, my little Angel of Death."
        "You are going to need heaps of it."
        scene black
        with Dissolve(1.0)
    
    label day1_start:
        scene black
        show day1 name:
            xalign 0.5
            yalign 0.3
        with Dissolve(1.0)
        pause 0.5
        scene forestday
        with Dissolve(0.7)
        define your_energy = 3
        define time_of_day = 1
        define asked_whatsbreakfast = False
        define marcy_alive = True
        define ate_with_marcy = False
        $ marcy_trust = 1
        "(Pretend I have a living room drawn up.)"
        "Marcy walked off to cook you and her some food, leaving you alone in the bedroom."
        "Quietly, you get up and leave the room."
        "You take a look around..."
        "Near the door, there are multiple books in the bookshelf."
        "A few scientific books, some romantic novels..."
        "The Odyssey, The Iliad..."
        "And the Bible."
        "Meanwhile, there are a few couches, and some other stuff."
        "You can hear Marcy humming in the kitchen"
        label do_stuff_day1:
            if time_of_day < 9:
                scene forestday
                menu:
                    "What will you do? You currently have [your_energy] energy and the time is [time_of_day]PM."
                    "Talk to Marcy":
                        jump talk_with_marcy
                    "Sleep":
                        jump sleep
                    "Attempt to Leave":
                        jump leave
                    "Go to 9PM":
                        jump nineoclock
            else:
                jump nineoclock
        
        label sleep:
            if time_of_day <= 6:
                scene black
                with Dissolve(0.5)
                "You decide to sleep to recover your energy."
                "..."
                "When you wake up, it is already evening..."
                $ time_of_day = 7
                $ your_energy += 2
            else:
                "You are not feeling tired."
            jump do_stuff_day1
        
        label leave:
            if marcy_trust < 4:
                "You try to leave through the front door, but Marcy calls out to you."
                m "Leaving already? But you still need time to heal!"
                m "I do not feel comfortable letting you leave in your current condition."
                "Against your common sense, you decide to stay."
                jump do_stuff_day1
            else:
                "You try to leave, and succeed."
                "I'll add more to this later."
                return
        
        label talk_with_marcy:
            "You walk towards the kitchen and find Marcy hunched over a pot on the stove, stirring intently. She notices you walk in and smiles."
            show marcy smiling
            m "Oh, hello there [name]!"
            show marcy regular
            m "I didn't expect you to already be up and about right now."
            y "Like you said. My healing factor is rather extraordinary."
            show marcy happy
            m "Hahah.... Ain't that the truth."
            m "What can I do for you?"
            show marcy smiling
            if your_energy > 0 and time_of_day == 1:
                menu:
                    "What is for breakfast?":
                        jump whatsbreakfast
                    "What do you think of me?":
                        jump whatshethinks
                    "When is your brother returning?":
                        jump about_bro
                    "How long have you lived here?":
                        jump howlongshehas
                    "Can I leave?":
                        jump noyoucannot
            elif your_energy == 0:
                y "Nothing. Just came to check in on you."
                show marcy bashful
                m "O-oh! That's..."
                m "Very... kind of you."
                $ time_of_day += 1
                jump do_stuff_day1
                with Dissolve(0.5)
            elif your_energy > 0 and 1 < time_of_day < 4:
                menu:
                    "Let's Eat.":
                        jump eat_with_marcy
                    "What do you think of me?":
                        jump whatshethinks
                    "When is your brother returning?":
                        jump about_bro
                    "How long have you lived here?":
                        jump howlongshehas
                    "Can I leave?":
                        jump noyoucannot
            elif 4 < time_of_day < 9:
                menu:
                    "You are very nice.":
                        jump marcy_compliment
                    "I don't feel as sore.":
                        jump marcy_thanks
                    "What's your story?":
                        jump about_her
                    "Did you know you're going to die soon?":
                        jump marcy_threat
            
            label whatsbreakfast:
                if asked_whatsbreakfast == False:
                    show marcy regular
                    y "What are you cooking?"
                    m "I am so glad you asked."
                    show marcy smiling
                    m "I'm cooking some sausage gravy here, and the biscuits are baking in the stove."
                    m "I hope you're not adverse to meat."
                    show marcy sus
                    y "Quite the opposite."
                    show marcy happy
                    m "Har har har! Well said, partner."
                    $ your_energy -= 1
                else:
                    show marcy unimpressed
                    m "Well, aren't you hungry as a horse?"
                    show marcy sus
                    m "You already know what I'm cooking, [name]."
                $ time_of_day += 1
                $ asked_whatsbreakfast = True
                jump do_stuff_day1
                with Dissolve(0.5)
            label eat_with_marcy:
                "You decide to sit down and eat with Marcy, now that her food is done."
                "As you eat, a bit of gravy gets on your chin, which you quickly swipe away. Marcy laughs."
                m "Haha... you are so darn weird! That's pretty cute."
                y "I am not cute. Do not call me that."
                m "Yeesh. Sorry. Touchy subject, I suppose."
                "An awkward silence falls between the two of you."
                m "Em, so... how is the food?"
                y "It is delicious. Thank you for such a heartly, bountiful meal."
                m "Heh... thank you."
                $ ate_with_marcy = True
                $ marcy_trust += 1
                $ your_energy += 1
                $ time_of_day += 1
                jump do_stuff_day1
                with Dissolve(0.5)
            label marcy_compliment:
                y "Of all the humans I've known, you are the nicest."
                show marcy smiling
                m "Aww, thank you!"
                m "I'm flattered."
                $ marcy_trust += 1
                $ your_energy -= 1
                $ time_of_day += 1
                jump do_stuff_day1
                with Dissolve(0.5)
            label marcy_thanks:
                y "I do not feel as sore anymore."
                y "You have done a very adequate job at repairing me."
                show marcy unimpressed
                m "Gee, thanks."
                m "Adequate is such high praise."
                $ your_energy -= 1
                $ time_of_day += 1
                jump do_stuff_day1
                with Dissolve(0.5)
            label about_her:
                y "So, what is your story?"
                m "Me? Well... I don't have much to say!"
                show marcy regular
                m "Born and raised down in Georgia along with my brother. Grew up going to boarding schools."
                m "I've fallen in love a few times, but none of them really stuck and held for me."
                m "Then, about a year ago, Rumors began spreading that the United States was on the brink of Civil War..."
                m "So my brother and I moved up here to Massachusets, and have been here since."
                m "Somedays, I miss my homeland, but..."
                show marcy depressed
                m "It is quite nice here."
                show marcy smiling
                y "Well, people like you definitely serve this place well."
                y "You are a good person."
                show marcy bashful
                m "Teehee. Oh, you."
                $ marcy_trust += 1
                $ your_energy -= 1
                $ time_of_day += 1
                jump do_stuff_day1
                with Dissolve(0.5)
            label marcy_threat:
                y "Did you know that you are going to die soon?"
                m "Excuse me?"
                show marcy sus
                y "Everyone is, if you think about it."
                y "It's just a matter of how soon it is."
                m "..."
                show marcy unimpressed
                m "...Okay, then."
                $ marcy_trust -= 1
                $ your_energy -= 1
                jump do_stuff_day1
                with Dissolve(0.5)

            label whatshethinks:
                y "What do you think of me?"
                show marcy regular
                m "That's an interesting question."
                m "Well, considering that we only met a few hours ago, and you've been very nice to me thus far..."
                show marcy smiling
                m "I'd say I have a good first impression of you."
                menu:
                    m "Why do you ask anyways?"
                    "I want you to like me.":
                        y "I want you to like me."
                        show marcy regular
                        m "Doesn't everyone wish to be liked?"
                        y "I am not."
                        y "At least, I'm not supposed to be."
                        y "But I trust you."
                        y "And I want you to like me."
                        show marcy smiling
                        m "Rest assured, [name]."
                        m "I come to like people quite easily."
                        m "Assuming they're nice to me first, of course."
                        $ your_energy -= 1
                        $ marcy_trust += 1

                    "I expected you to hate me.":
                        y "I expected you to hate me."
                        show marcy sus
                        m "Hate you? Why?"
                        y "Most humans do."
                        m "You say this like you're not a human too."
                        y "I am a human. I am."
                        y "That was a blunder. Please forgive me."
                        y "I am sorry. Please. Please forgive me."
                        y "Please."
                        m "..."
                        m "...Okay..."
                        $ marcy_trust -= 1
                $ your_energy -=1
                $ time_of_day += 1
                jump do_stuff_day1
                with Dissolve(0.5)
            label about_bro:
                show marcy regular
                y "When is your brother returning?"
                m "That is a mighty good question, [name]."
                m "I.... actually don't know."
                m "Usually he returns after 9PM or so..."
                m "Though, for all I know, he could come whenever."
                m "Just... be nice to him when he does arrive, okay?"
                m "He's a real sweetheart when you get to know him."
                y "I see."
                "Seems like something you should remember."
                $ your_energy -= 1
                $ time_of_day += 1
                jump do_stuff_day1
                with Dissolve(0.5)
            label howlongshehas:
                show marcy regular
                y "How long have you two lived in this cabin?"
                m "Not that long, actually."
                m "We recently moved up here to avoid the escalating conflicts down south."
                m "Mom and dad don't seem to mind. They doubt there'll ever be a war to begin with."
                m "But if you ask me? I hope that the United States settles down."
                m "I hate seeing blood when I'm not cooking or working."
                $ your_energy -= 1
                $ time_of_day += 1
                jump do_stuff_day1
                with Dissolve(0.5)
            label noyoucannot:
                show marcy regular
                y "When may I exit the premises?"
                m "...Leave?"
                y "Yes. I have something I need to do, and I do not wish to involve you in it."
                m "...I don't think you should leave quite yet."
                y "Why?"
                m "See, recently here in Westhelm, there's been.... How do I phrase this..."
                m "An 'incursion' of Penitents here."
                m "They come around every day around 10PM to see if anyone is out past curfew."
                m "If you are, they will kill you."
                y "Penitents..."
                y "(I cannot be here by the time they come...)"
                y "(I must finish whatever business I have here before 10PM...)"
                $ your_energy -= 1
                $ time_of_day += 1
                jump do_stuff_day1
                with Dissolve(0.5)

    label nineoclock:
        hide marcy
        scene forestnight
        with Dissolve(0.5)
        "It is late at night. The sun has set."
        "Marcy is asleep in her bedroom."
        "What will you do?"
        menu:
            "Go to Bedroom":
                jump marcy_death
            "Do Nothing":
                "You decide to wait it out. The Penitent should be here soon."
                jump tenpm
    
    label marcy_death:
        hide marcy
        "You enter her bedroom."
        "Marcy is sprawled out across her bed, asleep."
        "Her chest rises and falls as she sleeps peacefully."
        "..."
        menu:
            "Kill Her":
                jump marcy_murder
            "Do Nothing":
                "You decide that murdering her is not worth it."
                jump tenpm
    label marcy_murder:
        scene black
        with Dissolve(1.0)
        "You approach her bed, carefully, avoiding the creaking floorboards that could wake her up."
        "You don't want her to wake up. Not now."
        "Eventually, you come to loom over her."
        "She looks so beautiful as she sleeps."
        "..."
        "But you have a job to do."
        "You let your humanoid form shed away, the skin on your back bubbling and rippling as it gives way to your two large black wings."
        "Your hair parts as two great spiraling horns break skin, causing you to bleed onto her slightly."
        "Your irises narrow into slits, your teeth now jagged and your form beastly and stalking."
        "A drop of blood from your head falls onto her nose, causing her to open her eyes."
        m "E-eh.... whuh...?"
        "As she opens her eyes, she thinks it's just your facade."
        m "[name]...? Is that you...?"
        "Then she sees you. The real you."
        "And she screams out in horror."
        m "KYAAAAAH!!!!"
        "Instinctively, you grab her face, pulling her out of bed and holding her high into the air."
        "Tears begin to stream down her face as she flails in your grasp, gasping and pleading."
        m "Please... please don't hurt me..."
        "You don't say a word to her, still staring into her eyes."
        "For a moment, you think she's trying to appeal to your false humanity."
        "Clinging to any moment you two might have shared."
        if marcy_trust > 2:
            "And, for a few hours, there was..."
            "...But no longer."
        else:
            "But there was none."
            "Because you showed her your true nature as a demon."
        "Your mouth unhinges at the jaw, revealing that, inside your mouth, is a spiraling vortex of teeth and lights."
        "Her eyes widen as a tear runs down her cheek."
        "You bring her closer. And closer. And closer until..."
        pause 0.5
        "Her torsoless body falls to the ground, limp."
        "A leakage of blood floods the ground."
        "You wipe your mouth and return to your normal form."
        y "...One down."
        "You sigh, and walk out of the room."
        "You won't bother to clean up the rest."
        "The animals can have her."
        $ marcy_alive = False
    
    label tenpm:
        hide marcy
        if marcy_alive == True:
            jump tenpmwithher
        else:
            jump tenpmwithouther
    
    label tenpmwithher:
        "A penitent knocks at the door..."
        "Mary walks out of her room, which she had been sleeping in, and goes to answer the door."
        "Before opening it, she turns back to look at you."
        m "Just... let me do the talking, alright?"
        y "...Okay, Marcy."
        m "Good. Thank you."
        "Mary opens the door and lets a tall Penitent through."
        q "Good evening to you both."
        m "G-good evening, sir."
        p "My name is Harold Cromwell, and I have come to inspect your house for any unholy behavior."
        p "Who is this new person in your house, Ms. Whistifer?"
        m "Th-this is..."
        y "I am [name]."
        p "Mm. I see."
        p "Is this person causing you any trouble, madam?"
        m "Ah, well..."
        if marcy_trust < 1:
            jump ending_abrasive
        else:
            jump ending_friends
    
    label tenpmwithouther:
        "A penitent knocks at the door."
        "There is still so much blood on your body..."
        "But you do not care."
        "Not now."
        "The Penitent opens the door, and immediately notices how you look, covered in blood and sinue."
        "He draws his sword and begins to speak."
        q "You shall come no closer, unholy demon."
        p "I am Sir Cromwell, of the Order of the Broken Cross."
        p "I demand you explain your current appearance, and if anyone else is in your house right now."
        menu:
            ":)":
                jump withouther_contd
    label withouther_contd:
        "You smile at the man."
        y "Well, Sir Cromwell of the Order of the Broken Cross..."
        y "There was indeed someone else in this house."
        y "Do you wish to see her?"
        "The Knight grips his sword."
        p "...No. No, I do not."
        p "Because I already know what you have done."
        p "You killed the woman who really resides here... because you are a hellspawn."
        p "Reveal your name to me, demon!"
        "You shake your head."
        y "You do not deserve to hear it. So, in the meantime, call me [name]."
        y "It will be the last symphony I squeeze out of your self-righteous body."
        "The Penitent runs at you, his sword held in hand."
        "Will you fight back, or accept your fate?"
        menu:
            "Fight":
                jump ending_beast
            "Accept":
                jump ending_coward
# endings
    label ending_beast:
        "You charge at the Penitent and tackle him to the ground, smacking the sword out of his hand."
        "You pin him down, grabbing onto his helmet with unholy strength."
        p "Grh... let... Let go of me!"
        "You do not. Instead, you begin to apply pressure to either side, intending on bringing your hands together,"
        "No matter what may be in between them."
        "As his helmet begins to creak and groan under your grip, the Penitent begins to shout."
        p "Stop! Ah! Aah!!"
        "His shouts turn to wails, which quickly devolve into screams of agony as his helmet begins digging into the sides of his head."
        "Your smile widens as his eyeballs begin to go bloodshot and bulge out of their sockets. Just a bit more..."
        y "Sing for me, Cromwell."
        "The knight coughs blood onto your already bloody shirt, and lets out one haunting wail before..."
        "You clap."
        "His head explodes like a watermelon, spraying his brain matter all across the roof."
        "Some remnants of bone and eyeball even get on the ceiling."
        "You withdraw your hands from the headless knight and stand up."
        "It is time to leave."
        "You have already killed two people."
        "And now you have the capacity to prove yourself."
        scene black
        with Dissolve(1.0)
        pause 1.0
        show ending beast:
            xalign 0.5
            yalign 0.5
        with Dissolve(1.0)
        "YOU GOT THE BEAST ENDING."
        "YOU ARE A TRUE DEMON."
        "Thanks for playing the proof-of-concept for Daydream Calgary 2025!"
        return
        with Dissolve(1.0)
    label ending_coward:
        "The man buries his sword deep in your neck, and yet the smile plastered on your face doesn't leave."
        "He pulls it out of your neck and quickly sticks it in again, this time piercing straight through your abdomen."
        "You still don't react, even as you clutch your neck and fall to the ground, mortally wounded."
        "The knight stands above you, his sword poised directly at your chest."
        p "Any last words, demon?"
        "You stare at him. Look deep into his eyes."
        "You see everything he went through to get where he is. Everyone he's killed, everyone he's loved... Everyone he's lost."
        "Then, you begin to laugh."
        "A quiet, wheezing chuckle that breaks into body wracking laughs."
        "Then, those turn into body wracking sobs as your fake happiness fades."
        "The sudden shift in your demeanor gives the Knight pause."
        "You swallow and sigh."
        y "It is so funny how humans are afraid of death."
        y "Because that is not the terrifying part of it all."
        y "No."
        y "What they should be afraid of..."
        y "What we all truly fear..."
        y "Is the prospect that what comes after..."
        y "Is worse than you could ever imagine."
        "The knight stares down at you."
        p "What does that mean?"
        "You sigh and feel your eyes roll back, feeling your soul being pulled beneath the Earth back into HELL."
        y "HELL... HELL is full."
        "And with that... you are no more."
        "Good job at being a failure."
        scene black
        with Dissolve(1.0)
        pause 1.0
        show ending coward:
            xalign 0.5
            yalign 0.5
        with Dissolve(1.0)
        "YOU GOT THE COWARD ENDING."
        "YOU CANNOT CHOOSE BETWEEN THE WICKED AND THE WEAK."
        "Thanks for playing the proof-of-concept for Daydream Calgary 2025!"
        return
        with Dissolve(1.0)
    label ending_abrasive:
            m "He or she..."
            y "They."
            m "They... haven't really caused me any trouble... But I don't exactly want them in my house any more. Please take them away..."
            y "What?!"
            m "I'm so sorry, [name], but I don't feel safe around you."
            m "I thought we would get to connect, but..."
            m "...Forgive me."
            "Before you could object, the Penitent grabbed your hand and began dragging you out of the house, much to your dismay."
            "As you were whisked out of the cabin to be executed, all Marcy could do was turn away and close the door, locking you out."
            "Maybe you should act more human, and you'll last longer in a human world."
            scene black
            with Dissolve(1.0)
            pause 1.0
            show ending abrasive:
                xalign 0.5
                yalign 0.5
            with Dissolve(1.0)
            "YOU GOT THE ABRASIVE ENDING."
            "YOU LACK THE ABILITY TO CONNECT WITH OTHERS."
            "Thanks for playing this proof-of-concept for Daydream Calgary 2025!"
            return
    label ending_friends:
            m "...They are my friend. I trust them with my life, and found them severely wounded the other day..."
            m "So I saved them. In return, [name] granted me their kindness."
            p "..."
            p "I see."
            p "In that case, then, I shall take my leave."
            p "God be with you both."
            "The Penitent exits without conflict, leaving just the two of you alone in the dark house."
            "It is silent."
            "Then, you speak."
            y "Marcy."
            m "Yes?"
            y "Can you keep a secret?"
            y "I cannot stay here, so I owe you an explanation."
            m "Of course, [name]."
            y "So. The reason why you found me out in the woods..."
            y "Bloody, and bruised..."
            y "It isn't because of dogs."
            m "..."
            m "Hahahah! That's all?"
            m "I gotta say, I expected something far far-"
            y "It is because I am a demon from hell, and was cast out for not doing my job properly."
            m "..."
            m "Oh."
            m "That's..."
            m "Hm."
            y "I understand if you wish for me to leave at once."
            m "..."
            m "What job were you not doing well?"
            y "Torturing people."
            y "After a while, I.... I saw somebody I knew."
            y "So many people I knew from when I was alive, and I just..."
            y "I could not bring myself to harm them any more than I had already."
            y "So, my masters, they cast me out and sent me here."
            y "I have a week to kill as much as I can before I am judged, or else I will die."
            y "But... I do not want to kill. I really do not want to."
            m "..."
            m "Well..."
            m "I believe in you, [name]."
            m "No matter where you're from, you were nice to me and disobeyed your masters."
            m "That's morality."
            m "That's more human than some humans I've met."
            y "You really think so?"
            m "I do."
            m "And I understand why you must leave."
            m "I just hope..."
            m "You find some peace at the end of your journey."
            y "..."
            y "Thank you, Marcy."
            y "That is... something I shall never forget."
            "With that, you walk past her to the door, intent on leaving."
            "As you reach the door, she calls out to you one more time."
            m "Oh, also..."
            y "Hm?"
            $ m = Character("Marceline")
            m "My name is Marceline."
            m "Marceline Whistifer."
            m "I hope you remember me down the line."
            y "...."
            y "Do not fret... Marceline."
            y "I will remember you."
            "And so you exit the cabin, and make your way into the wilderness."
            "Who knows what you'll find next...?"
            scene black
            with Dissolve(1.0)
            pause 1.0
            show ending friends:
                xalign 0.5
                yalign 0.5
            with Dissolve(1.0)
            "YOU GOT THE FRIENDS ENDING."
            "YOU FOUND A NEW ALTERNATIVE. MAYBE THERE IS HOPE YET."
            "Thanks for playing this proof-of-concept for Daydream Calgary 2025!"
            return       


        
    return
