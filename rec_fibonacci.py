# returns nth fib number
def rec_fib(n):
    if n == 0 or n == 1:
        return n
    
    return rec_fib(n - 1) + rec_fib(n - 2)

def memo_fib(n):
    memo = [0, 1]
    while len(memo) <= n:
        memo.append(memo[-2] + memo[-1])

    return memo[n]

def main():
    print(memo_fib(6))

if __name__ == '__main__':
    main()