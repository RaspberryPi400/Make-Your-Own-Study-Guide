from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

import flask
from flask import Flask
score = 0
import random
import sys

app = Flask(__name__)
@app.route("https://raspberrypi400.github.io/Study-guide-creator/")
def create_app():
    return app

number_of_questions = int(input("How many questions would you like to have? "))

if number_of_questions == 0:
    print("Error. You cannot have 0 questions. Please input a value above 0.")
    # Exits the program
    sys.exit(0)

# Create a list to store questions/answers
question_answer_pairs = []

# Create a loop that asks what the questions/answers should be. The amount of times that it loops depends on how many questions the user said there should be.
for index in range(number_of_questions):
    # Asks for what the question should be and adds one every time so it shows what the question number is.
    question = input(f"What should question {index + 1} be? ")
    # Asks for what the answer should be for the same numbered question.
    answer = input(f"What should the answer be to question {index + 1}? ")

    # Adds the question/answer pair to the list
    question_answer_pairs.append((question, answer))

print("Time to answer!")
# Shuffles the list
random.shuffle(question_answer_pairs)

# Prints each question in the pair, asks for input, adds one to score if correct and displays correct answer if wrong
for question, answer in question_answer_pairs:
    print(question)
    user_answer = input("Your answer: ")
    if user_answer == answer:
        print("You got it correct!")
        score = score + 1
    else:
        print("You got it wrong!")
        print(f"The correct answer is: ", answer)

if score == 1:
    print(f"You have answered", score, "question correctly.")

else:
    print(f"You have answered", score, "questions correctly.")

print("Copyright (c) 2025 Elijah Corwin")
