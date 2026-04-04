# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define You = Character("You")
define Man = Character("Goetia")
define Chained = Character("Chained Woman")
define Elder = Character("Old Man")

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

    play music "audio/AreWeAlone.mp3" fadein 1.0

    window hide
    $ _dismiss_pause = False
    scene girl_city with Fade(1.5, 0.5, 1.5)
    $ renpy.pause(3.5, hard=True)
    $ _dismiss_pause = True
    window auto

    "You behold the city from afar."

    "From the outer gate it feigns smallness{cps=30}... like a thing that would not be feared, but the lie rots as you inch closer, It swells in the sight, 
    unfolding without end, until it stands like a continent raised from the bones of the world."
    
    "Its walls are sheer as cliffs, pale as flayed ivory. Within them festers a multitude, living things and dead things, so mingled they are no longer apart."

    "All is salt{cps=20}... All is wet... All is heavy."

    "The very air clings to your throat like cancerous plasma."

    scene city_gate01 with dissolve

    menu:

        "Check the statue":

            jump statue

        "Move to the gate":

            jump gate

label statue:

    scene statue

    "A statue stands by the path, a gargoyle, bowed, as if in grief or worship. At its base, words are carved deep:"

    "{cps=20}A paramour, of the sadness of creation from tears and mortars. After all these years and still, still learning, how to properly die."

    jump gate

label gate:

    scene city_gate02 
    
    "A man kneels before the gate, pale, naked."


    jump sitting
 

label sitting:

    scene sitting

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "As you draw near, he speaks, though he does not turn."

    Man "So. They have sent you."

    "When he speaks, it is as though the gravel has found a tongue."

    Man "I wondered who would replace me. I did not expect{cps=10}... this."

    "His back tightens."

    Man "Tell me, what is more insulting?{cps=10} That they sent a woman... or that they sent a child?"

    Man "Was my failure so profound, that they now must place their faith in you?"

    menu:

        "What is wrong with being a woman?":

            Man "The womb is a treacherous vessel. It carries life… or it carries disease."

        "I am not a child.":

            Man "You wear youth like a mark. Sixteen, perhaps seventeen. The difference means nothing here."

    Man "Hear me well."

    Man "{cps=20}Whatever you have been told, forget it. It is worse, not in count, but in kind.
    From the dust beneath your feet to the cold fires above, all things that devour come here to rest. Even the light here has teeth."

    Man "{cps=20}All your prayers, your signs, your holy teachings, they are wind.
    They shall tear through your guts and be as nothing. Your balm and cross are mere furnishings in the bellowing of the earth."

    menu:

        "You are blaspheming.":

            You "Your failure is your own. It is not the undoing of all things."

            "He laughs, bitterly."

            Man "My failure? No, ours. The thousands that came before me, the legions yet to come, beginning with you.
            You can hear their agonies in Basilidies' cube, begging for mercy, cursing priests and altars.
            Tearing at the horse's skull, in the breathing grave between bile and burial."

        "You should leave this place now.":

            You "Then go. Return to the one who sent you. Your duty is done."

            Man "Return?"

            "He lets out a hollow breath."

            Man "All who enter are sealed, pressed between orichalcum and cinders, marked with the marred finger of her name, 
            name unspoken, for it has none.The holy exsanguination, that incessant trembling of anything that dares to hide a spine."
            
            Man "This place is called Capita Mortua. Not without reason."

    Man "So which of them sent you?"

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

    Man "Then you arrive empty, as commanded.\nUntouched by verdict, unbranded by stain."

    #"The man stiffens. The chains at his wrists tighten without being touched."

    #Man "The Sanctum beyond sanctums?\nThe Silence that outlives prayer?"

    #"He studies you as one studies a relic dug from a grave."

    #Man "Then you arrive empty, as commanded.\nUntouched by verdict, unbranded by stain.Walk, pilgrim.\nThe city will measure you in due time."

    jump SittingMan01

label JudgeJudgments:

    #"The crouched man lowers his head further, as though pressed down by an unseen palm."

    #Man "Ah, The Gavel that falls before the crime.\nThe Eye that convicts the unborn."

    #"A dry laugh escapes him."

    #Man "Then you come already absolved by terror. The scales have leaned in your favor—but do not rejoice. Mercy is a debt that fattens."

    "The Gavel that falls before the crime. The Eye that convicts the unborn. Then you come already absolved by terror.
    The scales have leaned in your favor—but do not rejoice. Mercy is a debt that fattens."

    jump SittingMan01

