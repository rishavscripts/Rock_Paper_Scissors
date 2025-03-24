import random
l=['🪨','📄','✂️']

while True:
    print(f"choose 0 for {l[0]} \t choose 1 for {l[1]} \t choose 2 for {l[2]}.")
    uc = int(input("Enter your choice: "))
    cc = random.randint(0, 2)
    print(f"You chose {l[uc]}.")
    print(f"Computer chose {l[cc]}.")

    if cc == uc:
        print("It's a draw.")
    elif cc > uc:
        print("You lose.")
    elif cc < uc:
        print("You win.")
    elif cc == 0 and uc == 2:
        print("You lose.")
    elif cc == 2 and uc == 0:
        print("You win.")