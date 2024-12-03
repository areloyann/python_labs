import string
from collections import Counter

def count_word_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()

    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    word_counts = Counter(words)
    return word_counts

if __name__ == "__main__":
    filename = r'C:\Users\5308-2\Desktop\New folder (3)\tt219\pyy.txt'
    word_counts = count_word_frequency(filename)
    for word, count in word_counts.items():
        print(f"{word}: {count}")