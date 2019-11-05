# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pt = Character("Protagonist", color="#ffffff")
define cw = Character("Coworker Friend", color = "#ffffff")
define of = Character("Other Friend", color = "ffffff")
define gp = Character("Towering Figure", color = "ffffff")
define twoSecondFade = Fade(0.5, 1.0, 0.5)
define dissolveTwoSec = Dissolve(2.0)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene blackBackground
    with twoSecondFade

    "{i}You see an origami fortune-teller, closed and ready for you to use.{\i}"
    "{i}It is the only thing in sight, and you feel strangely compelled to ask it a question.{\i}"

    menu fortune_1st_question:
        "{i}Ask me a question:{\i}"

        "Will I be happy?":
            jump fortune_2nd_question

        "What will make me happy?":
            jump fortune_2nd_question

        "Why am I not happy?":
            jump fortune_2nd_question

    menu fortune_2nd_question:
        "{i}Pick a color:{\i}"

        "Blue":
            jump fortune_3rd_question

        "Red":
            jump fortune_3rd_question

        "Green":
            jump fortune_3rd_question

        "Pink":
            jump fortune_3rd_question

    menu fortune_3rd_question:
        "{i}Pick a number:{\i}"

        "One":
            jump fortune_4th_question

        "Two":
            jump fortune_4th_question

        "Three":
            jump fortune_4th_question

        "Four":
            jump fortune_4th_question

    menu fortune_4th_question:
        "{i}Pick another number:{\i}"

        "Five":
            jump fortune_result

        "Six":
            jump fortune_result

        "Seven":
            jump fortune_result

        "Eight":
            jump fortune_result

    label fortune_result:
        "{i}You will meet your true love.{\i}"

        pt "That's not even what I asked..."

        pt "This is dumb. I should get to bed."

        pt "I should have slept earlier."
        pt "Works going to suck tomorrow..Ugh."

        scene fortuneTeller
        with twoSecondFade

        pause 1.0

        scene messyCorner
        with pixellate

        pause 1.0

        scene messyDesk
        with pixellate

        pause 1.0

        scene overShoulder
        with pixellate

        pt "I'm going to be so late..."

        #insert character creation here

        pt "Well, I guess if I go now, at least I'm going."

        scene urbanBackground
        with twoSecondFade

        show protag
        with dissolve

        pt "Wow, it's nice out for once."

        #text tone

        pt "..."

        #text tone

        pt "..."

        #text tone
        #text tone

        pt "Good."

        #Ringtone

        pt "...God."

        #Ringtone

        #Answer tone

        #Friend theme

        cw "HEY, HOW COME YOU NEVER ANSWER MY TEXTS!"

        pt "Cause I know it’s you. You’re the only person who texts me."

        cw "What? I know you’ve been a hermit lately, but that doesn’t mean you should ignore me!"

        pt "Are you calling about work?"

        cw "Yeah! You were supposed to be here 10 minutes a--"

        pt "I know."

        cw "Why'd you answer my call then?"

        pt "Thought it'd be my mom or something."

        cw "You don't make any sense, [pt]. You're coming, right?"

    menu whenComing:
        "You're coming, right?"

        "I'll get there when I get there.":
            jump whenComingResponse1

        "I'm sorry, I'm on my way.":
            jump whenComingResponse2

        "...":
            jump whenComingResponse3

    label whenComingResponse1:
        cw "What's that supposed to mean???"
        jump finishWhenComing

    label whenComingResponse2:
        cw "Ah, don't worry about it--it's not too busy. I should buy you a better alarm, huh?"
        jump finishWhenComing

    label whenComingResponse3:
        cw "You're coming, right???????"
        jump finishWhenComing

    label finishWhenComing:
        pt "Aaaaand, I'm here."
        hide protag

    label inConvenienceStore:
        scene convenienceStore
        with dissolveTwoSec

        #Convenience store theme
        #Call-end tone

        show protag at left
        with dissolve

        show coworker at right
        with dissolve

        cw "You live like 5 minutes away! How are you {i}always{/i} late?"

    menu whyLate:
        "How are you {i}always{/i} late?"

        "At least I'm here.":
            jump whyLateResponse1

        "Sorry, I woke up late.":
            jump whyLateResponse2

        "There was some freak accident.":
            jump whyLateResponse3

    label whyLateResponse1:
        cw "Pft, after I opened the store alone. Just get changed--we've got a long morning!"
        jump finishWhyLate

    label whyLateResponse2:
        cw "Gah, it's fine, don't apologize about it. I'm used to it."
        cw "Just get changed--you haven't missed much."
        jump finishWhyLate

    label whyLateResponse3:
        cw "Yeah, yeah, and it somehow made walking two blocks an hour trip for you."
        cw "Get changed before another alien crashes through the door."
        jump finishWhyLate

    label finishWhyLate:
        pt "Alright."

        #customer enter chime

        show protag facing left at left
        show coworker facing right at right

        cw "Good morning! How can I help you! Please let me know if you need anything!"
        pt "Hi. This it?"
        cw "Wow, miss! You look amazing today! Just like everyday!"
        pt "Your total is $5. Bye."
        cw "Sir! Can I offer you our newest latte beverage? Local and organic!"
        pt "..."

        #Scan noise

        show protag at left
        show coworker at right

        cw "..."
        pt "...What?"
        cw "You're so upbeat today, [pt]! How refreshing!"

    menu soRefreshing:
        "You're so upbeat today, [pt]!"

        "Thanks.":
            jump soRefreshingResponse1

        "...":
            jump soRefreshingResponse2

        "You think so?":
            jump soRefreshingResponse3

    label soRefreshingResponse1:
        cw "Hah! You're welcome! Good to see you out and about, enjoying life!"
        jump finishSoRefreshing

    label soRefreshingResponse2:
        cw "Hah...I'm--I mean, you're always upbeat! Ah, never mind..."
        jump finishSoRefreshing

    label soRefreshingResponse3:
        cw "Definitely, we've been friends for so long, of course I'd notice. It's good to see!"
        jump finishSoRefreshing

    label finishSoRefreshing:
        cw "Anyway, you should come out with me and [of] tonight! We're gonna hang out and maybe catch a movie or something."

    menu watchMovie:
        "You should come with us tonight!"

        "No thanks, I've got to be home tonight.":
            jump watchMovieResponse1

        "Thanks for the offer, but maybe next time.":
            jump watchMovieResponse2

        "I'd rather not. But thank you.":
            jump watchMovieResponse3

    label watchMovieResponse1:
        cw "Oh! Yeah? Um...okay, no worries."
        jump finishWatchMovie

    label watchMovieResponse2:
        cw "Oh! Okay, understandable, yeah! Next time!"
        jump finishWatchMovie

    label watchMovieResponse3:
        cw "Oh, sure...!"
        jump finishWatchMovie

    label finishWatchMovie:
        #customer enter chime

        hide coworker

        show protag facing left at right
        with moveinright
        show gale at left
        with dissolve

        "{i}A tall stranger enters and buys NutriMame, which is essentially Soylent.{\i}"
        pt "Ah...so tall."

        gp "..."

        pt "Just this for you today?"

        gp "Yes."

    menu nutrimameComment:
        "{i}You try to make some small talk...{\i}"

        "My favorite's the beef-flavored one. Makes it a little more edible.":
            jump nutrimameCommentResponse1

        "These probably aren't good for you, y'know?":
            jump nutrimameCommentResponse2

        "That's $3.":
            jump nutrimameCommentResponse3

    label nutrimameCommentResponse1:

        jump finishNutrimameComment

    label nutrimameCommentResponse2:
        jump finishNutrimameComment

    label nutrimameCommentResponse3:
        jump finishNutrimameComment

    label finishNutrimameComment:









    return
