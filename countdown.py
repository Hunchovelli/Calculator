import time

def countdown(t):
    while t > 0:
        min, sec = divmod(t,60)
        timer = "%02d:%02d" % (min, sec)
        print (timer, end ="\r")
        time.sleep(1)
        t -= 1
    
    print("Countdown finished")

q = input("Enter how long you want countdown for in seconds: ")

print (countdown(int(q)))


