#!/usr/bin/env python

import sys

# a simple script that finds number of seconds from two timestamps

def secs_between_timestamps(min1, sec1, min2, sec2):
    if min1 > min2:
        return "Timestamps in wrong order"
    else:
        if min1 == min2:
            return sec2 - sec1
        else:
            return (sec2 + ((min2 - min1) * 60) - sec1)


while __name__ == "__main__":
    if len(sys.argv) < 5 or len(sys.argv) > 5:
        print("usage: time.py {min1} {sec1} {min2} {sec2}")
        break

    else:
        min1 = int(sys.argv[1])
        sec1 = int(sys.argv[2])
        min2 = int(sys.argv[3])
        sec2 = int(sys.argv[4])

        print(secs_between_timestamps(min1, sec1, min2, sec2))
        break

        


