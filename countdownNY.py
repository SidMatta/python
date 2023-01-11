import time

n_input = int(input("Enter the countdown: "))
n = max(n_input,10)

while n >0:
    print("00:{:02d}".format(n), end = '\r')
    time.sleep(1)
    n -= 1

print("HAPPY NEW YEAR !!")

