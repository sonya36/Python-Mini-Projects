import random
count_guess = 0
max_limit_range = input("Give the max limit up to which you want to guess: ")
if max_limit_range.isdigit():
    max_limit_range = int (max_limit_range)
    random_number = random.randint(0, max_limit_range)
else :
   print("Give input as number.")
   quit()


while True:
   count_guess = +1
   user_guess = input("Guess the number: ")
   if user_guess.isdigit():
    user_guess = int (user_guess)
   
    
    
   else : 
        print("Give input as number not string")
        continue
   
   if user_guess == random_number:
      print ("You got it right")
      break
   else:
      print ("You got it wrong!")
      if (user_guess<max_limit_range):
         print("Giver higher guess than before.")  
      else :
         print("Giver samller guess than before.") 
            

print("You got in ", count_guess,"guesses")  
     

  