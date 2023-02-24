def nickname_generator(name: str) -> str:
    if len(name) < 4:
        return "Error: Name too short"
    elif name[2] not in "aeiou":
        return name[0:3]
    else:
        return name[0:4]

x = "Samantha"
y = "Jeannie"
print(nickname_generator(y))