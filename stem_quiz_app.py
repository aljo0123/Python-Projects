```python
import random

question_bank = [
    # Mathematics
    {
        "question": "If x = 2, what is 2x + 3?",
        "options": ["5", "7", "8", "10"],
        "answer": "7",
        "category": "Mathematics",
        "difficulty": "Easy"
    },
    {
        "question": "What is the next number: 2, 4, 8, 16, ?",
        "options": ["20", "24", "30", "32"],
        "answer": "32",
        "category": "Mathematics",
        "difficulty": "Easy"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "12", "14", "16"],
        "answer": "12",
        "category": "Mathematics",
        "difficulty": "Easy"
    },
    {
        "question": "What is 15% of 200?",
        "options": ["15", "20", "30", "35"],
        "answer": "30",
        "category": "Mathematics",
        "difficulty": "Medium"
    },

    # Physics
    {
        "question": "What is the SI unit of force?",
        "options": ["Joule", "Newton", "Watt", "Pascal"],
        "answer": "Newton",
        "category": "Physics",
        "difficulty": "Easy"
    },
    {
        "question": "What is the approximate speed of light in vacuum?",
        "options": ["3 × 10^6 m/s", "3 × 10^8 m/s",
                    "3 × 10^10 m/s", "3 × 10^12 m/s"],
        "answer": "3 × 10^8 m/s",
        "category": "Physics",
        "difficulty": "Medium"
    },
    {
        "question": "Which law explains the relationship between force, mass and acceleration?",
        "options": ["Newton's First Law", "Newton's Second Law",
                    "Newton's Third Law", "Law of Conservation"],
        "answer": "Newton's Second Law",
        "category": "Physics",
        "difficulty": "Medium"
    },

    # Chemistry
    {
        "question": "What is the chemical symbol for oxygen?",
        "options": ["O", "Ox", "C", "N"],
        "answer": "O",
        "category": "Chemistry",
        "difficulty": "Easy"
    },
    {
        "question": "What is the pH of pure water at room temperature?",
        "options": ["3", "5", "7", "9"],
        "answer": "7",
        "category": "Chemistry",
        "difficulty": "Easy"
    },
    {
        "question": "Which particle has a negative charge?",
        "options": ["Proton", "Neutron", "Electron", "Nucleus"],
        "answer": "Electron",
        "category": "Chemistry",
        "difficulty": "Easy"
    },

    # Computer Science
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Processing Utility",
            "Central Program Unit",
            "Computer Power Unit"
        ],
        "answer": "Central Processing Unit",
        "category": "Computer Science",
        "difficulty": "Easy"
    },
    {
        "question": "What is the binary representation of decimal 5?",
        "options": ["100", "101", "110", "111"],
        "answer": "101",
        "category": "Computer Science",
        "difficulty": "Easy"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue",
        "category": "Computer Science",
        "difficulty": "Medium"
    },
    {
        "question": "Which language is commonly used for AI and machine learning?",
        "options": ["HTML", "Python", "CSS", "SQL"],
        "answer": "Python",
        "category": "Computer Science",
        "difficulty": "Easy"
    }
]


def show_categories():
    print("\nChoose a category:")
    print("1. Mathematics")
    print("2. Physics")
    print("3. Chemistry")
    print("4. Computer Science")
    print("5. Mixed STEM")


def choose_category():
    categories = {
        "1": "Mathematics",
        "2": "Physics",
        "3": "Chemistry",
        "4": "Computer Science",
        "5": "Mixed STEM"
    }

    while True:
        show_categories()
        choice = input("Enter your choice: ").strip()

        if choice in categories:
            return categories[choice]

        print("Invalid choice. Please try again.")


def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Mixed")

    difficulties = {
        "1": "Easy",
        "2": "Medium",
        "3": "Mixed"
    }

    while True:
        choice = input("Enter your choice: ").strip()

        if choice in difficulties:
            return difficulties[choice]

        print("Invalid choice. Please try again.")


def get_questions(category, difficulty):
    selected = []

    for question in question_bank:

        category_match = (
            category == "Mixed STEM"
            or question["category"] == category
        )

        difficulty_match = (
            difficulty == "Mixed"
            or question["difficulty"] == difficulty
        )

        if category_match and difficulty_match:
            selected.append(question)

    random.shuffle(selected)

    return selected


def ask_question(question, number, total):
    print("\n--------------------------------")
    print("Question", number, "of", total)
    print("Category:", question["category"])
    print("Difficulty:", question["difficulty"])
    print("--------------------------------")

    print(question["question"])

    for index, option in enumerate(question["options"], start=1):
        print(str(index) + ".", option)

    while True:
        choice = input("Your answer (1-4): ").strip()

        if choice in ["1", "2", "3", "4"]:
            selected_answer = question["options"][int(choice) - 1]

            if selected_answer.lower() == question["answer"].lower():
                print("Correct! ✓")
                return True

            print("Wrong!")
            print("Correct answer:", question["answer"])
            return False

        print("Please enter a number from 1 to 4.")


def show_results(name, score, total, category_scores):
    percentage = (score / total) * 100

    print("\n================================")
    print("          QUIZ RESULTS")
    print("================================")

    print("Player:", name)
    print("Score:", score, "/", total)
    print("Percentage:", round(percentage, 1), "%")

    if percentage == 100:
        print("Excellent! Perfect score!")
    elif percentage >= 80:
        print("Excellent work!")
    elif percentage >= 60:
        print("Good job! Keep improving.")
    elif percentage >= 40:
        print("You're getting there. Keep practicing.")
    else:
        print("Keep studying and try again!")

    print("\nCategory Performance:")

    for category, scores in category_scores.items():
        correct = scores["correct"]
        total_questions = scores["total"]

        if total_questions > 0:
            category_percentage = (correct / total_questions) * 100
            print(
                category + ":",
                correct,
                "/",
                total_questions,
                "-",
                round(category_percentage, 1),
                "%"
            )


def play_quiz():
    print("\n================================")
    print("          STEM QUIZ")
    print("================================")

    name = input("Enter your name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    category = choose_category()
    difficulty = choose_difficulty()

    questions = get_questions(category, difficulty)

    if not questions:
        print("\nNo questions are available for that combination.")
        return

    print("\nStarting quiz...")
    print("Good luck,", name + "!")

    score = 0

    category_scores = {}

    for number, question in enumerate(questions, start=1):

        current_category = question["category"]

        if current_category not in category_scores:
            category_scores[current_category] = {
                "correct": 0,
                "total": 0
            }

        category_scores[current_category]["total"] += 1

        if ask_question(question, number, len(questions)):
            score += 1
            category_scores[current_category]["correct"] += 1

    show_results(
        name,
        score,
        len(questions),
        category_scores
    )


while True:
    play_quiz()

    print("\nWould you like to play again?")
    again = input("Enter yes or no: ").strip().lower()

    if again != "yes":
        print("\nThanks for playing STEM Quiz!")
        print("Keep learning and keep coding!")
        break
```
