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
print ("GUESS A NUMBER")
guess = int (input())
d="yes"
while (d=="yes"or d== "y"):
     if (c==1):
        while(a<20):
            if(sys_no == guess):
                print("YOUR GUESS IS CORRECT")
            elif(sys_no < guess):
                print("YOUR GUESS IS LOWER THAN THE REAL NO")
            else:
                print("YOUR GUESS IS HIGHER THAN THE REAL NO"
        
            a= a+1
    elif (c==2):
        while (a<10) :
            if(sys_no == guess):
                print("YOUR GUESS IS CORRECT")
            elif(sys_no < guess):
                print("YOUR GUESS IS LOWER THAN THE REAL NO")
            else:
                print("YOUR GUESS IS HIGHER THAN THE REAL NO")
			a=a+1
            
    elif (c==3):
        while(a<6) :
             if(sys_no == guess):
                print("YOUR GUESS IS CORRECT")
             elif(sys_no < guess):
                 print("YOUR GUESS IS LOWER THAN THE REAL NO")
             else:
                 print("YOUR GUESS IS HIGHER THAN THE REAL NO")

            a=a+1

    else:
        print("wrong choice")
    print ("enter yes or y to continue")
    d = input()
