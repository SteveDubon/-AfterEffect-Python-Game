"""We decided to create a video demo because we are using the Pillow library. If you would like to play the game but dont want
to install the library simply get rid of line 4 and lines 98 and 99. You wont be able to see the images, but you'll be able to play"""

from PIL import Image                #imports Pillow (images)

import random
day=1
dead=0
water=3
food=3
bullets=0
list_of_places=["house", "store", "river", "mountain", "national park", "desert"]
current_location=list_of_places[random.randint(0,len(list_of_places)-1)]
inquiry=''
option_list=['A','B','C','D']
bool=False
k=0
print("WELCOME TO AfterEffect: Bill's Apocalyptic Adventures")
welcome = Image.open("Welcome.jpg")
welcome.show()

print("\nINSTRUCTIONS:")
print("Choose a letter to perform an action. Be mindful of your location and use capital letters for your option choices!")
print("Option A: Forage for food ")
print("Option B: Search for water ")
print("Option C: Search for bullets ")
print("Option D: Move locations")
#inquiry = input("Which option do you choose?")

while day<101 and dead==0:

   print("\nTurn: " +str(day))
   print("You have %d days worth of water" %water)
   print("You have %d days worth of food" %food)
   print("You have %d bullets" % bullets)
   print("You are now at a %s" %current_location)


   print("Choose a letter to perform an action. Be mindful of your location and use capital letters for your option choices!")
   #print("Option A: Forage for food ")
   #print("Option B: Search for water ")
   #print("Option C: Search for bullets ")
   #print("Option D: Move locations")
   inquiry=input("Which option do you choose?")


   if inquiry=='A':
       if current_location=='house' or current_location=='store':
           food_found= random.randint(0,5)
           food+=food_found
           print('\nYou found %d days supply worth of food!' % food_found)
       elif current_location=='river':
           food_found = random.randint(0, 2)
           food += food_found
           print('\nYou found %d days supply worth of food!' % food_found)
       elif current_location=='mountain' or current_location=='national park':
           food_found=random.randint(0,3)
           food+=food_found
           print("\nYou found %d days supply worth of food!" %food_found)
       else:
           food_found=random.randint(0,1)
           food+=food_found
           print("\nYou found %d days supply worth of food!" % food_found)


   elif inquiry=='B':
       if current_location == 'house' or current_location=='store':
           water_found = random.randint(0, 5)
           water += water_found
           print('\nYou found %d days supply worth of water' % water_found)
       elif current_location == 'river':
           water_found = random.randint(0, 10)
           water += water_found
           print('\nYou found %d days supply worth of water!' % water_found)
       elif current_location == 'mountain' or current_location=='national park':
           water_found = random.randint(0, 3)
           water += water_found
           print("\nYou found %d days supply worth of water!" % water_found)
       else:
           water_found = random.randint(0, 1)
           water += water_found
           print("\nYou found %d days supply worth of water!" % water_found)

   elif inquiry=='C':
       if current_location=='house' or current_location=='store':
           bullets_found=random.randint(0,20)
           bullets+=bullets_found
           print("\nYou found %d bullets!" %bullets_found)
       elif current_location=='mountain':
           print("\nYou didn't find any bullets on the mountain. What mountain has bullets laying around?")
       elif current_location=='desert':
           print("\nYou're in a desert! You didn't find any bullets!")
       elif current_location =='river':
           print("\nYou didn't find any bullets. Rivers aren't known for weapons and ammunition, don't be surprised")
       else:
           print("\nThere's nothing in the national park but trees...")
   elif inquiry=='D':
       world = Image.open("World.jpg")                      #This is the image of the map
       world.show()                                         #If you want to play without Pillow, get rid of these two lines
       current_location=list_of_places[random.randint(0,len(list_of_places)-1)]
       water-=2
       food-=2
       day+=2
       print("\nYou have been moved to %s. You used 2 days worth of food and water to move." %current_location)
   else:
           print("\nDidn't choose an option. No option executed this turn. Be sure to put the correct letters A B C or D.")

   if water<=0 or food<=0:
       dead+=1

   if day%10==0:
       zombies=random.randint(0,25)
       print("\nWatch out! A zombie horde of %d zombies is coming to attack you! Luckily you're a good aim and need only 1 bullet to kill a zombie. Hopefully you have enough bullets!" %zombies)
       if zombies>bullets:
           print("\nYou didn't have enough bullets. You tried to run, but there was no escape. ")
           dead+=1
       else:
           bullets=bullets-zombies
           print("\nYou did it! You killed them all! Thank God you had enough bullets.")



   day += 1
   water -= 1
   food -= 1


if dead==1:
   print("\nYou died. Game over. Thank you for playing!")
else:
   print("\nCongratulations! You survived!")
