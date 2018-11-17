# -*- coding:utf-8 -*-

# Copyright: Lustralisk
# Author: Cedric Liu
# Date: 2015-11-08

import sys, time
from PBar.progressBar import ProgressBar
bar = ProgressBar(total = 10)
for i in range(10):
    bar.move()
    bar.log('We have arrived at: ' + str(i + 1))
    time.sleep(1)
