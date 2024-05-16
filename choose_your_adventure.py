print("Welcome to adventure game")
name = input("Enter your name :")
answer= input("Which path you you want to select left or right? : ").lower()
if answer == "left":
  answer = input("You can swim or take a walk: choose swin or walk : ")
  if answer == "swim":
    print("You swam across and were eaten by an aligator.")
  elif answer == "walk":
    print ("You walked for many miles, you ran out of water and lost the game.")
  else:
    print("Not a valid option. You lose.")  
elif answer == "right":
  answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back): ").lower()
  if answer == "back":
    print("You go back and lose. ")
  elif answer == "cross":
    answer = input ("You cross the bridge and meet a stranger. Do you talk to them (yes/no)?" )
    if answer == "yes":
       print("You talk to the stranger and they give you gold.You WIN!")
    elif answer == "no": 
       print("You ignore the stranger and they offended and you lose.") 
  else:
    print("Not a valid option. You lose.")  

else:
    print("Not a valid option. You lose.")  

print ("Thank you for trying,",name)     