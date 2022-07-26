import statsd
import time
import random
import os

server = os.getenv('STATSD_SERVER', default="localhost")
port = os.getenv('STATSD_PORT', default=8125)
sleep_s = int(os.getenv('SLEEP_SECONDS', default=5))

c = statsd.StatsClient(server, port)

while True:
    r = random.randint(0,1000)
    print("setting 'random' to: ", r)
    c.gauge('random', r)
    time.sleep(sleep_s)

