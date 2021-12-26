"""--- Day 21: Dirac Dice ---"""
from dataclasses import dataclass
from pathlib import Path

from aoc import open_utf8


@dataclass
class Game:
    """Object to store the state of the game(s) for a point in time."""

    turn: int
    position1: int
    position2: int
    score1: int = 0
    score2: int = 0
    universes: int = 1

    def identity(self) -> str:
        """Returns a 'unique-ish' string identity for the game.

        Turn is always identical as we dispose of these every two turns.
        """
        return f"{self.position1},{self.position2},{self.score1},{self.score2}"


# All these variables are required + I don't want to stack a further function.
# pylint: disable=R0914
def __have_turns(game: Game, die: dict, limit: int, wins: list, next_games: {}):
    """Completes a turn on player one and a turn on player two and updates the
    universe state.

    :param game: Current game to complete the turn on.
    :param die: The dice being used.
    :param limit: Score after which the game is complete.
    :param wins: List tracking the universes wins on player one and player two.
    :param next_games: Dictionary for inplace update of additional games states to resolve.
    :return:
    """
    for roll_total_t1, universes_t1 in die.items():
        # even turn for player 1
        position1 = (game.position1 + roll_total_t1 - 1) % 10 + 1
        score1 = game.score1 + position1
        # Current universes multiplied by combinations that would produce this roll
        universes1 = game.universes * universes_t1
        if score1 >= limit:
            wins[0] += universes1  # P1 just won in this many inverses
            continue
        # odd turn for player 2
        for roll_total_t2, universes_t2 in die.items():
            position2 = (game.position2 + roll_total_t2 - 1) % 10 + 1
            score2 = game.score2 + position2
            universes2 = universes1 * universes_t2  # The data from p1 is for n-1 turn
            if score2 >= limit:
                wins[1] += universes2
                continue
            new_game = Game(  # Create a new game to continue this branch
                game.turn + 2,
                position1,
                position2,
                score1,
                score2,
                universes2,
            )
            if new_game.identity() not in next_games:  # stage a new game.
                next_games[new_game.identity()] = new_game
            else:  # Faster to treat these as the same rather than stage new games.
                next_games[new_game.identity()].universes += new_game.universes


def simulate_game(initial_game: Game, limit: int):
    """Starts the game and computes the distruption in the universe.

    :param initial_game: The starting game conditions.
    :param limit: The integer score after which the game has been won.
    :return:
    """
    games = {initial_game.identity(): initial_game}
    wins = [0, 0]
    die = dirac_dice()
    while len(games) > 0:
        next_games = {}
        for _, game in games.items():
            __have_turns(game, die, limit, wins, next_games)
        games = next_games
        print(len(next_games))
    print(wins)
    return max(wins)


def dirac_dice() -> {}:
    """Possible outcomes and how many universe states have that outcome."""
    die = {}
    faces = [1, 2, 3]
    for r1 in faces:
        for r2 in faces:
            for r3 in faces:
                if r1 + r2 + r3 not in die:
                    die[r1 + r2 + r3] = 1
                else:
                    die[r1 + r2 + r3] += 1
    return die


def load_dataset(dataset_path: Path):
    """Returns starting position between 0 and 9."""
    with open_utf8(dataset_path) as file:
        starting = [
            int(line.split(":")[1].strip()) for line in file if len(line.strip()) > 0
        ]
        return Game(0, starting[0], starting[1])
