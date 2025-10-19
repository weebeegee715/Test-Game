# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character(" [cat_character] ", color="#ebbce3")
define m= Character("Man", color="#1f569f")

# The game starts here.

label start:

    default cat_character = "Pusheen"

    default Tax_paid = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sky

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pusheen typing with moveinleft

    # These display lines of dialogue.

    p "Im really trying to make a game..."

    p "isnt that cool?"

    p "Wait I need to pat my taxes!!!"

    menu:
        "nah.":
            p "I don't got money like that..."
        
        "Ok let's do that":
            p "Ok boom paid."
            $ Tax_paid = True
        

    show pusheen dance

    # pusheen got up

    p "I think I'm making good progress!"

    p "At this rate, i'll be done in no time."

    p "Isnt it weird that we're floating??"

    scene bg flower
    with dissolve

    show pusheen flower at right
    with moveinright

    p "This is much better, right?"

    show man at left
    with moveinleft

    m "Hello pusheen I am the IRS"

    p "You're the entire IRS??"

    m "{b}{i}Don't question me!{/i}{/b}"

    if Tax_paid == True:
        jump boring

    elif Tax_paid == False:
        pass

    else:
        pass



    p "I am NOT paying my taxes LOL!!!"

    m "Nahh ur going to jail..."

    show pusheen angry 

    p "YOU CAN'T TAKE ME IM A SOVERIGN CITIZEN!!"

    m "Sure you are. Let's go."

    menu:
        "IM NOT GOING TO JAIL!!!!":
            $ cat_character = "Felon"
            m "YES YOU ARE!!!!"
        
        "Ok since im [cat_character] I guess I have to...":
            m "Yes, you do."
        
        "RUN AWAY!!":
            $ cat_character = "Runaway"
            jump RUN_AWAY

    scene black
    with dissolve

    p "NOOO!!"

    "They took pusheen to jail..."

    # This ends the game.

    return

label RUN_AWAY:
    p "IM RUNNING LOSER!!"
    m "HEYY! STOP THAT"

scene black
with dissolve

"Pusheen ran away from the IRS!"

return

label boring:
    m "Wait..."
    m "It seems you've already done your taxes."
    m "Have a nice day."

scene black
with dissolve

"Pusheen avoided the IRS!"

return
