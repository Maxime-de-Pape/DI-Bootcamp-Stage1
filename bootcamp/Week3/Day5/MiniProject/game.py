# What You Will Create
# Mini-Project: Rock, Paper, Scissors
# Rock-paper-scissors is an old game that can be played between two people. You can read about it in wikipedia
#
# We will create a game for the user to play Rock-paper-scissors against the computer.
#
# The user will input his/her move (rock/paper/scissors),
# and the computer will select either rock, paper or scissors at random.
# We will then compare the user’s move with the computer’s move, and determine the results of the game:
#
# The user won
#
# The computer won (the user lost)
# A draw (tie)
# We will print the outcome of each game: the user’s choice, the computer’s choice, and the result.
#
# The user will be able to play again and again. Once the user decides to exit the program, we will print a summary of the outcomes of all the games: how many times they won, lost or and tied the computer.
# Instructions
# Create a new directory for the game. Inside it, create 2 files:
# rock-paper-scissors.py – this will contain functions to show the main menu, handle user’s input, and show the game summary before exiting.
# game.py – this will contain a Game class which will have functions to play a single game of rock-paper-scissors against the computer, determine the game’s result, and return the result.
#
#
# Steps
# Part I - Game.Py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.
#
# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).
#
# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
#
# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it
#
# Get a random item for the computer (rock/paper/scissors) and remember it
#
# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”
#
# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
import random


class Game:
    def get_user_item(self):
        while True:
            user_choice = input("Select an item (rock/paper/scissors): ")
            if user_choice.lower() in ["rock", "paper", "scissors"]:
                return user_choice
            else:
                print("Invalid input. Please try again.")

    def get_computer_item(self):
        items = ["rock", "paper", "scissors"]
        return random.choice(items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (
                (user_item == "rock" and computer_item == "scissors")
                or (user_item == "paper" and computer_item == "rock")
                or (user_item == "scissors" and computer_item == "paper")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}.")

        if result == "win":
            print("You win!")
        elif result == "draw":
            print("It's a draw!")
        else:
            print("You lose!")

        return result


def get_user_menu_choice():
    while True:
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid input. Please try again.")


def print_results(results):
    print("Game results:")
    print(f"Win: {results['win']}")
    print(f"Loss: {results['loss']}")
    print(f"Draw: {results['draw']}")
    print("Thank you for playing!")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "2":
            print_results(result)
        elif choice == "3":
            print_results(results)
            break


if __name__ == "__main__":
    main()
