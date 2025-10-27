#!/usr/bin/env python3
"""
Demo script for the 5x5 Mini Crossword Generator.

This script demonstrates how to use the crossword generation library
to create mini crossword puzzles.
"""

from src.crossword_mini import *

def get_five_letter_word():
    """Request a five-letter word from the user and return their input."""
    while True:
        word = input("Please enter a 5-letter word: ").strip().upper()

        if len(word) == 5 and word.isalpha():
            return word
        else:
            print("Please enter exactly 5 letters (no numbers or special characters).")

def select_word_from_list(words: List[str]):
    while True:
        word = input("Enter your choice: ").strip().upper()

        if word in words:
            return word
        else:
            print("Sorry, can't find that word in the list. Please enter a word from this list:")
            print(words)

def get_first_word_and_generate_puzzle():
    # Demo: prompt user for a first word, place it, then try to auto-complete rows
    user_word = get_five_letter_word()
    print(f"Using user seed word: {user_word}")

    trie = load_words_from_file('dictionaries/combined-five.txt')
    grid = generate_puzzle(user_word, trie)

    if grid:
        print("Generated Puzzle!")
        print(grid.display())
    else:
        print("could not generate grid with your word!")

def get_first_word_and_generate_all_puzzles():
    # Demo: prompt user for a first word, place it, then try to auto-complete rows
    user_word = get_five_letter_word()
    print(f"Using user seed word: {user_word}")

    trie = load_words_from_file('dictionaries/combined-five.txt')
    grids = generate_all_puzzles(user_word, trie)

    if grids:
        print(f"Generated {len(grids)} Puzzles!")
        for grid in girds:
            print(grid.display())
    else:
        print("Could not generate any puzzle starting with your word!")

def ask_for_each_word():
    user_word = get_five_letter_word()
    print(f"Using user seed word: {user_word}")

    trie = load_words_from_file('mit-words-five.txt')
    grid = Grid()
    grid.place_word(user_word, 0)

    for row in range(1,5):
        print("Current grid")
        print(grid.display())

        next_words = generate_next_word_candidates(grid, row, trie)
        if not next_words:
            print("No more valid options!")
            return

        print("Choose next word from list")
        next_words.sort()
        print(next_words)
        user_word = select_word_from_list(next_words)
        grid.place_word(user_word, row)

    print("Your puzzle:")
    print(grid.display())


def test_puzzle():
    trie = load_words_from_file('dictionaries/combined-five.txt')
    grid = Grid()
    words = ["class", "lunch", "inner", "maine", "breed"]
    for row, word in enumerate(words):
        print(grid.can_place_word(word, row, trie))
        grid.place_word(word, row)
    print("success")
    print(grid.display())

def main():
    get_first_word_and_generate_puzzle()
    # ask_for_each_word()
    # get_first_word_and_generate_all_puzzles()
    # test_puzzle()

if __name__ == "__main__":
    main()
