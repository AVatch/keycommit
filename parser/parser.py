import re


def scan_text(text, identifiers, operators, flags, BANDWIDTH):
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
            candidates[identifier] = {}
            candidates[identifier]['operators'] = {}
            candidates[identifier]['snippet'] = ''
            candidates[identifier]['is_key'] = False
            candidates[identifier]['indecies'] = matches

    # check if assignment operator is present
    for identifier, properties in candidates.iteritems():
        for i in properties['indecies']:
            span = text[i+len(identifier):i+len(identifier)+BANDWIDTH]
            for operator in operators:
                matches = [m.start() for m in re.finditer(operator, span)]
                if matches:
                    candidates[identifier]['operators'][operator] = matches
                    # check if value is key
                    for j in matches:
                        span = text[i+len(identifier)+j+len(operator):
                            i+len(identifier)+BANDWIDTH+j+len(operator)]
                        candidates[identifier]['is_key'] = is_key(span, flags)
    return candidates

def is_key(s, flags):
    for f in flags:
        matches = [m.start() for m in re.finditer(f, s)]
        if not matches:
            return True
    return False

if __name__=="__main__":
    pass
