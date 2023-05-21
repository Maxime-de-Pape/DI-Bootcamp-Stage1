
# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.
#
# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
#
# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.
#
# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:
#
#
# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.
#

from bootcamp.Week3.Day5.MiniProject2.main.anagram_checker import AnagramChecker

def show_menu():
    print("ANAGRAM CHECKER")
    print("1. Input a word")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

def get_valid_word():
    while True:
        word = input("Enter a word: ").strip()
        if ' ' in word:
            print("Error: Only a single word is allowed.")
        elif not word.isalpha():
            print("Error: Only alphabetic characters are allowed.")
        else:
            return word

def display_word_info(word, valid, anagrams):
    print(f"YOUR WORD: {word}")
    if valid:
        print("This is a valid English word.")
        print("Anagrams for your word: " + ", ".join(anagrams))
    else:
        print("This is not a valid English word.")

def main():
    word_list_file = "sowpods.txt"
    anagram_checker = AnagramChecker(word_list_file)

    while True:
        choice = show_menu()
        if choice == '1':
            word = get_valid_word()
            valid = anagram_checker.is_valid_word(word)
            anagrams = anagram_checker.get_anagrams(word)
            display_word_info(word, valid, anagrams)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
