# Challenge Link: https://www.hackerrank.com/challenges/itertools-combinations


from itertools import combinations

data = input().split()
string, k = data
string = sorted(list(string))
k = int(k)

for i in range(1, k+1):
    result = list(combinations(string, i))
    result = list(map(lambda x: ''.join(x), result))
    result.sort()
    for i in result:
        print(i)