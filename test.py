#!/usr/bin/env python

import numpy
import talib

close = numpy.random.random(100)
output = talib.SMA(close)
print(output)