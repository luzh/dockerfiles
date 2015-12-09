#!/usr/local/bin/python2.7

import os
import time

print "The container is working properly if the current time is printed:", time.strftime("%H:%M:%S")
print "Timezone:", os.getenv("TZ")