label InnocenceInnocence:

    #"For the first time, he smiles faintly."

    #Man "Innocence?"

    #"He rises slightly from his crouch, joints cracking "

    #Man "To claim such origin is to confess ignorance of blood. You slouch forward with fragility, yet heavier than you believe"
    
    #"The incardinate moon throbs faintly behind him."

    #Man "Could not your geriatric order scrape the marrow of someone more fitting?\nA spine less green.\nOr at least… a man?"
    
    #You "…."

    Man "Innocence?"

    "He rises slightly from his crouch, joints cracking."

    "To claim such origin is to confess ignorance of blood. You crawl forward with fragility, yet heavier than you believe"

    jump SittingMan01

label SittingMan01:

    Man "Speak. Tell me what grotesque providence shaped you."

    menu:

        #When overwhelmed, you may cleanse a portion of Guilt.
        "It is my birthpain.":

            $ Player_choice02 = "my birthpain"

            "When overwhelmed, you may cleanse a portion of Guilt."

            jump SittingMan01_01

        #You may save once at any moment. Loading deletes the file forever.
        "I was bred solely for this purpose.":

            $ Player_choice02 = "bred for this purpose"

            "You may save once at any moment. Lodaing deletes the file forever."

            jump SittingMan01_02
        
        #When you take a life, there is a slim chance your Guilt will not increase.
        "No one else can carry the Dagger of Our Lady of Sorrow.":

            $ Player_choice02 = "the Dagger of Our Lady of Sorrow"

            "When you take a life, there is a slim chance your Guilt will not increase."

            jump SittingMan01_03
    
    return

label SittingMan01_01:

    "You do not flinch."

    You "It is my birthpain, bestowed upon me by blood, by the blood of my blood.\nA cursed lineage, a sacred anathema.
    I did not choose this wound.\nI inherited it. It gnaws me from within like an unborn twin."

    "The crouched man studies your trembling hands."

    Man "Ah. An heir to affliction. Very well.\nWhen the weight of your inheritance crushes your ribs, you may spill some of it upon the earth."

    "He presses his palm to the dust."
    
    Man "But know this: pain cleansed is still pain remembered."

    jump SittingMan02

label SittingMan01_02:

    "Your voice is steady, disturbingly so."

    You "I was honed through years to do this. Molded. Bred for this singular purpose and nothing else. I am a vessel.
    A burial that walks."

    "The man's lips twitch."

    Man "A creature without surplus{cps=20}... how efficient."

    "He rises an inch higher."

    Man "Then you may defy the flow of fate once. You may carve a moment into permanence.
    But when you return to it, the past will refuse to remember you again."

    "His shadow splits briefly in two before merging."

    Man "An urn can only break once the world will remember that you hesitated. And it will not offer you another mercy."

    jump SittingMan02

label SittingMan01_03:

    "Your hand brushes the hidden weight at your side."

    You "No one else can carry the Dagger of Our Lady of Stones. It answers only to my pulse, and thirsts only for my circulation."

    "The crouched man inhales through his teeth."

    Man "{cps=20}Interesting... interestin... fascinating, so young, too young."

    "He continues..."

    Man "So I assume that by her granular piety, there's a slim chance that your soul does not swell with the expected Guilt.
    The deed settles within you as sediment settles in a drowned cathedral."

    jump SittingMan02

label SittingMan02:

    Man "Finally, indulge an old sentinel in a useless curiosity. This will not bend your road, nor lighten nor blacken your soul. But words have weight, and I would feel yours."

    "He draws a circle in the sand with a cracked fingernail."
    
    Man "What compels you to approach this forsaken city, this open crypt that breathes with no lungs?"

    menu:

        "Conclusion":

            jump SittingMan02_01

        "Salvation":
        
            jump SittingMan02_02

        "Retribution":

            jump SittingMan02_03
return

