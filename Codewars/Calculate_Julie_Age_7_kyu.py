def age(x: int, y: int) -> int:
    """
        Julie = brother + x
        Julie = brother * y
        
        Julie = (x / (y - 1)) + x
    """
    
    return round((x / (y - 1)) + x)
