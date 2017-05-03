import random
import time

def magic():
    raw_input = input("What's up?\n")
    print("Let me think...")
    time.sleep(3)
    number = random.randint(0, 5)
    answers = ["Yes!", "No...", "Probably.", "Maybe...", "Hell, no.", "Seriously?"]
    print(answers[number])
    magic()

magic()