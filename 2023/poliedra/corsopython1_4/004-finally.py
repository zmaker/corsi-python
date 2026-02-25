try:
    #codice pericoloso
    f = open('readme.txt', 'w')
    #operazioni su file
    n = 0
    assert n != 0
except:
    #gestisco errore
    print("file error")
finally:
    #da eseguire sempre
    f.close()
    print("file chiuso")