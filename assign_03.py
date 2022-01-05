#!/usr/bin/env python3
# Created by: Logan Sweeney
# Created on: Dec 8, 2021
# This program asks the user to input a character
# if it is a consonant, it will display.
# if it is a vowel, it will display.


def main():

    # taking user input
    character_input = input("Enter a character: ")

    def ask_again():
        user_answer = str(input("Would you like to put another character? "))

        if user_answer == "yes":
            print()
            main()
        elif user_answer == "no":
            print()
            print("Thanks for trying it out anyway!")
        else:
            print()
            print("Error. Try again?")
            print()
            ask_again()

    if(character_input == 'A' or character_input == 'a' or
       character_input == 'E' or character_input == 'e' or
       character_input == 'I' or character_input == 'i' or
       character_input == 'O' or character_input == 'o' or
       character_input == 'U' or character_input == 'u'):
        print()
        print(character_input, "is a Vowel")
        print()
        ask_again()
    elif (character_input == "Jazz" or character_input == "jazz"):
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠠⢄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠉⠢⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢄⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠠⡀⣀⣤⣦⣷⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⣰⣷⣿⣿⠟⣫⠕⠒⢚⠹⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢐⣿⠟⠓⠂⠀⠀⠠⢨⣤⠉⠂⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡤⢶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠸⡏⡄⢢⣖⠠⠀⠀⠈⠉⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⡾⠗⢻⡷⠈⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢏⠀⠈⠋⠀⠀⠄⢀⠀⠉⠀⠀⢱⠀⠀⠐⠖⣖⠒⠋⠉⠁⣀⣀⣤⣾⠿⠋⠁⠀⠀⢸⣧⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⢦⡀⠐⠒⠒⠈⠀⠀⢀⣠⢆⡞⠀⠀⠀⣼⣏⠃⠀⠀⠀⣿⣿⣿⣿⡆⠀⡀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀  ⠀⠀⠈⠳⢤⣶⡶⣿⣿⣿⢟⡥⡊⠀⠀⠀⣼⣟⠂⠀⠀⠀⣸⣿⣿⣿⣿⠀⠀⣿⣆⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠧⠀⠙⠻⣿⣈⠀⠀⢀⣾⢟⠎⠀⠀⠀⢠⣿⣿⣿⣿⡟⠀⢀⣿⣿⡆⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠁⠜⠻⣾⣴⣿⣯⡂⠀⢀⠀⢀⣾⣿⣿⣿⡿⠁⠀⣼⣿⣿⢡⣻⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠈⠀⠘⠈⠛⠷⣷⣿⣷⣶⣌⣾⣿⣿⣿⣿⠃⠀⣼⣿⣿⠃⢸⠃⠻⣿⣧⠀⠀⠀⠀⣀⡀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⡤⠁⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣾⣿⣿⣿⡿⠿⠿⣶⣿⣿⣯⣀⣟⣠⣴⣷⣾⣿⡿⠛⠛⠻⣟⣷⠒⠄")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⣰⣿⣿⡿⠃⣸⠟⠉⠁⠀⠀⠟⠛⠛⠚⠫⠀⠠⠙⠠⠇")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠤⠾⠿⠿⠋⠐⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("                      Ya like jazz?                        ")
    elif (character_input == 'Y' or character_input == 'y'):
        print()
        print(character_input, "is both a vowel and consonant")
        print()
        ask_again()
    elif (character_input == 'b' or character_input == 'c' or
          character_input == 'd' or character_input == 'f' or
          character_input == 'g' or character_input == 'h' or
          character_input == 'j' or character_input == 'k' or
          character_input == 'l' or character_input == 'm' or
          character_input == 'n' or character_input == 'p' or
          character_input == 'q' or character_input == 'r' or
          character_input == 's' or character_input == 't' or
          character_input == 'v' or character_input == 'w' or
          character_input == 'x' or character_input == 'z' or
          character_input == 'B' or character_input == 'C' or
          character_input == 'D' or character_input == 'F' or
          character_input == 'G' or character_input == 'H' or
          character_input == 'I' or character_input == 'J' or
          character_input == 'K' or character_input == 'M' or
          character_input == 'N' or character_input == 'P' or
          character_input == 'Q' or character_input == 'R' or
          character_input == 'S' or character_input == 'T' or
          character_input == 'V' or character_input == 'W' or
          character_input == 'X' or character_input == 'Z'):
        print()
        print(character_input, "is a Consonant.")
        print()
        ask_again()
    else:
        print()
        print("Error, Please try again.")
        print()
        main()


if __name__ == "__main__":
    main()
