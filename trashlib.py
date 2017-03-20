import time
import sys
import math


for i in range(101):
    time.sleep(0.1)

    factor = math.ceil((i/2))

    progress_bar = "#" * int(factor)
    progress_bar += "-" * int(50 - factor)

    display_line = "|"+progress_bar+"|"
    sys.stdout.write("\r%d%%" % i)
    sys.stdout.write(display_line)
    sys.stdout.flush()