"""--- Day 10: Syntax Scoring ---"""
from dataclasses import dataclass
from pathlib import Path

from aoc import log
from aoc import open_utf8


# The score for each symbol type
ERROR_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
# Easier to reverse the below symbols and obtain directly from parent
REPAIR_SCORE = {"(": 1, "[": 2, "{": 3, "<": 4}


@dataclass
class ChunkTreeNode:
    """A linked node in the AST."""

    parent: object  # Link to the parent Chunk, None for root.
    symbol: str = None  # The type of operation of the node.
    # List of links to the children nodes.
    error_point: bool = False  # If the next node is syntax fault


def repair_branch(current_node: ChunkTreeNode) -> (ChunkTreeNode, int):
    """Adds missing nodes from the tree to complete the branch.

    :param current_node: The current node for parsing of the tree.
    :return: (The root node, autocomplete score)
    """
    auto_complete = 0  # track the autocomplete score
    # Return to the root node
    while current_node.symbol and current_node.parent is not None:
        auto_complete = (auto_complete * 5) + REPAIR_SCORE[current_node.symbol]
        current_node = current_node.parent
    return current_node, auto_complete


def __add_tree_symbol(current_node: ChunkTreeNode, symbol: str):
    """Steps up or down the tree based on the next symbol.

    :param current_node: The current node for parsing of the tree.
    :param symbol: The next char symbol to add to the tree.
    :return: The next node, or the current node with an error.
    """
    if closing_symbol := __decode_symbol(symbol):
        # The problem expects failures of this type
        if current_node.symbol != closing_symbol:
            log.debug(
                "Line error: Found closing symbol for '%s' "
                "at when closing symbol for '%s' expected.",
                closing_symbol,
                current_node.symbol,
            )
            current_node.error_point = True
            return current_node
        log.debug(
            "Closing node with '%s' and stepping back to parent.",
            symbol,
        )
        return current_node.parent
    # branching a new node
    log.debug(
        "Branching a new node from %s",
        symbol,
    )
    new_node = ChunkTreeNode(current_node, symbol=symbol)
    return new_node


def __decode_symbol(symbol: str):
    """Takes in a symbol and determines what to do with it.

    :param symbol: Single char symbol.
    :return: None if branch is continuing, else closing symbol.
    """
    if symbol in ("(", "[", "{", "<"):
        return None  # Branching a new node
    # closing parent nodes, use opening symbol for comparisons.
    if symbol == ")":
        return "("
    if symbol == "]":
        return "["
    if symbol == "}":
        return "{"
    if symbol == ">":
        return "<"
    raise ValueError(f"Mate, I dunno what to do with `{symbol}`.")


def parse_data(dataset_path: Path):
    """Loads the input data into an abstract syntax tree.

    :param dataset_path: Path to the navigation chunks dataset.
    :return:
    """
    syntax_score = 0
    errors = 0
    auto_complete_scores = []
    with open_utf8(dataset_path) as file:
        for line_index, line in enumerate(file):
            line = line.strip()
            if len(line.strip()) > 0:
                log.debug("Starting new branch on line %d", line_index)
                tree_root = ChunkTreeNode(None)
                current_node = tree_root
                for char in line:
                    # Iterate through the symbols and build the tree
                    current_node = __add_tree_symbol(current_node, char)
                    if current_node.error_point:
                        errors += 1
                        syntax_score += ERROR_SCORE[char]
                        break  # We drop errored lines.
                # branch is only syntactically complete if we return to root.
                if not current_node.error_point and current_node.symbol:
                    current_node, auto_complete = repair_branch(current_node)
                    auto_complete_scores.append(auto_complete)
    auto_complete_scores = sorted(auto_complete_scores)
    log.info(
        "Found %d rows with syntax errors for a score of %d.",
        errors,
        syntax_score,
    )
    log.info(
        "Autocompleted %d row with the middle score being %d.",
        len(auto_complete_scores),
        auto_complete_scores[len(auto_complete_scores) // 2],
    )
    return syntax_score, auto_complete_scores[len(auto_complete_scores) // 2]
