"""
School Management System

This module uses lists, sets, tuples, and dictionaries to manage school data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

Data Structures:

1. Lists: To store collections of students, teachers, and classes.
2. Tuples: To store immutable student and teacher details.
3. Sets: To manage unique subjects and extracurricular activities.
4. Dictionaries: To map student IDs and teacher IDs to their details and manage class assignments.

List of students with details (Student ID, Name, Age, Grade, Subjects):
students = [
    (1, "Alice", 14, "8th", {"Math", "Science"}),
    (2, "Bob", 15, "9th", {"English", "History"}),
    (3, "Charlie", 13, "7th", {"Math", "Art"}),
    (4, "Diana", 14, "8th", {"Science", "Physical Education"}),
    (5, "Eve", 15, "9th", {"History", "Math"})
]

List of teachers with details (Teacher ID, Name, Age, Department, Subjects):
teachers = [
    (101, "Mr. Smith", 40, "Math", {"Math", "Algebra"}),
    (102, "Ms. Johnson", 35, "Science", {"Biology", "Chemistry"}),
    (103, "Mrs. Brown", 50, "English", {"English", "Literature"}),
    (104, "Mr. White", 45, "History", {"History", "Geography"}),
    (105, "Ms. Green", 30, "Physical Education", {"Physical Education", "Health"})
]

List of classes (Class ID, Class Name, Teacher ID):
classes = [
    (201, "Math 101", 101),
    (202, "Biology 101", 102),
    (203, "English 101", 103),
    (204, "History 101", 104),
    (205, "PE 101", 105)
]

Set of unique subjects:
subjects = set()

Adding subjects from students and teachers:
for student in students:
    subjects.update(student[4])
for teacher in teachers:
    subjects.update(teacher[4])

Set of unique extracurricular activities:
activities = {"Soccer", "Basketball", "Drama Club", "Chess Club"}

Dictionary to map student IDs to their details:
student_catalog = {student[0]: student for student in students}

Dictionary to map teacher IDs to their details:
teacher_catalog = {teacher[0]: teacher for teacher in teachers}

Dictionary to manage class assignments:
class_assignments = {class_[0]: class_[2] for class_ in classes}

Functions:

List-Related Methods:
1. find_student_index(student_id): Finds the index of a student in the list.
2. find_teacher_index(teacher_id): Finds the index of a teacher in the list.
3. sort_students_by_age(): Sorts students by age.
4. sort_teachers_by_age(): Sorts teachers by age.
5. reverse_classes(): Reverses the list of classes.
6. append_class(class_): Appends a new class to the list.
7. remove_class(class_id): Removes a class from the list.

Tuple-Related Methods:
1. find_max_min_age_students(): Finds the maximum and minimum age of students.
2. find_max_min_age_teachers(): Finds the maximum and minimum age of teachers.
3. count_subject_occurrences(subject): Counts the occurrences of a specific subject.

Set-Related Methods:
1. add_subject(subject): Adds a new subject.
2. remove_subject(subject): Removes a subject.
3. list_all_subjects(): Lists all subjects.
4. add_activity(activity): Adds a new extracurricular activity.
5. remove_activity(activity): Removes an extracurricular activity.
6. list_all_activities(): Lists all extracurricular activities.
7. find_common_subjects(other_subjects): Finds common subjects between two sets.
8. find_unique_subjects(): Finds unique subjects in the school.
9. clear_subjects(): Clears all subjects.

Dictionary-Related Methods:
1. add_student(student_id, name, age, grade, subjects): Adds a new student to the school.
2. remove_student(student_id): Removes a student from the school.
3. get_student_details(student_id): Gets student details.
4. list_students_by_grade(grade): Lists all students by grade.
5. count_students_by_grade(grade): Counts students by grade.
6. add_teacher(teacher_id, name, age, department, subjects): Adds a new teacher to the school.
7. remove_teacher(teacher_id): Removes a teacher from the school.
8. get_teacher_details(teacher_id): Gets teacher details.
9. list_teachers_by_department(department): Lists all teachers by department.
10. count_teachers_by_department(department): Counts teachers by department.
11. update_student_details(student_id, new_details): Updates student details.
12. update_teacher_details(teacher_id, new_details): Updates teacher details.
13. merge_student_catalogs(other_catalog): Merges two student catalogs.
14. merge_teacher_catalogs(other_catalog): Merges two teacher catalogs.
15. get_all_student_ids(): Gets all student IDs.
16. get_all_teacher_ids(): Gets all teacher IDs.
17. clear_student_catalog(): Clears the student catalog.
18. clear_teacher_catalog(): Clears the teacher catalog.

"""
# school_management.py

