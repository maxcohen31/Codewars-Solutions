def is_valid_walk(walk):
    go_north, go_west = walk.count('n'), walk.count('w')
    go_south, go_east = walk.count('s'), walk.count('e')
    if len(walk) == 10:
        return go_north - go_south == 0 and go_west - go_east == 0
    else:
        return False
     
     
