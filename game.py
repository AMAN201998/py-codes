from ast import Pass
import random
print("Computer choose Rock(R) or Papper(P) or Scissor(S) ?")
a = random.randint(1,3)
if a==1:
    C="R"
elif a==2:
    C="P"
elif a==3:
    C="S"

print("Player choose Rock(R) or Papper(P) or Scissor(S) ?")
Guess = input() 
if (Guess != "P"  and Guess != "S" and Guess !="R"):
    print("Invalid Selection")
else:
    Pass

print(f"Your selecton is {Guess}")
print (f"Computer selection is {C}")

if Guess == C :
    print("TIE")
elif Guess == "R":
    if C == "P":
        print("LOSE")    
    else:
        print("WIN")    
elif Guess=="P": 
    if C == "S":
        print("LOSE")    
    else:
        print("WIN")        
elif Guess=="S":
    if C == "R":
        print("LOSE")    
    else:
        print("WIN") 
else:
    print("Error due to invalid selection!!")          