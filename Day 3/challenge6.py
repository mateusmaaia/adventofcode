# --- Part Two ---
# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

# For example, in the claims above, only claim 3 is intact after all claims are made.

# What is the ID of the only claim that doesn't overlap?

import re
import numpy as np

with open('../Data/day3.txt') as f:
    inp = []
    for r in f.readlines():
        r = re.split('[^0-9]+', r[1:].strip())
        inp.append([int(d) for d in r])

fabric = np.zeros((1000, 1000))

def noMatterHowYouSliceIt():
    for n, x, y, dx, dy in inp:
        fabric[x:x+dx, y:y+dy] += 1
    return np.sum(fabric > 1)

def doesntOverlap():
    noMatterHowYouSliceIt()
    for n, x, y, dx, dy in inp:
        if np.all(fabric[x:x+dx, y:y+dy] == 1):
            return n

print(doesntOverlap())