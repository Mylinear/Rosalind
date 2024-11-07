from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

file_path = "data/rosalind_gc.txt"

result = {}
with open (file_path, "r") as file:
    for record in SeqIO.parse(file, "fasta"):
        gc_content = gc_fraction(record.seq)
        result[record.id] = gc_content
        print(f"{record.id} {gc_content}")

max_gc_id = max(result, key=result.get)
print(f"{max_gc_id}\n{round(100 * result[max_gc_id],6)}")

# For simple and easy solutions, visit https://github.com/Mylinear/Rosalind
