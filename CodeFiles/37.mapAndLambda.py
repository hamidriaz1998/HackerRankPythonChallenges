# Challenge Link: https://www.hackerrank.com/challenges/map-and-lambda-expression

cube = lambda x: x**3

def fibonacci(n):
    fibs = []
    fibs.append(0) if n == 1 else fibs.extend([0, 1]) if n > 1 else fibs
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))