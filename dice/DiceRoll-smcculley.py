import random

user_input = input('Please enter "Y" to roll the dice.')
while(user_input.upper() == "Y"):
    die1 = random.randrange(6) +1
    die2 = random.randrange(6) +1
    total = die1 + die2

    print("The value of die 1 is ", die1, ".")
    print("The value of die 2 is ", die2, ".")
    print("The total of both dice is ", total, ".")

    if(total == 2):
        print("Snake Eyes")
    elif(total == 3):
        print("Ace Caught a Deuce")
    elif(die1 == 2 and die2 == 2):
        print("Little Joe from Kokomo")
    elif(total == 5):
        print("Little Phoebe")
    elif(die1 == 3 and die2 == 3):
        print("Jimmy Hicks from the Sticks")
    elif((die1 == 6 or die2 == 6) and total == 7):
        print("Six Ace")
    elif(die1 == 4 and die2 == 4):
        print("Eighter from Decatur")
    elif(total == 9):
        print("Nina from Pasadena")
    elif(die1 == 5 and die2 == 5):
        print("Puppy Paws")
    elif((die1 == 6 or die2 == 6) and total == 11):
        print("Six Five no Jive")
    elif(total == 12):
        print("Boxcars")
    user_input = input('\nPlease enter "Y" to roll the dice.')


