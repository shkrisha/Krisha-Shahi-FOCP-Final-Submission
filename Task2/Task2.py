import sys

def analyze_cat_shelter_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Initialize variables
        cat_visits = 0
        other_cats = 0
        total_time_in_house = 0
        durations = []

        # Parse the log file
        for line in lines:
            if line.strip() == 'END':
                break

            parts = line.strip().split(',')
            cat_name, entry_time, exit_time = parts

            entry_time = int(entry_time)
            exit_time = int(exit_time)

            duration = exit_time - entry_time
            total_time_in_house += duration

            if cat_name == 'OURS':
                cat_visits += 1
                durations.append(duration)
            elif cat_name == 'THEIRS':
                other_cats += 1

        # Calculate statistics
        avg_duration = sum(durations) / len(durations) if durations else 0
        longest_duration = max(durations) if durations else 0
        shortest_duration = min(durations) if durations else 0

        # Format time
        total_hours = total_time_in_house // 60
        total_minutes = total_time_in_house % 60

        # Display analysis results
        print("\nLog File Analysis")
        print("==================")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {other_cats}")
        print(f"\nTotal Time in House: {total_hours} Hours, {total_minutes} Minutes")
        print(f"\nAverage Visit Length: {avg_duration} Minutes")
        print(f"Longest Visit: {longest_duration} Minutes")
        print(f"Shortest Visit: {shortest_duration} Minutes")

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        # Run the analysis on the specified file
        analyze_cat_shelter_log(sys.argv[1])
