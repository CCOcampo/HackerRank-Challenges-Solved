if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    students = sorted(students,key = lambda x:x[1])
    
    second_lowest_score = sorted(set(score for _, score in students))[1]
    desired_students = sorted([name for name, score in students if score == second_lowest_score])
    print("\n".join(desired_students))
