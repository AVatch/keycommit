import re


def scan_text(text, identifiers, operators, BANDWIDTH):
    """
    Identifies potential api keys in a text file
    """
    candidates = {}
    # normalize the text
    text = text.lower()
    # identify indecies of identifiers 
    for identifier, identifier_weight in identifiers.iteritems():
        matches = [m.start() for m in re.finditer(identifier, text)]
        if matches:
            candidates[identifier] = matches

    # check if assigned value is key
    print candidates
    return candidates

if __name__=="__main__":
    pass
