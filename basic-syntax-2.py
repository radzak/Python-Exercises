"""
Write a program that takes a file name as command line argument,
count how many times each word appears in the file and prints the word that appears the most
(and its relevant count)
"""


import argparse
import os
from collections import Counter


def parse_arguments():
    description = 'Count how many times each word appears in ' \
                  'the file and print the word that appears the most.'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file_paths', metavar='file', type=str, nargs='+',
                        help='path of a file to count the words from')

    return parser.parse_args()


def find_most_common_word(file_path):
    """
    Find the most common word and return it with the number of occurrences.
    :return: (word, count) of the most common word
    """
    with open(file_path, 'r') as f:
        file_words = f.read().replace('\n', ' ').lower().split()
        counter = Counter(file_words)
        return counter.most_common()[0]


def main():
    args = parse_arguments()
    for file in args.file_paths:
        if os.path.exists(file):
            word, count = find_most_common_word(file)
            print(f'Most common word in {os.path.basename(file)} '
                  f'file is {word}, it occured {count} times.')
        else:
            print(f'File {file} doesn\'t exist.')


if __name__ == '__main__':
    main()
