import logging
import os
from dotenv import load_dotenv
from openai_client import OpenAIClient
from leetcode_processor import LeetCodeProcessor

# Load environment variables from .env file
load_dotenv()

# Initialize logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Function to save the output to a Markdown file
def save_to_markdown(problem_number, output):
    filename = f"problem_{problem_number}.md"
    with open(filename, "w") as file:
        file.write(output)
    logging.info(f"Saved output of problem {problem_number} to {filename}")


# Main loop to process a range of problem numbers
def main():
    assistant_id = os.getenv("PYVERSE_ASSISTANT_ID")
    api_key = os.getenv("OPENAI_API_KEY")
    if not assistant_id or not api_key:
        raise ValueError(
            "Environment variables PYVERSE_ASSISTANT_ID or OPENAI_API_KEY not found"
        )

    client = OpenAIClient(assistant_id, api_key)
    processor = LeetCodeProcessor(client)

    start_problem_number = 1  # Start number
    end_problem_number = 5  # End number
    results = {}

    for problem_number in range(start_problem_number, end_problem_number + 1):
        problem_number, output = processor.process_problem(problem_number)
        results[problem_number] = output
        print(f"Problem {problem_number}: {output}")

        # Save the output to a Markdown file
        if output is not None:
            save_to_markdown(problem_number, output)

    # Results contain all the responses indexed by problem numbers
    return results


# Run the main loop
if __name__ == "__main__":
    results = main()
