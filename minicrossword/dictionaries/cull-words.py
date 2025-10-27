#!/usr/bin/env python3
"""
Interactive word culling tool.
Press 'j' to keep a word, 'k' to discard, 's' to save and quit.
Progress is saved to a state file that can be resumed later.
"""

import sys
import tty
import termios
import json
import os

def get_single_key():
    """Read a single keypress without requiring Enter."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
        # Handle special keys
        if key.lower() == 'j':
            return 'j'
        elif key.lower() == 'k':
            return 'k'
        elif key.lower() == 's':
            return 's'
        elif key == '\x03':  # Ctrl+C
            raise KeyboardInterrupt
        return key
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def cull_words(input_file, state_file):
    """Interactively filter words from input file, saving state to state_file."""

    # Load or initialize state
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            state = json.load(f)
        kept = set(state.get('kept', []))
        discarded = set(state.get('discarded', []))
        print(f"Resuming from saved state: {len(kept)} kept, {len(discarded)} discarded")
    else:
        kept = set()
        discarded = set()

    try:
        with open(input_file, 'r') as f:
            words = [line.strip() for line in f if line.strip()]

        # Filter out already reviewed words
        reviewed = kept | discarded
        remaining = [w for w in words if w not in reviewed]

        print(f"Loaded {len(words)} words from {input_file}")
        print(f"Remaining to review: {len(remaining)}")
        print("Press 'j' to keep, 'k' to discard, 's' to save and quit\n")

        for i, word in enumerate(remaining):
            total_reviewed = len(kept) + len(discarded)
            print(f"[{total_reviewed + 1}/{len(words)}] {word}", end='', flush=True)

            key = get_single_key()

            if key == 'j':
                kept.add(word)
                print(" ✓ KEPT")
            elif key == 'k':
                discarded.add(word)
                print(" ✗ DISCARDED")
            elif key == 's':
                print("\n\nSaving and quitting...")
                break
            else:
                # Unknown key, ask again
                print(f" (unknown key, try again)", end='\r', flush=True)
                continue

        # Save state
        state = {
            'kept': sorted(list(kept)),
            'discarded': sorted(list(discarded))
        }
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)

        total = len(kept) + len(discarded)
        print(f"\nSaved state: {len(kept)} kept, {len(discarded)} discarded ({total}/{len(words)} reviewed)")

    except KeyboardInterrupt:
        print("\n\nInterrupted! Saving progress...")
        state = {
            'kept': sorted(list(kept)),
            'discarded': sorted(list(discarded))
        }
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)
        total = len(kept) + len(discarded)
        print(f"Saved state: {len(kept)} kept, {len(discarded)} discarded ({total}/{len(words)} reviewed)")
    except FileNotFoundError:
        print(f"Error: Could not find file '{input_file}'")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 cull-words.py <input_file> <state_file>")
        print("\nThe state file (JSON) tracks kept/discarded words and allows resuming.")
        sys.exit(1)

    input_file = sys.argv[1]
    state_file = sys.argv[2]

    cull_words(input_file, state_file)

if __name__ == "__main__":
    main()
