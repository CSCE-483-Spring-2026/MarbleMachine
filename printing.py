import time
import sys

while True:
    print(time.localtime(), file=sys.stderr)
    time.sleep(2);
