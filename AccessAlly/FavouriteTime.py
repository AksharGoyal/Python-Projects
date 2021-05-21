import datetime, re # we import the required modules

def sequence_checker(seq:list) -> bool:
    '''
    sequence_checker helps us to check if a list of integers are in arithmetic sequence or not
    
    seq (list of Int): list of integers who may or may not have constant difference
    '''
    diff = None                                     # Initialize the airthmetic difference
    for i in range(0, len(seq) - 1):                # we will skip the first element to avoid IndexError
        if diff == None:                            # Calculating the arithmetic difference first time
            diff = seq[i + 1] - seq[i]
        elif not(diff == (seq[i + 1] - seq[i])):    # Differences don't MATCH! Not an arithmetic sequence
            return False
    return True

def sequence_finder(D:int) -> int:
    '''
    sequence_finder takes in number of minutes passed and returns nimber of arithmetic sequences spotted
    between 12:00 and 12:00+D 
    
    D (Int): number of minutes passed after noon
    '''
    begin_time = datetime.datetime(2021, 5, 21, 12,0, 0)             # Initializing the noon time object
    # print(begin_time) # Debugging :)
    minutes_added = datetime.timedelta(minutes = D)
    end_time = begin_time + minutes_added           # Getting the time after D minutes have passed
    # print(end_time)
    # print(begin_time <= end_time)
    
    no_of_instances = 0                             # To get the number of times a sequence was observed
    while begin_time <= end_time:
        # We get the required sequence of digits from time by getting the correct time format
        # and then getting the required digits to check arithmetic sequence
        if (begin_time.hour > 12) and (begin_time.hour % 12):
            start_str = datetime.time(begin_time.hour % 12, begin_time.minute)
        elif (begin_time.hour % 12 == 0):
            start_str = datetime.time(12, begin_time.minute)
        else:
            start_str = datetime.time(begin_time.hour, begin_time.minute)
        start_str = str(start_str)                      # We got the required time format
        digits = re.findall('\d',start_str)
        digits = digits[1:4] if digits[0] == '0' else digits[:4]
        digits = list(map(lambda x: int(x), digits))    # We got the required digits too
        # Now we check if the time is arithmetic sequence or not
        if sequence_checker(digits):
            no_of_instances += 1     # If we find an arithmetic sequence, then we increment the count
        # print(start_str, digits, sequence_checker(digits))
        begin_time += datetime.timedelta(minutes = 1)   # Incrementing the loop variable
    return no_of_instances
    
if __name__ == '__main__':
    
    minutes_passed = int(input())
    print(sequence_finder(minutes_passed))
