import random

print("🎯Hi, Please guess a number between 1 to 100")
print("🎲 You have just 5 chances.")

num=random.randint(1,100)
atmp=1
while True:
    if atmp>5:
        print("❌so sorry you are unsuccessful.")
        print("🔴the number was:" + str(num))
        break
    guess=input("⏳please guess a number : ")
    atmp+=1

    if not guess.isdigit():
        print("⚠️please enter a valid number!")
        continue

    guss=int(guess)
    if guss>num:
        print("👇🏽it's too high ,guess on more time:")
    elif guss<num:
        print("👆🏽it's too low ,guess on more time:")
    else:
        print("🏆you win this game. congratulations!!")
        break