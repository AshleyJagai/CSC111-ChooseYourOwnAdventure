#        Name: <Aria Ramanathan, Ashley Jagai>
# Course Info: CSC111 - Fall 2021
# Description: Submission for Assignment 02
#        Date: <9.24.21>

# YOUR CODE HERE

#functions, mostly just print statements that set up story narrative, but also include battle(), reward(), and 
#bag functions that activate choices

def nar6(): #ending part 1 version 1on the left, flee path
  print("\"Oiy! Just where do you think you're doing?\" Yelled Wally. \"The assasins back behind me.")
  print("Lucky for you though, he seems to be out of commision.\"")
  print()
  print("Wally steps aside to reveal an opening to a blacked river. Laying on the ground is a passed out")
  print("druid with a flask in hand. You look to Wally for confirmation but the tall beast is gone")
  print("You look at your {:s} and approach the druid.".format(weapon))
  if weapon == "gun":
    print("You shoot your gun straight into the druid's chest.")
  else:
    print("You take your {:s} and stab it into the druids chest.".format(weapon))
  print("The druid let out a yelp before letting out it's final breath. You take a moment to look around and")
  print("notice a stack in the Druid's pocket. You take the stack and empty out the coins")
  print("You look one final time at the Druid, take a swig from his flask, and walk slowly home.")
  print()
  print("The End")

def nar5(): #ending part 1 version 2 on the left, fight path
  print("Taking your {:s} you charge Wally".format(weapon))
  if weapon == "gun":
    print("Firing randomly, you shoot your gun into the back of Wally the Rat.")
  else:
    print("You jump onto Wally's back and stab your {:s} into him.".format(weapon))
  print("Wally lets out a small yelp, before turning around and batting you sideways.")
  print()
  
def nar4(): #ending version 3 on the right, gold path
  print("You decide that the quest isn't worth it. With the some of that money in the chest, you'll never need to")
  print("work again. But when you go to reach for the coins you feel a hot sensaion against your skin")
  print("As you shriek in pain, the skin on your hands burns away, leaving your bare bones showing.")
  print("You divert your attention to the coins and see a layer of acid coating each piece of gold.")
  print("Clutching your hand in pain you run over to a nearby puddle and sink your hand into it.")
  print("After a little while with your hand in the water, the pain begins to go away.")
  print()

def nar3(): #ending part 2 for gold/glory path

  print("You cautiously continue onward, toward what appears to be a river, blacked by lead.")
  print("Laying on the ground is a passed out druid with a flask in hand.")
  print("You look at your {:s} and approach the druid.".format(weapon))
  if weapon == "gun":
    print("You shoot your gun straight into the druid's chest.")
  else:
    print("You take your {:s} and stab it into the druids chest.".format(weapon))
  print("The druid let out a yelp before letting out it's final breath. You take a moment to look around and")
  print("notice a stack in the Druid's pocket. You take the stack and empty out the coins")
  print("You look one final time at the Druid, take a swig from his flask, and walk slowly home.")
  print()
  print("The End")

def battle(): #fightOrFlee choice, leads into endings
  fightOrFlee = str(input("While Wally's back is turned, do you fight or flee? "))
  print()
  if fightOrFlee == "fight":
    nar5()
  elif fightOrFlee == "flee":
      print("Slowly, before Wally can notice you, you creep back toward the fork in the caves.")
      print("But before you can escape, Wally turns around.")
      print()
  nar6()

def reward():#goldOrGlory choice, leads into endings
  goldOrGlory = str(input("Do you choose the gold or glory? "))
  print()
  if goldOrGlory == "gold":
    nar4()
    nar3()
  elif goldOrGlory == "glory":
    nar3()
  print()

def bag1(): #weapon choice 1
  print("As you reach into the first bag, you feel cold metal against your skin.")
  weaponChoice = "gun"
  return weaponChoice

def bag2(): #weapon choice 2
  print("As you reach into the second bag, you feel a sharp blade against your skin.")
  weaponChoice = "knife"
  return weaponChoice
  
