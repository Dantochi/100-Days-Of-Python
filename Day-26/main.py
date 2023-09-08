# List Comprehension
numbers = [1, 2, 3, 4, 5]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
new_names = [n for n in names if len(n) > 5]
print(new_names)

# Dictionary Comprehensions
import random

new_dict = {student: random.randint(1, 101) for student in names}
print(new_dict)

passed_students = {student: score for (student, score) in new_dict.items() if score >= 60}
print(passed_students)
