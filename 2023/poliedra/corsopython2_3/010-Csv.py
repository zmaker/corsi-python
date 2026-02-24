from csv_reader_lib import CSV

def main():
    csv = CSV("magazzino.csv")
    
    n = csv.getRowsCount()
    print("righe: ", n)
    
    print("contenuto")
    print(csv)
    
    val = csv.getCell(1,1)
    print("cella 1:1 = ", val)

if __name__ == "__main__":
    main()