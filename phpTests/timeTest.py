from datetime import datetime
import time

for i in range(5):
    print(f"{datetime.now()} - He has risen! {i}", flush=True)
    time.sleep(1)
