import random
number = random.randint(0, 200)

while True:
    x = int(input("Enter a number: "))
    if x < number:
        print("Increase your number")
    elif x > number:
        print("Decrease your number")
    else:
        print("You guessed correctly")
        break

        
