#!/usr/bin/python2.7

from argparse import ArgumentParser
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.util import pmonitor

import time
from signal import SIGINT
import subprocess

def emulate():
    net = Mininet(controller=Controller,
                  switch=OVSSwitch,
                  link=TCLink,
                  autoStaticArp=True,
                  autoSetMacs=True,
                  cleanup=True)
    info("*** Creating (reference) controller ***\n")
    controller = net.addController('controller', port=6633)

    info("*** Creating switches ***\n")
    sw = net.addSwitch('s0', dpid="00:00:00:00:00:00:00:01")

    info("*** Creating hosts ***\n")
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
  
    info("*** Creating links ***\n")
    net.addLink(h1, sw)
    net.addLink(h2, sw)

    info("*** Starting network ***\n")
    net.build()
    controller.start()
    sw.start([controller])

    info("*** Testing network ***\n")
    net.pingAll()

    CLI(net)

    info("*** Stopping network ***\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')  # for CLI output
    emulate()