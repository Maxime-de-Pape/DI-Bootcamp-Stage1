# Instructions
# First Download this text file : right click –> Save As
#
# Create a new file called anagram_checker.py which contains a class called AnagramChecker.
#
# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.
#
# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)
#
# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.
#
# Note: None of the methods in the class should print anything.

class AnagramChecker:
    def __init__(self, word_list_file):
        self.word_list = self.load_word_list(word_list_file)

    def load_word_list(self, word_list_file):
        with open(word_list_file, 'r') as file:
            return [word.strip().lower() for word in file]

    def load_word_list(self, word_list_file):
        with open(word_list_file, 'r') as file:
            return [word.strip().lower() for word in file]

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def get_anagrams(self, word):
        anagrams = []
        for w in self.word_list:
            if self.is_anagram(word, w):
                anagrams.append(w)
        return anagrams

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
