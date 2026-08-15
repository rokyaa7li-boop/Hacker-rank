if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    scores = sorted(set([student[1] for student in students]))
    second_lowest = scores[1]
    
    second_lowest_names = sorted([student[0] for student in students if student[1] == second_lowest])
    
    for name in second_lowest_names:
        print(name)
