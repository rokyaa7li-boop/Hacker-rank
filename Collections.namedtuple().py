from collections import namedtuple

n = int(input())
columns = input().split()

StudentRecord = namedtuple('Student', columns)

total_marks = 0
for _ in range(n):
    row = input().split()
    student = StudentRecord(*row)
    total_marks += int(student.MARKS)

average = total_marks / n
print(f"{average:.2f}")