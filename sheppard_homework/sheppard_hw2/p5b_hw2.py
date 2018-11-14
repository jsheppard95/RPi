#!/usr/bin/env python3
# P5) Processor Temperature
# b) Function to print out repeated message in order to increase processor temperature

# See file p5a_hw2.py for part (a) program and comments explaining its use

while True:
  print('It\'s getting hotter!')

# Run p5a_hw2.py and p5b_hw2.py at the same time in separate terminal windows:
# Note increasing temperature of the processor
'''
We initially run ./p5a_hw2.py, which begins checking and recording the processor temperature in one second intervals.
The temperature behaves roughly constant with small fluctuations about 55-56 degrees celcius.
When we run ./p5b_hw2.py, the temperature rises quickly, at what appears to be roughly 1 degree per second. This increase appeared to slow approaching 67-68 degrees, but it did continue to increase. ./p5b_hw2.py (the infinite loop) was stopped when the temperature reached 73 degrees. At this point the temperature fell very rapidly and reached 62 degrees very quickly. It then began to fluctuate at about 60 degrees but did finally decrease after some time. The program was stopped when the temperature fluctuated at roughly 57-59 degrees C.
'''


