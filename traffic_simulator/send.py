#!/usr/bin/env python

from scapy.all import *
from utils import *
import argparse
import threading

iface = get_if()

# parse args
parser = argparse.ArgumentParser()
parser.add_argument('--duration', type=int, required=True, help="Length of sending")
parser.add_argument('--throughput', type=int, required=True, help="Number of packets per second")
args = parser.parse_args()

# send packets
parent = Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')/IP(src='10.0.0.1', dst='10.0.0.2')

p = parent / "bunchofdata"
p.summary()
sendpfast(p, pps=args.throughput, loop=args.throughput*args.duration)

print("Sent all data packets")

finish = parent / FINISHED
sendp(finish, iface=iface)

print("Sent termination packet")

print("========= Sender ========")
print("Done")
