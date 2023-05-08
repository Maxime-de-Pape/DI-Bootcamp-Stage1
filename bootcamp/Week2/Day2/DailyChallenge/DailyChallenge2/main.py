def challenge2():
    word = input("please choose a word: ")
    previous = ""
    final = ""
    for i in word:
        if i != previous:
            final += i
        previous = i
    print(final)