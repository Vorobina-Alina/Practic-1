#!/usr/bin/env python3
import sys

def process_names_from_input():
    for line in sys.stdin:
        name = line.strip()
        if not name:
            return
        if not name[0].isupper():  
            print(f"Error: Name '{name}' needs to start with an uppercase letter!", file=sys.stderr)
        elif not all(character.isalpha() for character in name):
            print(f"Error: Name '{name}' contains invalid characters!", file=sys.stderr)
        else:
            print(f"Nice to see you {name}!")

def greet_interactive():
    while True:
        try:
            name = input("Hey, what's your name? ")
            if not name[0].isupper(): 
                print(f"Error: Name '{name}' needs to start with an uppercase letter!", file=sys.stderr)
            elif not all(character.isalpha() for character in name):
                print(f"Error: Name '{name}' contains invalid characters!", file=sys.stderr)
            else:
                print(f"Nice to see you {name}!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    if sys.stdin.isatty():
        greet_interactive()
    else:
        process_names_from_input()

