from datetime import date
from time import sleep

today = date.today()
yy = today.year
mm = today.month
dd = today.day
print(f"data: {yy}.{mm}.{dd}")

while (True):
    cmd = input("comando? ")
    if not cmd:
        break;
    print("elaborazione in corso")
    sleep(1)
    today = date.today()
    yy = today.year
    mm = today.month
    dd = today.day
    print(f"data: {yy}.{mm}.{dd}")

    