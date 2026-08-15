n = int(input())
student_marks = {}

for _ in range(n):
    line = input().split()
    name = line[0]
    scores = list(map(float, line[1:]))
    student_marks[name] = scores

query_name = input()

scores = student_marks[query_name]
average = sum(scores) / len(scores)
print(f"{average:.2f}")
