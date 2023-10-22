class Pell:
    def get(self, n: int) -> int:
        if n <= 2:
            return n
        
        first = 1
        sec = 2
        
        for _ in range(3, n+1):
            pll = 2 * sec + first
            first = sec
            sec = pll
        return sec
