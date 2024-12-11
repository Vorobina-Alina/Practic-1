#!/usr/bin/env python3

import sys
import math

def main():
    try:
        data = input()
        num = float(data)
        
        if num < 0:
            raise Exception('Error! Value <0')

    except EOFError:
        print('Error!', file=sys.stderr)
    except ValueError:
        print('Error! Value is wrong!', file=sys.stderr)
    except Exception as e:
        print(e, file=sys.stderr)
    else:
        sqrt_num = math.sqrt(num)
        print(f"Квадратный корень: {sqrt_num}")

if __name__ == "__main__":
    main()
