# Challenge Link: https://www.hackerrank.com/challenges/symmetric-difference/

m = int(input())
M = input().split()
M = set(map(int, M))
n = int(input())
N = input().split()
N = set(map(int, N))

answer = set()
answer.update(M.difference(N), N.difference(M))
answer = list(answer)
answer.sort()
for i in answer:
    print(i)