import random

def roll_dice():
    """Simulate rolling a fair six-sided dice."""
    return random.randint(1, 6)

def play_game():
    """Play the dice rolling game."""
    num_rolls = 6
    count_5_or_6 = 0

    for i in range(1, num_rolls + 1):
        result = roll_dice()
        print("Roll", i, ":", result)
        if result in (5, 6):
            count_5_or_6 += 1

    if count_5_or_6 >= 2:
        print("Congratulations! You won the game.")
        return True
    else:
        print("Sorry, you lost the game.")
        return False

def main():
    print("Welcome to the Dice Rolling Game!")
    num_games = 100
    wins = 0
    losses = 0

    for _ in range(num_games):
        if play_game():
            wins += 1
        else:
            losses += 1

    print("\nOut of", num_games, "games:")
    print("Wins:", wins)
    print("Losses:", losses)

if __name__ == "__main__":
    main()
