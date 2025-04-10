# Create a Timer with the Time module
import time
run = input("Start? >")
seconds = 0

# If the input tells the timer to start, while loop starts
# While seconds are less then ten it will will wait 1 second,
#increment by 1, print seconds elapsed and repeat
if run == "yes" or 'y' or 'start':
    while seconds < 10:
        print(">", seconds)
        time.sleep(1)
        seconds += 1
    print(">", seconds)