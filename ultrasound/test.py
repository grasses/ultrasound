#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time
ROOT = os.path.dirname(os.path.abspath(__file__))
try:
    import ultrasound
except ImportError:
    sys.path.append(os.path.join(ROOT, ".."))

TRIG = 20
ECHO = 21
TIME_BREAK = 0.5

def main( trig, echo, time_break ):
    sensor = ultrasound.Ultrasound( trig, echo, time_break)
    while True:
        distance = int(sensor.get_distance())
        print distance
        time.sleep(0.04)

if __name__ == "__main__":
    trig = sys.argv[1] if len(sys.argv) > 1 else TRIG
    echo = sys.argv[2] if len(sys.argv) > 2 else ECHO
    time_break = sys.argv[3] if len(sys.argv) > 3 else ECHO
    main(trig, echo, time_break)
