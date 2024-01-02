# Challenge Link: https://www.hackerrank.com/challenges/itertools-permutations

from itertools import permutations

data = input().split()
string, k = data
k = int(k)

result = list(permutations(string, k))
result = list(map(lambda x: ''.join(x), result))
result.sort()
for i in result:
    print(i)