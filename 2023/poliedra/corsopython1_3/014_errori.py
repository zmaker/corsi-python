#errore 1
#print(x)

#errore 2
#x = 0
#if (x > 0) print(x)

#errore 3
#n = 10
#for i in range(10):
#    r = n/(i-5)
#    print(i)

import time

count = 0
while True:
    print(f"elaborazione n. {count}")
    time.sleep(1)
    count += 1
    try:
        if (count == 1):
            n = count / 0
        
        if (count == 2):
            print(conteggio)
    #except Exception as e:
    #    print("errore di stampa: ", e.__class__)
    except (NameError, TypeError):
        print("variabile non esiste")
    except ZeroDivisionError:
        print("diviso per 0")
    except:
        print("errore non previsto")
        
