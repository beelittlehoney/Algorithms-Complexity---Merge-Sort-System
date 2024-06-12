def merge_sort(students, keys):
    if len(students) > 1:
        mid = len(students) // 2  # Finding the mid of the array
        left_half = students[:mid]  # Dividing the elements into 2 halves
        right_half = students[mid:]

        merge_sort(left_half, keys)  # Sorting the first half
        merge_sort(right_half, keys)  # Sorting the second half

        i = j = k = 0

        # Custom comparison function for sorting with multiple keys
        def compare(student1, student2):
            for key, reverse in keys:
                if student1[key] < student2[key]:
                    return -1 if not reverse else 1
                elif student1[key] > student2[key]:
                    return 1 if not reverse else -1
            return 0

        # Merge process with custom comparison
        while i < len(left_half) and j < len(right_half):
            if compare(left_half[i], right_half[j]) <= 0:
                students[k] = left_half[i]
                i += 1
            else:
                students[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            students[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            students[k] = right_half[j]
            j += 1
            k += 1

    return students

def display_students(students):
    for student in students:
        name = f"{student['firstname']} {student['lastname']}"
        print({'name': name, 'id': student['id'], 'grade': student['grade']})

def add_student(students):
    firstname = input("Enter the student's first name: ").strip()
    lastname = input("Enter the student's last name: ").strip()
    while True:
        try:
            student_id = int(input("Enter the student's ID: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")
    
    while True:
        try:
            grade = int(input("Enter the student's grade: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    
    students.append({'firstname': firstname, 'lastname': lastname, 'id': student_id, 'grade': grade})

# Sample student records
students = [
    {'firstname': 'Alice', 'lastname': 'Smith', 'id': 1, 'grade': 85},
    {'firstname': 'Bob', 'lastname': 'Johnson', 'id': 2, 'grade': 90},
    {'firstname': 'Charlie', 'lastname': 'Brown', 'id': 3, 'grade': 95},
    {'firstname': 'David', 'lastname': 'Davis', 'id': 4, 'grade': 80},
    {'firstname': 'Eve', 'lastname': 'Martinez', 'id': 5, 'grade': 92}
]

while True:
    # Main menu
    print("\nOptions:")
    print("1. Add a student")
    print("2. Sort students")
    print("3. Display students")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()
    
    if choice == '1':
        add_student(students)
    elif choice == '2':
        # Ask the user by what keys and order they want to sort
        print("Enter the keys you want to sort by, separated by commas (e.g., 'firstname, lastname, grade').")
        print("For each key, specify the order as 'asc' for ascending or 'desc' for descending (e.g., 'firstname:asc, lastname:desc').")
        input_keys = input().strip().lower()

        # Parse input keys and orders
        keys = []
        valid_keys = {'firstname', 'lastname', 'grade'}
        try:
            for part in input_keys.split(','):
                key, order = part.split(':')
                if key.strip() not in valid_keys or order.strip() not in {'asc', 'desc'}:
                    raise ValueError
                keys.append((key.strip(), order.strip() == 'desc'))
        except ValueError:
            print("Invalid input format. Please follow the format 'key:order'.")
            continue

        # Sorting student records by the chosen keys and order
        sorted_students = merge_sort(students, keys)
        sort_criteria = ', '.join([f"{key} ({'desc' if reverse else 'asc'})" for key, reverse in keys])
        print(f"Sorted student records by {sort_criteria}:")
        display_students(sorted_students)
    elif choice == '3':
        print("Current student records:")
        display_students(students)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select an option from 1 to 4.")
