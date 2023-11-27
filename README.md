# Basic-Hacking-Scripts
These are some basic python scripts, that are essential for maintaining good opsec and for anyone looking to get into cybersecurity.
Installation Guide:
First make sure you have python installed, latest version is recommended

Then install the git package
      apt-get install git

Then clone or download this repo
      sudo git clone https://github.com/SanskaarPathak/Basic-Hacking-Scripts
      
Install all the packages in requirements.txt,
linux is recommended, and you might get some error while installing netfilterqueue package
I am actively working on switching to a new module.

After doing all the steps mentioned above, you can run the scripts and start Hacking.

Scripts in detail:
1) arpspoof.py - for man in the middle attack :
   Open the script and put your router's ip in the gateway_ip and the ip you want to spoof in target_ip.
   After running, all the packets will be forwarded to you first.
 
2) dns_spoof.py - spoof a website:
     To run this successfully, firsf run the arpspoof.py file, the. replace the www.google.com in script with your site in this format, www.site.com
     after this put your targets ip in rdata.
     
3) file_inter.py - intercept a file downloaded by the victim:
     Can be used after running arpspoof.py to intercept the files downloaded by the victims
     to run, replace the link in the scapy_packet[scapy.Raw].load variable to your malicious one
    
4) mac_address_spoofer.py - spoof your mac address:
     To run, replace the content in interface_name with the name of your network card and the content of new_mac_address with your new desired mac address
     
5) nScan.py - simple script to scan all the devices connected to your network:
     Remember to run all the script with sudo
     
6) packet_sniffer.py - used for capturing usernames and passwords:
     It will only work after running arpspoof.py, replace the eth0 with the name of the wireless card you used for arpspoof.py
     
