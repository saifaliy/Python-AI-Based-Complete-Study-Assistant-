import sys
import os
sys.path.append(os.path.abspath('.')) 

from src.quiz.tf_classifier import classify_question

sample = "What is an API?"
print(f"'{sample}' → Difficulty: {classify_question(sample)}")
