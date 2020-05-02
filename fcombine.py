import sys

__author__ = "QSoloX"

def main():
    # This var will hold all our values from the files
    fileSet = []
    # This checks to see if we passed any args, it will always show len of 1 because of the python file itself
    if len(sys.argv) == 1:
        print("You need to add args!")
        exit()
    # Here we are setting args to all the args passed except the python filename
    args = sys.argv[1:]
    # Now we iterate over each argument and do work on it
    for arg in args:
        # Open the argument as file (this is because we are passing files in as arguments)
        with open(arg) as file:
            # Here we set the output of a our list comprehension into fileSet
            # [i.strip() for i in file] goes over all the contents in the file and runs .strip() on them to remove things like \n
            fileSet += [i.strip() for i in file]
    # Now we iterate over our list as a set which will remove all duplicates
    for i in set(fileSet):
        # Then just print them, we can redirect this to a file using > file.txt
        print(i)
if __name__ == "__main__":
    main()