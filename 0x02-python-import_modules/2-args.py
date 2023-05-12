
#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    print("{} arguments:".format(count))
    if count == 1:
        print(".")
    else:
        print(":")
    for i in range(1, count):
        print("{}: {}".format(i, sys.argv[i]))
