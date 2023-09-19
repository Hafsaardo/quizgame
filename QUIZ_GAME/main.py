questions = (
    "What is the most valuable company in the world?",
    "What is the name of the president of Nigeria?",
    "What is the name of the tallest mountain on earth?",
    "Who is the greatest football player ever?",
    "How many countries are in South America?",
)
options = (
    ("A. Apple", "B. Saudi Aramco", "C. Walmart", "D. Amazon"),
    ("A. Muhammadu Buhari", "B. Bola Ahmed Tinubu", "C. Nasir El-rufa'i", "D. Hafsat Ardo"),
    ("A. Dhaulagiri", "B. lhotse", "C. Everest", "D. Makalu"),
    ("A. Pele", "B. Diego Maradona", "C. Lionel Messi", "D. Cristiano Ronaldo"),
    ("A. 12", "B. 13", "C. 14", "D. 15"),
)
answers = ("A", "B", "C", "D", "A")

guesses = []
score = 0

for question_num in range(len(questions)):
    print(".......................")
    print(questions[question_num])

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

# Calculate the final score
score = int((score / len(questions)) * 100)

# Print the results after all questions
print("......................")
print("     RESULTS          ")
print("......................")

print("Answers:", answers)
print("Guesses:", guesses)
print(f"Your score is: {score}%")