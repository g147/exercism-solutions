def distance(seq1, seq2):
    if len(seq1)!=len(seq2):
        raise ValueError(".+")
    return sum(1 for a, b in zip(seq1, seq2) if a != b)
