import random
num=random.randint(1,10)
guess=int(input("guess number between 1 to 10:"))

while guess !=num:
    if guess<num:
        print("it too low")
    elif guess>num:
        print("its too high")
    guess=int(input("guess again:" ))
print("you guess it right.")
    