def bag3(): #weapon choice 3
  print("As you reach into the third bag, you feel a splinter pierce your skin")
  weaponChoice = "stick"
  return weaponChoice
    
def storyNar3(pathChoice): #after chosen path, leads into final choices
  print("You make your way down the path on the {:s} as you hear a sudden crash.".format(pathChoice))
  print("Gripping you {:s}, you continue cautiously down the path. Out of no where, you see".format(weapon))
  print("a dim light in the distance. As you approach it, you let out an audible gasp.")
  print()
  if pathChoice == "left": #meaning you get fight/flee choice
    print("A terrifying beast with its back turned stands stoutly in front of you. Scales poke out of its")
    print("spine and the floor was splattered with blood. You glance across the room and look at the monster's")
    print("face through a shattered mirror. Horrified, you stumble backwards as you realize...")
    print("It's Wally the Rat. But he's big. He must be the assassin.")
    battle()
  else: #meaning you picked right and get gold/glory choice
    print("In front of you was an untouched chest full of treasure. ")
    print("With that sum on money, you would never have the need to fulfill stupid quest for nobles again.")
    print("But if you please this noble, you'll continue to build your reputation.")
    reward()

def storyNar2(): #after you've choosen weapon, which doesn't affect plot
  print("You look down to find a", weapon, "in your hand")
  print()
  print("\"Interesting. Follow the map inside the bag to get to the mine. Now scram.\"")
  print()
  print("And with that Wally grabbed the other two bags and scuried away from the table.")
  print("You make your way out of the pub and toward the mineshaft. Clenching your", weapon)
  print("you make your way down the mineshaft. Eventually you come to two diverging paths.")
  print("The map is unclear which to take. The one on the left reeks of feces while the") 
  print("other appears to be scattered with rotting flesh.")
  print()
  path = str(input("pick which path left or right (left  or right): " )) #path choice, after this brances start
  print()
  if path == "left":
    storyNar3(path)
  elif path == "right":
    storyNar3(path)

def main():
  storyNar2()


#Beginning Story Narr
print("It was a dreary November night when you first recieved the letter")
print("from Lord Benjamin Jamal. As you rip open the envelope a hefty sum")
print("of money falls out. You break the red seal and read the following:")
print()
print("\"My sources tell me you're the deadliest rogue this side of the mountain.")
print("Think of this as a downpayment for your services. Meet me at Topelli's Pub tonight")
print("at 1:15 am. We'll discuss your quest and reward soon.\"")
print()
print("You look again at the sum of money and place it under your floor board before")
print("glancing at your clock. Quarter to 1. You lace up your boots and take a swig of")
print("mead before heading out the door.")
print()
print("You enter Topelli's and immediately notice a dark figure lurking in the corner.")
print("As you begin to approach them, they leave their seat and make their way to the")
print("basement steps. They motion for you to go down. As you decend the eerie")
print("creaking steps, you hear the door slam the door behind you. As you reach the bottom")
print("and make your way toward the light in the middle of the room, you notice")
print("a rat standing in front of three large bags.")
print("")
print("\"Oiy, took ye long enough!\" Yelled the rat.")
print("\"I'm Wally. I'm a rat. You get the picture.\" ")
print("\"Lord Benjamin Jamal's rival, Lord Faar Quahd, has been plotting an")
print("assasination attempt for weeks. We've recieved word the assasin is hiding out")
print("in the abandoned mineshaft upstream. You are to kill the assasin and bring his ")
print("companion, alive. Pick a bag and inside it will be your weapon.\"")
print()

weapon = str(input("Do you pick bag 1, 2, or 3? "))
print()
if weapon == "1":
  weapon = bag1()

elif weapon == "2":
  weapon = bag2()

elif weapon == "3":
  weapon = bag3()
else:
  print("Alright smart ass you get the third one then.")
  weapon = bag3()
  
  
if name == "main":
  main()
