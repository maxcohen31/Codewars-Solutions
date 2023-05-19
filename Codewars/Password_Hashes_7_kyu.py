from hashlib import md5

def pass_hash(s: str) -> str:
    return md5(s.encode()).hexdigest()


if __name__ == "__main__":
    print(pass_hash("abc123"))