"""
parser.py: Module for parsing formulas into functions
"""

from math import *
from drawer.tokens import ALIASES


def parse_formula(expr: str):
    """
    Parse given formula and return corresponding function.
    Currently supports only one variable named "x".
    If formula has any functions, all arguments must be in braces (e.g. log(x, 2))

    :param expr: formula to parse
    :return: lambda function with argument x as input and value calculated by formula as return value
    """
    # if re.fullmatch(".*(\w{7,}|[:;]).*", expr.replace(" ", "")):
    #     raise AttributeError("Wrong formula: " + expr)
    expr = _replace_entities(expr)
    return lambda x: eval(expr)


def _replace_entities(expr: str) -> str:
    expr = expr.lower().replace("^", "**")
    tokens = []
    buffer = ""
    for ch in expr:
        if ch.isalpha() or ch.isdecimal():
            # buffer should contain only letters or only digits
            assert len(buffer) == 0 or ch.isalpha() == buffer[-1].isalpha()

            buffer += ch

        else:
            if buffer in ALIASES:
                buffer = ALIASES[buffer]

            if buffer:
                tokens.append(buffer)
                buffer = ""

            if ch == "!":
                _add_factorial(tokens)
            else:
                tokens.append(ch)

    if buffer:
        tokens.append(buffer)

    return "".join(tokens)


def _add_factorial(tokens: list):
    # TODO: empty tokens exception
    # 2 + 27! | 2 + 27
    insert_index = -1
    if tokens[-1] == ")":
        insert_index = _find_opening_bracket_index(tokens, len(tokens) - 1)

    tokens.insert(insert_index, "factorial")
    tokens.insert(insert_index, "(")
    tokens.append(")")


def _find_opening_bracket_index(tokens: list, cl_bracket_index: int) -> int:
    assert tokens[cl_bracket_index] == ")"

    token_ptr = cl_bracket_index - 1
    prev_token = tokens[token_ptr]
    balance = 1
    while balance != 0:
        if prev_token == ")":
            balance += 1
        elif prev_token == "(":
            balance -= 1
        token_ptr -= 1
        prev_token = tokens[token_ptr] if token_ptr >= 0 else None
    return token_ptr + 1
