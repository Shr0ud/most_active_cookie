'''
Helper functions for most active cookie

'''

from collections import defaultdict

# Function that reads the input file and populates two dictionaries
# One dictionary will contain the occurence count of each cookie for the input date
# the other dictionary will contain sets of cookies grouped by their occurence count
# inputs: 
# the opened file (file), with format:
# cookiename1, date1
# cookiename2, date2
# 
# the selected date (string), with format YYYY-MM-DD
#
# outputs: 
# same_occurences_sets, dictionary of {ocurrence count : set of cookies}
# cookie_occurences_count, dictionary of {cookie name : occurence count}
def process_file(input_file, input_date):

    # Boolean variable 
    # TRUE if the first line with our target date has been reached
    # used to terminate the for loop earlier
    target_date_found = False

    # Constant value for the number of characters in each date string
    # YYYY-MM-DD has a length of 10
    LENGTH_OF_DATE = 10

    # A dictionary (defaultdict) of sets
    # this is used to group cookies that have the same number of occurences
    # each set contains the number of cookies and its key is number of occurences
    # key : value pair -> number of occurences(integer) : cookies (set of strings)
    same_occurences_sets = defaultdict(None)

    # A dictionary (defaultdict) 
    # keeps track of the occurences of each cookie
    # key : value pair -> cookie name (string) : numer of occurences (int)
    cookie_occurences_count = defaultdict(None)

    lines = input_file.readlines()
    # We can also have for line in file: to loops through the lines
    # But I personally enjoy using indexes because it allows us to check which line has an issue
    # if an issue ever comes up
    for line_number in range(len(lines)):
        # split the line based on comma
        split_line = lines[line_number].split(',')

        # Get the cookie and the date of each line
        try:
            cookie = split_line[0]
            date = split_line[1][0:LENGTH_OF_DATE]
        except IndexError:
            raise IndexError("File format incorrect.")

        if (date != input_date):
            # If we get here then it means that we have already read the lines of our date
            # So in this case we can exit the loop earlier
            if target_date_found:
                break
            continue
        else:
            # Here we have found the correct date
            # since the dates are sorted, we can loop until the date changes
            # So we can update our boolean variable here
            target_date_found = True
            
            # update the dictionary of each cookie's occurence
            if cookie_occurences_count.get(cookie) == None:
                cookie_occurences_count[cookie] = 1
            else:
                cookie_occurences_count[cookie] += 1
            
            # update the same occurence sets
            occurence_count = cookie_occurences_count[cookie]
       
            # check if the set exists first
            if same_occurences_sets.get(occurence_count) == None:
                # make a new set for that occurence count key
                same_occurences_sets[occurence_count] = set()

            if occurence_count > 1:
                # In this case the cookie already belongs to a set 
                # need to remove it from that set
                same_occurences_sets[occurence_count-1].discard(cookie)
            
            # add the cookie to the set
            same_occurences_sets[occurence_count].add(cookie)

    return same_occurences_sets, cookie_occurences_count


# Find the key with the highest value from an input dictionary
# then returns its corresponding dictionary value
# inputs: dictionary where keys are numerical
# outputs: The value corresponding to the highest key 
def get_value_with_highest_key(input_dictionary):
    if len(input_dictionary.keys()) == 0:
        return None

    if type(list(input_dictionary.keys())[0]) not in {int, float}:
        raise ValueError("Input dictionary keys must be numerical")

    highest_occurence_count = max(input_dictionary.keys())

    return input_dictionary[highest_occurence_count]

