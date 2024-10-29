'''
    This file contains the template for Assignment1.  For testing it, I will place it
    in a different directory, call the function <min_attendance_for_long_weekend>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''
def min_attendance(input_file_path, output_file_path):
    '''
    This function will read from the file <input_file_path>,
    and will write its output to the file <output_file_path>.
    '''

    infile = open(input_file_path, 'r')
    
    # Read club sizes from the first line
    clubs = []
    for x in infile.readline().strip().split(','):
        clubs.append(int(x))  # Sizes of each club
    infile.close()
    
    D = 3  # Fixed number of days

    def is_schedule_possible(max_capacity):
        days_used = 1
        current_day_total = 0

        for club in clubs:
            if current_day_total + club <= max_capacity:
                current_day_total += club
            else:
                # Move to the next day
                days_used += 1
                current_day_total = club
                # If we exceed the number of days, return False
                if days_used > D:
                    return False
        return True

    low = max(clubs)  # Minimum possible admittance
    high = sum(clubs)  # Maximum possible admittance

    # Binary search to find the minimum possible admittance
    while low <= high:
        mid = (low + high) // 2
        if is_schedule_possible(mid):
            high = mid - 1  # Try for a smaller capacity
        else:
            low = mid + 1  # Increase capacity

    # Writing the result to the output file
    with open(output_file_path, 'w') as outfile:
        outfile.write(str(low) + '\n')

'''
    To test your function, you can uncomment the following command with the input/output
    files paths that you want to read from/write to.  Do NOT forget to comment it out before
    submitting.
'''
# Uncomment the following line to test
min_attendance('tests/input3.txt', 'testing_output_files/output_text.txt')
