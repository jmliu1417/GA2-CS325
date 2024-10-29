'''
    This file contains the template for Assignment1.  For testing it, I will place it
    in a different directory, call the function <min_attendance_for_long_weekend>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

def min_attendance_for_long_weekend(input_file_path, output_file_path):
    '''
        This function will contain your code.  It wil read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.

         infile = open(input_file_path, 'r')
    D = int(infile.readline().strip())
    clubs = []
    for x in infile.readline().strip().split(','):
        clubs.append(int(x))
    infile.close()

    def is_schedule_possible (max_capacity,D):
        days_used = 1
        current_day_total = 0

        for club in clubs: 
            if current_day_total + club <= max_capacity:
                current_day_total += club
            else: 
                days_used += 1
                current_day_total = club
                if days_used > D: 
                    return False
        return True

    low = max(clubs)
    high = sum(clubs)

    while low <= high: 
        mid = (low + high) // 2
        if is_schedule_possible (mid, D):
            high = mid - 1
        else:
            low = mid + 1 


    outfile = open(output_file_path, 'w')
    outfile.write(str(low) + '\n')
    outfile.close()

    '''
    pass

'''
    To test your function, you can uncomment the following command with the the input/output
    files paths that you want to read from/write to.  Do NOT forget to comment it out before
    submitting.
'''
# min_attendance_for_long_weekend('', '')
