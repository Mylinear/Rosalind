with open('data/rosalind_dna.txt', 'r') as file:
    text = file.read()
print(text.count('A'), text.count('C'), text.count('G'), text.count('T'))
# For simple and easy solutions, visit https://github.com/Mylinear/Rosalind