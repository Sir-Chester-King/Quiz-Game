# This is the scope for the new game.
import os

# This function just clear the console interpreter to a fancy view.
def clear_console():
     os.system('clear')

def new_game(questions, number_correct_answer, *correct_answer):
     for index in correct_answer:
          print("List of correct anwer is: ", index, end="\n")
          #print("Correct answer number {}: ".format(index))

