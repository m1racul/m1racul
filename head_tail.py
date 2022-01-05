import random

def ht():
	numb = ["0","1"]

	rand_num = random.choice(numb)

	if rand_num == "0":
		print("heads")
	else:
		print("tails")
