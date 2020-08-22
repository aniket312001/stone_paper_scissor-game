import random
game=["stone","paper","scissor"]

c = 0
y = 0
while(1):
    computer = random.choice(game)
    you = input("\nEnter \n'st' for stone\n'p' for paper \n'sc' for scissor\n'e' for exit \nEnter your choice:")

    if you =="st":               #stone
        if computer =="stone":
            print("same")
        elif computer =="paper":
            print("You lose   , computer->",computer)
            c +=1
        else:
            print("You win   ,  computer->",computer)
            y +=1

    elif you =="p":
        if computer == "stone":
            print("You win   , computer->",computer)
            y += 1
        elif computer == "paper":
            print("same")
        else:
            print("You lose  , computer->",computer)
            c += 1

    elif you =="sc":
        if computer == "stone":
            print("You lose   , computer->",computer)
            c += 1
        elif computer == "paper":
            print("You win   , computer->",computer)
            y += 1
        else:
            print("same")
    elif you=="e":
        break

print("-----------------------------------------")
print("Result: \n\tyou win :",y,"\n\tComputer win :",c)
if y>c:
    print("\nHence You win")
elif y<c:
    print("\nHence Computer win")
else:
    print("\nHence Score Equal")
n = input()