class SchoolManagement:
    """
    School Management System

    This module uses lists, sets, tuples, and dictionaries to manage school data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

    Data Structures:

    1. Lists: To store collections of students, teachers, and classes.
    2. Tuples: To store immutable student and teacher details.
    3. Sets: To manage unique subjects and extracurricular activities.
    4. Dictionaries: To map student IDs and teacher IDs to their details and manage class assignments.
    """

    def __init__(self):
        # List of students with details (Student ID, Name, Age, Grade, Subjects)
        self.students = [
            (1, "Alice", 14, "8th", {"Math", "Science"}),
            (2, "Bob", 15, "9th", {"English", "History"}),
            (3, "Charlie", 13, "7th", {"Math", "Art"}),
            (4, "Diana", 14, "8th", {"Science", "Physical Education"}),
            (5, "Eve", 15, "9th", {"History", "Math"})
        ]

        # List of teachers with details (Teacher ID, Name, Age, Department, Subjects)
        self.teachers = [
            (101, "Mr. Smith", 40, "Math", {"Math", "Algebra"}),
            (102, "Ms. Johnson", 35, "Science", {"Biology", "Chemistry"}),
            (103, "Mrs. Brown", 50, "English", {"English", "Literature"}),
            (104, "Mr. White", 45, "History", {"History", "Geography"}),
            (105, "Ms. Green", 30, "Physical Education", {"Physical Education", "Health"})
        ]

        # List of classes (Class ID, Class Name, Teacher ID)
        self.classes = [
            (201, "Math 101", 101),
            (202, "Biology 101", 102),
            (203, "English 101", 103),
            (204, "History 101", 104),
            (205, "PE 101", 105)
        ]

        # Set of unique subjects
        self.subjects = set()

        # Adding subjects from students and teachers
        for student in self.students:
            self.subjects.update(student[4])
        for teacher in self.teachers:
            self.subjects.update(teacher[4])

        # Set of unique extracurricular activities
        self.activities = {"Soccer", "Basketball", "Drama Club", "Chess Club"}

        # Dictionary to map student IDs to their details
        self.student_catalog = {student[0]: student for student in self.students}

        # Dictionary to map teacher IDs to their details
        self.teacher_catalog = {teacher[0]: teacher for teacher in self.teachers}

        # Dictionary to manage class assignments
        self.class_assignments = {class_[0]: class_[2] for class_ in self.classes}

    # List-Related Methods
    def find_student_index(self, student_id):
        """Finds the index of a student in the list."""
        for index, student in enumerate(self.students):
            if student[0] == student_id:
                return index
        return -1

    def find_teacher_index(self, teacher_id):
        """Finds the index of a teacher in the list."""
        for index, teacher in enumerate(self.teachers):
            if teacher[0] == teacher_id:
                return index
        return -1

    def sort_students_by_age(self):
        """Sorts students by age."""
        return sorted(self.students, key=lambda student: student[2])

    def sort_teachers_by_age(self):
        """Sorts teachers by age."""
        return sorted(self.teachers, key=lambda teacher: teacher[2])

    def reverse_classes(self):
        """Reverses the list of classes."""
        return self.classes[::-1]

    def append_class(self, class_):
        """Appends a new class to the list."""
        self.classes.append(class_)
        print(f"Class '{class_}' added.")

    def remove_class(self, class_id):
        """Removes a class from the list."""
        self.classes = [c for c in self.classes if c[0] != class_id]
        print(f"Class ID '{class_id}' removed.")

    # Tuple-Related Methods
    def find_max_min_age_students(self):
        """Finds the maximum and minimum age of students."""
        ages = [student[2] for student in self.students]
        return max(ages), min(ages)

    def find_max_min_age_teachers(self):
        """Finds the maximum and minimum age of teachers."""
        ages = [teacher[2] for teacher in self.teachers]
        return max(ages), min(ages)

    def count_subject_occurrences(self, subject):
        """Counts the occurrences of a specific subject."""
        return sum(1 for student in self.students if subject in student[4])

    # Set-Related Methods
    def add_subject(self, subject):
        """Adds a new subject."""
        self.subjects.add(subject)
        print(f"Subject '{subject}' added.")

    def remove_subject(self, subject):
        """Removes a subject."""
        self.subjects.discard(subject)
        print(f"Subject '{subject}' removed.")

    def list_all_subjects(self):
        """Lists all subjects."""
        return self.subjects

    def add_activity(self, activity):
        """Adds a new extracurricular activity."""
        self.activities.add(activity)
        print(f"Activity '{activity}' added.")

    def remove_activity(self, activity):
        """Removes an extracurricular activity."""
        self.activities.discard(activity)
        print(f"Activity '{activity}' removed.")

    def list_all_activities(self):
        """Lists all extracurricular activities."""
        return self.activities

    def find_common_subjects(self, other_subjects):
        """Finds common subjects between two sets."""
        return self.subjects.intersection(other_subjects)

    def find_unique_subjects(self):
        """Finds unique subjects in the school."""
        return self.subjects.difference({"Math", "Science", "English", "History", "Physical Education"})

    def clear_subjects(self):
        """Clears all subjects."""
        self.subjects.clear()
        print("All subjects cleared.")

    # Dictionary-Related Methods
    def add_student(self, student_id, name, age, grade, subjects):
        """Adds a new student to the school."""
        if student_id not in self.student_catalog:
            self.student_catalog[student_id] = (student_id, name, age, grade, subjects)
            self.subjects.update(subjects)
            print(f"Student '{name}' added.")
        else:
            print(f"Student ID '{student_id}' already exists.")

    def remove_student(self, student_id):
        """Removes a student from the school."""
        if student_id in self.student_catalog:
            student_details = self.student_catalog.pop(student_id)
            print(f"Student '{student_details[1]}' removed.")
        else:
            print(f"Student ID '{student_id}' not found.")

    def get_student_details(self, student_id):
        """Gets student details."""
        return self.student_catalog.get(student_id, "Student not found.")

    def list_students_by_grade(self, grade):
        """Lists all students by grade."""
        return [student for student in self.students if student[3] == grade]

    def count_students_by_grade(self, grade):
        """Counts students by grade."""
        return sum(1 for student in self.students if student[3] == grade)

    def add_teacher(self, teacher_id, name, age, department, subjects):
        """Adds a new teacher to the school."""
        if teacher_id not in self.teacher_catalog:
            self.teacher_catalog[teacher_id] = (teacher_id, name, age, department, subjects)
            self.subjects.update(subjects)
            print(f"Teacher '{name}' added.")
        else:
            print(f"Teacher ID '{teacher_id}' already exists.")

    def remove_teacher(self, teacher_id):
        """Removes a teacher from the school."""
        if teacher_id in self.teacher_catalog:
            teacher_details = self.teacher_catalog.pop(teacher_id)
            print(f"Teacher '{teacher_details[1]}' removed.")
        else:
            print(f"Teacher ID '{teacher_id}' not found.")

    def get_teacher_details(self, teacher_id):
        """Gets teacher details."""
        return self.teacher_catalog.get(teacher_id, "Teacher not found.")

    def list_teachers_by_department(self, department):
        """Lists all teachers by department."""
        return [teacher for teacher in self.teachers if teacher[3] == department]

    def count_teachers_by_department(self, department):
        """Counts teachers by department."""
        return sum(1 for teacher in self.teachers if teacher[3] == department)

    def update_student_details(self, student_id, new_details):
        """Updates student details."""
        if student_id in self.student_catalog:
            self.student_catalog[student_id] = new_details
            print(f"Updated details for student ID '{student_id}'.")
        else:
            print(f"Student ID '{student_id}' not found.")

    def update_teacher_details(self, teacher_id, new_details):
        """Updates teacher details."""
        if teacher_id in self.teacher_catalog:
            self.teacher_catalog[teacher_id] = new_details
            print(f"Updated details for teacher ID '{teacher_id}'.")
        else:
            print(f"Teacher ID '{teacher_id}' not found.")

    def merge_student_catalogs(self, other_catalog):
        """Merges two student catalogs."""
        for student_id, details in other_catalog.items():
            if student_id not in self.student_catalog:
                self.student_catalog[student_id] = details
                self.subjects.update(details[4])
        print("Student catalogs merged.")

    def merge_teacher_catalogs(self, other_catalog):
        """Merges two teacher catalogs."""
        for teacher_id, details in other_catalog.items():
            if teacher_id not in self.teacher_catalog:
                self.teacher_catalog[teacher_id] = details
                self.subjects.update(details[4])
        print("Teacher catalogs merged.")

    def get_all_student_ids(self):
        """Gets all student IDs."""
        return list(self.student_catalog.keys())

    def get_all_teacher_ids(self):
        """Gets all teacher IDs."""
        return list(self.teacher_catalog.keys())

    def clear_student_catalog(self):
        """Clears the student catalog."""
        self.student_catalog.clear()
        print("Student catalog cleared.")

    def clear_teacher_catalog(self):
        """Clears the teacher catalog."""
        self.teacher_catalog.clear()
        print("Teacher catalog cleared.")

