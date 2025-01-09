# Keylogger-Detection
This Python script is designed to detect keyloggers by searching for specific words within files in a given directory.

## Features

- Loads words from a specified file.
- Recursively searches for these words in all files within a specified directory.
- Outputs the file paths where the words are found.
- Handles errors gracefully with informative messages.

## Prerequisites

- Python 3.x

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/yourusername/keylogger-detection.git
```

```
cd keylogger-detection
```

```
python keylogger_detection.py
```

## Key Improvements
  
  - Added to describe the purpose of functions.
  - Included more specific error messages and caught general exceptions.
  - Users can specify the directory and word file when running the script.
  - The search_words_in_file function was created to handle file-specific searches.

