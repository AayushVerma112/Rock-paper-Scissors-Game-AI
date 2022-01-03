import random  

print("You ready?!!!\n Rock.....\nPaper.....\nScissors.....")

Roc = "Rock"
Pap = "Paper"
Sci = "Scissors"



p1 = input("What do choose to do? Choose Wisely my friend! \n")
rand_num = random.randint(0,2)
if rand_num == 0:
	computer = Roc
elif rand_num == 1:
	computer = Pap
else:
	computer = Sci
print(f"Computer plays {computer}")	

#The shortest method really felt right
if (p1 == Roc and computer == Sci) or (p1 == Sci and computer == Pap) or (p1 == Roc and computer == Pap): 
	# USING THE OR OPERATOR I CLUBBED ALL THE CONDITIONS TOGETHER !!! SO IF ANY ONE OF THEM WOULD BE TRUE , PLAYER1 WILL WIN
	print("You have won the game ! Congratulations")
elif (p1 == Sci and computer == Roc) or ( p1 == Pap and computer == Sci) or (p1 == Pap	and computer == Roc):
	# USING THE OR OPERATOR AS I DID FOR PLAYER1 . NOW THE SAME CAN BE DONE FOR PLAYER2
	print("Computer has won !")
elif (p1 == Pap and computer == Pap) or (p1 == Roc and computer == Roc) or (p1 == Sci and computer == Sci):
	print("It is draw !")
else:
	print("Why are you wasting my time ? Man I am a computer but I have some feelings !!!")