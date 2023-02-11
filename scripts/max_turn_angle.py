#!/usr/bin/env python3

from math import atan, tau # because 2pi is stupid
from sys import argv

def max_turn_angle(w: float, s: float) -> float:
    return atan(2*s*w)

if __name__ == "__main__":
    try:
        width = float(argv[1])
        space = float(argv[2])
        res: float = 0.0

        argv[3] = argv[3] if len(argv) == 4 else ""
        if argv[3] == "deg":
            res = max_turn_angle(width, space)*360/tau
        else:
            res = max_turn_angle(width, space)

        print(res)

    except ValueError:
        print("One of the arguments wasn't a number!")
    except IndexError:
        print("2 arguments needed: width of wagon, space between wagons")
