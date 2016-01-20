#!/bin/env python
import os
import time

def brower():
   cmd = 'curl -v 127.0.0.1:8000/index.html'
   n = 0
   while n < 500000:
       os.system(cmd)
#time.sleep(0.1)

if __name__ == '__main__':
   brower()
