import random
print("Welcome to rock, paper and scissor game!!")

user_win = 0
computer_win = 0
while True:
    user_choice = input("Enter your choice : ")
    choice = ["rock","paper","scissor"]
    if user_choice == "q":
        break
    
    if user_choice not in choice:
        print("invalid input!")
        continue
    else:
        
        random_choice= random.randint(0,2)
        computer_choice = choice[random_choice]
        if user_choice == " rock " and computer_choice == "scissor":
            print("You Won!")
            user_win =+ 1
        elif  user_choice == " scissor" and computer_choice == "paper" :
            print("You Won!") 
            user_win =+ 1 
        elif   user_choice == " paper " and computer_choice == "scissor" :
            print("You Won!") 
            user_win += 1 
        else:
            print ("You lost!")
            computer_win += 1
            
print("Your score:", user_win,".") 
print("Computer score:", computer_win,".")   