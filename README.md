# TerminalGoFish

A command-line version of the classic card game Go Fish, implemented in Python.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Game Rules](#game-rules)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Introduction

**TerminalGoFish** is a simple, text-based implementation of the classic card game Go Fish. Play against the computer in your terminal and enjoy a nostalgic game experience.

## Features

- Play against a computer opponent
- Follows standard Go Fish rules
- Simple and intuitive command-line interface

## Installation

### Prerequisites

- Python 3.x

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/BBelcher9/Terminal_Go_Fish.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Terminal_Go_Fish
    ```

## Usage

Run the game by executing the Python script:
```bash
python go_fish.py

## Game Rules

1. The game starts with each player being dealt 7 cards.
2. Players take turns asking their opponent for a specific rank of card.
3. If the opponent has cards of the requested rank, they must give them all to the player.
4. If the opponent does not have any cards of the requested rank, the player must "go fish" by drawing a card from the deck.
5. The game continues until all 13 sets of four cards are collected.
6. The player with the most sets of four cards wins.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.