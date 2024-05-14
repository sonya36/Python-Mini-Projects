print("Welcome to my quiz game!")
playing = input ("Do you want to play? ")

if playing.lower() != "yes" :
    quit()
else :
    print("Okay,let's play the game.")
    score = 0
    answer = input ("What is the name of highest mountain in the world? ")
    if answer.lower() == "mount everest":
        print("!Correct")
        score = + 1
    else:
        print("!Incorrect")

print("You got " + str(score) + " question correct!")
print("You got " + str((score/2) * 100)+"%.")
    


