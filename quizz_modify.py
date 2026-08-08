questions = ()
while True:

    ques = str(input(print("Enter your question (q to exit): ")))
    if ques == "q":
        break
    else:
        questions.append(ques)

options = (("A.Sujal ", "B.Rohan", "C.Dhwaj", "D.Sumit"), 
           ("A.2024", "B.2025", "C.2023", "D.2026"),
           ("A.HSNC", "B.MIT", "C.IIT", "D.None"),
           ("A.Btech", "B.IT", "C.BSC", "D.Law"),
           ("A.JJ", "B.HSNC", "C.Wilson", "D.KC"),
           ("A.Mahalaxmi", "B.Lower parel", "C.Charniroad", "D.Borivali"))

answers = ("A",
           "D",
           "A",
           "A",
           "B",
           "A")
guesses = []
score = 0
question_number = 0

for question in questions:
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_number]} is the correct answer")
    question_number +=1       

print(*answers)
print("--------------")
print(*guesses)
print(f"This is your score: {score}")
if (score>3):
    print("Congrats you Pass!")
else:
    print("Fail, Better luck next time:(")    