#!/usr/bin/env python3
"""
Extract kept words from a cull-words.py state file.
Outputs the kept words to a text file (one per line).
"""

import sys
import json

def extract_kept_words(state_file, output_file):
    """Read state file and write kept words to output file."""
    try:
        with open(state_file, 'r') as f:
            state = json.load(f)

        kept = state.get('kept', [])
        discarded = state.get('discarded', [])

        with open(output_file, 'w') as f:
            for word in kept:
                f.write(word + '\n')

        print(f"Extracted {len(kept)} kept words to {output_file}")
        print(f"(Discarded {len(discarded)} words)")

    except FileNotFoundError:
        print(f"Error: Could not find state file '{state_file}'")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{state_file}' is not a valid JSON file")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 extract-kept-words.py <state_file> <output_file>")
        sys.exit(1)

    state_file = sys.argv[1]
    output_file = sys.argv[2]

    extract_kept_words(state_file, output_file)

if __name__ == "__main__":
    main()
