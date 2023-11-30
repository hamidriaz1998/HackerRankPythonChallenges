# Challenge Link: https://www.hackerrank.com/challenges/py-set-union

n = int(input())
n = set(map(int, input().split()))
b = int(input())
b = set(map(int, input().split()))

s = n.union(b)
print(len(s))