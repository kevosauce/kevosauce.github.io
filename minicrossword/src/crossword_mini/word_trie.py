"""
Trie data structure for efficient word storage and prefix-based lookups.
"""

from typing import List, Set, Optional


class TrieNode:
    """A node in the Trie data structure."""

    def __init__(self):
        self.children = {}  # Dictionary mapping character to TrieNode
        self.is_end_of_word = False
        self.word = None  # Store the complete word at end nodes


class WordTrie:
    """
    Trie data structure for storing words with efficient prefix-based operations.

    Provides O(m) time complexity for insertions, lookups, and prefix searches,
    where m is the length of the word/prefix.
    """

    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.

        Args:
            word: The word to insert (will be converted to uppercase)
        """
        word = word.upper().strip()
        if not word:
            return

        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        if not node.is_end_of_word:
            self.word_count += 1

        node.is_end_of_word = True
        node.word = word

    def search(self, word: str) -> bool:
        """
        Check if a word exists in the trie.

        Args:
            word: The word to search for

        Returns:
            True if the word exists, False otherwise
        """
        word = word.upper().strip()
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the trie starts with the given prefix.

        Args:
            prefix: The prefix to search for

        Returns:
            True if at least one word starts with the prefix, False otherwise
        """
        prefix = prefix.upper().strip()
        return self._find_node(prefix) is not None

    def get_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Get all words that start with the given prefix.

        Args:
            prefix: The prefix to search for

        Returns:
            List of words that start with the prefix
        """
        prefix = prefix.upper().strip()
        node = self._find_node(prefix)

        if node is None:
            return []

        words = []
        self._collect_words(node, words)
        return words

    def get_words_by_length(self, length: int) -> List[str]:
        """
        Get all words of a specific length.

        Args:
            length: The desired word length

        Returns:
            List of words with the specified length
        """
        words = []
        self._collect_words_by_length(self.root, "", length, words)
        return words

    def get_words_with_pattern(self, pattern: str, wildcard: str = '?') -> List[str]:
        """
        Get all words that match a pattern with wildcards.

        Args:
            pattern: Pattern string where wildcard represents any character
            wildcard: Character used as wildcard (default '?')

        Returns:
            List of words matching the pattern
        """
        pattern = pattern.upper().strip()
        words = []
        self._match_pattern(self.root, pattern, 0, "", wildcard, words)
        return words

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        """Find the node corresponding to a prefix."""
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]

        return node

    def _collect_words(self, node: TrieNode, words: List[str]) -> None:
        """Recursively collect all words from a node."""
        if node.is_end_of_word:
            words.append(node.word)

        for child in node.children.values():
            self._collect_words(child, words)

    def _collect_words_by_length(self, node: TrieNode, current_word: str,
                                target_length: int, words: List[str]) -> None:
        """Recursively collect words of specific length."""
        if len(current_word) == target_length:
            if node.is_end_of_word:
                words.append(node.word)
            return

        if len(current_word) < target_length:
            for char, child in node.children.items():
                self._collect_words_by_length(child, current_word + char,
                                            target_length, words)

    def _match_pattern(self, node: TrieNode, pattern: str, pos: int,
                      current_word: str, wildcard: str, words: List[str]) -> None:
        """Recursively match pattern with wildcards."""
        if pos == len(pattern):
            if node.is_end_of_word:
                words.append(node.word)
            return

        char = pattern[pos]

        if char == wildcard:
            # Wildcard matches any character
            for next_char, child in node.children.items():
                self._match_pattern(child, pattern, pos + 1,
                                  current_word + next_char, wildcard, words)
        else:
            # Exact character match
            if char in node.children:
                self._match_pattern(node.children[char], pattern, pos + 1,
                                  current_word + char, wildcard, words)

    def get_stats(self) -> dict:
        """Get statistics about the trie."""
        return {
            'total_words': self.word_count,
            'total_nodes': self._count_nodes(self.root),
            'max_depth': self._max_depth(self.root),
            'words_by_length': {
                length: len(self.get_words_by_length(length))
                for length in range(1, 11)
            }
        }

    def _count_nodes(self, node: TrieNode) -> int:
        """Count total nodes in the trie."""
        count = 1
        for child in node.children.values():
            count += self._count_nodes(child)
        return count

    def _max_depth(self, node: TrieNode) -> int:
        """Find maximum depth of the trie."""
        if not node.children:
            return 0

        return 1 + max(self._max_depth(child) for child in node.children.values())


def load_words_from_file(filepath: str) -> WordTrie:
    """
    Load words from a text file into a WordTrie.

    Args:
        filepath: Path to the text file containing words (one per line)

    Returns:
        WordTrie containing all words from the file

    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    trie = WordTrie()

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if word:  # Skip empty lines
                    trie.insert(word)

        print(f"Loaded {trie.word_count} words from {filepath}")
        return trie

    except FileNotFoundError:
        raise FileNotFoundError(f"Word file not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading word file: {e}")


def create_word_trie() -> WordTrie:
    """
    Create and return a WordTrie loaded with words from words_alpha.txt.

    Returns:
        WordTrie instance with loaded words
    """
    return load_words_from_file('words_alpha.txt')


if __name__ == "__main__":
    # Example usage and testing
    print("Creating word trie from words_alpha.txt...")

    try:
        trie = create_word_trie()

        # Display statistics
        stats = trie.get_stats()
        print(f"\nTrie Statistics:")
        print(f"Total words: {stats['total_words']}")
        print(f"Total nodes: {stats['total_nodes']}")
        print(f"Max depth: {stats['max_depth']}")

        print(f"\nWords by length:")
        for length, count in stats['words_by_length'].items():
            if count > 0:
                print(f"  {length} letters: {count} words")

        # Example searches
        print(f"\nExample searches:")
        print(f"'HELLO' exists: {trie.search('HELLO')}")
        print(f"'WORLD' exists: {trie.search('WORLD')}")
        print(f"Words starting with 'APP': {trie.get_words_with_prefix('APP')[:10]}")
        print(f"5-letter words starting with 'A': {[w for w in trie.get_words_with_prefix('A') if len(w) == 5][:10]}")
        print(f"Words matching 'H?LL?': {trie.get_words_with_pattern('H?LL?')}")

    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        print("Make sure words_alpha.txt exists in the current directory.")
