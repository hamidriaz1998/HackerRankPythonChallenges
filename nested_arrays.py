if __name__ == "__main__":
    students = [
        ["Harsh", 20],
        ["Beria",20],
        ["varun", 19],
        ["kakunami",19],
        ["vikas",21],
    ]
    scores = list(set([students[i][1] for i in range(0,len(students))]))
    scores.sort()
    required_score = scores[1]
    required_students = [students[i][0] for i in range(0,len(students)) if students[i][1] == required_score]
    required_students.sort()
    for i in required_students:
        print(i)

# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21