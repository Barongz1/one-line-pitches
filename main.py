"""A Day of One-Line Pitches — entry for make.fun.

Writes one sentence to /output/entry.txt.
The sentence is one pitch, under 240 characters, for a friend who has never coded.
"""
import os

LINE = "You describe your idea in plain words, an AI agent builds your first app on make.fun, and you watch it work — no code, no jargon, just your idea coming alive."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
