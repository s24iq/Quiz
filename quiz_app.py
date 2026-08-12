import random

def start_quiz():
    print("=== Math Quiz App ===\n")
    
    # 1. Ask user for number of questions
    while True:
        try:
            total_questions = int(input("Enter number of questions: "))
            if total_questions > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    score = 0
    operators = ['+', '-', '*'] # operations
    
    print(f"\nQuiz started with {total_questions} questions!\n")

    # 2. Loop through each question
    for i in range(1, total_questions + 1):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        op = random.choice(operators)

        # Calculate correct answer
        if op == '+':
            correct_ans = num1 + num2
        elif op == '-':
            correct_ans = num1 - num2
        elif op == '*':
            correct_ans = num1 * num2

        # Display question format required by client
        print(f"Question {i}/{total_questions}: {num1} {op} {num2} = ?")
        
        # Get and validate user input
        while True:
            try:
                user_ans = int(input("User answer: "))
                break
            except ValueError:
                print("Please enter an integer answer!")

        # Check score
        if user_ans == correct_ans:
            score += 1

        print()  # Empty line for clean display

    # 3. Print final score
    print("--------------------")
    print(f"Final Score: {score}/{total_questions}")
    print("--------------------")

# Call the function directly
start_quiz()