"""
Implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA(Cumulative grade point average)in descending order.Each student object
has the following attributes:name(string), roll_number (string),and cgpa (float). Test the function 
with different input lists of students.
"""

class student:
    def __init__(self, name,roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students in descending order of cgpa
    sorted_students = sorted(student_list, key=lambda student: student.cgpa,reverse=True)
    return sorted_students

# Example usage:
students = [
   Student("Sumi", "A123", 7.8),
   Student("Iniya", "A124", 8.9),
   Student("Priya", "A125", 9.1),
   Student("Nadhin", "A126", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print("Name: {}, Roll Number:{}, CGPA: {}".format(student.name,student.roll_number, students.cgpa))