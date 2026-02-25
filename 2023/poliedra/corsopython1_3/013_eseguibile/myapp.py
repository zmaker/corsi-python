from sys import argv

def main():
    if len(argv) > 1:
        nome = argv[1]
        print("hello", nome)
    else:
        print("hello!")

if __name__ == '__main__':
    main()