label SittingMan02_01:

    scene hand_circle
    
    You "I come to bring things to an end. For better or for worse."

    Man "Ah. The mercy of cessation."

    "He nods, almost tenderly."

    Man "You seek the last page, be warned, endings are gluttonous. To conclude is to deny resurrection."

    "He smudges the circle into nothing."

    jump ManEnd

label SittingMan02_02:

    scene hand_x
    
    You "I come to save what can still be saved."

    "A faint, brittle smile fractures his face."

    Man "Salvation… that arrogant tenderness. You may rescue a fragment, a memory, a single uncorrupted syllable.
    But understand, salvation is subtraction. To save one thing is to abandon another."

    "The circle in the dust remains unbroken, but he draws a single vertical line that splits it into two"

    jump ManEnd

label SittingMan02_03:

    scene hand_star
    
    You "I come to purify all the putrescent spleens!"

    "The crouched man laughs softly"

    Man "Purification is a beautiful word for violence."

    "He is quite for a second" 

    Man "{cps=20}But maybe that's our only, and final hope"

    "He presses his palm against the circle"

    jump ManEnd

label ManEnd:

    Man "{cps=15}Very well. End it. Save it. Scour it. No one will resist your reason."

    "The gates open with the metal wheezing of cancerous ribcage."

    Man "But know this, you do not get second chances in this place. And child, regardless of the path you take,
    you will end up alone in the end"

    menu:

        "Market":

            jump girl_market01

        "Square":

            jump square

        "Cathedral":

            jump cathedral

label square:


    window hide
    $ _dismiss_pause = False
    scene girl_square with Fade(1.5, 0.5, 1.5)
    $ renpy.pause(3, hard=True)
    $ _dismiss_pause = True
    window auto

    "The breath of others, the pious masses overwhelms yours, too many Gods populate this place,
    too many fingers fold and break in strange prayers."

    menu:

        "West, Del'ut The Hollow":

            scene girl_square_god03

            "He stands as you read about him, perhaps a little less visceral, his ribs and fascis are devoid of skin or flesh,
            Del'ut the hollow at the feet of his idol, his teachings are inscribed."
            
            "Bleed from thy mouth, from thy ankles,and from thy breasts, And bathe yourselves in blood, and drown in blood, 
            and sate yourselves with blood."
            
        "East, Mal-Ithus The Blind":

            scene girl_square_god01

            "East, Mal-thus the blind is bent almost like a beast, his face is unrecognizable from the burns and scars,
            at his foot it reads “I am the holiest, but nothing holy remains within me”"

        "South, Tanis, The Cold":

            scene girl_square_god02

            "I still love this world, even its dark places, revelations 6:12-13"

        "North, Nadine, The Hurtless.":

            scene girl_square_goddess

            "I've damned myself but more importantly, I have damned young men who understood nothing but the taste of coffee and tobacco"

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

            Chained "I am asking if you, fledgling thing— you whose voice has not yet cracked upon real grief, whose blood has not learned the taste of ash. What salvation do you presume to offer me?
            \nWhat limb of the broken world have you ever lifted? For seven years I have borne the cairn of my husband, my mother,and the child who perished unnamed within me. Seven years more are decreed."

            jump chainedWoman03
        
        "I have nothing, but the dagger on my back.":

            Chained "So you bring me a cruel remedy, then where did you get the gall to inquire after my weight? creature with a whiny voice, and beleaguered blood,You have known inconvenience, not ruin. 
            For seven years I have borne the cairn of my husband, my mother,and the child who perished unnamed within me. Seven years more are decreed."

            jump chainedWoman03

        "I can help remove the rocks off your back.":
            
            Chained "And what inherent mercy compels you, child of exalted roots, that you might carry the dust of others and not be buried with it?
            \nFor seven years I have borne the cairn of my husband, my mother,and the child who perished unnamed within me. Seven years more are decreed.
            \nAnd all through time we had sufferers. And if it's our birthright to suffer then let it be. And if it's our blight to be lied to continually, 
            blight growing more, then it's also our right. So see the mucous and the veins thicken."

            $ Guilt -= 1

            jump chainedWoman03

label chainedWoman03:

    menu:

        "I am here to relieve your pain.":

            $ Grace += 1

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

