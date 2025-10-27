"""
5x5 Mini Crossword Generator

A Python package for generating 5x5 mini crossword puzzles with word placement algorithms.
"""

__version__ = "0.1.0"
__author__ = "kevinu"

from .crossword_generator import *
from .grid import Grid
from .word_trie import WordTrie, load_words_from_file