# Example usage
if __name__ == "__main__":
    school = SchoolManagement()

    print("Student Catalog:")
    for student_id, details in school.student_catalog.items():
        print(f"{student_id}: {details}")

    print("\nTeacher Catalog:")
    for teacher_id, details in school.teacher_catalog.items():
        print(f"{teacher_id}: {details}")

    print("\nSubjects Available:")
    print(school.subjects)

    print("\nExtracurricular Activities Available:")
    print(school.activities)

    print("\nClass Assignments:")
    for class_id, teacher_id in school.class_assignments.items():
        print(f"Class ID {class_id}: Teacher ID {teacher_id}")

    # Add and remove students
    school.add_student(6, "Frank", 16, "10th", {"Math", "Science"})
    school.remove_student(3)

    print("\nStudent Catalog After Changes:")
    for student_id, details in school.student_catalog.items():
        print(f"{student_id}: {details}")

    # Get student details
    print("\nStudent Details for ID 2:")
    print(school.get_student_details(2))

    # List students by grade
    print("\nStudents in 9th Grade:")
    print(school.list_students_by_grade("9th"))

    # Count students by grade
    print("\nCount of Students in 8th Grade:")
    print(school.count_students_by_grade("8th"))

    # Find student index
    print("\nIndex of Student ID 2:")
    print(school.find_student_index(2))

    # Add and remove subjects
    school.add_subject("Physics")
    school.remove_subject("Art")

    # List all subjects
    print("\nAll Subjects:")
    print(school.list_all_subjects())

    # Add and remove activities
    school.add_activity("Robotics Club")
    school.remove_activity("Drama Club")

    # List all activities
    print("\nAll Extracurricular Activities:")
    print(school.list_all_activities())

    # Append and remove classes
    school.append_class((206, "Physics 101", 102))
    school.remove_class(202)

    print("\nClasses After Changes:")
    for class_ in school.classes:
        print(class_)

    # Sort students by age
    print("\nStudents Sorted by Age:")
    for student in school.sort_students_by_age():
        print(student)

    # Sort teachers by age
    print("\nTeachers Sorted by Age:")
    for teacher in school.sort_teachers_by_age():
        print(teacher)

    # Reverse the list of classes
    print("\nReversed List of Classes:")
    print(school.reverse_classes())

    # Find the maximum and minimum age of students
    max_age_students, min_age_students = school.find_max_min_age_students()
    print(f"\nMaximum Age of Students: {max_age_students}, Minimum Age of Students: {min_age_students}")

    # Find the maximum and minimum age of teachers
    max_age_teachers, min_age_teachers = school.find_max_min_age_teachers()
    print(f"\nMaximum Age of Teachers: {max_age_teachers}, Minimum Age of Teachers: {min_age_teachers}")

    # Count the occurrences of a specific subject
    print(f"\nOccurrences of 'Math': {school.count_subject_occurrences('Math')}")

    # Find common subjects between two sets
    other_subjects = {"Math", "Physics", "Chemistry"}
    print(f"\nCommon Subjects: {school.find_common_subjects(other_subjects)}")

    # Find unique subjects in the school
    print(f"\nUnique Subjects: {school.find_unique_subjects()}")

    # Update student details
    school.update_student_details(2, (2, "Bob", 16, "10th", {"Math", "Physics"}))
    print(f"\nUpdated Student Details for ID 2: {school.get_student_details(2)}")

    # Update teacher details
    school.update_teacher_details(102, (102, "Ms. Johnson", 36, "Science", {"Physics", "Chemistry"}))
    print(f"\nUpdated Teacher Details for ID 102: {school.get_teacher_details(102)}")

    # Merge two student catalogs
    other_student_catalog = {
        7: (7, "Grace", 14, "8th", {"Math", "Science"}),
        8: (8, "Hank", 15, "9th", {"English", "History"})
    }
    school.merge_student_catalogs(other_student_catalog)
    print("\nMerged Student Catalog:")
    for student_id, details in school.student_catalog.items():
        print(f"{student_id}: {details}")

    # Merge two teacher catalogs
    other_teacher_catalog = {
        106: (106, "Mr. Blue", 50, "Math", {"Math", "Geometry"}),
        107: (107, "Ms. Red", 45, "Science", {"Biology", "Physics"})
    }
    school.merge_teacher_catalogs(other_teacher_catalog)
    print("\nMerged Teacher Catalog:")
    for teacher_id, details in school.teacher_catalog.items():
        print(f"{teacher_id}: {details}")

    # Get all student IDs
    print("\nAll Student IDs:")
    print(school.get_all_student_ids())

    # Get all teacher IDs
    print("\nAll Teacher IDs:")
    print(school.get_all_teacher_ids())

    # Clear the student catalog
    school.clear_student_catalog()
    print("\nStudent Catalog After Clearing:")
    print(school.student_catalog)

    # Clear the teacher catalog
    school.clear_teacher_catalog()
    print("\nTeacher Catalog After Clearing:")
    print(school.teacher_catalog)