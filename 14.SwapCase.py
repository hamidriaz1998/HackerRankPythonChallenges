# Challenge Link: https://www.hackerrank.com/challenges/swap-case/

def swap_case(s):
    s = list(s)
    s = [i.upper() if i.islower() else i.lower() for i in s]
    s = "".join(s)
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)