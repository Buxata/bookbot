from stats import report
from sys import argv,exit

def main(argv):
    if len(argv) < 2:
        exit("Usage: python3 main.py <path_to_book>")
    report(argv[1])

main(argv)
