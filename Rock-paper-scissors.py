import random

opponentchoice=['R','P','S']
while True:
    userchoice=input("wanna play a game! type Y for Yes or N for no")
    usrscore=0
    oppscore=0
    
    if (userchoice=='Y'):
        print("let's have fun")

        
        while (usrscore<5 or oppscore<5):
            userch=input("[R]ock , [P]aper,[S]cissors")
            opponentch=random.choice(opponentchoice)
            if userch.upper()=='R' and opponentch=='P':
                oppscore= oppscore+1
            if userch.upper()=='P' and opponentch=='S':
                oppscore= oppscore+1
            if userch.upper()=='S' and opponentch=='R':
                oppscore= oppscore+1    
            if userch.upper()==opponentch:
                continue
            else:
                usrscore=usrscore+1
        
        if usrscore==5:
            print("congrants you won")
        else :
            print("you lost , better luck next time",usrscore)
        
    else :
        break