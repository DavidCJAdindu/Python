print("Welcome to my first game!")

name = input("What is your name? ")
age = int(input("What is your age? "))
 
print("")
print("Hello " + name.capitalize() + ". You are" ,age, "years old!")

if age >= 18:
 print("You are old enough to play!")
 print("")

 lets_play = input("Do you want to play? (Y/N) ").lower() 
 print("")
 if lets_play == "y" or lets_play == "yes":
  print("Lets Play! ")

  left_or_right = input("First choice.. Left or Right? (left/right) ").lower()
  if left_or_right == "right": 
   print("")
   boss = input("You are the boss! You can now become the master. Do you want to become the master? (Y/N) ").lower() 
   if boss == "y" or lets_play == "yes":
    print("")
    print("Then you must keep learning!")
   else:
    print("You gotta grind to shine!")
    
  else:
   print("")
   print("Make sure you are alright next time bro!")

 else:
  print("Come back next time!")
  
else:
 print("")
 print("You are not old enough to play :( ")