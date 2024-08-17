import random 
target = random.randint(1,100)

while True:
    Userchoice= input("Guess the Number or quit\n")
    if(Userchoice == "quit"):
         print("QuIt!!?")
         break 

    Userchoice = int(Userchoice)
    if(Userchoice==target):
        print("CORRECT GUESS!!!YAYY")
        break
    elif(Userchoice<target):
        print("Number too SMALL,try another")
    elif(Userchoice>target):
        print("Number too BIG,try another")
   
print("--GAMEOVER--\n--WANNA TRY AGAIN?")



         