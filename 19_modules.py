import sys
import re

print(sys.path)

text = "mi numero de telefono es 320 333 44 11 , el codigo del pais es 57, mi numero de la suerte es el 33"

result = re.findall('[0-9]+', text)
print(result)

import time

timestamp = time.time()
local = time.localtime()
result_time = time.asctime(local)

print('local time:  time.localtime() -> ',local)

print('time stamp:  time.time() -> ',timestamp)

print('time.asctime(local)-> ',result_time)