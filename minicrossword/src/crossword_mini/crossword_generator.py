"""
Main crossword generator class that orchestrates the puzzle creation.
"""

import random
from typing import List, Optional, Dict, Any
from .grid import Grid
from .word_trie import WordTrie
import copy

def _search_pattern_for_char_at_index(char: str, index: int) -> str:
    return "?" * index + char + "?" * (5 - index - 1)

def generate_next_word_candidates(grid: Grid, row: int, trie: WordTrie) -> List[str]:
    candidates = None
    for col in range(grid.size):
        current_column = grid.get_column(col)
        column_candidates = trie.get_words_with_prefix(current_column)
        next_row_letters = set([word[row] for word in column_candidates])
        col_matches = set()
        for letter in next_row_letters:
            pattern = _search_pattern_for_char_at_index(letter, col)
            match = trie.get_words_with_pattern(pattern)
            col_matches.update(match)
        if candidates is None:
            candidates = col_matches
        else:
            candidates.intersection_update(col_matches)

    return list(candidates)


def generate_puzzle(seed_word: str, trie: WordTrie) -> Optional[Grid]:
    grid = Grid()
    grid.place_word(seed_word, 0)
    possible_grids = [grid]
    while possible_grids:
        candidate_grid = possible_grids.pop()

        next_row = candidate_grid.first_empty_row()
        if not next_row:
            return candidate_grid

        candidate_words = generate_next_word_candidates(candidate_grid, next_row, trie)

        for word in candidate_words:
            new_grid = copy.deepcopy(candidate_grid)
            if new_grid.can_place_word(word, next_row, trie):
                new_grid.place_word(word, next_row)
                possible_grids.append(new_grid)

    return None

def generate_all_puzzles(seed_word: str, trie: WordTrie) -> List[Grid]:
    grid = Grid()
    grid.place_word(seed_word, 0)
    num_rows = grid.size
    possible_grids = [grid]
    complete_puzzles = []
    while possible_grids:
        candidate_grid = possible_grids.pop()

        next_row = candidate_grid.first_empty_row()
        if not next_row:
            print(candidate_grid.display())
            complete_puzzles.append(candidate_grid)
            continue

        candidate_words = generate_next_word_candidates(candidate_grid, next_row, trie)

        for word in candidate_words:
            new_grid = copy.deepcopy(candidate_grid)
            new_grid.place_word(word, next_row)
            possible_grids.append(new_grid)

    return complete_puzzles
