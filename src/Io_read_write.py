import os

# Define the file path
text_file_path = 'nested_list.txt'
text_file2_path = 'nested2_list.txt'

if not os.path.exists(text_file2_path):
    with open(text_file2_path,'w') as file:
        file.write('1,2,3,4,5\n6,7,8,9,10\n11,12,13,14,15\n')

nested2_list = []
with open(text_file2_path,'r') as file:
    for line in file:
        nested2_list.append([int(num) for num in line.strip().split(',')])
# Check if the file exists, if not, create it with sample data
if not os.path.exists(text_file_path):
    with open(text_file_path, 'w') as file:
        file.write('1,2,3\n4,5,6\n7,8,9\n')
        
odd_numbers = [num for sublist in nested2_list for num in sublist if num % 2 ==1]
print(odd_numbers)


# Read the file and process the data
nested_list = []
with open(text_file_path, 'r') as file:
    for line in file:
        nested_list.append([int(num) for num in line.strip().split(',')])

# Filter and flatten the list of lists
even_numbers = [num for sublist in nested_list for num in sublist if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8]


import json

# Define the file path
json_file_path = 'students.json'

# Check if the file exists, if not, create it with sample data
if not os.path.exists(json_file_path):
    sample_data = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 75},
        {"name": "Charlie", "grade": 90},
    ]
    with open(json_file_path, 'w') as file:
        json.dump(sample_data, file, indent=4)

# Read the JSON file and process the data
with open(json_file_path, 'r') as file:
    students = json.load(file)

# Extract specific elements
high_scorers = [student["name"] for student in students if student["grade"] > 80]
print(high_scorers)  # Output: ['Alice', 'Charlie']


import csv

# Define the file path
csv_file_path = 'lists.csv'

# Check if the file exists, if not, create it with sample data
if not os.path.exists(csv_file_path):
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['list1', 'list2'])
        writer.writerow([1, 4])
        writer.writerow([2, 5])
        writer.writerow([3, 6])

# Read the CSV file and process the data
list1 = []
list2 = []
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        list1.append(int(row['list1']))
        list2.append(int(row['list2']))

# Combine two lists with a condition
even_sum_pairs = [(x, y) for x in list1 for y in list2 if (x + y) % 2 == 0]
print(even_sum_pairs)  # Output: [(1, 5), (2, 4), (3, 5)]

