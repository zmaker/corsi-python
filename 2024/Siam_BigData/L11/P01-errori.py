import time
count = 0

while(True):
    print("count: ", count)
    time.sleep(1)
    count += 1
    try:
        if count == 2:
            r = count / 0;
        else:    
            print(conteggio)
    except NameError:
        print("variabile non esistente")
    except ZeroDivisionError:
        print("r=infinito")
    except:
        print("errore generico")