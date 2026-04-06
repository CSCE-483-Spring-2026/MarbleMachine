import sys

if sys.prefix != sys.base_prefix:
    print("Inside a virtual environment")
else:
    print("Not inside a virtual environment")

print("Also, he has risen!")
