#Q)5)The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups.
# A lab group is 24 students, since this is the number of PCs in a lab. 
# Write a program that calculates how many groups are needed for the following number of students: 113, 175, 12. Display how many full groups there will be, and how many students will be in the smaller "left over" group.

# Given data
student_counts = [113, 175, 12]
students_per_lab_group = 24

# Function to calculate the number of full groups and remaining students
def calculate_groups_and_remainder(num_students, students_per_group):
    full_groups = num_students // students_per_group
    remaining_students = num_students % students_per_group
    return full_groups, remaining_students

# Calculate and display for each number of students
for num_students in student_counts:
    full_groups, remaining_students = calculate_groups_and_remainder(num_students, students_per_lab_group)
    print(f"For {num_students} students: Full groups: {full_groups}, Remaining students: {remaining_students}")

