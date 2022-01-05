import random

rps = ["paper","rock","scissor"]


rps1 = ""

point = 0


while True:
    rps1 = input("rock,paper,scissor:")

    

    rand_rps = random.choice(rps)

    print(rand_rps)

    if rps1==rand_rps:
        print("draw")
        print(point)

    elif rps1=="rock" and rand_rps=="scissor":
        print("win")
        point = point + 1
        print(point)

    elif rps1=="rock" and rand_rps=="paper":
        print("lost")
        point = point - 1
        print(point)

    elif rps1=="paper" and rand_rps=="scissor":
        print("lost")
        point = point - 1
        print(point)

    elif rps1=="paper" and rand_rps=="rock":
        print("win")
        point = point + 1
        print(point)

    elif rps1=="scissor" and rand_rps=="paper":
        print("win")
        point = point + 1
        print(point)

    elif rps1=="scissor" and rand_rps=="rock":
        print("lost")
        point = point - 1
        print(point)

    elif rps1=="exit" or rps1=="quit":
        break

    else:
        print("BLA")
