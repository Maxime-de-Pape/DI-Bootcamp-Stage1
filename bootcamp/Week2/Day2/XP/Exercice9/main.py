# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Ask a family the age of each person who wants a ticket.
#
# Store the total cost of all the family’s tickets and print it out.

num_people = int(input("How many people need tickets? "))
total_cost = 0

for i in range(num_people):
    age = int(input("Enter age of person #" + str(i+1) + ": "))
    if age < 3:
        ticket_cost = 0
    elif age <= 12:
        ticket_cost = 10
    else:
        ticket_cost = 15

    total_cost += ticket_cost

print("The total cost of all tickets is $" + str(total_cost))


# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

teenagers = ['Lise', 'Juliana', 'Charlie', 'David', 'Emma', 'Frank']
allowed_ages = range(16, 21)
i = 0
while i < len(teenagers):
    name = teenagers[i]
    age = int(input("Enter age of " + name + ": "))
    if age not in allowed_ages:
        print(name + " is not allowed to watch the movie.")
        teenagers.remove(name)
    else:
        i += 1

print("Final list of teenagers allowed to watch the movie:")
print(teenagers)
