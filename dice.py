import  random     #  select a random number
min = 1  
max = 6
roll="yes"
while(roll == "yes"or roll=="y"):
	print ("dice is rolling\n")
	print("the values is")
	print (random.randint(min,max))    #selecting a random no from max and min
	roll = input("Roll the dices again?")