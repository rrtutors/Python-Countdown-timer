# import the time module
import time
# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Timeout!!')

# input time in seconds
t = input("Input the Countdown time in seconds: ")
# function call
countdown(int(t))

