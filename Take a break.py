import time
import webbrowser

total_breaks = 3
break_count = 0
delay = 1

print("The program started on " + time.ctime())

while(break_count < total_breaks):
    time.sleep(delay)
    webbrowser.open("http://www.twitter.com")
    break_count += 1;

print("The program ended on " + time.ctime())
