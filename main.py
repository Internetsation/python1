# This program has three functions
# 1. Prompt user for name and print to screen
# 2. Prompt user for a number to be squared and printed to screen.
# 3. Prompts user for a word and prints the number of characters in that word to the screen.

def main():
    char_counter = 0
    user_name = input("Please enter your name:  ")
    user_number = float(input("Please enter a number to be squared:  "))
    user_word = input("Please enter a word that you would like to know how many characters it contains:  ")
    char_counter += len(user_word)

    user_number = (user_number * user_number)

    print("Your name is: ", user_name)
    print("This number squared is a: ", user_number)
    print("The word you entered has ", char_counter, " characters")


main()
