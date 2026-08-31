import time
import os
time_=float(input("Enter time i: "))
unit=input("Enter time is in minutes or seconds?(min/sec) :").lower()
if unit=="min":
    time_in_sec=time_*60
    for x in range(int(time_in_sec),0,-1):
        second=int(x%60)
        minutes=(x//60)%60
        hour=x//3600
        os.system("cls")
        print(f"{hour:02}:{minutes:02}:{second:02}")
        time.sleep(1)
    print("Time's up!")
elif unit=="sec":
    time_=int(time_)
    for x in range(time_,0,-1):
        second=int(x%60)
        minutes=(x//60)%60
        hour=x//3600
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{hour:02}:{minutes:02}:{second:02}")
        time.sleep(1)
    print("Time's up!")



    

