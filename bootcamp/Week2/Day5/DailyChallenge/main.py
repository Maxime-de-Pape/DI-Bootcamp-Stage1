#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Use List Comprehension
#Example:

#Suppose the following input is supplied to the program: without,hello,bag,world
#Then, the output should be: bag,hello,without,world


word_sequence = input("Enter a comma-separated sequence of words: ")
words = word_sequence.split(",")
sorted_words = sorted([word for word in words])
result = ",".join(sorted_words)
print(result)
