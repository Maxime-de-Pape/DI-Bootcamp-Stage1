# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.
#
#
#
# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
#
# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
#
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
#
#
# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
#
# Implement a classmethod that returns a Text instance but with a text file:
#
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
#
#
# Now, use the provided the_stranger.txt file and try using the class you created above.


class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return f"The word '{word}' does not appear in the text."
        return f"The word '{word}' appears {count} time(s) in the text."

    def most_common_word(self):
        words = self.text.split()
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        if not word_counts:
            return "The text is empty."
        most_common = max(word_counts, key=word_counts.get)
        return f"The most common word in the text is '{most_common}'."

    def unique_words(self):
        words = self.text.split()
        unique = list(set(words))
        return unique

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            text = file.read()
        return cls(text)


text = Text.from_file('the_stranger.txt')

frequency = text.word_frequency('the')
print(frequency)

most_common = text.most_common_word()
print(most_common)

unique_words = text.unique_words()
print(unique_words)
