
def main():

    div : int = int(input("Enter a number to be divided: "))

    div2 : int = int(input("Enter a number to  be divide by: "))

    quotient : int = div // div2 

    remainder : int = div % div2 

    print("The result of the division is " + str(quotient) + " with a remainder of " + str(remainder)) 


if __name__ == "__main__":
    main()
