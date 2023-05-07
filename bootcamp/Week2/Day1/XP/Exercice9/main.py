height_in_inches = float(input("What is your height in inches? "))

height_in_cm = height_in_inches * 2.54

if height_in_cm > 145:
    print("Woah, you are big")
else:
    print("Nope, eat more soup")
