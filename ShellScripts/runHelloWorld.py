import time
from datetime import datetime

while True:
    print(f"Hello, World! it's {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(5)
