print('''       /||\
                ||||
                ||||
                |||| /|\
           /|\  |||| |||
           |||  |||| |||
           |||  |||| |||
           |||  |||| d||
           |||  |||||||/
           ||b._||||~~'
           \||||||||
            `~~~||||
                ||||
                ||||
~~~~~~~~~~~~~~~~||||~~~~~~~~~~~~~~
  \/..__..--  . |||| \/  .  ..
\/         \/ \/    \/
        .  \/              \/    .
. \/             .   \/     .
   __...--..__..__       .     \/
\/  .   .    \/     \/   . __..--..''')
print("Welcome to the Mojave Desert.")
print("Your mission is to make it to the Tops Casino in New Vegas.") 


answer = input("Do you follow the road or walk through the desert? type 'R' for road or type 'D' for desert\n").lower()
if answer == "d":
  print ("You were eaten by Deathclaws. Game Over")
if answer == "r":
  print("You've made it to the entrance of New Vegas")
if answer == "r": 
  answer = input("Do you have a Passport, Y/N?\n").lower()
if answer == "n":
  print("You've been killed by the securitrons, Game Over") 
elif answer == "y":
   print("You've made it into the city")
if answer == "y":
  answer = input("What direction do you go? Left, Right or Center? L/R/C\n").lower()
if answer == "l":
  print("You were stabbed by a hobo, Game Over")
elif answer == "r":
  print("You were spit on by a super stripper, you've contraced super aids. Game Over")
elif answer == "c":
  print("You've made it to the Tops Casino, Congratulations, and good luck winning some caps!")
