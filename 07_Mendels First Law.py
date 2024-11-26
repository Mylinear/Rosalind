k = 17
m = 23
n = 18
total = k + m + n

def k_and_k(k):
    return k/total * ((k-1)/ (total-1)) 

def k_and_m(k,m):
    return k/total * (m/ (total-1)) * 2

def k_and_n(k,n):
    return k/total * (n/ (total-1)) * 2

def m_and_m(m):
    return m/total * ((m -1)/ (total-1)) * .75 

def m_and_n(m,n):
    return m/total * (n/ (total-1)) * 2 *.5

def result(k,m,n):
    return k_and_k(k) + k_and_m(k,m) + k_and_n(k,n) + m_and_m(m) + m_and_n(m,n)

print(round(result(k,m,n),5))

# For simple and easy solutions, visit https://github.com/Mylinear/Rosalind