# simple quiz game and I got the Question and Answers from GOOGLE (thanks google)
import time

# function for my print to pause for 2 secs
def print_pause(message):
    print(message)
    time.sleep(2)

# asking the player's name
player_name = str(input("Input your Fullname: ")).upper()

# welcome and instructions.
print("Welcome to my Quiz game!", player_name, ".")
print("     ")
print_pause("Read the Question and Choices thoroughly before you answer.")
print_pause("This quiz have 5 questions only.")
print_pause("Your Answers should be '1', '2' and '3' only.")

print("======================================================================================")
print("     ")
print("     ")

#list of questions, choices and the correct answer.
questions = [
# Question 1 
    {
        "question": "What is software engineering?",
        "options": ["Write code for games for a variety of formats, such as PCs, consoles, web browsers and mobile phones.",
                    "The process of designing, building, and maintaining software systems in a structured and efficient manner.",
                    "Collecting data from various data sources and creating Data Pipelines." ],
# Ans 1 - no.2
        "answer": "The process of designing, building, and maintaining software systems in a structured and efficient manner."
    },
    
# Question 2
    {
        "question": "What is the difference between a local variable and a global variable?", 
        "options": ["A local variable is only accessible within the same class or object where it is declared, while a global variable is accessible anywhere in the program.",
                    "A local variable is only accessible within the same module or package where it is declared, while a global variable is accessible anywhere in the program.",
                    "A local variable is only accessible within the same function or block where it is declared, while a global variable is accessible anywhere in the program."],
# Ans 2 - no.3
        "answer": "A local variable is only accessible within the same function or block where it is declared, while a global variable is accessible anywhere in the program."
    },
    
# Question 3
    {
        "question": "What is the difference between a class and an object?", 
        "options": ["A class is a blueprint for an object, while an object is an instance of a class.",
                    "A class is a blueprint for an object, while an object is a blueprint for a class.",
                    "A class is an instance of an object, while an object is a blueprint for a class."],
# Ans 3 - no.1
        "answer": "A class is a blueprint for an object, while an object is an instance of a class."
    },
    
# Question 4
    {
        "question": "What is the difference between a software developer and a software engineer?",
        "options": [ "A software developer primarily focuses on writing code, while a software engineer is responsible for the complete software development life cycle, including design, coding, testing, and maintenance.",
                    "A software developer primarily focuses on writing code, while a software engineer is responsible for the design Only.",
                    "A software developer primarily focuses on design, while a software engineer is responsible for coding." ],
# Ans 4 - no.1
        "answer": "A software developer primarily focuses on writing code, while a software engineer is responsible for the complete software development life cycle, including design, coding, testing, and maintenance."
    },

# Question 5
    {
        "question": "What is Object-Oriented Programming (OOP)?",
        "options": [ "Out Of Place",
                    "To show recognition of a mistake or minor accident, often as part of an apology.",
                    "OOP is a programming paradigm that uses objects and classes to model real-world concepts and encapsulate data and behavior." ],
# Ans 5 - no.3
        "answer": "OOP is a programming paradigm that uses objects and classes to model real-world concepts and encapsulate data and behavior."
    }]

# function to start the quizzz
def start_quiz():
    score = 0

    for question in questions:
        print(question["question"])
        print("\nChoices:")

        # this make the options only 1, 2 and 3
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")

        user_answer = input("\nEnter your answer [1, 2, or 3]: ")

        # if the user's answer is correct
        if question["options"][int(user_answer)-1] == question["answer"]:
            print("\nCorrect! Great job.")
            print_pause("\n...")
            score += 1

        # if the user's answer is wrong
        else:
            print("\nWrong! Study again.")
            print_pause("\n...")

    print(f"\nQuiz finished. \nYour score is {score}/{len(questions)}.")
    print_pause("\nThankyou for playing! <3 \n")

start_quiz()
