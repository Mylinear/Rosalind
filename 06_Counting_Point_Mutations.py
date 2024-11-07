def count_mutations(s, t):
    return sum(1 for i in range(len(s)) if s[i] != t[i])

s = "GCAAGCTAATAAAACGGCTCA"
t = "GGTAACCTGTTAATCGTTGAG"
print(count_mutations(s, t))

# For simple and easy solutions, visit https://github.com/Mylinear/Rosalind