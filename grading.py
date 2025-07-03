import math
from typing import List, Tuple

# Prompt user for student names and scores, return two lists
def prompt_names_and_scores() -> Tuple[List[str], List[float]]:
    while True:
        try:
            count = int(input("Number of students to grade: "))
            if count > 0:
                break
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Enter a whole number.")

    names, scores = [], []

    print("\nEnter student names and scores:")

    # Input loop for each student
    for i in range(count):
        name = input(f"Student {i + 1} name: ").strip() or f"Student{i + 1}"
        names.append(name)

        # Validate score input
        while True:
            try:
                score = float(input(f"Score for {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid score. Enter a number.")

    return names, scores

# Assign grade based on score
def match_grade(score: float) -> str:
    if score >= 70: return "A"
    if score >= 60: return "B"
    if score >= 50: return "C"
    if score >= 40: return "D"
    return "F"

# Compute and return the average score
def compute_avg(scores: List[float]) -> float:
    return round(sum(scores) / len(scores), 2)

# Display formatted results table with names, scores, and grades
def generate_results_table(names: List[str], scores: List[float]) -> None:
    print("\n=== Student Results ===")
    print(f"{'Name':<15} {'Score':<10} {'Grade'}")
    print("-" * 30)

    # Display each student's result
    for name, score in zip(names, scores):
        grade = match_grade(score)
        print(f"{name:<15} {score:<10.2f} {grade}")

    # Compute and display average score and rounded values
    avg = compute_avg(scores)
    print(f"\nClass Average: {avg}")
    print(f"Rounded Up: {math.ceil(avg)}")
    print(f"Rounded Down: {math.floor(avg)}")

# Main program loop
def main():
    print("=== Grading System ===")
    print("Course: Data Structures and Algorithms")

    # Allow grading multiple classes
    while True:
        names, scores = prompt_names_and_scores()
        generate_results_table(names, scores)
        # Check if the user wants to continue
        if input("\nGrade another class? (yes/no): ").strip().lower() != "yes":
            print("Thank you for using the Python grading system!")
            break

# Run the program
if __name__ == "__main__":
    main()