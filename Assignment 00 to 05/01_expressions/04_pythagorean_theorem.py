import math

def main():
    AB = float(input("Enter the length of side AB: "))
    AC = float(input("Enter the length of side BC: "))

    BC = math.sqrt(AB**2 + AC**2) 

    print(f"The length of the hypotenouse is {BC}")


if __name__ == "__main__":
    main()
