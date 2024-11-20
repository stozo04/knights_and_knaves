from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentence0 = And(
    Or(AKnight, AKnave),  # Either A is a Knight OR a Knave
    Not(And(AKnight, AKnave)),  # A can not be a knight AND a knave
    # if A is a knight: If A is a knight, their statement must be true, If A is a knave, their statement must be false
    Biconditional(AKnight, And(AKnight, AKnave))
)
# print(sentence0.formula())


knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence1 = And(
    Or(AKnight, AKnave),  # A is a Knight OR a Knave
    Or(BKnight, BKnave),  # B is a Knight OR a Knave
    Not(And(AKnight, AKnave)),  # A can not be a knight AND a knave
    Not(And(BKnight, BKnave)),  # B can not be a knight AND a knave
    # If A is a knight, then "we are both knaves" must be true
    Biconditional(AKnight, And(AKnave, BKnave))
)
# print(sentence1.formula())

knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence2 = And(
    Or(AKnight, AKnave),  # A is a Knight OR a Knave
    Or(BKnight, BKnave),  # B is a Knight OR a Knave
    Not(And(AKnight, AKnave)),  # A can not be a knight AND a knave
    Not(And(BKnight, BKnave)),  # B can not be a knight AND a knave
    # If A is a knight, then "We are the same kind." Either both Knights OR both Knaves
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If B is a knight, then "We are of different kinds." Either B is a knight and A is knave OR B is a knave and A is a knight
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)
# print(sentence2.formula())

knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

sentence3 = And(
    # Each character must be knight or knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # No character can be both
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    # A says either "I am a knight" or "I am a knave"
    Biconditional(AKnight, Or(AKnight, AKnave)),
    # B says "A said 'I am a knave'"
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    # B says "C is a knave"
    Biconditional(BKnight, CKnave),
    # C says "A is a knight"
    Biconditional(CKnight, AKnight)
)
# print(sentence3.formula())

knowledge3 = And(
    # Each character must be knight or knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # No character can be both
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    # A says either "I am a knight" or "I am a knave"
    Biconditional(AKnight, Or(AKnight, AKnave)),
    # B says "A said 'I am a knave'"
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    # B says "C is a knave"
    Biconditional(BKnight, CKnave),
    # C says "A is a knight"
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(f"puzzle: {puzzle}")
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
