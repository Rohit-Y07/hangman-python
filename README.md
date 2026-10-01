# Hangman in Python

A command-line word game from CSCI 180, Fall 2024 at McNeese State University.

## Features

- Random word selection from the supplied `words.txt` file.
- Guess validation and repeated-guess handling.
- Tracking revealed letters and remaining guesses.
- Hints that match the revealed word pattern against the dictionary.
- Scoring based on remaining guesses and unique letters.

## Run locally

Python 3 is required. No third-party packages are needed. From the repository directory:

```sh
python Hangman1.py
```

Keep `words.txt` in the same working directory. Follow the terminal prompts to play.

## What I practiced

Functions, strings, collections, file input, and translating game rules into program state. A next improvement would be making hints exclude words containing letters already guessed incorrectly.

## Context and credits

Coursework by **Rohit Kumar Yadav and Prince Gupta**, developed with AI assistance. The dictionary is supplied project data, not a dataset I created. Original source credits are retained.

[Portfolio](https://rohit-yadav-portfolio.web.app/)
