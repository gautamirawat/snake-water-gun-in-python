import random
print("----------------- Welcome to the game ------------------")
print('''
-> Computer VS Player (Press 1)
''')
o=int(input("enter number: "))

def game(c,y):
    cm=0
    ym=0
    if c==1:
         if y==1:
            print("Tie")
            
         elif y==2:
            print("Computer wins!")
            cm=cm+1
            
         elif y==3:
            print("You win!")
            ym=ym+1
            
        
    if c==2:
        if y==1:
            print("You win!")
            ym=ym+1
            
        elif y==2:
            print("Tie")
            
        elif y==3:
            print("Computer wins!")
            cm=cm+1
            
        
    if c==3:
        if y==1:
            print("Computer wins!")
            cm=cm+1
            
        elif y==2:
            print("You win!")
            ym=ym+1
            
        elif y==3:
            print("tie")

    print("Score :")
    print("Computer - " + str(cm))
    print("You - " + str(ym))

         
       

    

def cp():
    print("---------- Welcome to Computer VS Player Mode ----------")
    reps = int(input("enter the number of rounds you want in one game: "))
    for i in range(0,reps):
        comp = random.randint(1,3)
        you = int(input("Its your turn (1 for SNAKE | 2 for WATER | 3 for GUN) - "))
        print("Its Computer's turn -")
        if(comp==1):
            print("SNAKE")
        elif(comp == 2):
            print("WATER")
        elif(comp == 3):
            print("GUN")
        game(comp,you)

    



if(o==1):
    cp()
else:
    print("Enter a valid option!")
