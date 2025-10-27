"""
Grid module for 5x5 crossword puzzle management.
"""

from enum import Enum, auto
from typing import List, Optional, Tuple
from .word_trie import WordTrie

class Direction(Enum):
    """Enum for crossword placement directions."""
    ACROSS = auto()
    DOWN = auto()

class Grid:
    """Represents a 5x5 crossword grid."""

    def __init__(self):
        """Initialize a 5x5 grid with empty cells."""
        self.size = 5
        self.grid = [['' for _ in range(self.size)] for _ in range(self.size)]

    def set_cell(self, row: int, col: int, letter: str) -> None:
        """Set a letter in the grid at the specified position."""
        if 0 <= row < self.size and 0 <= col < self.size:
            self.grid[row][col] = letter.upper()

    def get_cell(self, row: int, col: int) -> str:
        """Get the letter at the specified position."""
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col]
        return ''

    def is_empty(self, row: int, col: int) -> bool:
        """Check if a cell is empty."""
        return self.get_cell(row, col) == ''

    def is_black_cell(self, row: int, col: int) -> bool:
        """Check if a cell is blocked (black)."""
        return self.get_cell(row, col) == '#'

    def set_black_cell(self, row: int, col: int) -> None:
        """Mark a cell as blocked (black)."""
        if 0 <= row < self.size and 0 <= col < self.size:
            self.grid[row][col] = '#'

    def first_empty_row(self) -> Optional[int]:
        """Return the index of the first empty row, or None if all are filled."""
        for row in range(self.size):
            if self.is_empty(row, 0):
                return row
        return None

    def get_column(self, col: int) -> str:
        """Get the letters in a specified column as a string."""
        return ''.join(self.get_cell(row, col) for row in range(self.size))

    def can_place_word(self, word: str, row: int, word_trie: WordTrie) -> bool:
        # assume row is first empty row
        acrosses = set(self.get_acrosses())
        word = word.strip().upper()
        for col in range(self.size):
            prefix = self.get_column(col) + word[col]
            words = word_trie.get_words_with_prefix(prefix)
            if not words:
                return False

            remaining = set(words) - acrosses
            if not remaining:
                return False

        return True

    def place_word(self, word: str, row: int):
        word = word.upper()
        for col, letter in enumerate(word):
            self.set_cell(row, col, letter)

    def get_acrosses(self) -> List[str]:
        acrosses = []
        for row in range(self.size):
            acrosses.append(''.join(self.get_cell(row, col) for col in range(self.size)))
        return acrosses

    def display(self) -> str:
        """Return a string representation of the grid."""
        result = []
        result.append("  " + " ".join(str(i) for i in range(self.size)))
        result.append("  " + "-" * (self.size * 2 - 1))

        for i, row in enumerate(self.grid):
            row_str = f"{i}|"
            for cell in row:
                if cell == '':
                    row_str += "."
                else:
                    row_str += cell
                row_str += " "
            result.append(row_str.rstrip())

        return "\n".join(result)

    def get_word_positions(self) -> List[Tuple[int, int, str, str]]:
        """
        Get all word positions in the grid.

        Returns:
            List of tuples (row, col, direction, word)
        """
        words = []

        # Find horizontal words
        for row in range(self.size):
            current_word = ""
            start_col = 0
            for col in range(self.size):
                if not self.is_black_cell(row, col) and self.get_cell(row, col) != '':
                    if current_word == "":
                        start_col = col
                    current_word += self.get_cell(row, col)
                else:
                    if len(current_word) > 1:
                        words.append((row, start_col, 'across', current_word))
                    current_word = ""
            if len(current_word) > 1:
                words.append((row, start_col, 'across', current_word))

        # Find vertical words
        for col in range(self.size):
            current_word = ""
            start_row = 0
            for row in range(self.size):
                if not self.is_black_cell(row, col) and self.get_cell(row, col) != '':
                    if current_word == "":
                        start_row = row
                    current_word += self.get_cell(row, col)
                else:
                    if len(current_word) > 1:
                        words.append((start_row, col, 'down', current_word))
                    current_word = ""
            if len(current_word) > 1:
                words.append((start_row, col, 'down', current_word))

        return words

    def clear(self) -> None:
        """Clear the grid of all letters but keep black cells."""
        for row in range(self.size):
            for col in range(self.size):
                if not self.is_black_cell(row, col):
                    self.grid[row][col] = ''
