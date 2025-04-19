def main():


    fahrenheit = float(input("\033[1;3m Enter temparature in fehrenheit: \033[0m"))

    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"temparature : {fahrenheit}f = {celsius}c ")


if __name__ == "__main__":
    main()