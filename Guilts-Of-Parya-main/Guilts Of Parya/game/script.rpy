# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define You = Character("You")
define Man = Character("The Man")
define Chained = Character("Chained Woman")

default Player_choice01 = ""
default Player_choice02 = ""
default Guilt = 0
default Grace = 0
default d4 = 0
default d6 = 0
default d10 = 0

# Dice roll function that needs to be called inside the label to be used
label dice_roll:
    $ d4 = renpy.random.randint(1,4)
    $ d6 = renpy.random.randint(1,6)
    $ d10 = renpy.random.randint(1,10)
    return

# The game starts here.

label start:

    scene girl_city with Fade(1.5, 0.5, 1.5)

    "you see a girl"

    scene city_gate01 with dissolve

    "a girl sees you"

    scene statue

    "Lorem episum"

    scene city_gate02 
    
    "you see each other"
 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene sitting

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    "You see him before you reach the gates.\nA man crouched in the dust, knees pressed into stone worn smooth by centuries of exile. The city walls rise behind him like a petrified wave. 
    An incardinate moon—red as a cauterized wound—hangs low and halos his bowed head. His shadow kneels taller than he does.\nWhen he speaks, it is as though the gravel has found a tongue."

    Man "\nWhat ignorant beast dragged you these gates?\nWhat trembling sack of marrow sent you to the threshold of reckoning?\nName the hand that hurled you into our shadow."

    menu:

        #Game starts with 0 guilt and 0 grace
        "I was sent by the Holy of Holies.":

            $ Player_choice01 = "Holy of Holies"
            $ Guilt = 0
            $ Grace = 0

            jump HolyHolies


        #Game starts with less guilt and less grace
        "I was sent by the Judge of Judgments.":

            $ Player_choice01 = "Judge of Judgments"
            $ Guilt -= 1
            $ Grace -= 1

            jump JudgeJudgments


        #Game starts with extra guilt and extra grace
        "I was sent by the Innocence of Innocence.":

            $ Player_choice01 = "Innocence of Innocence"
            $ Guilt += 1
            $ Grace += 1
            
            jump InnocenceInnocence

    return

label HolyHolies:

    "The man stiffens. The chains at his wrists tighten without being touched."

    Man "The Sanctum beyond sanctums?\nThe Silence that outlives prayer?"

    "He studies you as one studies a relic dug from a grave."

    Man "Then you arrive empty, as commanded.\nUntouched by verdict, unbranded by stain.Walk, pilgrim.\nThe city will measure you in due time."

    jump SittingMan01

label JudgeJudgments:

    "The crouched man lowers his head further, as though pressed down by an unseen palm."

    Man "Ah, The Gavel that falls before the crime.\nThe Eye that convicts the unborn."

    "A dry laugh escapes him."

    Man "Then you come already absolved by terror. The scales have leaned in your favor—but do not rejoice. Mercy is a debt that fattens."

    jump SittingMan01

label InnocenceInnocence:

    "For the first time, he smiles faintly."

    Man "Innocence?"

    "He rises slightly from his crouch, joints cracking "

    Man "To claim such origin is to confess ignorance of blood. You slouch forward with fragility, yet heavier than you believe"
    
    "The incardinate moon throbs faintly behind him."

    Man "Could not your geriatric order scrape the marrow of someone more fitting?\nA spine less green.\nOr at least… a man?"
    
    You "…."

    jump SittingMan01

label SittingMan01:

    Man "Speak. Tell me what grotesque providence shaped you."

    menu:

        #When overwhelmed, you may cleanse a portion of Guilt.
        "It is my birthpain.":

            $ Player_choice02 = "my birthpain"

            jump SittingMan01_01

        #You may save once at any moment. Loading deletes the file forever.
        "I was bred solely for this purpose.":

            $ Player_choice02 = "bred for this purpose"

            jump SittingMan01_02
        
        #When you take a life, there is a slim chance your Guilt will not increase.
        "No one else can carry the Dagger of Our Lady of Sorrow.":

            $ Player_choice02 = "the Dagger of Our Lady of Sorrow"

            jump SittingMan01_03
    
    return

label SittingMan01_01:

    "You do not flinch."

    You "It is my birthpain — bestowed upon me by blood,\nby the blood of my blood.\nA cursed lineage, a sacred anathema.\nI did not choose this wound.\nI inherited it.\nIt gnaws me from within like an unborn twin."

    "The crouched man studies your trembling hands."

    Man "Ah. An heir to affliction.\nVery well.\nWhen the weight of your inheritance crushes your ribs,\nyou may spill some of it upon the earth."

    "He presses his palm to the dust."
    
    Man "But know this: pain cleansed is still pain remembered."

    jump SittingMan02

label SittingMan01_02:

    "Your voice is steady, disturbingly so."

    You "I was honed through years to do this.\nMolded.\nBred for this singular purpose and nothing else.\nI am a vessel. A burial that walks."

    "The man's lips twitch."

    Man "A creature without surplus… how efficient."

    "He rises an inch higher."

    Man "Then you may defy the flow of fate once.\nYou may carve a moment into permanence. But when you return to it,\nthe past will refuse to remember you again"

    "His shadow splits briefly in two before merging."

    Man "An urn can only break once — the world will remember that you hesitated.\nAnd it will not offer you another mercy."

    jump SittingMan02

