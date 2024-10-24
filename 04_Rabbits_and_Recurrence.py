# For simple and easy solutions, visit https://github.com/Mylinear/Rosalind
def total_rabbits(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return total_rabbits(n-1, k) + k * total_rabbits(n-2, k)

n = 31 # number of months
k = 5 # number of offspring per pair
print(total_rabbits(n, k))