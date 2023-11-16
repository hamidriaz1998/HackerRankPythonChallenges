# Challenge Link: https://www.hackerrank.com/challenges/nested-list/
if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    scores = list(set([students[i][1] for i in range(0,len(students))]))
    scores.sort()
    required_score = scores[1]
    required_students = [students[i][0] for i in range(0,len(students)) if students[i][1] == required_score]
    required_students.sort()
    for i in required_students:
        print(i)
    

