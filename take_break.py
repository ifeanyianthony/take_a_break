import webbrowser
import time

total_breaks = 3
break_count = 0

## Opens the link after waiting for 10 seconds.
print('This program started on '+time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=5qhEJIgnC08&list=RD5qhEJIgnC08&start_radio=1")
    break_count +=1
