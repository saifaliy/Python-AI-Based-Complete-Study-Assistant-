import sys
import os
sys.path.append(os.path.abspath('.')) 

from src.summarize.question_generator import generate_quiz_questions
from src.quiz.tf_classifier import classify_batch

text = """
Recursion is a method of solving problems where the solution depends on smaller instances of the same problem.
A function that calls itself is known as a recursive function. The base case stops the recursion.
"""

questions = generate_quiz_questions(text)
difficulties = classify_batch(questions)

for q, d in zip(questions, difficulties):
    print(f"{q} → {d}")
