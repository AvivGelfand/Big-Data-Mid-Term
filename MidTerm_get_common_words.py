import numpy as np
import re
import sys


def script(file_path, k):
    # Normalise all words from file into a list of words
    all_words = open(file_path, "r").read().lower()
    all_words = np.array(re.sub(r"[^\w\s']", "", all_words).split())

    # Converting stop_words.txt into an array of words
    stop_words = np.array(open('stop_words.txt', "r").read().replace('"', '').strip('{').strip('}').split(", "))
    stop_words = np.array([word.strip("'").strip('"') for word in stop_words])

    # Finding all words from file that aren't in stop_words
    valid_words = all_words[~np.isin(all_words, stop_words)]

    # Counting the number of occurrences
    unique_words, count = np.unique(np.array(valid_words), return_counts=True)
    sorted_ind = np.argsort(count)
    unique_words, count = unique_words[sorted_ind], count[sorted_ind]

    # Creating a single array of tuples (word, word count)
    sorted_words = list(zip(unique_words, count))[::-1]

    for word in sorted_words[:k]:
        print(word)


if __name__ == '__main__':
    if (sys.argv[1] is not None) and (sys.argv[2] is not None) and sys.argv[2].isdigit():
        script(sys.argv[1], int(sys.argv[2]))
    else:
        print('Invalid Arguments')
