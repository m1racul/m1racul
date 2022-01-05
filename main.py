from head_tail import *
from guess_num import *
from calculator import *

name = input("Name:")
passwd = input("Password:")

if name=="miraz" and passwd=="1234":
	print("welcome")
	com = ""
	while True:
		com = input("command:")
		if com == "calculator":
			calc()
		elif com == "toss":
			ht()
		elif com == "guess":
			guess_numb()
		elif com == "exit" or com == "quit":
			break

else:
	print("wrng username or pass")
