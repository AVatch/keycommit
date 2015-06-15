import fileinput

from parser.reader import load_csv
from parser.parser import scan_text

BANDWIDTH = 5

def init():
    # read in the commited snippet
    commit = ""
    for line in fileinput.input():
        commit += line

    # load the dependency files
    identifiers = load_csv("data/identifiers.csv")
    assignment_operators = load_csv("data/assignment_operators.csv")
    flags = load_csv("data/assignment_operators.csv")

    # pass commited snippet with data
    # to parser
    candidates = scan_text(commit,
                           identifiers,
                           assignment_operators,
                           flags,
                           BANDWIDTH)


    # validate candidates


if __name__=="__main__":
    init()