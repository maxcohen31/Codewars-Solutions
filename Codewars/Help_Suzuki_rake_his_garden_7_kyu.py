def rake_garden(garden: str) -> str:
    gard = garden.split()
    result = []

    for word in gard:
        if word not in ["rock", "gravel"]:
            word = "gravel"
        result.append(word)
    return " ".join(result)


