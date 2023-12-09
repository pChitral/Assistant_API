import os
import logging


def save_to_markdown(problem_number, output):
    # Define the path for the solutions folder
    solutions_folder = "solutions"

    # Check if the solutions folder exists, create if it doesn't
    if not os.path.exists(solutions_folder):
        os.makedirs(solutions_folder)

    # Update the filename to include the solutions folder path
    filename = os.path.join(solutions_folder, f"{problem_number}.md")

    with open(filename, "w") as file:
        file.write(output)
    logging.info(f"Saved output of problem {problem_number} to {filename}")
