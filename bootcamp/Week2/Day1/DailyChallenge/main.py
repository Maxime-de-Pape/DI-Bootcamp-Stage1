Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.

Then, print the first and last characters of the given text.

Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
The user enters "Hello World"
Then, you have to construct the string character by character
H
He
Hel
... etc
Hello World

text = input("Please enter a string that is 10 characters long: ")

if len(text) < 10:
    print("String not long enough")
elif len(text) > 10:
    print("String too long")
else:
    # print first and last characters
    print("First character:", text[0])
    print("Last character:", text[-1])

    # print the string character by character
    for i in range(1, len(text) + 1):
        print(text[:i])
