#!/usr/bin/env python

from scapy.all import *
from utils import *
from time import time
import signal

iface = get_if()

# stats
start = None
counter = 0

def proc_pkt(p):
    global start, counter
    if not start:
        start = time()
    data = p.lastlayer()
    if str(data) == str(FINISHED):
        terminate()
        exit(0)
    else:
        counter += 1

# terminate handler
def terminate():
    end = time()
    print("======= Receiver =======")
    elapsed = (end - start) / 1000
    print("Elapsed: %fs" % elapsed)
    print("Received: %d data packets" % counter)
    print("Throughput: %f packets/s" % (counter/elapsed))


print("sniffing on %s" % iface)
sniff(iface=iface,
      prn=lambda x: proc_pkt(x))
