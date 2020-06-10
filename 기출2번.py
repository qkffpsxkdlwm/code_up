import sys
sys.setrecursionlimit(2000)

def calculate_recursive(n,m) :
    if n == 0 or m == 0:
        return 1
    else:
        return calculate_recursive(n-1,m)+calculate_recursive(n,m-1)


N,M,K = map(int,input().split())
i1 = (K - 1) // M;
j1 = ((K - 1) % M);
i2 = N - i1 - 1;
j2 = M - ((K - 1) % M) - 1;
print(calculate_recursive(i1,j1) * calculate_recursive(i2,j2))