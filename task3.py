#!/usr/bin/env python3

import math

num = float(input())
sqrt_num = math.sqrt(num)
with open("output.txt", "w") as f:
   f.write(str(sqrt_num) + "\n")
