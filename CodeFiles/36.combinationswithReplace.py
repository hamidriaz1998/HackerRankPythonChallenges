# Challenge Link: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement


from itertools import combinations_with_replacement

data = input().split()
string, k = data
string = sorted(list(string))
k = int(k)

for i in combinations_with_replacement(string,k):
    print(''.join(i))