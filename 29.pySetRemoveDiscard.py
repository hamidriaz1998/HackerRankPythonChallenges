# Challenge Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop

n = int(input())
s = set(map(int, input().split()))
num = int(input())
commands = []
for i in range(num):
    commands.append(input())
commands = [i.split() for i in commands]
commands = [[int(j) if j.isdigit() else j for j in i] for i in commands]
for i in commands:
    if i[0] == "pop":
        s.pop()
    elif i[0] == "remove":
        s.remove(i[1])
    elif i[0] == "discard":
        s.discard(i[1])
print(sum(s))