#Develop a MapReduce program to calculate the frequency of a given word in a given file.
import sys
import re
from collections import defaultdict

def mapper(file_path):
    """Map step: emit (word, 1) pairs"""
    mapped = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            #remove punctuation and convert to lowercase
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                mapped.append((word,1))

    return mapped

def reducer(mapped_data, target_word):
    """Reduce step: sum counts for target word"""
    word_count = defaultdict(int)

    #shuffle and sort (grouping)
    for word, count in mapped_data:
        word_count[word] += count

    return word_count[target_word.lower()]

file_path = input("Enter file path: ")
target_word = input("Enter word to count: ")

mapped = mapper(file_path)
frequency = reducer(mapped, target_word)


print(f"Frequency of '{target_word}': {frequency}")
