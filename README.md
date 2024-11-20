# Knights and Knaves Puzzle Solver

This Python program solves logic puzzles inspired by Raymond Smullyan's Knights and Knaves puzzles. In these puzzles, each character is either a Knight (who always tells the truth) or a Knave (who always lies).

## Overview

The program uses propositional logic to solve four different Knights and Knaves puzzles of increasing complexity. Each puzzle involves determining whether characters are Knights or Knaves based on their statements.

## Requirements

- Python 3.x
- logic.py (provided utility file for propositional logic)

## Puzzle Descriptions

### Puzzle 0
- Single character (A)
- A says: "I am both a knight and a knave."

### Puzzle 1
- Two characters (A and B)
- A says: "We are both knaves."
- B says nothing.

### Puzzle 2
- Two characters (A and B)
- A says: "We are the same kind."
- B says: "We are of different kinds."

### Puzzle 3
- Three characters (A, B, and C)
- A says either "I am a knight." or "I am a knave." (but you don't know which)
- B says: "A said 'I am a knave'."
- B says: "C is a knave."
- C says: "A is a knight."

## Code Structure

- `puzzle.py`: Main program file containing puzzle definitions and solutions
- `logic.py`: Utility file providing propositional logic functionality

### Key Components

1. Symbol definitions for each character's possible states:
```python
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
# etc.
```

2. Knowledge bases for each puzzle (knowledge0, knowledge1, etc.)
3. Main function that checks models and prints results

## How It Works

1. Each puzzle is represented as a set of logical statements (knowledge base)
2. The program uses model checking to determine which statements must be true
3. Basic rules applied to all puzzles:
   - Each character must be either a Knight or a Knave (not both)
   - Knights always tell the truth
   - Knaves always lie

## Usage

Run the program from the command line:
```bash
python puzzle.py
```

The program will output the solution for each puzzle, indicating which characters are Knights and which are Knaves.

## Solution Format

The output will show for each puzzle which of the following are true:
- "A is a Knight"
- "A is a Knave"
- "B is a Knight"
- "B is a Knave"
- "C is a Knight"
- "C is a Knave"

## Example Output
```
puzzle: Puzzle 0
    A is a Knave

puzzle: Puzzle 1
    A is a Knave
    B is a Knight

# etc.
```

## Logic Rules

1. Basic character constraints:
   - `Or(AKnight, AKnave)`: Each character must be either a Knight or a Knave
   - `Not(And(AKnight, AKnave))`: No character can be both

2. Statement handling:
   - For a character's statement S: `Biconditional(XKnight, S)`
   - This means: "X is a Knight if and only if statement S is true"

## Troubleshooting

Common issues:
1. "Must be a logical sentence" error:
   - Ensure you're using logical symbols and operators, not Python booleans
   - Check that all statements are properly constructed using the logic library

2. No solution found:
   - Verify the logical constraints are not contradictory
   - Check that all necessary rules are included in the knowledge base

## Contributing

Feel free to extend the program with:
1. Additional puzzles
2. More complex logical relationships
3. Enhanced output formatting
4. Performance optimizations

## License

This project is open source and available for educational purposes.
