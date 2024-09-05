import time
import os
import json
import re

from dotenv import load_dotenv

import utils._global as _global

def main():
    load_dotenv()
    pass



if __name__ == '__main__':
    start = time.time()
    main()
    print(f'{round(time.time() - start, 2)} seconds.')