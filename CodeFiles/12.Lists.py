# Challenge Link: https://www.hackerrank.com/challenges/python-lists/

if __name__ == '__main__':
    N = int(input())
    commands=[]
    for i in range(N):
        command = input()
        commands.append(command)
    commands = [i.split() for i in commands]
    commands = [[int(j) if j.isdigit() else j for j in i] for i in commands]
    mainList= []
    for i in commands:
        if i[0] == "insert":
            mainList.insert(i[1],i[2])
        elif i[0] == "print":
            print(mainList)
        elif i[0] == "remove":
            mainList.remove(i[1])
        elif i[0] == "append":
            mainList.append(i[1])
        elif i[0] == "sort":
            mainList.sort()
        elif i[0] == "pop":
            mainList.pop()
        elif i[0] == "reverse":
            mainList.reverse()
