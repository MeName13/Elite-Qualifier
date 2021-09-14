import random

"""
Personalities will go here
"""
#class Friend:
#  def Bot (Personality, name):
""""
Variables like "Conversation_mode == Greeting" will go here
flavor text kinda
"""

boredom = random.randrange(100) + 20
personalitytype = 0
usergreeting = 0
personalitychoice = 0
confidance = random.randrange(100)

#personality = ("Anxious", "Confident")
#peronalitychoice == random.choice(personality)

"""
Boredom system
Higher bordom values make AI more interesteed in conversation.

When boredom reaches 0 the AI will ask for the conversation to end
If the user cannot increse the AI's boredom above 20 quickly, the AI ill refuse to respond further

Personality can be deided based off of RNG
"""


"""
Main loop, 
Lean switch staments, faster/less lag and better orginization
"""

while boredom > 0:
  print (boredom) #for testing, delete later
  usergreeting = input (f'Type "Hi!" to wake the AI! ') #starting phrase, change later
  while usergreeting == ("Hi!"):


    if confidance <= (0):
      print ("The AI seems nervous")
      name = input ("hello, I am nervous AI. what's your name?")
      print ("You can ask several questions. Would you like, the weather, or ")
      input (f'Hi, {name}. Can i help you with anything today?')


    elif confidance >= 50:
      print (f'The AI seems confidant!') 
      name = input ("Hello, I am confidant AI! what's your name?")
      print (f'Its great to meet you {name}')
  