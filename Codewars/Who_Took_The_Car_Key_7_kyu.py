from typing import List

def who_took_the_car_key(message: List[str]) -> str:
    return "".join([chr(int(i, 2)) for i in message])


