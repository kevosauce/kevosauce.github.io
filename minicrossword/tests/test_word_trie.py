"""
Tests for WordTrie pattern matching functionality.
"""

import pytest
from src.crossword_mini.word_trie import WordTrie


class TestWordTriePatternMatch:
    """Test cases for the get_words_with_pattern method."""

    @pytest.fixture
    def sample_trie(self):
        """Create a trie with sample words for testing."""
        trie = WordTrie()
        words = [
            "APPLE", "APPLY", "APRON",
            "BROWN", "BROKE", "BRUSH",
            "CREAM", "CRISP", "CROWN",
            "TABLE", "TAKEN", "TASTE",
            "HELLO", "HELPS", "HEAVY"
        ]
        for word in words:
            trie.insert(word)
        return trie

    def test_pattern_no_wildcards(self, sample_trie):
        """Test pattern matching with no wildcards (exact match)."""
        result = sample_trie.get_words_with_pattern("APPLE")
        assert result == ["APPLE"]

    def test_pattern_single_wildcard_start(self, sample_trie):
        """Test pattern with wildcard at the start."""
        result = sample_trie.get_words_with_pattern("?PPLE")
        assert result == ["APPLE"]

    def test_pattern_single_wildcard_middle(self, sample_trie):
        """Test pattern with wildcard in the middle."""
        result = sample_trie.get_words_with_pattern("AP?LY")
        assert result == ["APPLY"]

    def test_pattern_single_wildcard_end(self, sample_trie):
        """Test pattern with wildcard at the end."""
        result = sample_trie.get_words_with_pattern("APPL?")
        assert set(result) == {"APPLE", "APPLY"}

    def test_pattern_multiple_wildcards(self, sample_trie):
        """Test pattern with multiple wildcards."""
        result = sample_trie.get_words_with_pattern("?R???")
        assert set(result) == {"BROWN", "BROKE", "BRUSH", "CREAM", "CRISP", "CROWN"}

    def test_pattern_all_wildcards(self, sample_trie):
        """Test pattern with all wildcards (get all 5-letter words)."""
        result = sample_trie.get_words_with_pattern("?????")
        expected = [
            "APPLE", "APPLY", "APRON", "BROWN", "BROKE", "BRUSH",
            "CREAM", "CRISP", "CROWN", "TABLE", "TAKEN", "TASTE",
            "HELLO", "HELPS", "HEAVY"
        ]
        assert set(result) == set(expected)

    def test_pattern_no_matches(self, sample_trie):
        """Test pattern that matches no words."""
        result = sample_trie.get_words_with_pattern("XYZ??")
        assert result == []

    def test_pattern_alternating_wildcards(self, sample_trie):
        """Test pattern with alternating wildcards and letters."""
        result = sample_trie.get_words_with_pattern("?R?S?")
        assert set(result) == {"BRUSH", "CRISP"}

    def test_pattern_case_insensitive(self, sample_trie):
        """Test that pattern matching is case-insensitive."""
        result_upper = sample_trie.get_words_with_pattern("AP?LE")
        result_lower = sample_trie.get_words_with_pattern("ap?le")
        assert result_upper == result_lower
        assert result_upper == ["APPLE"]

    def test_pattern_custom_wildcard(self, sample_trie):
        """Test pattern matching with custom wildcard character."""
        result = sample_trie.get_words_with_pattern("AP*LE", wildcard='*')
        assert result == ["APPLE"]

    def test_pattern_empty_trie(self):
        """Test pattern matching on empty trie."""
        trie = WordTrie()
        result = trie.get_words_with_pattern("?????")
        assert result == []

    def test_pattern_single_letter_wildcard(self, sample_trie):
        """Test pattern with single wildcard."""
        trie = WordTrie()
        trie.insert("A")
        trie.insert("B")
        trie.insert("C")
        result = trie.get_words_with_pattern("?")
        assert set(result) == {"A", "B", "C"}

    def test_pattern_first_and_last_letter(self, sample_trie):
        """Test pattern specifying only first and last letters."""
        result = sample_trie.get_words_with_pattern("A???E")
        assert set(result) == {"APPLE"}

    def test_pattern_with_spaces(self, sample_trie):
        """Test that pattern is properly stripped of whitespace."""
        result = sample_trie.get_words_with_pattern(" APPLE ")
        assert result == ["APPLE"]

    def test_pattern_length_mismatch(self, sample_trie):
        """Test pattern that is wrong length returns no matches."""
        result = sample_trie.get_words_with_pattern("AP?")
        assert result == []

    def test_pattern_consecutive_known_letters(self, sample_trie):
        """Test pattern with consecutive known letters."""
        result = sample_trie.get_words_with_pattern("??OWN")
        assert set(result) == {"BROWN", "CROWN"}

    def test_pattern_short_with_wildcards(self, sample_trie):
        """Test short pattern with wildcards."""
        trie = WordTrie()
        trie.insert("SEA")
        trie.insert("TEA")
        trie.insert("PEA")
        trie.insert("SKI")
        result = trie.get_words_with_pattern("??A")
        assert set(result) == {"SEA", "TEA", "PEA"}