label SittingMan01_03:

    "Your hand brushes the hidden weight at your side."

    You "No one else can carry the Dagger of Our Lady of Stones. It answers only to my pulse, and thirsts only for my circulation"

    "The crouched man inhales through his teeth."

    Man "Interesting.. interesting… fascinating, so young, too young"

    "he continues,"

    Man "So I assume that by her granular piety, there's a slim chance that Your soul does not swell with the expected Guilt. The deed settles within you as sediment settles in a drowned cathedral."

    jump SittingMan02

label SittingMan02:

    Man "Finally, indulge an old sentinel in a useless curiosity.\nThis will not bend your road, nor lighten nor blacken your soul.\nBut words have weight, and I would feel yours."

    "He draws a circle in the sand with a cracked fingernail."
    
    Man "What compels you to approach this forsaken city — this open crypt that breathes with no lungs?"

    menu:

        "Conclusion":

            jump SittingMan02_01

        "Salvation":
        
            jump SittingMan02_02

        "Retribution":

            jump SittingMan02_03
return

label SittingMan02_01:
    
    You "I come to bring things to an end.\nFor better or for worse."

    Man "Ah. The mercy of cessation."

    "He nods, almost tenderly."

    Man "You seek the last page, be warned — endings are gluttonous. To conclude is to deny resurrection"

    "He smudges the circle into nothing."

    jump ManEnd

label SittingMan02_02:
    
    You "I come to save what can still be saved."

    "A faint, brittle smile fractures his face."

    Man "Salvation… that arrogant tenderness. You may rescue a fragment, a memory, a single uncorrupted syllable. But understand — salvation is subtraction. To save one thing is to abandon another."

    "The circle in the dust remains unbroken, but he draws a single vertical line that splits it into two"

    jump ManEnd

label SittingMan02_03:
    
    You "I come to purify all the putrescent spleens!"

    "The crouched man laughs softly —"

    Man "Purification is a beautiful word for violence."

    "He is quite for a second" 

    Man "But maybe that's our only, and final hope"

    "He presses his palm against the circle"

    jump ManEnd

label ManEnd:

    Man "Very well.\nEnd it. Save it. Scour it.\nNo one will resist your reason"

    "The gates open with the metal wheezing of cancerous ribcage."

    Man "But know this — You do not get second chances in this place. And child, regardless of the path you take, you will end up alone in the end"

    scene chained_woman with fade

    jump chainedWoman01

label chainedWoman01:

    "You see a woman with a small family of medium, moribund rocks lashed to her bent back, fastened by rusting bronze chains that trail forward to wind loosely around her bruised wrists.In her pale, 
    trembling hands she cradles two extra rock, as though they were something breakable, something beloved.  Every time she tries to stand straight the weights pull her down and she releases a soft, 
    almost inaudible moan of pain.\nShe remains bowed, she doesn't look at you, or she can't look at you."

    menu:

        "Kneel down to her level":

            $ Grace += 1
            
            jump chainedWoman02

        "Remain upright":

            $ Guilt += 1

            jump chainedWoman02

        "Choose nothing":

            $ Guilt += 1
            
            jump chainedWoman02

label chainedWoman02:

    You "Do you need Help?"

    Chained "And what help can you give me that I have not been given before, girl? What God-given virtue travels through your small-boned body? What weight can you add that I have not carried before?"

    menu:
        
        "I not understand what you are saying":

            "I am asking if you, fledgling thing— you whose voice has not yet cracked upon real grief, whose blood has not learned the taste of ash. What salvation do you presume to offer me?
            \nWhat limb of the broken world have you ever lifted? For seven years I have borne the cairn of my husband, my mother,and the child who perished unnamed within me. Seven years more are decreed."

            jump chainedWoman03
        
        "I have nothing, but the dagger on my back.":

            "So you bring me a cruel remedy, then where did you get the gall to inquire after my weight? creature with a whiny voice, and beleaguered blood,You have known inconvenience, not ruin. 
            For seven years I have borne the cairn of my husband, my mother,and the child who perished unnamed within me. Seven years more are decreed."

            jump chainedWoman03

        "I can help remove the rocks off your back.":
            
            "And what inherent mercy compels you, child of exalted roots, that you might carry the dust of others and not be buried with it?
            \nFor seven years I have borne the cairn of my husband, my mother,and the child who perished unnamed within me. Seven years more are decreed.
            \nAnd all through time we had sufferers. And if it's our birthright to suffer then let it be. And if it's our blight to be lied to continually, 
            blight growing more, then it's also our right. So see the mucous and the veins thicken."

            $ Guilt -= 1

            jump chainedWoman03

label chainedWoman03:

    menu:

        "I am here to relieve your pain.":

            jump chainedWoman04_01

        "I am here to end your suffering.":

            $ Guilt += 1

            if Guilt >= 3:

                "guilt = [Guilt]"

                jump death_scene

            jump chainedWoman04_02

        "Say Nothing.":

            $ Guilt += 1

            if Guilt >= 3:

                "guilt = [Guilt]"

                jump death_scene

            jump chainedWoman04_3

label chainedWoman04_02:

    "Your tone is firmer."

    You "I was sent by the One who governs my hand [Player_choice01] to end your suffering. There is no further need for your pain."

    scene chained_woman_angry
    
    "The air tightens. Her eyes flare.
    \'End?\' she repeats."

label chainedWoman04_3:

    "guilt = [Guilt]"

    "You remain silent"

    return

label death_scene:

    scene death_scene with Fade (1.5, 0.7, 1.5)

    "You are overwhelmed with seeing too much girls"

    "Game Over"
