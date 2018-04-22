import sys
from application import Application

def main(args=None):
    """The main routine.""" # these are doc strings. in python CLI you can type help(main) and it'll print this.
    if args is None:
        args = sys.argv[1:]

    Application()

    print('This is the main routine')
    print('it should do something...')


if __name__ == "__main__":
    main()
