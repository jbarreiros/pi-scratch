# 10 segment led bar graph

import lib as lib

leds = [14, 15, 18, 23, 24, 25, 8, 7]
lib.init(leds)

try:
    lib.back_and_forth(leds, 0.1)
    # lib.middle_out(leds, 0.2)

finally:
    lib.cleanup()
