# For simple and easy solutions, visit https://github.com/Mylinear/Rosalind

dna_seq = 'GATATATGCATATACTT'
motif = 'ATAT'

def find_motif(dna_seq, motif):
    positions = []
    for i in range(len(dna_seq)):
        if dna_seq[i:i+len(motif)] == motif:
            positions.append(i+1)
    return positions
result = find_motif(dna_seq, motif)
print(*result)