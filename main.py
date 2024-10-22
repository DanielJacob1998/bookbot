from collections import Counter
import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # Get word and character data
    word_count = count_words(text)
    char_count = count_characters(text)

    # Generate and print the report
    generate_report(word_count, char_count)


def get_book_text(path):
    with open(path, "r") as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    # Convert the text to lowercase and filter out non-alphabetic characters
    text = text.lower()
    
    # Use a generator expression to keep only alphabetic characters
    filtered_text = (char for char in text if char in string.ascii_lowercase)
    
    # Count occurrences of each character
    char_count = Counter(filtered_text)
    return dict(char_count)  # Convert to a dictionary for the required format


def generate_report(word_count, char_count):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    # Sort characters by their frequency in descending order
    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    
    # Print the character frequencies in the specified format
    for char, count in sorted_char_count.items():
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


# Call the main function
if __name__ == "__main__":
    main()
