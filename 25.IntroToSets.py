# Challenge Link: https://www.hackerrank.com/challenges/py-introduction-to-sets

def average(array):
    # your code goes here
    return (sum(list(set(array)))/len(list(set(array))))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)