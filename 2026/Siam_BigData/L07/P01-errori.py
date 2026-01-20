import time
count = 0

while True:
    print("count: ", count)
    count += 1
    time.sleep(1)

    try:
        if count == 2:
            r = count / 0
    except ZeroDivisionError:
        print("divisione per 0")
    except:
        print("errore generico")