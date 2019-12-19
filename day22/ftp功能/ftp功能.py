import time

# for i in range(20):
#     # print('>', end='')
#     # print('\r>', end='')
#     n = '>' * i
#     print('\r%s' %n, end='')
#     time.sleep(1)

import sys
import time

for i in range(10):
    sys.stdout.write('>')
    sys.stdout.flush()
    time.sleep(0.5)