label chainedWoman04_01:

    "Your voice does not rise above hers."

    You "I was sent by the One who named me [Player_choice01] to release you from your suffering. You have borne enough."

    "You step no closer."

    "Your pain has ripened. It need not continue."
    
    "Her breath stutters, The tension in her jaw softens."

    "\"Relief…\" she murmurs, as though uttering an extinct word."

    "The veins along her neck recede slightly."

    Chained "If this is grace, let it be quiet."

    jump girl_market01


label chainedWoman04_02:

    "Your tone is firmer."

    You "I was sent by the One who governs my hand [Player_choice01] to end your suffering. There is no further need for your pain."
    
    "The air tightens. Her eyes flare.
    \'End?\' she repeats."

    Chained "You presume completion. You presume authority over my sin, you lowborn bitch?"

    "Her hands clench."

    Chained "Pain is not a candle for you to snuff. It is mine,"

    scene chained_woman_angry

    "Her portrait shifts — harsher lines, brighter glare."

    jump girl_market01

label chainedWoman04_3:

    "guilt = [Guilt]"

    "You remain silent"

    jump girl_market01

label girl_market01:

    scene girl_market_transition with Fade(1.5, 0.5, 1.5)
    
    window hide
    pause 10.0 
    window auto

    "The air alters.\nA faint sweetness intrudes upon the cadaverine rot—the sour reek of opened marrow, 
    the chalk-dust incense of bioceramic skulls long emptied of prayer." 

    "Above you, iron hooks sway and creak like censers in a desecrated liturgy. 
    \nLife, if it may still be named so, reveals itself here in its most honest form."

    menu: 

        "Find Ishaq":

            jump martyr_of_hate


        "Explore the Market":

            jump explore_market

label explore_market:

    scene explore_market01

    "exploring the market1"

    scene explore_market02

    "exploring the market2"

    jump martyr_of_hate

label martyr_of_hate:

    
    scene girl_market_walk01  

    "As you pass, their stares pierce you—not with curiosity, but with a dull, forensic knowing, Your skull, 
    not yet fully ripened into its final shape, draws their gaze like a wound draws flies."

    "No one speaks to you. No one touches you."

    scene girl_market_walk02

    "Only murmurs, thin, papery whispers, flutter in your wake.\nAll your preparation, your childhood's severities, 
    your youth's disciplines, the catechisms etched into atom and nerve, collapse here into insufficiency."


    "You were honed for this, filed down, sanctified, emptied, and refilled until your very marrow recited it and still, it is not enough.
    The reality exceeds the scripture. No illumination, no illumination ever rendered the texture of it, the industrial century of gore"

    scene girl_standing_market

    "You find him where your spleen insisted he would be... {w= 3.0} {cps=30}Not by sight, but by that deeper organ-memory, He has already noticed you.
     Or rather, he has already smelled you."

    scene girl_looking_market

    "A solitary, crawling aberration in a place where carcasses hang like vestments And there he is, withdrawn from it all in a monk's parody of seclusion.
    He resembles a beggar, or something more primitive: a first attempt at man, abandoned mid-creation."

    "He has no lower half. From the waist down, his body gives way not to absence—but to growth. A small garden blooms from him; 
    Stems, roots, pale blossoms pushing outward where organs should have continued, anchoring him into the earth as though he had chosen to be planted rather than buried."

    scene elder01

    Elder "I would know that scent... {w=3.0} {cps=30}as I know the prayer of Our Lady the Hurtless."

    "His head tilts, not toward your face, but toward your circulation." 
    
    Elder "You are not of this place. No… no… it is impossible. Nothing born here could carry such a fragrance."

    "He inhales, deeply."

    Elder "You have traveled far. I can smell it unraveling in your arteries… threaded through your flesh… clinging to the roof of your mouth, and inside your iris"

    "{cps=20} ........."

    Elder "Blood."

    "Another inhale, sharper, desperate."

    Elder "Within… and without. {w=1.0} {cps=20} Heh…"

    Elder "I smell you."

    scene girl_market_cut

    "His blind eyes, white, obliterated, turn with impossible precision."

    Elder "The scent of amputated resurrection, the perfume of mutilated deliverance."

    "He tries to lift himself up in futility."

    scene elder_lift_up with Fade(0.60, 0.10, 1.0)

    "You feel it then, Not fear, not entirely, But exposure.\nAs though you existed without consent."

    Elder "You carry it poorly"

    "A soft, almost pitying judgment."

    Elder "Chimeras always do. It escapes you… leaks from you… like heat from fresh slaughter."

    You "What?"

    Elder "I would know that scent anywhere."

    Elder "Blood. Perfect blood. Red, vital, unspent."

    scene girl_market_crouch with Fade(0.60, 0.10, 1.0)

    "His lips twitch, remembering."

    Elder "I built an arsenal from it. Not of iron, no, but of men. Real men. 
    Men swollen with circulation, with surplus, with the obscene generosity of flowing life."

    "His voice sharpens, almost proud."

    Elder "Men who found no satisfaction in women, nor in books. 
    Men whose hunger coiled like vipers, driving them beyond the last ruins of reason."

    scene girl_elder_head

    Elder "A brotherhood of arteries. A congregation of overflow."

    Elder "They could not live on bread. They could not drink wine. Poetry did not touch them. 
    Beauty did not slow them. They were abundance made flesh, Angels, at times. Demons, more often."

    Elder "And they longed, for the crucifix, and I gave them death."

    scene girl_hand_blood

    "There is blood on my hand"

    scene girl_blood_touch

    Elder "You know the secret of being a good commander?"

    menu:

        "Yes":

            Elder "then speak."

            jump answers

        "No":

            Elder "Then think. Think until it wounds you."

            jump answers
        
        "I am not interested in the theology of beasts":

            Elder "Fair"

            jump answers

