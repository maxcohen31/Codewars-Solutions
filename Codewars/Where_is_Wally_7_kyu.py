import re
def wheres_wally(string):
    wally = re.match(r'(^|.*[\s])(Wally)([\.\,\s\']|$)', string)
    return wally.start(2) if wally else -1