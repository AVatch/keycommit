import fileinput

from parser.reader import load_csv
from parser.parser import scan_text


def init():
    # read in the commited snippet
    commit = ""
    for line in fileinput.input():
        commit += line

    # load the dependency files
    assignment_operators = load_csv("data/assignment_operators.csv")
    identifiers = load_csv("data/identifiers.csv")

    # pass commited snippet with data
    # to parser


    # validate candidates


if __name__=="__main__":
    init()