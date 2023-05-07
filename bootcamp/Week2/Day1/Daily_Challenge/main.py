user_string = input("enter a string of exactly 10 characters: ")

if len(user_string) < 10:
    print("String is not long enough.")
elif len(user_string) > 10:
    print("String is too long.")
else:
    print("The first character is:", user_string[0])
    print("The last character is:", user_string[-1])

    for i in range(len(user_string)):
        print(user_string[:i + 1])

        import random

        original_string = "Helloworld"

        char_list = list(original_string)

        random.shuffle(char_list)

        jumbled_string = "".join(char_list)

        print(jumbled_string)

