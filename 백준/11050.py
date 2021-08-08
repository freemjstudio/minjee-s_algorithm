N, K = map(int, input().split())

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

print(factorial(N)//(factorial(K)*factorial(N-K)))