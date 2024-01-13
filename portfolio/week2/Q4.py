#Q)4)A kindly teacher wishes to distribute a tub of sweets between her pupils. She will first count the sweets and then divide them according to how many pupils attend that day. Write a program that will tell the teacher 
# how many sweets to give to each pupil, and how many she will have left over.


# Prompt the user for the total number of sweets and the number of pupils
total_sweets = int(input("Enter the total number of sweets: "))
num_pupils = int(input("Enter the number of pupils: "))

# Calculate sweets per pupil and leftover sweets
sweets_per_pupil = total_sweets // num_pupils
leftover_sweets = total_sweets % num_pupils

# Display the result
print(f"Each pupil will receive {sweets_per_pupil} sweets.")
print(f"There will be {leftover_sweets} sweets left over.")
