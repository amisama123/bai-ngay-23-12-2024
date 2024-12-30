def giaithua(n):
    gt=1
    for i in range (1,n+1):
        gt=gt*i
    return gt
def A(n,k):
    return giaithua(n)/giaithua(n-k)
def C(n,k):
    return A(n,k)/giaithua(k)
print(A(5,4))
print(C(7,6))