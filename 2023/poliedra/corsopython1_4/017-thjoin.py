import threading
import time

def myThread(name, wait):
    print(f"{name}: avvio")
    time.sleep(int(wait))
    print(f"{name}: end")

if __name__ == "__main__":
    th = threading.Thread(target=myThread, args=('exe1', 3))
    print("main: avvio")
    th.start()
    
    th.join()
    print("main: end")
