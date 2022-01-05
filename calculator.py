def calc():
	op = ""

	while True:
		num1 = float(input("numb1:"))
		op = input("operator:")
		num2 = float(input("numb2:"))
		if op == "+":
			add = num1 + num2
			print(add)
		elif op == "-":
			sub = num1 - num2
			print(sub)
		elif op == "*":
			mult = num1 * num2
			print(mult)
		elif op == "/":
			divd = num1 / num2
			print(divd)
		elif op == "exit" or op == "quit":
			break
		else:
			print("error")
