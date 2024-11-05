# employee_management.py
"""
Employee Management System

This module uses lists, sets, tuples, and dictionaries to manage employee data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

Data Structures:

1. Lists: To store collections of employees and departments.
2. Tuples: To store immutable employee details.
3. Sets: To manage unique skills and departments.
4. Dictionaries: To map employee IDs to their details and manage department assignments.

List of employees with details (ID, name, age, department, skills):
employees = [
    (1, "Alice", 30, "HR", {"Recruitment", "Training"}),
    (2, "Bob", 25, "IT", {"Python", "Networking"}),
    (3, "Charlie", 28, "Finance", {"Accounting", "Excel"}),
    (4, "Diana", 35, "IT", {"Java", "Security"}),
    (5, "Eve", 40, "HR", {"Recruitment", "Employee Relations"})
]

List of departments:
departments = ["HR", "IT", "Finance", "Marketing"]

Set of unique skills:
skills = set()

Adding skills from employees:
for employee in employees:
    skills.update(employee[4])

Dictionary to map employee IDs to their details:
employee_catalog = {emp[0]: emp for emp in employees}

Dictionary to manage department assignments:
department_assignments = {dept: [] for dept in departments}

Assign employees to departments:
for employee in employees:
    department_assignments[employee[3]].append(employee[0])

Functions:

List-Related Methods:
1. find_employee_index(emp_id): Finds the index of an employee in the list.
2. sort_employees_by_age(): Sorts employees by age.
3. reverse_departments(): Reverses the list of departments.
4. append_department(department): Appends a new department to the list.
5. remove_department(department): Removes a department from the list.

Tuple-Related Methods:
1. find_max_min_age(): Finds the maximum and minimum age of employees.

Set-Related Methods:
1. add_skill(skill): Adds a new skill.
2. remove_skill(skill): Removes a skill.
3. list_all_skills(): Lists all skills.
4. count_skill_occurrences(skill): Counts the occurrences of a specific skill.
5. find_common_skills(other_skills): Finds common skills between two sets.
6. find_unique_skills(): Finds unique skills in the company.
7. clear_skills(): Clears all skills.

Dictionary-Related Methods:
1. add_employee(emp_id, name, age, department, skills_set): Adds a new employee.
2. remove_employee(emp_id): Removes an employee.
3. get_employee_details(emp_id): Gets employee details.
4. list_employees_by_department(department): Lists all employees in a department.
5. count_employees_by_department(department): Counts employees in a department.
6. update_employee_details(emp_id, new_details): Updates employee details.
7. merge_employee_catalogs(other_catalog): Merges two employee catalogs.
8. get_all_employee_ids(): Gets all employee IDs.
9. clear_employee_catalog(): Clears the employee catalog.

"""

# List of employees with details (ID, name, age, department, skills)
employees = [
    (1, "Alice", 30, "HR", {"Recruitment", "Training"}),
    (2, "Bob", 25, "IT", {"Python", "Networking"}),
    (3, "Charlie", 28, "Finance", {"Accounting", "Excel"}),
    (4, "Diana", 35, "IT", {"Java", "Security"}),
    (5, "Eve", 40, "HR", {"Recruitment", "Employee Relations"})
]

# List of departments
departments = ["HR", "IT", "Finance", "Marketing"]

# Set of unique skills
skills = set()

# Adding skills from employees
for employee in employees:
    skills.update(employee[4])

# Dictionary to map employee IDs to their details
employee_catalog = {emp[0]: emp for emp in employees}

# Dictionary to manage department assignments
department_assignments = {dept: [] for dept in departments}

# Assign employees to departments
for employee in employees:
    department_assignments[employee[3]].append(employee[0])

# Function to add a new employee
def add_employee(emp_id, name, age, department, skills_set):
    if emp_id not in employee_catalog:
        employee_catalog[emp_id] = (emp_id, name, age, department, skills_set)
        department_assignments[department].append(emp_id)
        skills.update(skills_set)
        print(f"Employee '{name}' added.")
    else:
        print(f"Employee ID '{emp_id}' already exists.")

# Function to remove an employee
def remove_employee(emp_id):
    if emp_id in employee_catalog:
        emp_details = employee_catalog.pop(emp_id)
        department_assignments[emp_details[3]].remove(emp_id)
        print(f"Employee '{emp_details[1]}' removed.")
    else:
        print(f"Employee ID '{emp_id}' not found.")

# Function to get employee details
def get_employee_details(emp_id):
    return employee_catalog.get(emp_id, "Employee not found.")

# Function to list all employees in a department
def list_employees_by_department(department):
    return [emp_id for emp_id in department_assignments.get(department, [])]

# Function to count employees in a department
def count_employees_by_department(department):
    return len(department_assignments.get(department, []))

# Function to find the index of an employee in the list
def find_employee_index(emp_id):
    for index, employee in enumerate(employees):
        if employee[0] == emp_id:
            return index
    return -1

# Function to add a new skill
def add_skill(skill):
    skills.add(skill)
    print(f"Skill '{skill}' added.")

# Function to remove a skill
def remove_skill(skill):
    skills.discard(skill)
    print(f"Skill '{skill}' removed.")

# Function to list all skills
def list_all_skills():
    return skills

# Function to sort employees by age
def sort_employees_by_age():
    return sorted(employees, key=lambda emp: emp[2])

# Function to reverse the list of departments
def reverse_departments():
    return departments[::-1]

