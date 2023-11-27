import subprocess
import platform

def change_mac(interface, new_mac):
    print(f"Changing MAC address of {interface} to {new_mac}")

    if platform.system().lower() == "linux":
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["sudo", "ifconfig", interface, "up"])
    elif platform.system().lower() == "windows":
        subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=disable"])
        subprocess.call(["netsh", "interface", "set", "interface", interface, "newmac="+new_mac])
        subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=enable"])
    else:
        print("Unsupported operating system")

# Example usage:
interface_name = "Ethernet"  # Replace with your network interface name
new_mac_address = "00:11:22:33:44:55"  # Replace with the desired MAC address

change_mac(interface_name, new_mac_address)
