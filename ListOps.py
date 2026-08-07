students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
marks = [85, 92, 78, 95, 88, 70, 99, 82, 91, 75]

max_mark = max(marks)
min_mark = min(marks)
max_student = students[marks.index(max_mark)]
min_student = students[marks.index(min_mark)]

print(max_student, max_mark)
print(min_student, min_mark)

sample_marks = [85, 92, 78, 95, 88, 70, 99, 82, 91, 75, 85, 78, 92, 85, 70, 88, 95, 85, 91, 82]

average = sum(sample_marks) / len(sample_marks)
print(average)

above_average = sum(1 for mark in sample_marks if mark > average)
print(above_average)

mode_mark = max(set(sample_marks), key=sample_marks.count)
print(mode_mark)
