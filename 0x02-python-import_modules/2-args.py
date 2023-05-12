
#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv[1:])
    if count == 0:
        print("0 arguments.")
    else:
        print(count, "argument" + ("s" if count > 1 else "")
        print(":")

        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i]))
