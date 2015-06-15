import sys
from parser.reader import load_csv
from parser.parser import scan_text

BANDWIDTH = 5

def init():
    # read in the commited snippet
    commit = sys.argv[1]

    # load the dependency files
    identifiers = load_csv("data/identifiers.csv")
    assignment_operators = load_csv("data/assignment_operators.csv")
    flags = load_csv("data/flags.csv")

    # pass commited snippet with data
    # to parser
    candidates = scan_text(commit,
                           identifiers,
                           assignment_operators,
                           flags,
                           BANDWIDTH)


    # validate candidates
    print "*"*50
    for k in candidates:
        if candidates[k]["is_key"]:
            print candidates[k]
            print "KeyCommit has detected the following potential keys in your commit."
            print "Index:\tSnippet:"
            print "-"*50
            print candidates[k]['indecies'][0], "\t", candidates[k]['snippet']

            decision = raw_input("Would you like to continue? Y/N: ")
            print decision

if __name__=="__main__":
    init()