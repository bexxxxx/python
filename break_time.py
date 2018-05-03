#!python2
import time
import webbrowser

total_breaks = 3
count = 0

print("This program started on "+time.ctime())
while(count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=U9BwWKXjVaI")
    count = count + 1
    
#2*60*60 if want to break for 2 hours
