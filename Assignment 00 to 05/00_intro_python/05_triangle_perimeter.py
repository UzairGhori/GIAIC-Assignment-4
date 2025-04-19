def main():

    side1 = float(input("\033[1;3m Enter the length of side 1:\033[0m "))
    side2 = float(input("\033[1;3m Enter the length of side 2:\033[0m "))
    side3 = float(input ("\033[1;3m Enter the length of side 3:\033[0m "))

    Perimeter = side1 + side2 + side3

    print(f"The perimeter of the triangle is {Perimeter} ")

if __name__ == "__main__":
    main()
