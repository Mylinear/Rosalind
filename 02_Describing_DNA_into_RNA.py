from Bio.Seq import Seq

with open('data/rosalind_rna.txt', 'r') as file:
    text = file.read()
# print(text.replace('T', 'U')) # This is the easy way to solve the problem

# Using Biopython
dna_sequence = Seq(text)
rna_sequence = dna_sequence.transcribe()
print(rna_sequence)
# You can find solutions in easy way in https://github.com/Mylinear/Rosalind