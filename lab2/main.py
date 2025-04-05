from io_manager import IOManager

def main(): 
    io = IOManager()
    choice = io.select_equation()
    print(choice)


if __name__ == "__main__":
    main()