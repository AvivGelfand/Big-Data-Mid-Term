import sys
from collections import Counter
import re

def read_file(file_path):
    """Reads a file and returns a list of words composed of alphabetic characters only, in lowercase."""
    with open(file_path, 'r') as file:
        content = file.read().lower()
    # Use regular expression to match words with alphabetic characters only
    word_list = re.findall(r'\w+', content)
    return word_list

def calculate_relative_frequencies(word_list):
    """Calculates and returns the relative frequency of words in a list."""
    total_words = len(word_list)
    word_counts = Counter(word_list)
    return {word: count / total_words for word, count in word_counts.items()}

def main(file1_path, file2_path, k):
    # Read and process the files
    words_file1 = read_file(file1_path)
    words_file2 = read_file(file2_path)
    
    # Calculate relative frequencies
    freqs_file1 = calculate_relative_frequencies(words_file1)
    freqs_file2 = calculate_relative_frequencies(words_file2)
    
    # Calculate the difference in relative frequencies
    diff_freqs = {word: abs(freqs_file1.get(word, 0) - freqs_file2.get(word, 0)) for word in set(freqs_file1) | set(freqs_file2)}
    
    # Get the top k words with the maximum difference in relative frequency
    top_diff_words = sorted(diff_freqs, key=diff_freqs.get, reverse=True)[:k]
    
    # Print the results
    for word in top_diff_words:
        print(f"{word}: {diff_freqs[word]}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 count_top_diff_freq_words.py file1.txt file2.txt k")
        sys.exit(1)
    
    file1, file2, k = sys.argv[1], sys.argv[2], int(sys.argv[3])
    main(file1, file2, k)
