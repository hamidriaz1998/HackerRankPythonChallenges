# Challenge Link: https://www.hackerrank.com/challenges/zipped

n, x = list(map(int, input().split()))
marks = [list(map(float, input().split())) for i in range(x)]
marksStudents = list(zip(*marks))

average = [round(sum(i)/len(i),1) for i in marksStudents]
for i in average:
    print(i)