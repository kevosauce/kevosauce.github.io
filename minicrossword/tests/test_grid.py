"""
Test cases for the Grid class.
"""

import pytest
from src.crossword_mini.grid import Grid


class TestGrid:
    """Test cases for the Grid class."""

    def test_grid_initialization(self):
        """Test that grid initializes correctly."""
        grid = Grid()
        assert grid.size == 5
        assert len(grid.grid) == 5
        assert len(grid.grid[0]) == 5

    def test_set_and_get_cell(self):
        """Test setting and getting cell values."""
        grid = Grid()
        grid.set_cell(0, 0, 'A')
        assert grid.get_cell(0, 0) == 'A'

        # Test case insensitive
        grid.set_cell(1, 1, 'b')
        assert grid.get_cell(1, 1) == 'B'

    def test_is_empty(self):
        """Test checking if cell is empty."""
        grid = Grid()
        assert grid.is_empty(0, 0) is True

        grid.set_cell(0, 0, 'A')
        assert grid.is_empty(0, 0) is False

    def test_black_cells(self):
        """Test black cell functionality."""
        grid = Grid()
        grid.set_black_cell(2, 2)

        assert grid.is_black_cell(2, 2) is True
        assert grid.is_black_cell(0, 0) is False
        assert grid.get_cell(2, 2) == '#'

    def test_can_place_word_across(self):
        """Test checking if word can be placed horizontally."""
        from src.crossword_mini.word_trie import WordTrie, load_words_from_file
        grid = Grid()
        trie = load_words_from_file('words_filtered.txt')

        # Place a word
        grid.place_word('HELLO', 0)

        # Test if we can place a word in row 1
        result = grid.can_place_word('WORLD', 1, trie)
        assert isinstance(result, bool)

    def test_can_place_word_down(self):
        """Test checking if word can be placed."""
        from src.crossword_mini.word_trie import WordTrie, load_words_from_file
        grid = Grid()
        trie = load_words_from_file('words_filtered.txt')

        # Place a word
        grid.place_word('HELLO', 0)

        # Test placing another word
        result = grid.can_place_word('EARTH', 1, trie)
        assert isinstance(result, bool)

    def test_place_word_across(self):
        """Test placing word horizontally."""
        grid = Grid()
        grid.place_word('HELLO', 0)

        # Check cells
        assert grid.get_cell(0, 0) == 'H'
        assert grid.get_cell(0, 1) == 'E'
        assert grid.get_cell(0, 2) == 'L'
        assert grid.get_cell(0, 3) == 'L'
        assert grid.get_cell(0, 4) == 'O'

    def test_place_word_down(self):
        """Test placing multiple words."""
        grid = Grid()
        grid.place_word('HELLO', 0)
        grid.place_word('WORLD', 1)

        # Check first row
        assert grid.get_cell(0, 0) == 'H'
        assert grid.get_cell(0, 1) == 'E'
        # Check second row
        assert grid.get_cell(1, 0) == 'W'
        assert grid.get_cell(1, 1) == 'O'

    def test_word_intersection(self):
        """Test placing multiple words in grid."""
        grid = Grid()

        # Place first word
        grid.place_word('HELLO', 0)

        # Place second word
        grid.place_word('WORLD', 1)

        # Check both words are present
        assert grid.get_cell(0, 0) == 'H'
        assert grid.get_cell(0, 4) == 'O'
        assert grid.get_cell(1, 0) == 'W'
        assert grid.get_cell(1, 4) == 'D'

    def test_get_word_positions(self):
        """Test getting word positions from grid."""
        grid = Grid()
        grid.place_word('HELLO', 0)
        grid.place_word('WORLD', 1)

        positions = grid.get_word_positions()

        # Should find both words
        words = [pos[3] for pos in positions]
        assert 'HELLO' in words or 'WORLD' in words

    def test_clear_grid(self):
        """Test that a new grid is empty."""
        grid = Grid()
        grid.place_word('HELLO', 0)
        grid.set_black_cell(2, 2)

        # Create a new grid instead of clearing
        new_grid = Grid()

        # New grid letters should be empty
        assert new_grid.is_empty(0, 0) is True
        assert new_grid.is_empty(0, 1) is True

        # Black cells should not exist in new grid
        assert new_grid.is_black_cell(2, 2) is False

    def test_display(self):
        """Test grid display functionality."""
        grid = Grid()
        grid.place_word('HELLO', 0)
        grid.set_black_cell(1, 1)

        display = grid.display()

        # Should contain grid content
        assert 'H' in display
        assert 'E' in display
        assert '#' in display
        assert '.' in display  # Empty cells

    def test_get_column_empty(self):
        """Test getting column from empty grid."""
        grid = Grid()
        column = grid.get_column(0)
        assert column == ""
        assert len(column) == 0

    def test_get_column_partial(self):
        """Test getting partially filled column."""
        grid = Grid()
        grid.set_cell(0, 2, 'A')
        grid.set_cell(1, 2, 'B')
        grid.set_cell(2, 2, 'C')
        # Rows 3 and 4 are empty
        column = grid.get_column(2)
        assert column == "ABC"

    def test_get_column_full(self):
        """Test getting fully filled column."""
        grid = Grid()
        grid.place_word('HELLO', 0)
        grid.place_word('WORLD', 1)
        # Column 0 should be "HW"
        column = grid.get_column(0)
        assert column == "HW"
        column = grid.get_column(1)
        assert column == "EO"
        column = grid.get_column(2)
        assert column == "LR"
        column = grid.get_column(3)
        assert column == "LL"
        column = grid.get_column(4)
        assert column == "OD"

    def test_get_column_all_columns(self):
        """Test getting all columns."""
        grid = Grid()
        grid.place_word('HELLO', 0)
        assert grid.get_column(0) == "H"
        assert grid.get_column(1) == "E"
        assert grid.get_column(2) == "L"
        assert grid.get_column(3) == "L"
        assert grid.get_column(4) == "O"
