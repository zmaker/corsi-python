import threading
import time

def mythread(name, wait):
    print(name, ": avviato")
    time.sleep(int(wait))
    print(name, ": end")
    
if __name__ == "__main__":
    th = threading.Thread(target=mythread, args=('thr1', 2))
    print("main: start")
    th.start()
    
    th.join()
    print("main: end")
