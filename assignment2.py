'''
    This file contains the template for Assignment1.  For testing it, I will place it
    in a different directory, call the function <min_attendance_for_long_weekend>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''
def calculate_min_capacity(input_file_path, output_file_path):

    infile = open(input_file_path, 'r')
    clubs = []
    with open(input_filename, 'r') as infile:
        for x in infile.readline().strip().split(','):
            clubs.append(int(x))
    
    n = len(clubs)  # Number of clubs
    l = max(clubs)  # Max number of members in a club


    dp = [[float('inf')] * 4 for _ in range(n + 1)]
    dp[0][0] = 0  # 0 clubs over 0 days needs 0 attendance


    print(f"Clubs: {clubs}")
    print(f"Number of clubs (n): {n}, Max club size (l): {l}")


    # Fill the DP table
    for i in range(1, n + 1):  # for each club
        for j in range(1, 4):  # for 1, 2, and 3 days
            for k in range(i):  # last club assigned to day j is club k to club i-1
                # Calculate the sum for clubs from k to i-1
                day_total = sum(clubs[m] for m in range(k, i))

                # Update the DP value considering the max of previous days and this day's total
                max_attendance = max(dp[k][j - 1], day_total)
                dp[i][j] = min(dp[i][j], max_attendance)


                # Debug prints to trace calculations
                print(f"\nConsidering clubs from {k} to {i-1} for day {j}:")
                print(f"Day total (clubs {k} to {i-1}): {day_total}")
                print(f"Previous max attendance from day {j-1} (clubs up to {k}): {dp[k][j - 1]}")
                print(f"Max attendance for current setup: {max_attendance}")
                print(f"Current min max attendance for dp[{i}][{j}]: {dp[i][j]}")


    # The answer is the minimum maximum attendance required for all clubs over 3 days
    min_max_attendance = dp[n][3]
    print(f"\n Final DP table:")
    for row in dp:
        print(row)


    # Write result to output file
    with open(output_filename, 'w') as file:
        file.write(f"Minimum attendance required: {min_max_attendance}\n")
    print(f"Minimum attendance required: {min_max_attendance} written to {output_filename}")


# Example call (uncomment for testing):
min_attendance_for_long_weekend('tests/input1.txt', 'output.txt')


#below is code for n*3^n time complexity I think but it gives the right answers :(
#def min_attendance_for_long_weekend(input_filename, output_filename):
    # Read club sizes from input file
    with open(input_filename, 'r') as file:
        clubs = list(map(int, file.readline().strip().split(',')))

    n = len(clubs)
    max_club_size = max(clubs)

    # Initialize a variable to store the minimized maximum attendance
    min_max_attendance = float('inf')

    # Function to check all possible distributions of clubs into three days
    def distribute(clubs, day1, day2, day3):
        nonlocal min_max_attendance
        max_day_attendance = max(sum(day1), sum(day2), sum(day3))
        min_max_attendance = min(min_max_attendance, max_day_attendance)

    # Recursive function to distribute clubs
    def backtrack(index, day1, day2, day3):
        if index == n:
            distribute(clubs, day1, day2, day3)
            return
        
        # Include the current club in day 1
        backtrack(index + 1, day1 + [clubs[index]], day2, day3)
        # Include the current club in day 2
        backtrack(index + 1, day1, day2 + [clubs[index]], day3)
        # Include the current club in day 3
        backtrack(index + 1, day1, day2, day3 + [clubs[index]])

    # Start the backtracking
    backtrack(0, [], [], [])

    # Write the result to output file
    with open(output_filename, 'w') as file:
        file.write(f"Minimum attendance required: {min_max_attendance}\n")
    
    print(f"Minimum attendance required: {min_max_attendance} written to {output_filename}")

# Example call (uncomment for testing):
# min_attendance_for_long_weekend('tests/input1.txt', 'output.txt')
