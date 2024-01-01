# Challenge Link: https://www.hackerrank.com/challenges/capitalize

def solve(s:str):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s   

if __name__ == '__main__':
    fptr = open('h.txt', 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()