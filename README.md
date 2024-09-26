# Pasur Card Game
#### Video Demo:  <[URL HERE](https://aparat.com/v/lxg2u3a)>
**Pasur** or **chahar barg** (Persian: پاسور; also spelled **Pasour** or **Pasur**) is a fishing card game of Persian origin. Played widely in Iran, it is played similarly to the Italian games of Cassino or Scopa and even more similarly to the Egyptian game of Bastra. Pasur is also known by the names *Chahâr Barg* (4 cards), *Haft Khâj* (seven clubs) or *Haft Va Chahâr*, *Yâzdah* (7+4=11, the significance being that players want to win 7 clubs in a game of 4-card hands where 11 is a winning number).

## Table of Contents

- [Game Rules](#game-rules)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [How the Game Works](#how-the-game-works)
- [Scoring System](#scoring-system)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Game Rules

- **Objective**: Capture cards from the table by playing a card from your hand that either matches in rank or sums to 11 with cards on the table.
- **Capture by Rank**: Kings capture Kings, Queens capture Queens, and Jacks capture all cards except Kings and Queens.
- **Capture by Sum**: Any combination of cards that sum to 11 with the card played can be captured.
- **Scoring**:
  - 2♣: 2 points
  - 10♦: 3 points
  - Most Clubs (7 or more): 7 points
  - Each Ace: 1 point
  - Each Jack: 1 point
  - Each Pasur (Sur): 5 points (a Sur is when a player clears the table)

## How to Play

1. The game starts by shuffling the deck and dealing 4 cards each to the player, the computer, and the table.
2. Players take turns playing a card and trying to capture cards from the table.
3. If a capture is not possible, the played card remains on the table.
4. Once all cards are played, new cards are dealt if there are any left in the deck.
5. The game continues until all cards from the deck have been played and captured.
6. The final score is calculated based on the cards captured and Surs made.

## Installation

### Prerequisites
- Python 3.x
- External libraries are [listed](requirements.txt).
  ```bash
  pip install termcolor
  pip install pytest
  pip install pyfiglet

### Cloning the repository

```bash
git clone https://github.com/montajebii/Pasur.git
cd Pasur
```

### Running the game

To start the game, simply run:

```bash
python project.py
```

### Example Gameplay

```
--- Pasur Game Starts ---

Player's turn
Table cards: A♠, 2♦, 3♣, 4♥
Your cards: 5♠, 6♦, 7♣, 8♥

Select a card to play (1-4): 2

Captured: 7♣
No capture possible.
```

## Running Tests

To run tests, use the Pytest framework. Install Pytest if you don’t have it:

```bash
pip install pytest
```

Then run the tests with:

```bash
pytest test_project.py
```

## Project Structure

```
.
├── project.py           # Main game file
├── test_project.py      # Test cases for the project
└── README.md            # This readme file
```

## How the Game Works

- **deal_cards**: Deals a specific number of cards from the deck.
- **player_turn**: Handles the player's move, including input and capturing logic.
- **computer_turn**: Handles the computer's move using a simple AI to decide whether to capture cards or place one on the table.
- **capture_possible**: Determines whether the played card can capture any cards from the table based on the game rules.
- **find_sum_to_11**: Finds cards that sum to 11 when combined with the played card.
- **calculate_score**: Calculates the final score based on captured cards and Surs.

## Scoring System
The following points are awarded based on captures:

2♣ (Two of Clubs): 2 points
10♦ (Ten of Diamonds): 3 points
7 or more ♣ (Clubs): 7 points
Each Ace (A): 1 point
Each Jack (J): 1 point
Each Sur (clearing the table): 5 points
At the end of the game, the player and computer's points are compared, and the winner is declared.

## Future Improvements
These following future improvements will be soon available on [Pasur](https://github.com/montajebii/Pasur)
- The game has 2 minor Bugs:
  - When the table if full of under 11 ranked cards, and You play a J, It counts you a Sur which it shouldn't
  - When table cards are "7♣, 8♠, 2♠, 7♥" and computer plays 4♠ it captures both 7s on the table which it shouldn't
- Add graphical interface for better user experience.
- Implement more advanced AI for the computer's turn.
- Add multiplayer mode for two players.

## Contributing
Contributions are welcome! If you'd like to improve this project, please feel free to fork the repository and submit a pull request.

## License

This project is open-sourced under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