# Function to find the maximum and minimum age of employees
def find_max_min_age():
    ages = [emp[2] for emp in employees]
    return max(ages), min(ages)

# Function to count the occurrences of a specific skill
def count_skill_occurrences(skill):
    return sum(1 for emp in employees if skill in emp[4])

# Function to find common skills between two sets
def find_common_skills(other_skills):
    return skills.intersection(other_skills)

# Function to find unique skills in the company
def find_unique_skills():
    return skills.difference({"Python", "Java"})

# Function to update employee details
def update_employee_details(emp_id, new_details):
    if emp_id in employee_catalog:
        old_department = employee_catalog[emp_id][3]
        new_department = new_details[3]
        if old_department != new_department:
            department_assignments[old_department].remove(emp_id)
            department_assignments[new_department].append(emp_id)
        employee_catalog[emp_id] = new_details
        print(f"Updated details for employee ID '{emp_id}'.")
    else:
        print(f"Employee ID '{emp_id}' not found.")

# Function to merge two employee catalogs
def merge_employee_catalogs(other_catalog):
    for emp_id, details in other_catalog.items():
        if emp_id not in employee_catalog:
            employee_catalog[emp_id] = details
            department_assignments[details[3]].append(emp_id)
            skills.update(details[4])
    print("Employee catalogs merged.")

# Function to append a new department to the list
def append_department(department):
    if department not in departments:
        departments.append(department)
        department_assignments[department] = []
        print(f"Department '{department}' added.")
    else:
        print(f"Department '{department}' already exists.")

# Function to remove a department from the list
def remove_department(department):
    if department in departments:
        departments.remove(department)
        del department_assignments[department]
        print(f"Department '{department}' removed.")
    else:
        print(f"Department '{department}' not found.")

# Function to clear all skills
def clear_skills():
    skills.clear()
    print("All skills cleared.")

# Function to get all employee IDs
def get_all_employee_ids():
    return list(employee_catalog.keys())

# Function to clear the employee catalog
def clear_employee_catalog():
    employee_catalog.clear()
    for dept in department_assignments:
        department_assignments[dept] = []
    print("Employee catalog cleared.")

# Example usage
if __name__ == "__main__":
    print("Employee Catalog:")
    for emp_id, details in employee_catalog.items():
        print(f"{emp_id}: {details}")

    print("\nDepartments Available:")
    print(departments)

    print("\nSkills Available:")
    print(skills)

    print("\nDepartment Assignments:")
    for dept, emp_ids in department_assignments.items():
        print(f"{dept}: {emp_ids}")

    # Add and remove employees
    add_employee(6, "Frank", 29, "Marketing", {"SEO", "Content Writing"})
    remove_employee(3)

    print("\nEmployee Catalog After Changes:")
    for emp_id, details in employee_catalog.items():
        print(f"{emp_id}: {details}")

    # Get employee details
    print("\nEmployee Details for ID 2:")
    print(get_employee_details(2))

    # List employees by department
    print("\nEmployees in IT Department:")
    print(list_employees_by_department("IT"))

    # Count employees by department
    print("\nCount of Employees in HR Department:")
    print(count_employees_by_department("HR"))

    # Find employee index
    print("\nIndex of Employee ID 2:")
    print(find_employee_index(2))

    # Add and remove skills
    add_skill("Project Management")
    remove_skill("Networking")

    # List all skills
    print("\nAll Skills:")
    print(list_all_skills())

    # Sort employees by age
    print("\nEmployees Sorted by Age:")
    for emp in sort_employees_by_age():
        print(emp)

    # Reverse the list of departments
    print("\nReversed List of Departments:")
    print(reverse_departments())

    # Find the maximum and minimum age of employees
    max_age, min_age = find_max_min_age()
    print(f"\nMaximum Age: {max_age}, Minimum Age: {min_age}")

    # Count the occurrences of a specific skill
    print(f"\nOccurrences of 'Python': {count_skill_occurrences('Python')}")

    # Find common skills between two sets
    other_skills = {"Python", "SEO", "Data Analysis"}
    print(f"\nCommon Skills: {find_common_skills(other_skills)}")

    # Find unique skills in the company
    print(f"\nUnique Skills: {find_unique_skills()}")

    # Update employee details
    update_employee_details(2, (2, "Bob", 26, "Finance", {"Python", "Accounting"}))
    print(f"\nUpdated Employee Details for ID 2: {get_employee_details(2)}")

    # Merge two employee catalogs
    other_catalog = {
        7: (7, "Grace", 32, "IT", {"Python", "Machine Learning"}),
        8: (8, "Hank", 45, "HR", {"Recruitment", "Training"})
    }
    merge_employee_catalogs(other_catalog)
    print("\nMerged Employee Catalog:")
    for emp_id, details in employee_catalog.items():
        print(f"{emp_id}: {details}")

    # Append a new department to the list
    append_department("Legal")
    print("\nUpdated List of Departments:")
    print(departments)

    # Remove a department from the list
    remove_department("Marketing")
    print("\nUpdated List of Departments After Removal:")
    print(departments)

    # Clear all skills
    clear_skills()
    print("\nSkills After Clearing:")
    print(skills)

    # Get all employee IDs
    print("\nAll Employee IDs:")
    print(get_all_employee_ids())

    # Clear the employee catalog
    clear_employee_catalog()
    print("\nEmployee Catalog After Clearing:")
    print(employee_catalog)