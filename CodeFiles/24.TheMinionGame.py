# Challenge Link: https://www.hackerrank.com/challenges/the-minion-game

def minion_game(string:str):
    # your code goes here
    vowels = 'AEIOU'
    kevin_start = list(set([i for i in string if i in vowels]))
    stuart_start = list(set([i for i in string if not i in vowels]))
    kevin_score = 0
    stuart_score = 0
    word = ''
    for i in kevin_start:
        word = i
        kevin_score += string.count(word)
        for j in string:
            word += j
            kevin_score += string.count(word)
    for i in stuart_start:
        word = i
        stuart_score += string.count(word)
        for j in string:
            word += j
            kevin_score += string.count(word)
    print(f"Stuart {stuart_score}" if stuart_score>kevin_score else f"Kevin {kevin_score}")


if __name__ == '__main__':
    s = input()
    minion_game(s)