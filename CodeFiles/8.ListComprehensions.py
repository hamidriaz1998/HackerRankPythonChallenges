# Challenge Link: https://www.hackerrank.com/challenges/list-comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    possible_i = [i for i in range(0,x+1)]
    possible_j = [j for j in range(0,y+1)]
    possible_k = [k for k in range(0,z+1)]

    all_permutation = [[i,j,k] for i in possible_i for j in possible_j for k in possible_k]
    final = [i for i in all_permutation if sum(i) != n]
    print(final)
