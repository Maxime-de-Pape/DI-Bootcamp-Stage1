def challenge1():
    choices = input("please enter a number and length, separate by space: ").split(' ')
    number = int(choices [0])
    length = int(choices [1])
    numlist = [(i + 1) * number for i in range(length)]
    print(numlist)