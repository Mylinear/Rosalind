from Bio.Seq import Seq

with open('data/rosalind_revc.txt', 'r') as file:
    text = file.read()

dna_sequence = Seq(text)
reverse_complement = dna_sequence.reverse_complement()
print(reverse_complement)

# You can find solutions in easy way in https://github.com/Mylinear/Rosalind