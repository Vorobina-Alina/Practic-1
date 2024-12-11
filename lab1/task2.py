#!/usr/bin/env python3

import random
import sys

def main():
   try:
      data = input()
      A = int(data)
      B = random.randint(-10, 10)
      
      res = A / B
   except ValueError:
      print('Wrong value', file=sys.stderr)
   except ZeroDivisionError:
      print('Error! B=0', file=sys.stderr)
   else:
      print(res)

if __name__ == "__main__":
   main()
