# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.
#
# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.
#
#

def print_builtin_functions():
     The program prints: abs(), int(), and input(). It then prints the results of each function
    # get abs() function of -10
    number = -10
    absolute_value = abs(number)
    print("The absolte value of -10 is :" abs_value)

 # Convert the string "123" to an integer.
  integer = int("123")
  print("The ineteger value of '123' is:", integer)

    # get input() function
    user_input = input("Enter your number: ")
    print("You entered:", user_input)


if __name__ == "__main__":
  print_results()




# 🌟 Exercise 2: Currencies
# Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
#
    Your code starts HERE
#
#
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)
#
# >>> str(c1)
# '5 dollars'
#
# >>> int(c1)
# 5
#
# >>> repr(c1)
# '5 dollars'
#
# >>> c1 + 5
# 10
#
# >>> c1 + c2
# 15
#
# >>> c1
# 5 dollars
#
# >>> c1 += 5
# >>> c1
# 10 dollars
#
# >>> c1 += c2
# >>> c1
# 20 dollars
#
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
#

class Currency:
  """This class represents a currency.

  Attributes:
    currency: The currency symbol.
    amount: The amount of currency.
  """

  __counter = 0

  @classmethod
  def add(cls, currency, amount):
    """Creates a new currency instance with the given currency and amount.

    Args:
      currency: The currency symbol.
      amount: The amount of currency.

    Returns:
      A new currency instance.
    """
    cls.__counter += 1
    return cls(currency, amount)

  def __init__(self, currency, amount):
    self.currency = currency
    self.amount = amount

  def __str__(self):
    """Returns a string representation of the currency.

    Returns:
      A string representation of the currency.
    """
    return f"{self.amount} {self.currency}"

  def __int__(self):
    """Returns the amount of currency as an integer.

    Returns:
      The amount of currency as an integer.
    """
    return self.amount

  def __repr__(self):
    """Returns a string representation of the currency that can be used to recreate the object.

    Returns:
      A string representation of the currency that can be used to recreate the object.
    """
    return f"Currency({self.currency}, {self.amount})"

  def __add__(self, other):
    """Adds two currencies together.

    Args:
      other: The other currency to add.

    Returns:
      The sum of the two currencies.

    Raises:
      TypeError: If the two currencies are not of the same type.
    """
    if self.currency != other.currency:
      raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
    return Currency(self.currency, self.amount + other.amount)

  def __iadd__(self, other):
    """Adds another currency to the current currency.

    Args:
      other: The other currency to add.

    Returns:
      The current currency, with the other currency added.
    """
    self.amount += other.amount
    return self


c1 = Currency.add('dollar', 5)
c2 = Currency.add('dollar', 10)
c3 = Currency.add('shekel', 1)
c4 = Currency.add('shekel', 10)

print(str(c1))
# 5 dollars

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1)
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>