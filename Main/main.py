# This is the main scope about this project
import os
import New_Game, Check_Answer, Play_Again, Display_Score

# This function just clear the console interpreter to a fancy view.
def clear_console():
     os.system('clear')

clear_console()
print("Hello gamer, here a simple Quiz game thought to entretainement you.\n\nEnjoy it!!!\n")

question = {
     "Who is the first American's President?" : "B",
     "When was the second world war?" : "A",
     "In which country was intented the pizza?" : "C"    
}

question_1 = {
     "A" : "Joe Biden",
     "B" : "George Whashington",
     "C" : "Barack Obama",
     "D" : "John Kennedy"
}
question_2 = {
     "A" : "1940",
     "B" : "2001",
     "C" : "1390",
     "D" : "1930"
}
question_3 = {
     "A" : "France",
     "B" : "United Kingdom",
     "C" : "Italy",
     "D" : "America"
}

number_correct_answer = 0

New_Game.new_game(question, number_correct_answer, question_1,question_2, question_3)