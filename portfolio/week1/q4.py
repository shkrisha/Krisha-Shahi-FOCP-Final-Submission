#Q)4)In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014 times, was not out 162 times, and scored 48426 runs. Write a program to calculate and display Boycott's batting average.
#Note: A batting average is the number of runs scored divided by the number of completed innings (i.e. the total times batted minus the times not out).
# Program to calculate batting average

# Given statistics for Geoffrey Boycott
total_matches = 609
total_bats = 1014
not_out_count = 162
total_runs = 48426

# Function to calculate completed innings
def calculate_completed_innings(bats, not_out):
    return bats - not_out

# Calculate completed innings
completed_innings = calculate_completed_innings(total_bats, not_out_count)

# Calculate batting average
batting_avg = total_runs / completed_innings

# Display Geoffrey Boycott's batting average
print(f"Geoffrey Boycott's Batting Average: {batting_avg:.2f}")

