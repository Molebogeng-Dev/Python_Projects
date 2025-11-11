import sys

class Rover:
    
    def __init__(self, path):
        try:
            with open(path) as file:
                self.file= file.readlines()
        except FileNotFound:
            sys.exit('Cannot open file')


def main():
    rover= Rover(sys.agrv[1])

if __name__ == "__main__":
    main()