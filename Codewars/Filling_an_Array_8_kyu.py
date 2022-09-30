def arr(n=None) -> list: 
    return [i for i in range(n)] if isinstance(n, int) else []
