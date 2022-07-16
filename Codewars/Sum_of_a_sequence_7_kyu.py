def sequence_sum(begin_number, end_number, step):
    seq_sum = 0
    for n in range(begin_number, end_number + 1, step):
        seq_sum +=  n
    return seq_sum

print(sequence_sum(2, 6, 2))    