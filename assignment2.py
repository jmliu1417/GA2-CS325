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
    for x in infile.readline().strip().split(','):
        clubs.append(int(x))
    infile.close()
    
    
    for i in range(len(clubs)):
        for j in range(i + 1, len(clubs)):
            if clubs[i] < clubs[j]:
                clubs[i] = clubs[j] = clubs[j], clubs[i]

    min_capacity = min(clubs)
    max_capacity = sum(clubs)

    for capacity in range(min_capacity, max_capacity + 1):
        daily_sums = [0, 0, 0]
        current_day = 0
        capacity_invalid = False

        remaining_clubs = []
        for item in clubs:
            remaining_clubs.append(item)

        while remaining_clubs:
            added = False
            for idx in range(len(remaining_clubs)):
                if daily_sums[current_day] + remaining_clubs[idx] <= capacity:
                    daily_sums[current_day] += remaining_clubs[idx]
                    remaining_clubs.pop(idx)
                    added = True
                    break
            
            if not added:
                current_day += 1
                if current_day > 2:
                    capacity_invalid = True
                    break

        if not capacity_invalid:
            with open(output_file_path, 'w') as outfile:
                outfile.write(str(capacity) + '\n')
            break

# Example usage
calculate_min_capacity("tests/input6.txt", "output.txt")