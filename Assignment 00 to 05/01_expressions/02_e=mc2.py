
C :int = 299792458 # speed of light in m/s 

def main() :

    mass_in_kg = float(input("Enter Kilos of mass: "))

    Energy_in_Joules : float = mass_in_kg * (C ** 2)


    print("Energy in Joules: ", Energy_in_Joules)


if __name__ == "__main__":
    main() 