# Assistant API

## Overview

Assistant API is a Python project designed to interact with the OpenAI API to process and respond to LeetCode problem statements. It demonstrates structured and modular code organization, including error handling, logging, and unit testing.

## Features

- Interacts with OpenAI's API to process LeetCode problems.
- Modular codebase with clear separation of concerns.
- Comprehensive error handling and logging.
- Unit tests ensuring code reliability and maintainability.

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/pChitral/Assistant_API.git
   ```
2. Navigate to the project directory:
   ```
   cd Assistant_API
   ```
3. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

Run the main application:

```
python src/main.py
```

### Running Tests

Execute the following command to run unit tests:

```
python -m unittest discover -s tests
```

## Project Structure

- `src/`: Source code for the main application.
  - `main.py`: The main script to run the program.
  - `openai_client.py`: Module to handle OpenAI API interactions.
  - `leetcode_processor.py`: Module for processing LeetCode problems.
- `tests/`: Unit tests for the application.
  - `test_openai_client.py`: Tests for the OpenAI client module.
  - `test_leetcode_processor.py`: Tests for the LeetCode processor module.
- `venv/`: Virtual environment for project dependencies.
- `requirements.txt`: Required Python dependencies.
- `README.md`: Project documentation (this file).

## Contributing

Contributions to the Assistant API are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

Chitral Patil - [chitralpatil@gmail.com](mailto:chitralpatil@gmail.com)

Project Link: [https://github.com/pChitral/Assistant_API](https://github.com/pChitral/Assistant_API)
