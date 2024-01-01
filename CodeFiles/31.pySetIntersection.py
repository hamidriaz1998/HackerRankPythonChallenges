# Challenge Link: https://www.hackerrank.com/challenges/py-set-intersection-operation

n = int(input())
n = set(map(int, input().split()))
b = int(input())
b = set(map(int, input().split()))

print(len(n.intersection(b)))