#print(x)

#x = 0
#if (x > 0) print(x)

n = 10
for i in range(10):
    
    try:
        r = n / (5-i)
    except ZeroDivisionError:
        print("diviso per zero")
        r = -1;
    except NameError:
        print("err1")
        r = -2;
    except:
        print("err generico")
        r = -3;
    else:
        print(">", end="")
    print(r)