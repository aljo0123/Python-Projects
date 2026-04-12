while True:
    questions = {
        "If x = 2, what is 2x + 3?": "7",
        "What is the next number: 2, 4, 8, 16, ?": "32",
        "What is 15 * 3?": "45",
        "What is 2^5?": "32",
        "What is square root of 81?": "9",
        "Which language is used for AI? (python/java/c)": "python",
        "What does CPU stand for?": "central processing unit",
        "Binary of 5 is (101 or 111)?": "101",
    }

    score = 0

    name = input("\nEnter your name: ")
    print("\nWelcome to Quiz,", name, "!\n")

    for question, answer in questions.items():
        user_answer = input(question + " ")

        if user_answer.lower() == answer:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer is:", answer, "\n")

    print(name, "your final score is:", score, "/", len(questions))
    if user_answer.lower().strip() == answer:

   
     if score == len(questions):
        print("Excellent!")
    elif score >= 2:
        print("Good job!")
    else:
        print("Keep practicing!")
    

   
    cont = input("\nDo you want to play again? (yes/no): ")
    if cont.lower() != "yes":
        print("Thanks for playing!")
        break
