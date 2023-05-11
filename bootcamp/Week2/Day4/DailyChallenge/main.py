#Instructions
#Given a “Matrix” string:
#
#   7i3
#   Tsi
#   h%x
#   i #
#   sM
#   $a
#   #t%
#   ^r!
#
#
#The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
#A grid means that you could potentially break it into rows and columns, like here:
#
#7	i	3
#T	s	i
#h	%	x
#i		#
#s	M
#$	a
#	t	%
#^	r	!


#To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

#Using his technique, try to decode this matrix.

#Hints:
#Use
#● lists for storing data
#● Loops for going through the data
#● if/else statements to check the data
#● String for the output of the secret message

#Hint (if needed) : Look at the remote learning “Matrix” videos

matrix = [
    "7i3",
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

transposed_matrix = []
for i in range(len(matrix[0])):
    column = ''
    for j in range(len(matrix)):
        column += matrix[j][i]
    transposed_matrix.append(column)

secret_message = ''
for column in transposed_matrix:
    for char in column:
        if char.isalpha():
            secret_message += char

decoded_message = secret_message[0]
for i in range(1, len(secret_message)):
    if secret_message[i].isalpha() and secret_message[i-1].isalpha():
        decoded_message += secret_message[i]
    else:
        decoded_message += ' '

print(decoded_message)
