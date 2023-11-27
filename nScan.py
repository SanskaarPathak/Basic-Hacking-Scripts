#!/usr/bin/env python

import scapy.all as scapy
import argparse


def getargum():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="target IP/IP range.")
    options = parser.parse_args()
    return options


def scan(ip):
    arpReq = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_brodcast = brodcast/arpReq
    ans = scapy.srp(arp_req_brodcast, timeout=1, verbose=False)[0]

    clili = []

    for element in ans:
        clidi = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clili.append(clidi)
    return (clili)


def print_result(clisult):
    print("IP\t\t\tMacAddress\n-----------------------------------")
    for client in clisult:
        print(client["ip"] + "\t\t" + client["mac"])


options = getargum()
scanresult = scan(options.target)
print_result(scanresult)