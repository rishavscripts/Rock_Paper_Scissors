# Rock Paper Scissors Game

This is a simple Rock-Paper-Scissors game implemented in Python. The user plays against the computer, which makes a random choice.

## How to Play
1. Run the script in a Python environment.
2. Choose one of the following options by entering the corresponding number:
   - `0` for 🪨 (Rock)
   - `1` for 📄 (Paper)
   - `2` for ✂️ (Scissors)
3. The computer randomly selects its choice.
4. The game determines the winner based on the standard Rock-Paper-Scissors rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - Identical choices result in a draw

## Installation
Make sure you have Python installed on your system. To run the game, simply execute the script using:
```sh
python rock_paper_scissors.py
```

## Example Gameplay
```
Choose 0 for 🪨   choose 1 for 📄   choose 2 for ✂️.
Enter your choice: 1
You chose 📄.
Computer chose ✂️.
You lose.
```

## Known Issues
- The current logic has an issue where `cc > uc` determines a loss, which is not always accurate.
- Edge cases (Rock vs. Scissors) are not handled correctly in the conditions.

## Future Improvements
- Fix incorrect win/loss conditions.
- Add input validation to handle non-integer inputs.
- Implement a score-tracking system.
- Allow multiple rounds of play with an exit option.

## License
This project is open-source and available for use under the MIT License.

## Contributions
Feel free to fork the repository and submit pull requests for improvements!

