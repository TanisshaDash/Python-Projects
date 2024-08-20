import random 
target = random.randint(1,50)
attempts = 5

while attempts > 0 :
    Userchoice= input("Guess the Number or type 'q' to quit\n")
    if(Userchoice == "q"):
         print("QuIt!!?")
         break 

    Userchoice = int(Userchoice)
    if(Userchoice==target):
        print("CORRECT GUESS!!!YAYY")
        break
    elif(Userchoice<target):
        print("Number too SMALL,Guess Again")
    elif(Userchoice>target):
        print("Number too BIG,Guess Again")

    attempts -=1
    print(f"Attempts Remaining : {attempts}")
    if attempts==0:
        print(f"GAME OVER!! the correct number was {target}")

        
print("--GAMEOVER--\n--WANNA TRY AGAIN?")



        