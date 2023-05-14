#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

#for i in range(10000):
sleep(1)
"""
sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
    random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9),
    datetime.datetime.now(),
    random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
    random.randint(1, 1024)
))
"""
sys.stdout.write("166.152.170.40 - [2017-02-05 23:28:50.535640] \"GET /projects/260 HTTP/1.1\" 405 977\n")
sys.stdout.flush()
sleep(1)
sys.stdout.write("58.70.209.187 - [2017-02-05 23:28:50.564010] \"GET /projects/260 HTTP/1.1\" 401 708\n")
#sys.stdout.flush()
sleep(1)
sys.stdout.write("125.218.201.102 - [2017-02-05 23:28:51.484960] \"GET /projects/260 HTTP/1.1\" 500 684\n")
#sys.stdout.flush()
sleep(1)
sys.stdout.write("93.202.122.198 - [2017-02-05 23:28:52.060026] \"GET /projects/260 HTTP/1.1\" 500 1002\n")
#sys.stdout.flush()
sleep(1)
sys.stdout.write("83.93.222.77 - [2017-02-05 23:28:52.920758] \"GET /projects/260 HTTP/1.1\" 200 551\n")
#sys.stdout.flush()
sleep(1)
sys.stdout.write("186.161.131.204 - [2017-02-05 23:28:53.006680] \"GET /projects/260 HTTP/1.1\" 500 665\n")
#sys.stdout.flush()
sleep(1)
sys.stdout.write("61.146.36.164 - [2017-02-05 23:28:53.792909] \"GET /projects/260 HTTP/1.1\" 401 299\n")
#sys.stdout.flush()
sleep(1)
sys.stdout.write("70.139.77.18 - [2017-02-05 23:28:54.747004] \"GET /projects/260 HTTP/1.1\" 403 543\n")
#sys.stdout.flush()
sleep(1)
sys.stdout.write("241.71.80.100 - [2017-02-05 23:28:55.573972] \"GET /projects/260 HTTP/1.1\" 500 222\n")
#sys.stdout.flush()
sleep(1)
sys.stdout.write("219.109.138.129 - [2017-02-05 23:28:55.755290] \"GET /projects/260 HTTP/1.1\" 200 186\n")
#sys.stdout.flush()
sleep(1)
sys.stdout.write("118.99.189.189 - [2017-02-05 23:28:56.091266] \"GET /projects/260 HTTP/1.1\" 403 278\n")
sys.stdout.flush()
