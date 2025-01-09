import os
import argparse

def load_words_from_file(word_file):
   
    try:
        with open(word_file, 'r') as f:
            return set(word.strip() for word in f)
    except FileNotFoundError:
        print(f"Error: The word file '{word_file}' was not found.")
        return set()
    except Exception as e:
        print(f"An error occurred while loading words from file '{word_file}': {e}")
        return set()

def search_words_in_file(file_path, words):
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            for word in words:
                if word in content:
                    print(f'Found word "{word}" in file: {file_path}')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def search_words_in_directory(directory, words):
    
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            search_words_in_file(file_path, words)

def main():
    parser = argparse.ArgumentParser(description="Keylogger Detection Script")
    parser.add_argument('directory', type=str, help='Directory to search for keylogger words')
    parser.add_argument('word_file', type=str, help='File containing words to search for')

    args = parser.parse_args()

    words = load_words_from_file(args.word_file)
    if words:
        print(f"Searching for {len(words)} words in directory '{args.directory}'...")
        search_words_in_directory(args.directory, words)
    else:
        print("No words to search for. Make sure the word file is valid.")

if __name__ == '__main__':
    main()
