def rps(p1: str, p2: str) -> str:
        
    rock_paper_scissors = { 
                            ('rock', 'rock'): 'Draw!',
                            ('rock', 'paper'): 'Player 2 won!',
                            ('rock', 'scissors'): 'Player 1 won!',
                            ('paper', 'rock'): 'Player 1 won!',
                            ('paper', 'paper'): 'Draw!',
                            ('paper', 'scissors'): 'Player 2 won!',
                            ('scissors', 'rock'): 'Player 2 won!',
                            ('scissors', 'paper'): 'Player 1 won!',
                            ('scissors', 'scissors'): 'Draw!'
                            }
    
    return rock_paper_scissors[(p1, p2)]