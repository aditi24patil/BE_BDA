#Develop a MapReduce program to calculate the frequency of a given word in a given file.
import re
from collections import defaultdict

def mapper(file_path, target_word):
    """Map step: emit (word, 1) only for target word"""
    mapped = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word == target_word.lower():
                    mapped.append((word, 1))

    return mapped

def shuffle_sort(mapped_data):
    """Shuffle step: group values by key"""
    grouped = defaultdict(list)
    for word, count in mapped_data:
        grouped[word].append(count)
    return grouped

def reducer(grouped_data):
    """Reduce step: sum counts"""
    reduced = {}
    for word in grouped_data:
        reduced[word] = sum(grouped_data[word])
    return reduced

# Input
file_path = input("Enter file path: ")
target_word = input("Enter word to count: ")

try:
    mapped = mapper(file_path, target_word)
    grouped = shuffle_sort(mapped)
    result = reducer(grouped)

    frequency = result.get(target_word.lower(), 0)

    print(f"Frequency of '{target_word}': {frequency}")

except FileNotFoundError:
    print("File not found. Please check the path.")
