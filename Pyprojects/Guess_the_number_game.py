import random
number = random.randint(1,10)   #random module is able to generate random numbers in given range
for i in range(0,3):
    user = int(input("Guess the number:"))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        break
if user != number:
    print(f"Your guess is incorrect the number is {number}")