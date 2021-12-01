from statistics import mean


def average_grade(values):
    return sum(values) / len(values)


n = int(input())
students = {}
for _ in range(n):
    name, x = input().split()
    grade = float(x)
    if name not in students:
        students[name] = []
    students[name].append(grade)
# print(students)
for name, grade in students.items():
    avg = mean(grade)
    # avg = average_grade(grade)
    # avg = sum(grade) / len(grade)
    grade_str = ' '.join(str(f'{x:.2f}') for x in grade)
    print(f'{name} -> {grade_str} (avg: {avg:.2f})')
