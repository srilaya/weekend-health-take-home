# weekend-health-take-home

## Overview

This project is a solution to a coding challenge that involves finding words from a dictionary that can be formed using characters from a given input string. Each character from the input string can be used only once per word.

## High-Level Approach

1. **Input Handling**: 
   - The function `find_words` takes an input string and a list of words (dictionary) as arguments.
   - The function `build_frequency_map` creates a character frequency map from the input string to keep track of available characters.

2. **Processing**: 
   - For each word in the dictionary, the helper function `can_form_word` checks if the word can be formed using the characters from the input string by comparing character frequencies.

3. **Output**: 
   - The function `find_words` returns a list of words that can be formed from the input string for a given list of words ( dictionary ) .

## Project Structure

weekend-health-take-home
├── README.md
└── src
    ├── __init__.py
    ├── main.py
└── tests
    ├── __init__.py
    ├── test_main.py

- `main.py`: Contains the implementation of the `find_words` function.
- `test_main.py`: Contains unit tests for the `find_words`, `can_form_word`, `build_frequency_map` function.
- `README.md`: Project documentation.

## Installation and Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/srilaya/weekend-health-take-home.git
    cd weekend-health-take-home
    ```

2. **Run the tests**:
    ```python3 tests/test_main.py
    ```