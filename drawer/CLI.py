"""
CLI.py: main module for running a program
"""


import re
from math import *
from drawer.plotdrawer import *
from drawer.parser import *
from drawer.tokens import TOKENS, ALIASES


def print_debug(msg) -> None:
    if "--debug" in sys.argv:
        print(msg)


def read_xs() -> list:
    xs = None
    while not xs:
        try:
            min_x = float(input("Enter minimum x value: "))
            max_x = float(input("Enter maximum x value: "))

        except ValueError as e:
            # print_debug(e)
            print("Wrong argument: " + str(e).split(": ")[-1] + "\n")
            continue

        while True:
            try:
                precision = float(input("Enter precision (1 by default, must be power of 10): "))
            except ValueError as e:
                print("Wrong argument: " + str(e).split(": ")[-1] + "\n")
                continue

            if precision == "":
                break
            else:
                if not _is_power_of_ten(precision):
                    print("Not a power of ten!")
                    continue
                if max_x - min_x < precision:
                    print("Too small precision, try reduce the number")
                    continue
                break

        if precision:
            xs = get_xs(min_x, max_x, precision)
        else:
            xs = get_xs(min_x, max_x)
    return xs


def _is_power_of_ten(n: float) -> bool:
    return log10(float(n)) == int(log10(float(n)))


def read_ys(xs: list) -> list:
    ys = None
    while not ys:
        formula = input("Enter formula: ")
        parsed_formula = parse_formula(formula)
        try:
            ys = get_ys(xs, parsed_formula)
        except NameError as e:
            # print_debug(formula + "\n" + str(e))
            print("Wrong formula: " + formula + " ({})".format(str(e)))
    return ys


def main():
    print("Welcome to plot drawer!", end=" ")

    xs = ys = None
    while True:
        op = input(OP_MESSAGE + ">> ")
        if op == "0":
            if xs and ys:
                draw_plot(xs, ys, filename=None,
                          title="Title", xlabel="x", ylabel="y", legend="line")
                break
            else:
                print("Points are not set yet. Type 1 to set them.")
                continue

        elif op == "1":
            xs = read_xs()
            ys = read_ys(xs)

        elif op == "2":
            print("Unsupported yet, sorry")

        else:
            print("Wrong operation: " + op)


if __name__ == "__main__":
    OP_MESSAGE = """\nType:
0 to draw a plot
1 to set points
2 to show appearance settings (unsupported yet)
"""
    main()
