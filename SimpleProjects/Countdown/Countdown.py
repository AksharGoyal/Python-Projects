# import the time module
import time

def countdown(h, m ,s, timer_name):
        
    # if no name provided
    if(len(timer_name) == 0):
        timer_name = 'Countdown Over'

    # convert the time into a number
    count = (h*3600) + (m*60) + s
    
    try:
        # the timer starts
        while count >= 0:
            h, m, s = count//3600, (count%3600)//60, count%60
            timer = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
            print(timer, end="\r")  # erases the printed time
            time.sleep(1)           # wait for the new time to be shown
            count-= 1               # the time is running out
        
        # After the timer is completed
        print(f"\nTimer completed: {timer_name}!")
    except:
        # if the timer is interrupted
        print("Timer Interrupted! Exiting!")
        exit()

    # Ask for a name for our timer
timer_name = input('Hello! Enter a label for your timer: ')
# hour, min, sec = 0, 0, 0
hour = int(input("Enter the hour for the timer: "))
minute = int(input("Enter the minute for the timer: "))
second = int(input("Enter the second for the timer: "))

if hour < 0 or minute < 0 or second < 0:
    print("Inputs should be non-negative!")
    exit()

countdown(hour, minute, second, timer_name)
