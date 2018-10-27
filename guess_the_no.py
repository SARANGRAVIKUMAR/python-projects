import random
name = input("enter the your name")
print ("Hello",name,"welcome to the the game GUESS THE NUMBER")
guess = 0
n=0
print("enter the limit upto which you wish to guess and enter the limit greater than 20")
n = int(input())
sys_no =random.randint(1,n)
print ("select the game difficulty")
print("enter 1) BEGINER \n 2) MEDIUM \n 3)ADVANCED")
print ("NUMBER OF CHANCES\n  BEGINER : 20 \n MEDIUM : 10 \n ADVANCED : 6")
c = int(input())  

d="yes"
while (d=="yes"or d== "y"):
    if (c==1):
        for a in range(0,20):
            print ("GUESS A NUMBER")
            guess = int (input())
            if(sys_no == guess):
                print("YOUR GUESS IS CORRECT")
                break
            elif(sys_no < guess):
                print("YOUR GUESS IS HIGHER THAN THE REAL NO")
                continue
            else:
                print("YOUR GUESS IS LOWER THAN THE REAL NO")
                continue        
            
    if c==2 :
        for a in range(0,10):
            print ("GUESS A NUMBER")
            guess = int (input())
            if(sys_no == guess):
                print("YOUR GUESS IS CORRECT")
                break
            elif(sys_no < guess):
                print("YOUR GUESS IS HIGHER THAN THE REAL NO")
                continue
            else:
                print("YOUR GUESS IS LOWER THAN THE REAL NO")
                continue
            
    if (c==3):
        for a in range(0,6):
            print ("GUESS A NUMBER")
            guess = int (input())
            if(sys_no == guess):
                print("YOUR GUESS IS CORRECT")
                break
            elif(sys_no < guess):
                 print("YOUR GUESS IS HIGHER THAN THE REAL NO")
                 continue
            else:
                 print("YOUR GUESS IS LOWER THAN THE REAL NO")
                 continue

    else:
        print("wrong choice")
    print ("enter yes or y to continue")
    d = input()
