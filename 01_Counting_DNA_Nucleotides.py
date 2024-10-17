with open('data/rosalind_dna.txt', 'r') as file:
    text = file.read()
print(text.count('A'), text.count('C'), text.count('G'), text.count('T'))
# You can find all solutions in https://github.com/Mylinear/Rosalind