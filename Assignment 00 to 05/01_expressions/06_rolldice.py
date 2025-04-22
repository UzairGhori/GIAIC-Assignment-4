import random 


NUM_SIDES: int = 6 

def main():

    die1 = random.randint(1 , NUM_SIDES)
    die2 = random.randint(1 , NUM_SIDES)

    total : int = die1 + die2

    print("Dice have" , NUM_SIDES , "sides each.")

    print("Die 1: ", die1)
    print("Die 2: ", die2)
    print("Total: ", total)


if __name__ == "__main__":
    main()  

