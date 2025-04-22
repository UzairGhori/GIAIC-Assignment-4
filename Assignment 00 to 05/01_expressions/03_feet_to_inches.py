
Inches_per_foot = 12 

def main():

    feet : float = float(input("Enter the number of Feet: "))
    
    Inches : float = feet * Inches_per_foot 

    print("That is", Inches, "Inches")


if __name__ == "__main__":
    main()