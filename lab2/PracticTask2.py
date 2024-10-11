#!/usr/bin/env python3
import sys

def greet_from_file():
    error_log = open("error.txt", "w")
    with open("names.txt", "r") as f:
        for line in f:
            name = line.strip()
            if not name:
                continue
            if not name[0].islower():
                error_log.write(f"Error: Name '{name}' needs to start in lowercase!\n")
            elif not name.isalpha():
                error_log.write(f"Error: Name '{name}' contains invalid characters!\n")
            else:
                print(f"Nice to see you {name}!")
    error_log.close()

def greet_interactive():
    try:
        while True:
            name = input("Hey, what's your name? ")
            if not name[0].isupper():
                print(f"Error: Name '{name}' needs to start in uppercase!")
            elif not name.isalpha():
                print(f"Error: Name '{name}' contains invalid characters!")
            else:
                print(f"Nice to see you {name}!")
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        greet_from_file()
    else:
        greet_interactive()
