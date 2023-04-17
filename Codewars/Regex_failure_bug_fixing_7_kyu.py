from re import sub, IGNORECASE

def filter_words(phrase):
    return sub("(?i)(bad|mean|ugly|horrible|hideous)", "awesome", phrase)

def filter_words2(phrase):
    return sub("(bad|mean|ugly|horrible|hideous)", "awesome", phrase, flags=IGNORECASE)


print(filter_words2("you're MEAN timmy!"))