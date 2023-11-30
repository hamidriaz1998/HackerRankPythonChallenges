# Challenge Link: https://www.hackerrank.com/challenges/py-set-difference-operation

n = int(input())
n = set(map(int, input().split()))
b = int(input())
b = set(map(int, input().split()))

print(len(n.difference(b)))