import os, time

f = open("tempfile.txt", 'x')
f.close()

time.sleep(5)
os.remove("tempfile.txt")