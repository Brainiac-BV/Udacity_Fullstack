import webbrowser
import time

num = 1
print("This is being run at" + time.ctime())
while(num < 4):
    time.sleep(3)
    webbrowser.open("http://google.com")
    num = num + 1