label answers:

    "Three answers form in you"

    menu:

        "Authority":

            Elder "Wrong{cps= 30}... Command is not authority."

            jump commander_answer

        "Intelligence":

            Elder "Wrong{cps= 30}... Command is not intelligence."

            jump commander_answer

        "Faith":

            Elder "Wrong{cps= 30}... Command is not intelligence."

            jump commander_answer


label commander_answer:
        
    Elder "It is measure. It is accounting."

    Elder "To command… is to understand that every order you give is a grave already dug, and to give it anyway."

    "His nose twitching as your scent reaches him once more."
    
    Elder "{cps=20} Ah… Yes… There it is again…"

    Elder "Like a dog catching fresh game. The morning after the burning of Laith Kheifar. I looked at the sky, and felt nothing but distance."

    Elder "For nearly four centuries, no rain fell—not a single drop. Then one night, in the east, the heavens broke. 
    It rained as if only heaven could bear such weight. They say God could no longer hold back his tears"

    Elder "You smell of fire and salt. Of flowering corpses. Of bells tolling over open earth, and shovels striking wet soil in the dark."

    Elder "Twelve thousand marched beneath my banners, twelve thousand sons, husbands, boys. What they found instead… was me."

    "He exhales, slow as a dying wind."

    Elder "Seven returned. Seven men out of twelve thousand."

    Elder "I sowed the womb of the earth with blood and tears; I inseminated Gaia with ruin. I brought grief to their gods and desolation to 
    their houses, and in the night, they come, twelve thousand footfalls rising from the dark. their faces split open in agony."

    Elder "I lived as I knew how, and now my sins unmake me, thread by thread, sinew by sinew."

    Elder "So… you. Slave of Morthiel. You stink of christened alumina and sanctified dust. 
    Have you come at last to finish what was decreed? To bend yourself to command?"

    Elder "I have endured here eight hundred years. I counted each one."

    Elder "Did they teach you Arabic in that myrrh-plagued cathedral of yours? Did they whisper to you that khalas is both ending and 
    deliverance—that enough is the only mercy left to man? There is no peace in persistence. Only delay."

    "You instinctively get down to his level, as he open his hands to you, begging for your touch."

    menu:

        "hold his hands":

            $ Grace += 1

            scene hands_held

            "You have never felt such coldness, such burning coldness"

        "Don't hold his hand":

            $ Guilt += 1

            scene hands_not_held

            "Stuck in this putrid existence, how come the bird can fly where I could not walk"


scene black_screen

"wait"

label hands_held:



label hands_not_held:



label death_scene:

    scene death_scene with Fade (1.5, 0.7, 1.5)

    "You are overwhelmed with seeing too much girls"

    "Game Over"
